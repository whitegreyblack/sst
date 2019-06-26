# reader.py

"""
Simple file reader to pull all characters from file
"""

from util.output_handler import handle_output


def from_file(input_handler, output_handler, file_name):
    with open(file_name, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    for line in lines:
        output = input_handler(line)
        output_handler(output)

if __name__ == "__main__":
    from_file(
        input_handler=lambda x: [f'got {x}'], 
        output_handler=handle_output,
        file_name='instructions.txt'
    )

