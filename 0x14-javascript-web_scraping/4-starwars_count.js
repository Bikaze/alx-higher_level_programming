#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const data = JSON.parse(body).results;
    const sum = data.reduce((count, episode) => {
      return episode.characters.find((character) => character.endsWith('/18/')) ? count + 1 : count;
    }, 0);
    console.log(sum);
  }
});
