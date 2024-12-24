import os
from styles import *

# ! Developer Mode
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

developerModeEnabled = True #TODO Change to false when done

def developer_mode(message):
    if developerModeEnabled:
        print(f"{colors.YELLOW}Developer Mode: {colors.GRAY}{message}")

developer_mode("Activated")

# ! Main code
pwd = os.getcwd()
developer_mode(f"Script called from: {colors.BLUE}{pwd}")

# Get list of files to ignore
ddd_ignore = []

# Gets .dddignore if exist
try:
    with open(".dddignore", "r") as file:
        for line in file:
            if not line.startswith("#") and line.strip():
                ddd_ignore.append(line.strip("/\n"))
            else:
                pass
except FileNotFoundError:
    pass

developer_mode(f"Ignored files: {ddd_ignore}")

# Get list of files to audit
component_files = []
def get_files(directory):
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

get_files(pwd)

developer_mode(f"Files to audit: {component_files}")

# Start auditing
for file in component_files:
    developer_mode(f"{colors.GREEN}Auditing {file}")
    # TODO Audit file

# TODO find where the CSS is in the files
# TODO go through each CSS property to discover if it needs to be changed to utilize DDD
# TODO Print the results in the terminal with the line number, what property needs to be changed, and recommendations to change it to
  # TODO Ensure anything that cannot be done with DDD is ignored.
