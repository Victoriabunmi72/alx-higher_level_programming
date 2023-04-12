#!/usr/bin/node
// import { argv } from 'node:process';
const arg = process.argv[2];

if (!arg) {
  console.log('No argument');

} else {
  console.log(arg);
}
