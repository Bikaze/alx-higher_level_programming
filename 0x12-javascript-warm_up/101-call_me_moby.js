#!/usr/bin/node

function callMeMoby (x, funct) {
  for (let i = 0; i < x; i++) {
    funct();
  }
}

module.exports = { callMeMoby };
