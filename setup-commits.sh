#!/bin/bash
# run this once inside the folder, it makes the commits one by one
# then add your remote and push (steps printed at the end)
git init -b main
git add .gitignore && git commit -m "add gitignore"
git add requirements.txt && git commit -m "add requirements, just fastapi and uvicorn"
git add main.py && git commit -m "first endpoints, events kept in a list for now"
git add .devcontainer && git commit -m "devcontainer so codespaces just works"
git add README.md && git commit -m "write the readme"
echo ""
echo "done. now:"
echo "  git remote add origin https://github.com/elvis-cdev/gdg-mku-backend-starter.git"
echo "  git push -u origin main"
