# repl.py

"""
Simple loop function to take user input
"""

from util.output_handler import handle_output

def user_input(input_handler, output_handler, prompt='>>> '):
    """
    Takes in input from user then passes input to input_handler for other code 
    execution. Input handler should return an output of type list of strings.
    """
    while 1:
        try:
            user_input = input(prompt)
        except KeyboardInterrupt:
            break
        else:
            if user_input == 'exit':
                break
            output = input_handler(user_input)
            handle_output(output)

if __name__ == "__main__":
    user_input(input_handler=lambda x: [f'got {x}'], 
               output_handler=handle_output)

