#!/usr/bin/node

const arg2 = parseInt(process.argv[2]);

if (isNaN(arg2)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < arg2; i++) {
    console.log('C is fun');
  }
}
