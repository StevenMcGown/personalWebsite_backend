#!/bin/bash
git add .
git commit -m "Automatic SAM deploy"
git push
sam build && sam deploy