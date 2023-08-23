# Bluey Bioinformatics Scripts

This repository is a collection of bioinformatic scripts designed for use on the EMAI HPC "Bluey". These scripts are tailored to facilitate and automate various bioinformatics operations and analyses.

## Current Scripts:

1. **Project Directory Creator**: This script sets up a comprehensive directory structure for bioinformatics projects, ensuring consistency and a smooth workflow. It creates directories such as 'analyses', 'bin', 'docs', 'raw', and more. It also initializes a Git repository in the project directory for version control. 

### How to use the Project Directory Creator:

1. Clone this repository to your HPC.
   `
   git clone [https://github.com/Jwebster89/Bluey_scripts.git]
   `

2. Navigate to the directory containing the script.
   `
   cd Bluey_scripts
   `

3. Make the script executable.
   `
   chmod +x Project_creator.py
   `

4. Run the script with the desired project name as an argument.
   `
   python Project_creator.py <Project_name>
   `

   Replace <Project_name> with the desired name of your project.

## Directory Structure:

The script `Project_creator.py` will produce the following directory structure:

`
<project_name>
│
├── analyses/
│
├── bin/
│   ├── driver_script.sh    # Script for re-running an entire analysis.
│   └── analysis_creator.py # Script for setting up analysis directories.
│
├── docs/
│
├── raw/
│   ├── sequence_data/
│   └── SRA/
│
└── data/
    ├── assembly/
    │   ├── input/
    │   ├── logs/
    │   └── output/
    ├── processed_raw/
    └── references/
`

## Future Scripts:

As more scripts are developed, they will be added to this repository and documented in this README.

## Contribution:

Feel free to contribute to this repository by either proposing changes via pull requests or by raising issues if you encounter any problems.


---

**Disclaimer**: This README was generated with the assistance of ChatGPT by OpenAI.
