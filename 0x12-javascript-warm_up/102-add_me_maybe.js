#!/usr/bin/node

function addMeMaybe (x, funct) {
  funct(++x);
}

module.exports = { addMeMaybe };
