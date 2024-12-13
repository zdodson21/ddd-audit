# If you are looking to test on Windows, use the psTest.ps1 (PowerShell) or cmdTest.bat (Command Prompt) file.
cd test-element;

BLUE='\033[0;34m'
NC='\033[0m'
case $(uname -s) in
  "Linux"*) 
    echo "${BLUE}Running Linux Test...${NC}";
    python3 ../main.py;
  ;;
  "Darwin"*)
    echo "${BLUE}Running macOS Test...${NC}";
    python3 ../main.py;
  ;;
  *)
    echo "${BLUE}Unknown Operating System. Aborting.${NC}";
    exit 1;
  ;;
esac