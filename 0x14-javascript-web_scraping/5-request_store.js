#!/usr/bin/node
const fs = require("fs");
const request = require("request");
const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if ((response, body)) {
    res = body;
    try {
      fs.writeFileSync(filePath, res, "utf-8");
      return;
    } catch (err) {
      console.log(err);
    }
  } else {
    console.error(error);
  }
});
