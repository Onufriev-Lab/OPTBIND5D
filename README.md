# OPTBIND5D
Optimal Radii for MMGBSA


`OPTBIND5D.py` is a Python script designed to automate the process of modifying atomic radii in AMBER topology files (.prmtop) to OPTBIND5D radii. It updates specific radii based on predefined mappings from Bondi radii to OPTBIND5D. This script uses ParmEd, a tool for editing and analyzing parameter/topology files in computational chemistry.

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
   
   - Path to the input prmtop file (e.g., “./all.prmtop”).
   - Path to the input crd file (e.g., “./all.crd”).

The script will generate a new `.prmtop` file with OPTBIND5D radii.

