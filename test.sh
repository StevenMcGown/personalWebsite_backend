sam build && sam local invoke LambdaTestFunction
pip install pytest
pip install boto3
python3 -m pytest hello_world/app_test.py --verbose
ret=$?
if [ "$ret" = 5 ]; then
  echo "No tests collected.  Exiting with 0 (instead of 5)."
  exit 0
fi
exit "$ret"