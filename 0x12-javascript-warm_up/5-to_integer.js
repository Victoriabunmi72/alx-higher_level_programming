#!/usr/bin/node

const number = require('process');
const input = parseInt(number.argv[2]);

if (isNaN(input)) {
  console.log('Not a number');
} else {
  console.log('My number= ' + input);
}
