#!/usr/bin/node
const Bunmi = require('process');
const input = Bunmi.argv[2];

if (input) {
	console.log(input);
} else {
	console.log(No input);
}
