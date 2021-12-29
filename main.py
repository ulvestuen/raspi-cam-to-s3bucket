from os import getenv

from dotenv import load_dotenv

from camera import Camera
from image_scheduler import ImageScheduler
from s3_uploader import S3Uploader

load_dotenv()

if __name__ == '__main__':
    print("Starting raspi-cam-to-s3bucket integration...")
    image_files_folder = getenv("RASPI_CAM_ROOT_FOLDER") + "/files"
    camera = Camera((2592, 1944), image_files_folder)
    s3_uploader = S3Uploader(image_files_folder)
    image_scheduler = ImageScheduler(camera, s3_uploader)
    image_scheduler.run()
