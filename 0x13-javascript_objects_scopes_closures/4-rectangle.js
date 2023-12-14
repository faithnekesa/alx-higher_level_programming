#!/usr/bin/node
//Definition for class Rectangle which defines a rectangle

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i, j, printString;
    for (i = 0; i < this.height; i++) {
      printString = '';
      for (j = 0; j < this.width; j++) {
        printString += 'X';
      }
      console.log(printString);
    }
  }

  rotate () {
    let tempString;
    tempString = this.height;
    this.height = this.width;
    this.width = tempString;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}

module.exports = Rectangle;
