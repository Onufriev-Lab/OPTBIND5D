# OPTBIND5D
Optimal Radii for MMGBSA


`OPTBIND5D.py` is a Python script designed to automate the process of modifying atomic radii in AMBER topology files (.prmtop) to OPTBIND5D radii in order to prepare the input files for MMGBSA calculations. Regardless of the radii set of the input topology file, it updates that radii based on predefined mappings from Bondi radii to OPTBIND5D. This script uses ParmEd, a tool for editing and analyzing parameter/topology files in computational chemistry. **This current version works only for structures with C, H, N, O, and S atoms and shouldn't be applied to any other atoms such as metal atoms, ions, Cl, and F. If your structure contains some of these atoms you can still change the radii values into mbondi manually. NOTE: This procedure is a post-processing step (inputs for MMGBSA) and has no effect on explicit solvent MD simulations. An update in AMBER suit will be available soon to automate the process.**

## Requirements

- **Python**: Python 3.x
- **ParmEd**: This script requires the ParmEd tool to be installed and properly configured. You can install ParmEd using pip:

  ```bash
  pip install parmed
  ```

- **AMBER**: Proper setup of AMBER tools if not already installed.

## Installation

Clone the repository or download the `OPTBIND5D.py` script directly into your working environment.

```bash
git clone https://github.com/Onufriev-Lab/OPTBIND5D
cd OPTBIND5D
```

## Usage

Before running the script, ensure that you have the necessary `.prmtop` and `.crd` files prepared and located in accessible directories.

1. **Prepare Your Files**: Place your `.prmtop` and `.crd` files in the directory or ensure the paths are correctly specified.
2. **Run the Script**: Execute the script by running:

   ```bash
   python OPTBIND5D.py
   ```

3. **Follow Prompts**: Input the required file paths when prompted (as a string):
   
   - Enter the path to the input prmtop file, make sure to give the path to the file as String and the file format should be .prmtop NOT .top : "./example_input.prmtop"
   - Enter the path to the input crd file: "./example_input.crd"
     
The script will generate a new `.prmtop` file with OPTBIND5D radii.
