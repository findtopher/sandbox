# Testing EC2 Resources

This is just me messing around with how to test ec2 resources from boto3 using botocore.stub.Stubber

## Execute the test

Create a Virtual Environment using [pipenv](https://docs.pipenv.org/en/latest/install/)
```
pipenv --three
```

Install the dependencies and execute the tests
```
pipenv install --dev
pipenv run python3 -m pytest tests
```
