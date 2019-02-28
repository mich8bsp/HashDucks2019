class InputState(object):

    def __init__(self, images):
        self.images = images

    def add_image(self, image):
        self.images.append(image)
