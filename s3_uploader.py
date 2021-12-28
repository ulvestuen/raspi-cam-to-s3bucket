import mimetypes
from os import listdir, getenv

import boto3


class S3Uploader:
    def __init__(self):
        self.s3 = boto3.resource('s3')
        self.bucket = self.s3.Bucket(getenv('S3_BUCKET_NAME'))

    def upload_files(self):
        for filename in listdir('files'):
            with open('files/' + filename, 'rb') as data:
                key = filename
                self.bucket.put_object(
                    Key=key,
                    Body=data,
                    ContentType=mimetypes.guess_type(filename)[0],
                    Metadata={
                        'Content-Type': mimetypes.guess_type(filename)[0]
                    }
                )
                object_acl = self.s3.ObjectAcl(getenv('S3_BUCKET_NAME'), key)
                object_acl.put(ACL='public-read')
