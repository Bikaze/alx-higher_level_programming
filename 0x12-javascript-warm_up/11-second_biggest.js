#!/usr/bin/node

let argv = process.argv;
let array;

if (argv.length < 4) {
  console.log(0);
} else {
  argv = argv.slice(2);
  for (let i = 0; i < argv.length; i++) {
    argv[i] = parseInt(argv[i]);
  }
  argv.sort((a, b) => (b - a));
  array = argv.filter(item => item !== argv[0]);
  console.log(array[0]);
}
