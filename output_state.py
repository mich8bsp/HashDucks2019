class OutputState(object):

    def __init__(self, slides):
        self.slides = slides

    def add_slide(self, slide):
        self.slides.append(slide)
