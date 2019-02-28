from entities import Orientation
from input_state import InputState
from output_state import OutputState
import knapsack

def run_logic(input_state):
    images = input_state.images
    if len(images == 1):
        image = images[0]
        if image.orientation == Orientation.VERTICAL:
            raise Exception("WTF")
        output_state = OutputState([image.id])
    else:
        if images[0].orientation == Orientation.HORIZONTAL:
            output_state = OutputState([images[0].id])
        elif images[1].orientation == Orientation.HORIZONTAL:
            output_state = OutputState([images[1].id])
        else:
            output_state = OutputState([images[0].id], images[1].id)
    return output_state
