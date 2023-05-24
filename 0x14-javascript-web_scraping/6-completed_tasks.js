#!/usr/bin/node
//script that computes the number of tasks completed by user id.
const request = require('request');
const url = process.argv[2];

request(url, (err, resp, body) => {
  if (err) { console.log(err); }

  const completed = {};
  const jsonBody = JSON.parse(body);
  for (const task of jsonBody) {
    if (task.completed) {
      if (completed[task.userId]) {
        completed[task.userId]++;
      } else {
        completed[task.userId] = 1;
      }
    }
  }
  console.log(completed);
});
