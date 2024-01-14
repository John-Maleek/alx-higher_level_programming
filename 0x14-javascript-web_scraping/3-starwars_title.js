#!/usr/bin/node
const request = require("request");
const id = process.argv[2];

request(
  `https://swapi-api.alx-tools.com/api/films/${id}`,
  (error, response, body) => {
    if ((response, body)) {
      console.log(JSON.parse(body).title);
    } else {
      console.error(error);
    }
  }
);
