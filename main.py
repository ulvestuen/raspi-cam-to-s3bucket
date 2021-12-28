from dotenv import load_dotenv

from camera import Camera
from image_scheduler import ImageScheduler
from s3_uploader import S3Uploader

load_dotenv()

if __name__ == '__main__':
    camera = Camera((2592, 1944), "files")
    s3_uploader = S3Uploader()
    image_scheduler = ImageScheduler(camera, s3_uploader)
    image_scheduler.run()
    print("Started raspi-cam-to-s3bucket integration...")
