#!/usr/bin/node

function esrever (list) {
  let p;
  const len = list.length;
  for (let i = 0; i < len / 2; i++) {
    p = list[i];
    list[i] = list[len - (i + 1)];
    list[len - (i + 1)] = p;
  }
  return list;
}

module.exports = { esrever };
