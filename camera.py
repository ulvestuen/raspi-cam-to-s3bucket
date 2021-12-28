from picamera import PiCamera
from time import sleep


class Camera:
    def __init__(self, resolution, output_folder):
        self.camera = PiCamera()
        self.camera.resolution = resolution
        self.output_folder = output_folder

    def take_picture(self, filename="image.jpg"):
        self.camera.start_preview()
        sleep(2)
        self.camera.capture(self.output_folder + filename)
        self.camera.stop_preview()
