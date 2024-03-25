# Directory Structuring for Bioinformatics Projects on EMAI AGTC HPC

Welcome to the Project Directory Creator! This tool is designed to help researchers and students working on bioinformatics projects to set up a standardized directory structure quickly and efficiently. By creating a consistent framework for your project files, you're setting the stage for smoother data management, analysis, and collaboration. This script is especially useful if you're new to working on a High-Performance Computing (HPC) environment or if you're looking for ways to keep your projects organized from the start.

*"Make sure that your analyses are structured in such a way that someone who knows nothing about your project can follow. Because half of the time, that will be **you** 3 weeks down the track*"
## Getting Started

### Prerequisites
Before you begin, ensure you have access to a Linux command line environment and have basic familiarity with navigating directories and running scripts. If you're new to Linux or command line interfaces, we recommend looking up introductory tutorials on these topics. (You might find resources like "Linux Command Line Basics" or "Introduction to the Unix Shell" helpful.)

### How to Use the Project Directory Creator

1. **Clone the Repository**: First, you need to get the script onto your HPC. Open your terminal, navigate to the folder where you want to download the script, and run:
   ```bash
   git clone https://github.com/Jwebster89/Directory_structuring.git
   ```
   
2. **Navigate to the Script Directory**: Change into the directory containing the newly cloned script.
   ```bash
   cd Directory_structuring
   ```

3. **Make the Script Executable**: Before running the script, you need to give it permission to execute on your machine. This is done with the `chmod` command.
   ```bash
   chmod +x Project_creator.py
   ```

4. **Run the Script**: Now, you're ready to create a new project directory structure. Simply run the script with the name of your project as an argument. Remember to replace `<Project_name>` with your actual project name.
   ```bash
   python Project_creator.py <Project_name>
   ```
   
### Example
If your project name is "Drop_bear_genomics", you would run:
```bash
python Project_creator.py Drop_bear_genomics
```

## Directory Structure Created
The script organizes your project into several directories, each with a specific purpose:

- `analyses/`: For analysis scripts and notebooks.
- `bin/`: Contains utility scripts like `driver_script.sh` for adding all projects scripts to for rebuilding projects and `analysis_creator.py` for setting up new analysis directories.
- `docs/`: Documentation for your project.
- `raw/`: Raw data, subdivided into `sequence_data/` and `SRA/`.
- `data/`: Processed data, with subdirectories for different stages of data processing and analysis.

This structure helps keep your project organized and facilitates reproducibility and collaboration.

## Using the `analysis_creator.py` script

After setting up your project structure with the main script, you can create standardized folder structures for individual analyses using the `analysis_creator.py` script. This script generates a specific directory setup for a new analysis within the `analyses` directory of your project. It also creates a README file for documenting the analysis details.

### Steps to Create an Analysis Structure

1. **Navigate to Your Project's home Directory**: First, ensure you're in the Project main directory where the bin folder is located, so `analysis_creator.py` is located at `./bin/analysis_creator.py`.

2. **Run the Script with Analysis Name**: Execute the `./bin/analysis_creator.py` script by providing the name of your analysis as an argument. This name will be used to create a new directory under `analyses` with subdirectories for `bin`, `input`, and `output`.
   `./analysis_creator.py <Analysis_Name>`

   Replace `<Analysis_Name>` with the desired name for your analysis. For example, if your analysis is named "Spades_assembly_010224", run:
   `./analysis_creator.py Spades_assembly_010224`

Recommendation: Include the date in your analysis name so that re-runs of an analysis are distinguishable.

### What Happens Next?

- A new directory for your analysis will be created under `analyses/<Analysis_Name>`.
- Within this directory, three subdirectories will be created: `bin`, `input`, and `output`.
- A `README.md` file will also be created in the analysis directory. It includes the name of the analysis and the current date. This file is intended for you to document the specifics of the analysis, such as its purpose, methods, and any important findings.

### Benefits of Using `analysis_creator.py`

- **Standardization**: Ensures consistent directory structures across different analyses within the project, making it easier to navigate and understand the project's organization.
- **Documentation**: Encourages the documentation of each analysis, aiding in reproducibility and traceability.
- **Flexibility**: Allows for the easy addition of new analyses to the project without disrupting existing structures.

Remember, maintaining a well-organized and documented project structure is key to successful bioinformatics analyses, especially when working on complex or collaborative projects.



## Need Help?

If you encounter any issues while using this script or have suggestions for improvement, feel free to contribute to the repository by proposing changes via pull requests or by raising issues


```
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
```

**Disclaimer**: This README was generated with the assistance of ChatGPT by OpenAI.
