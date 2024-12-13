import os

# ! Developer Mode
developerModeEnabled = True #TODO Change to false when done

def developer_mode(message):
  if developerModeEnabled:
    print(f"Developer Mode: {message}")

developer_mode("Activated")

# ! Main code
# TODO find .dddignore file
# TODO for each loop through .dddignore, adding to ignore list
ddd_ignore = []
with open(".dddignore", "r") as file:
  for line in file:
    ddd_ignore.append(line.strip())
developer_mode(ddd_ignore)

pwd = os.getcwd()
developer_mode(f"Script called from: {pwd}")
# TODO save list of all JS files to an array 
files = []
# for each loop to go through each file in the directory, and append it to the array
# for each loop needs to go through folders as well







# TODO read the files
# TODO find where the CSS is in the files
# TODO go through each CSS property to discover if it needs to be changed to utilize DDD
# TODO Print the results in the terminal with the line number, what property needs to be changed, and recommendations to change it to
  # TODO Ensure anything that cannot be done with DDD is ignored.


