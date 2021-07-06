#!/bin/bash
git pull
git add .
read -p "message: " message_var
git commit -m "$message_var"
git push
sam build
sam deploy --confirm-changeset