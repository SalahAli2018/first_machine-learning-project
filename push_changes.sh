#!/bin/bash

git init
git add .
git commit -m "first commit"
git tag -a v1.0.1 -m "Version 1.0.1"
# git remote add origin https://github.com/SalahAli2018/first_machine-learning-project.git
git push -u origin master --tags