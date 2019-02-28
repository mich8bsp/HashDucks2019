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
