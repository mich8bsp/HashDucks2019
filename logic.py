from entities import Orientation, Slide
from input_state import InputState
from output_state import OutputState
import knapsack


def calc_pair_score(slide1, slide2):
    intersections = len(slide1.tags.intersection(slide2.tags))

    if intersections > len(slide1):
        if len(slide1.tags) > len(slide2.tags):
            return len(slide2.tags)
        return len(slide1.tags)
    if intersections > len(slide2):
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