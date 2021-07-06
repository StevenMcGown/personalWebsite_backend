#!/bin/bash
git pull
git add .
git commit -m "Automatic SAM deploy"
git push
sam build
sam deploy --confirm-changeset