# repl.py

"""
Simple loop function to take user input
"""

def user_input(input_handler, prompt='>>> '):
    while 1:
        try:
            user_input = input(prompt)
        except KeyboardInterrupt:
            break
        else:
            if user_input == 'exit':
                break
            output = input_handler(user_input)
            message = '\n'.join(output)
            if message:
                print(message)

if __name__ == "__main__":
    user_input(fn=lambda x: ['base repl loop'])
