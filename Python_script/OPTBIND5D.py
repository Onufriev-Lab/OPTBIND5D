import os

def modify_radii(topology_file_path):
    # Define the mapping from atom first letter to old and new radii values
    radii_changes = {
        'C': ('1.70000000E+00', '2.23000000E+00'),
        'N': ('1.55000000E+00', '2.37000000E+00'),
        'H': ('1.20000000E+00', '1.47000000E+00'),
        'O': ('1.50000000E+00', '1.09000000E+00')
    }
    
    # Read the entire topology file into memory
    with open(topology_file_path, 'r') as file:
        lines = file.readlines()

    # Change the comment about radii
    for i, line in enumerate(lines):
        if "Bondi radii (bondi)" in line:
            lines[i] = line.replace("Bondi radii (bondi)", "Bondi radii (optbind5d)")
            break  # Assuming only one such line exists

    # Find the index of RADII flag
    radii_index = next(i for i, line in enumerate(lines) if '%FLAG RADII' in line) + 2  # Assuming the data starts two lines after the flag

    # Read and modify radii
    for i in range(radii_index, len(lines)):
        line = lines[i].strip()
        if line and line[0].isdigit():  # Ensure we are processing a line with numeric values
            radii_values = line.split()
            modified_radii = []
            for radius in radii_values:
                modified_radius = radius
                for atom_type, (old_radius, new_radius) in radii_changes.items():
                    if "{:.8E}".format(float(radius)) == old_radius:
                        modified_radius = new_radius
                        break
                modified_radii.append("{:16.8E}".format(float(modified_radius)))
            lines[i] = ''.join(modified_radii) + '\n'
        elif not line[0].isdigit():  # Break the loop if a non-numeric line is encountered
            break

    # Write the modified topology file
    with open(topology_file_path, 'w') as file:
        file.writelines(lines)

# Main code execution starts here

# Get input file paths from the user

prmtop_file = input("Enter the path to the input prmtop file, make sure to give the path to the file as String and the file format should be .prmtop NOT .top  (e.g. ./example_input.prmtop): ")
crd_file = input("Enter the path to the input crd file (e.g. ./example_input.crd): ")

# Prepare the new prmtop file path
bondi_prmtop = prmtop_file.replace('.prmtop', '_OPTBIND5D.prmtop')

# Check if the new prmtop file already exists and handle accordingly
if os.path.exists(bondi_prmtop):
    os.remove(bondi_prmtop)  # or use os.rename() to keep a backup

# Run ParmEd with ptraj script to change radii to Bondi
ptraj_script = "parmed.ptraj"
with open(ptraj_script, "w") as ptraj_file:
    ptraj_file.write("changeRadii bondi\n")
    ptraj_file.write("parmout {}\n".format(bondi_prmtop))

os.system("parmed -p {} -c {} -i {}".format(prmtop_file, crd_file, ptraj_script))

# Now, modify the radii and comment in the new prmtop file as specified
modify_radii(bondi_prmtop)  # Modify the same file in place

