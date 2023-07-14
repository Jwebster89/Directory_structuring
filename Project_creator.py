#!/usr/bin/env python

import os, sys, subprocess

def create_project_structure(project_name):
    # Create the project directory
    os.makedirs(project_name)

    # Create the analyses directory
    os.makedirs(os.path.join(project_name, 'analyses'))

    # Create the bin directory
    os.makedirs(os.path.join(project_name, 'bin'))

    os.makedirs(os.path.join(project_name, 'docs'))
    os.makedirs(os.path.join(project_name, 'raw', 'sequence_data'))
    os.makedirs(os.path.join(project_name, 'raw', 'SRA'))

    # Create the data, docs, and raw directories
    os.makedirs(os.path.join(project_name, 'data', 'assembly'))
    os.makedirs(os.path.join(project_name, 'data', 'assembly', 'input'))
    os.makedirs(os.path.join(project_name, 'data', 'assembly', 'logs'))
    os.makedirs(os.path.join(project_name, 'data', 'assembly', 'output'))
    os.makedirs(os.path.join(project_name, 'data', 'processed_raw'))
    os.makedirs(os.path.join(project_name, 'data', 'references'))

        
    # Create the driver_script.py file in the bin directory
    driver_script_path = os.path.join(project_name, 'bin', 'driver_script.py')
    with open(driver_script_path, 'w') as driver_script:
        driver_code='''\
#!/usr/bin/env python

# This script is for being able to re-run an entire analysis. Keep up to date with project methods.
 
'''
        driver_script.write(driver_code)

    # Create the analysis_creator.py script in the bin directory of analysis1
    analysis_creator_path = os.path.join(project_name, 'bin', 'analysis_creator.py')
    with open(analysis_creator_path, 'w') as analysis_creator:
        analysis_code='''\
#!/usr/bin/env python
import os, sys
from datetime import date

def create_analysis_structure(analysis_name):
    os.makedirs(os.path.join('analyses', analysis_name, 'bin'))
    os.makedirs(os.path.join('analyses', analysis_name, 'input'))
    os.makedirs(os.path.join('analyses', analysis_name, 'output'))
    with open(os.path.join('analyses', analysis_name, 'README.md'), 'w') as readme_h:
        readme_name = f'# {analysis_name}'
        current_date = date.today().strftime("%d-%m-%Y")
        readme_date = f'## {current_date}\\n'
        readme_h.write(f'{readme_name}\\n')
        readme_h.write(readme_date)

analysis_name=sys.argv[1]
create_analysis_structure(analysis_name)
'''
        analysis_creator.write(analysis_code)
    
    os.chmod(analysis_creator_path, 0o755)

def print_usage():
    print("Usage: python Project_creator.py <Project_name>")

if len(sys.argv) != 2:
    print("Error: Please provide the Project name.")
    print_usage()
    sys.exit(1)

project_name = sys.argv[1]
create_project_structure(project_name)

# Initialize a Git repository
subprocess.run(['git', 'init'], cwd=project_name)