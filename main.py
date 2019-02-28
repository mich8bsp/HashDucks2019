from io_parser import parse_input_file, write_output_to_file
from logic import run_logic

if __name__ == "__main__":
    input_file_path = 'test.txt'
    state = parse_input_file(input_file_path)
    output_state = run_logic(state)
    write_output_to_file(output_state)
