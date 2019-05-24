# sst
A Simple Syntax Tree

## Overview
  * Currently uses two projects: AST and BST. 
    * AST covers evaluation and translation of valid input into an expression tree.
    * BST covers tree operations for a binary search tree. This will be used for demoing the effectiveness of the AST expression tree.
  * This project aims to create a simple library to build a two-word or more parser for use in other projects.

## Usage:
* Run the bst demo that uses the sst as in interface to call bst operations:
  * `py -m bst.repl`
* Import the bst tree object as an object in python repl:
  * `from bst.tree import Tree`

## Features:
  * Interpreter to recognize basic tokens such as words or numbers.

## Wants and TODOs:
  * Ability to add patterns to recognize non numeric or alphabetic tokens (ie '\d+d\d+(+|-\d)' to recognize die roll pattern)
