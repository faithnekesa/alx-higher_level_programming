#!/usr/bin/node

// Function definition that returns number of occurrences of an element in a list

exports.nbOccurences = function (list, searchElement) {
  return list.filter(x => x === searchElement).length;
};
