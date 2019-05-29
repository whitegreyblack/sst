# reader.py

"""
Simple file reader to pull all characters from file
"""

def from_file(input_handler, file_name):
    with open(file_name, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    for line in lines:
        output = input_handler(line)
        try:
            message = '\n'.join(output)
        except TypeError as e:
            message = output
        if message:
            print(message)

if __name__ == "__main__":
    from_file(input_handler=lambda x: print(x), file_name='instructions.txt')

