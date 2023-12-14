#!/usr/bin/node
// Definition of class Square which defines a square
// It inherits from Square

const Square_ = require('./5-square');

const Square = class Square extends Square_ {
  charPrint (c) {
    if (c) {
      let printString = '';
      for (let cont = 0; cont < this.height; cont++) {
        for (let cont = 0; cont < this.height; cont++) {
          printString = printString + c;
        }
        console.log(printString);
        printString = '';
      }
    } else {
      super.print();
    }
  }
};

module.exports = Square;
