import os
from styles import *
from prettytable import PrettyTable

class colors:
    RED='\033[91m'
    GREEN='\033[92m'
    YELLOW='\033[93m'
    ORANGE='\033[94m'
    BLUE='\033[94m'
    MAGENTA='\033[95m'
    CYAN='\033[96m'
    GRAY='\033[90m'
    RESET='\033[0m'

# ! Developer Mode
developerModeEnabled = True #TODO Change to false when done

def developer_mode(message):
    if developerModeEnabled:
        print(f"{colors.YELLOW}Developer Mode: {colors.GRAY}{message}")

# ! Variables
pwd = os.getcwd()
ddd_ignore = []
component_files = []
ignore_exists = True
audit_output = []

def get_dddignore():
    """
    Gets values from .dddignore if it exists
    """
    try:
        with open(".dddignore", "r") as file:
            for line in file:
                if not line.startswith("#") and line.strip():
                    ddd_ignore.append(line.strip("/\n"))
                else:
                    pass
        return True
    except FileNotFoundError as error:
        print(f"{colors.RED}{error}")
        return False

def get_files(directory):
    """
    Gets files to audit, ignoring files in .dddignore
    """
    developer_mode(f"{colors.MAGENTA}Getting files from {directory}")
    
    for file in os.listdir(directory):
        developer_mode(f"Examining {file}")
        if os.path.isdir(os.path.join(directory, file)) and file != "node_modules" and file not in ddd_ignore:
            developer_mode(f"{colors.RED}Recursively getting files from {file}")
            get_files(os.path.join(directory, file))
        elif file.endswith(".js") and file not in ddd_ignore:
            developer_mode(f"{colors.GREEN}Adding {file}")
            component_files.append(file)
        else:
            developer_mode(f"{colors.BLUE}Skipping {file}")

# Start auditing
def audit_files():
    """
    Audits files, outputs to terminal the line number, what property needs to be changed, and recommendations to change it to
    """
    for file in component_files:
        developer_mode(f"{colors.GREEN}Auditing {file}")
    # TODO Audit file

# TODO find where the CSS is in the files
# TODO go through each CSS property to discover if it needs to be changed to utilize DDD

def output_table(auto_audit: bool):
    """
    Outputs a table of audited data, color coded to tell the user what can automatically be changed
    """
    # TODO REMOVE THIS LINK: https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data
    table = PrettyTable(['Line Number', 'Property', 'Recommended Change'])
    # TODO for loop add values, branch based on auto_audit value, color code everything. 


if __name__ == "__main__":
    developer_mode("Activated")

    developer_mode(f"Script called from: {colors.BLUE}{pwd}")

    # Gets .dddignore
    if(get_dddignore()):
        developer_mode("Found .dddignore")
    else:
        developer_mode("Unable to find .dddignore")
        ignore_exists = False
    developer_mode(f"Ignored files: {ddd_ignore}")

    # Gets files to audit
    get_files(pwd)
    developer_mode(f"Files to audit: {component_files}")

    # Audits files
    audit_files()