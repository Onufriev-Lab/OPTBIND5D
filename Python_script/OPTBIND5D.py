def read_section(file, start_flag, end_flag):
    collect_data = False
    data = []
    for line in file:
        if start_flag in line:
            collect_data = True
            file.readline()  # Skip the format line
            continue
        if end_flag in line:
            break  # Stop reading when end flag is reached
        if collect_data and line.strip() and any(char.isdigit() for char in line):
            data.extend(line.strip().split())
    return data

def modify_radii(atomic_numbers, radii, radii_map):
    new_radii = []
    original_radii_list = list(radii)  # Copy original radii list to maintain sequence
    for num in atomic_numbers:
        num = int(num)
        if num in radii_map:
            new_radii.append(radii_map[num])
        else:
            if original_radii_list:
                new_radii.append(original_radii_list.pop(0))  # Use the next available radii from the list if not in map
    return new_radii

def write_new_top_file(original_file_path, new_radii):
    new_file_path = original_file_path.replace('.top', '_OPTBIND5D.top')
    with open(original_file_path, 'r') as original, open(new_file_path, 'w') as modified:
        radii_written = False
        for line in original:
            if '%FLAG RADII' in line:
                # Write the radii section header and format
                modified.write(line)
                modified.write(next(original))
                # Write modified radii values
                for i in range(0, len(new_radii), 5):
                    modified.write(''.join(f'{r:<16}' for r in new_radii[i:i+5]) + '\n')
                radii_written = True
            elif radii_written and '%FLAG' in line:
                # Once new radii are written, continue copying the rest of the file
                radii_written = False
                modified.write(line)
            elif not radii_written:
                # Copy lines from the original file to the new file
                modified.write(line)

def process_topology_file():
    file_path = input("Please enter the path to your .top file: ")
    try:
        with open(file_path, 'r') as file:
            atomic_numbers = read_section(file, '%FLAG ATOMIC_NUMBER', '%FLAG MASS')
            radii = read_section(file, '%FLAG RADII', '%FLAG SCREEN')

        radii_map = {
            1: '1.47000000E+00',
            6: '2.23000000E+00',
            7: '2.37000000E+00',
            8: '1.09000000E+00',
            16: '1.80000000E+00',
        }
        new_radii = modify_radii(atomic_numbers, radii, radii_map)
        write_new_top_file(file_path, new_radii)

        print(f"New .top file written as: {file_path.replace('.top', '_OPTBIND5D.top')}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Trigger the function to prompt the user
process_topology_file()

