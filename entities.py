from enum import Enum


class Orientation(Enum):
    HORIZONTAL = "H"
    VERTICAL = "V"


class Photo(object):

    def __init__(self, id, orientation, tags):
        self.id = id
        self.orientation = orientation
        self.tags = tags
        self.numTags = len(tags)

class Slide(object):

    def __init__(self, images):
        self.ids = [x.id for x in images]
        self.tags = set()
        for image in images:
            for tag in image.tags:
                self.tags.add(tag)

    # def __init__(self, ids, tags):
    #     self.ids = ids  # list
    #     self.tags = tags  # set
