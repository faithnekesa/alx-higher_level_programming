#!/usr/bin/node

// Function that converts a number from base 10 to base no passed as argument
// with Closure

exports.converter = function (base) {
  function myConverter (n) {
    return n.toString(base);
  }

  return myConverter;
};
