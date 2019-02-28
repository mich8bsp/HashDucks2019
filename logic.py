from entities import Orientation, Slide
from output_state import OutputState


def calc_pair_score(slide1, slide2):
    intersections = len(slide1.tags.intersection(slide2.tags))

    if intersections > len(slide1.tags):
        if len(slide1.tags) > len(slide2.tags):
            return len(slide2.tags)
        return len(slide1.tags)
    if intersections > len(slide2.tags):
        return len(slide2.tags)
    return intersections


def calc_score(slides):
    score = 0
    for index, slide in enumerate(slides):
        if index + 1 < len(slides):
            score += calc_pair_score(slide, slides[index + 1])

    return score


def run_logic(input_state):
    images = input_state.images
    if len(images) == 1:
        image = images[0]
        if image.orientation == Orientation.VERTICAL:
            raise Exception("WTF")
        output_state = OutputState([image.id])
    else:
        if images[0].orientation == Orientation.HORIZONTAL:
            output_state = OutputState([Slide([images[0]])])
        elif images[1].orientation == Orientation.HORIZONTAL:
            output_state = OutputState([Slide([images[1]])])
        else:
            output_state = OutputState([Slide([images[0], images[1]])])
    return output_state


def distinct_vertical_tags(image1, image2):
    pass


class InvalidSolution(Exception):
    def __init__(self, reason):
        self.reason = reason

class InvalidInput(Exception):
    def __init__(self, reason):
        self.reason = reason


def validate(input_state, output_state):
    input_size = len(input_state.images)
    for i in range(len(input_state.images)):
        if i != input_state.images[i].id:
            raise InvalidInput("input image " + str(input_state.images[i]) + " makes no sense")
    id_to_Image = {}
    for image in input_state.images:
        id_to_Image[image.id] = image

    ids_seen = set()
    for slide in output_state.slides:
        if not isinstance(slide, Slide):
            raise InvalidSolution("this appears in the outout but is not a slide:" + str(slide))
        if len(slide.ids) > 2 or len(slide.ids) == 0:
            raise InvalidSolution("slide " + str(slide.ids) + "invalid length")

        for id in slide.ids:
            if id in ids_seen or id >= input_size:
                raise InvalidSolution("recurring photo id: " + str(id))
            else:
                ids_seen.add(id)
            if len(slide.ids) == 2:
                if id_to_Image[slide.ids[0]].orientation == Orientation.HORIZONTAL or \
                        id_to_Image[slide.ids[1]].orientation == Orientation.HORIZONTAL:
                    raise InvalidSolution("image " + str(slide.ids[0]) + " and " + str(
                        slide.ids[1]) + " slided together altough one is horizontal")
            elif len(slide.ids) == 1:
                if id_to_Image[slide.ids[0]].orientation == Orientation.VERTICAL:
                    raise InvalidSolution("lonely vertical in slide: " + str(slide.ids[0]))
    return True
