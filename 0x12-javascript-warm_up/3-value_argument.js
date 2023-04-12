#!/usr/bin/node
const proc = require('process');
const arg = proc.argv[2];

if (arg) {
  console.log('No argument');
} else {
  console.log(arg);
}
