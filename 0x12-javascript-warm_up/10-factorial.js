#!/usr/bin/node

//Script that computes and prints a factorial'

const n = require('process');
const value = parseInt(n.argv[2]);

function myFactorial(value){
	if (value === 1 || value === undefined)
	{  console.log(1);
	}  else  {
		console.log(value * myFactorial(value - 1));
	}
}
myFactorial(value);
