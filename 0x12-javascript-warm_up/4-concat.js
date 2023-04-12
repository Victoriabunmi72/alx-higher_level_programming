#!/usr/bin/node

const container = require('process');
const result1 = container.argv[2];
const result2 = container.argv[3];

console.log(result1 + ' is ' + result2);
