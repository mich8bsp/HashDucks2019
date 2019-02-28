from entities import Orientation, Slide
from input_state import InputState
from output_state import OutputState
import knapsack

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
