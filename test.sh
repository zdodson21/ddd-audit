cd test-element;
# pwd;

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
  "CYGWIN_NT-*" | "MINGW64_NT-*" | "MSYS_NT-10.0"*)
    echo "${BLUE}Running Windows Test...${NC}";
    py ../main.py;
  ;;
  *)
    echo "${BLUE}Unknown Operating System. Aborting.${NC}";
    exit 1;
  ;;
esac
# echo "Test done";