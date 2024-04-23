#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;
request(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    for (let i = 0; i < characters.length; i++) {
      request(characters[i], function (error, response, body) {
        console.log(error || JSON.parse(body).name);
      });
    }
  }
});
