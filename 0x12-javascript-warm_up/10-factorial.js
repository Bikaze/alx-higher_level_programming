#!/usr/bin/node

function factorial (n) {
  n = parseInt(n);
  if (isNaN(n) || n <= 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

const argv = process.argv;

console.log(factorial(argv[2]));
