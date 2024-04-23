#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const data = JSON.parse(body);
    const completed = {};
    for (const task of data) {
      if (task.completed && !completed[task.userId]) {
        completed[task.userId] = 1;
      } else if (task.completed) {
        completed[task.userId] = (completed[task.userId] || 0) + 1;
      }
    }
    console.log(completed);
  }
});
