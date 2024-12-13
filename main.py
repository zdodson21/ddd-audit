import os

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

ddd_ignore = []
try:
    with open(".dddignore", "r") as file:
        for line in file:
            ddd_ignore.append(line.strip("/\n"))
except FileNotFoundError:
    pass

developer_mode(f"Ignored files: {ddd_ignore}")


# TODO save list of all JS files to an array 
component_files = []
# for each loop to go through each file in the directory, and append it to the array
# for each loop needs to go through folders as well
# developer_mode(files) when it goes through files
# for loop again to go through files and if it matches a file in the ddd_ignore array, remove it from files







# TODO read the files
# TODO find where the CSS is in the files
# TODO go through each CSS property to discover if it needs to be changed to utilize DDD
# TODO Print the results in the terminal with the line number, what property needs to be changed, and recommendations to change it to
  # TODO Ensure anything that cannot be done with DDD is ignored.
