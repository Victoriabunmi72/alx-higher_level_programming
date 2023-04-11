#!/usr/bin/node
// import { argv } from 'node:process';
const { argv } = require('process');
const Bunmi = argv.length;

if (Bunmi <= 2) {
  console.log('No argument');
} else if (Bunmi === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
