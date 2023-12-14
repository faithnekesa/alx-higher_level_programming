#!/usr/bin/node
// script that imports a dictionary of occurrences by user id
// and computes a dictionary of user ids by occurrence

const { dict } = require('./101-data.js');
const myDict = {};
for (const N in dict) {
    if (myDict[dict[N]] === undefined) {
	myDict[dict[N]] = [];
    }
    myDict[dict[N]].push(N);
}
console.log(myDict);
