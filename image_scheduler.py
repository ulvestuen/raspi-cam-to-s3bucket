import time
from os import getenv
from sched import scheduler

from camera import Camera
from s3_uploader import S3Uploader


class ImageScheduler:
    def __init__(self, camera: Camera, s3_uploader: S3Uploader):
        self.camera = camera
        self.s3_uploader = s3_uploader
        self.scheduler = scheduler(time.time, time.sleep)

    def schedule_new_picture(self):
        self.scheduler.enter(float(getenv("S3_UPLOAD_INTERVAL")),
                             1,
                             self.take_picture_upload_and_reschedule)

    def take_picture_upload_and_reschedule(self):
        self.camera.take_picture()
        print("Image captured")

        self.s3_uploader.upload_files()
        print("Image uploaded to S3")

        self.schedule_new_picture()
        print("New image capture scheduled")

    def run(self):
        self.take_picture_upload_and_reschedule()
        self.scheduler.run()
