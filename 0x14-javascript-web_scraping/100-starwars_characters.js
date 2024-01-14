#!/usr/bin/node
const request = require("request");
const id = process.argv[2];
const url = "https://swapi-api.alx-tools.com/api/films/" + id;

function getCharacter(el) {
  request(el, (error, response, body) => {
    if ((response, body)) {
      console.log(JSON.parse(body).name);
    } else {
      console.error(error);
    }
  });
}

request(url, (error, response, body) => {
  if ((response, body)) {
    res = JSON.parse(body);
    res?.characters?.forEach((el) => {
      getCharacter(el);
    });
  } else {
    console.error(error);
  }
});
