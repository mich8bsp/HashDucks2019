class OutputState(object):

    def __init__(self, slides):
        self.slides = slides

    def add_slide(self, slide):
        self.slides.append(slide)

    def __str__(self):
        result = ""
        for slide in self.slides:
            result += (" ".join([str(id) for id in slide.ids])) + "\n"
        return result