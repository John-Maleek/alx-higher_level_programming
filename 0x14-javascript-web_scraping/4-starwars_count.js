#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if ((response, body)) {
    const res = JSON.parse(body).results;

    let count = 0;
    res.forEach((el) => {
      const characters = el.characters;
      if (
        characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
      ) {
        count += 1;
      }
    });
    console.log(count);
  } else {
    console.error(error);
  }
});
