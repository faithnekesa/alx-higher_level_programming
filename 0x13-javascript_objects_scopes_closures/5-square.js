#!/usr/bin/node

// Definition of class Square which defines a square
// It inherits from class Rectangle

const Rectangle = require('./4-rectangle');

const Square = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};

module.exports = Square;
