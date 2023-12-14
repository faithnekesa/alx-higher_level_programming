#!/usr/bin/node
// Function that returns reversed version of a list

exports.esrever = function (list) {
  let len = list.length - 1;
  let i = 0;
  while ((len - i) > 0) {
    const temipList = list[len];
    list[len] = list[i];
    list[i] = temipList;
    i++;
    len--;
  }
  return list;
};
