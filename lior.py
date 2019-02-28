import time

import io_parser
from entities import *
from logic import validate, arrange_vertical_images, InvalidSolution
from output_state import OutputState


def match_verticals(slides_by_size, images_by_size):
    waiting_vertical = None
    for size in images_by_size.keys():
        for image in images_by_size[size]:
            if waiting_vertical is not None:
                add_to_mapping(Slide([image, waiting_vertical]), slides_by_size)
                waiting_vertical = None
            else:
                waiting_vertical = image


def run_logic(input_state):
    slides_by_size = {}
    images_by_size = {}
    verticals = []

    images = input_state.images

    for image in images:
        if image.orientation is Orientation.HORIZONTAL:
            add_to_mapping(Slide([image]), slides_by_size)
        else:
            add_to_mapping(image, images_by_size)
            verticals += [image]

    match_verticals(slides_by_size, images_by_size)

    result = []

    for slide_size in slides_by_size.keys():
        result += slides_by_size[slide_size]
    # result += arrange_vertical_images(verticals)

    return OutputState(result)


def add_to_mapping(image, images_by_size):
    images_by_size[len(image.tags)] = images_by_size.get(len(image.tags), []) + [image]


if __name__ == "__main__":
    file_a = "a_example.txt"
    file_b = "b_lovely_landscapes.txt"
    file_c = "c_memorable_moments.txt"
    file_d = "d_pet_pictures.txt"
    file_e = "e_shiny_selfies.txt"
    start_time = time.clock()
    input = io_parser.parse_input_file(file_e)
    output = run_logic(input)
    end_process_time = time.clock()
    try:
        is_valid = validate(input, output)
    except InvalidSolution as e:
        print(e.reason)
    else:
        is_vaild = False
    end_validation_time = time.clock()
    if not is_valid:
        print("invalid output!")
    else:
        print("valid output!")
    print(output)
    print("processing time: " + str(end_process_time - start_time))
    print("validation time: " + str(end_validation_time - end_process_time))
