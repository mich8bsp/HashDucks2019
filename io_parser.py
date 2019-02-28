import os

from entities import Photo
from output_state import OutputState
from input_state import InputState
import time


def parse_input_file(file_path):
    # type: (str) -> InputState
    with open(os.path.join("input_files", file_path)) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

        return build_input_state(lines)


def build_input_state(input_lines):
    photos_num = int(input_lines[0])
    photos = [build_photo(i, input_lines[i+1]) for i in range(photos_num)]

    return InputState(photos)

def build_photo(id, photo_line):
    params = photo_line.split()
    orientation = params[0]
    tags_num = int(params[1])
    tags = set([params[i+2] for i in range(tags_num)])
    Photo(id, orientation, tags)



def write_output_to_file(output_state):
    # type: (OutputState) -> None
    millis = int(round(time.time() * 1000))
    with open(os.path.join("output_files", "output." + str(millis) + ".txt"), "w+") as out_file:
        out_file.writelines("\n".join(get_out_lines(output_state)))


def get_out_lines(output_state):
    # type: (OutputState) -> [str]
    return ["abc"]
