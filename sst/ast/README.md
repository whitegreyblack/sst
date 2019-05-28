# AST
Abstract Syntax Tree

## Overview
* Create a process to turn user input into a consumable and tokenized expression tree

## Function Order
Starting from user input, the string is passed into the interpreter to build a set of tokens indicating WORD or INT values. 
These are then passed into the evaluate function to determine if the tokenized string is well formed and can be further 
transformed into a valid ast statement.
Finally, if no errors are found during evaluation, then an AST is produced.

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
