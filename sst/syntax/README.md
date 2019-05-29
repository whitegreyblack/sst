# AST
Abstract Syntax Tree

## Overview
* Create a process to turn user input into a consumable and tokenized expression tree

## Function Order
Starting from user input, the string is passed into the tokenizer to be separated into individual tokens. These tokens will
carry the exact text parsed from the string as well as additional information such as token type (LETTER or NUMBER). The
tokens then be passed as a list into the interpreter then the evaluation functions, which will produce the ast as long as
no errors are found during this process.

## Example Grammar with BST OPs
```
let user_input = "add 1 2 3"
interpret(user_input) =>
  | method_name: add
  | method_args: [
  |   token: (1, NUM) 
  |   token: (2, NUM)
  |   token: (3, NUM)
  | ]
evaluate(tokens) =>
  | something else
```
