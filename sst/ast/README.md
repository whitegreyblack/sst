# AST
Abstract Syntax Tree

## Overview
* Create a process to turn user input into a consumable and tokenized expression tree

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
