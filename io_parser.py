import os

from output_state import OutputState
from input_state import InputState


def parse_input_file(file_path):
    with open(os.path.join("input_files", file_path)) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

        return build_input_state(lines)


def build_input_state(input_lines):
    return InputState()


def write_output_to_file(output_state):
    import time
    millis = int(round(time.time() * 1000))
    with open(os.path.join("output_files", "output." + str(millis) + ".txt"), "w+") as out_file:
        out_file.writelines("\n".join(get_out_lines(output_state)))


def get_out_lines(output_state):
    return ["abc"]
