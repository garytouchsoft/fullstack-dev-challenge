# Full-stack web developer challenge


## Required Environment variables

export AWS_ACCESS_KEY_ID=[aws id with read and write s3 access]
export AWS_SECRET_ACCESS_KEY=[aws secret key]
export AWS_STORAGE_BUCKET_NAME=[desired bucket]


## Setup Steps

python -m venv .env
source .env/bin/activate
cd [project root]
pip install -r requirements.txt
python manage.py runserver


## Contents

Main shop page:
http://127.0.0.1:8000/

Api view:
http://127.0.0.1:8000/api

Admin:
http://127.0.0.1:8000/admin
admin
asd$fdd%6dgNMbvFw£s


When a shoe order is made a json file is saved to S3.


My bucket has block public disabled and a policy:

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::garyk-static/*"
        }
    ]
}




