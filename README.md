# raspi-cam-to-s3bucket
### Prerequisites for running the raspi-cam-to-s3bucket integration
* Clone the source code of `raspi-cam-to-s3bucket` from the [raspi-cam-to-s3bucket GitHub-repository](https://github.com/ulvestuen/raspi-cam-to-s3bucket) 
##Run on host machine
### Setup
The `raspi-cam-to-s3bucket` integration relies on the following
environmental variables:
```
export S3_BUCKET_NAME=...
export S3_UPLOAD_INTERVAL=60

export AWS_REGION=...
export AWS_ACCESS_KEY_ID=...
export AWS_SECRET_ACCESS_KEY=...
```

From within the `raspi-cam-to-s3bucket/` folder, first create a python virtual environment:
```
python3 -m venv env
```
Activate the python virtual environment:
```
source env/bin/activate
```
Install dependencies:
```
pip install -r requirements.txt
```

### Start the application
```
python3 main.py
```
