#!/usr/bin/node

const args = process.argv.slice(2);
let i = 0;
while (i < args[0]) {
  console.log('C is fun');
  i++;
}
if (!(args[0])) {
  console.log('Missing number of occurrences');
}
