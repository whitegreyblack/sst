# output_handler.py

"""Defines a general-use function to handle outputs of type list of strings."""

def handle_output(output):
    try:
        message = '\n'.join(output)
    except TypeError as e:
        message = output
    if message:
        print(message)

if __name__ == "__main__":
    handle_output(['This is the output handler'])
