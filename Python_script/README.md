# OPTBIND5D
Optimal Radii for MMGBSA


`OPTBIND5D.py` is a python script that automates the process of modifying atomic radii in AMBER topology files (`.top`) to the OPTBIND5D radii set. It is designed to prepare topology files for MMGBSA calculations by updating specific atomic radii.

---

## Features

- Updates the radii for hydrogen (H), carbon (C), nitrogen (N), oxygen (O), and sulfur (S) to OPTBIND5D values.
- Leaves radii of other atom types unchanged from the original input file.


---

## Atomic Radii Mapping

The script modifies radii based on the following mapping:

| Atomic Number | Atom Type  | OPTBIND5D Radii (Å)      |
|---------------|------------|--------------------------|
| 1             | Hydrogen   | 1.47000000E+00          |
| 6             | Carbon     | 2.23000000E+00          |
| 7             | Nitrogen   | 2.37000000E+00          |
| 8             | Oxygen     | 1.09000000E+00          |
| 16            | Sulfur     | 1.80000000E+00 (Same as mbondi) |


## Requirements

- **Python**: Python 3.x


## Installation

Clone the repository or download the `OPTBIND5D.py` script directly into your working environment.

```bash
git clone https://github.com/Onufriev-Lab/OPTBIND5D
cd OPTBIND5D/Python_script
```

## Usage

Before running the script, ensure that you have the necessary `.top` file prepared and located in accessible directories.

1. **Prepare Your Files**: Place your `.top` file in the directory or ensure the paths are correctly specified.
2. **Run the Script**: Execute the script by running:

   ```bash
   python3 OPTBIND5D.py
   ```

## Example Usage

Run the script and provide the path to your `.top` file when prompted:

```bash
Please enter the path to your .top file: ./example.top
New .top file written as: .example_OPTBIND5D.top
