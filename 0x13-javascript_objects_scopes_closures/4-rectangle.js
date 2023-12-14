#!/usr/bin/node
// Definition for class Rectangle which defines a rectangle
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let printString = '';
      for (let j = 0; j < this.width; j++) {
        printString += 'X';
      }
      console.log(printString);
    }
  }

  rotate () {
    const tempString = this.width;
    this.width = this.height;
    this.height = tempString;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
