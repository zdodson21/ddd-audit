#!/bin/bash
# echo "Running Test";
# echo $OSTYPE;
cd test-element;
# pwd;
case "$OSTYPE" in
  linux*) 
    echo "Linux";
    python3 ../main.py;
  ;;
  darwin*)
    echo "Mac";
    python3 ../main.py;
  ;;
  msys*)
    echo "Windows";
    py ../main.py;
  ;;
  *)
    echo "Unknown";
    exit 1;
  ;;
esac
# echo "Test done";