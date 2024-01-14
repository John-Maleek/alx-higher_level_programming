#!/usr/bin/node
const request = require("request");
const url = process.argv[2];

request(url, (error, response, body) => {
  if ((response, body)) {
    res = JSON.parse(body);

    let arr = [];
    res.forEach((el) => {
      user = el.userId;
      if (!arr.includes(user)) {
        arr.push(user);
      }
    });

    let obj = {};
    arr.forEach((el) => {
      let count = 0;
      res.forEach((item) => {
        if (item.userId === el && item.completed) {
          count += 1;
          obj[`${el}`] = count;
        }
      });
    });

    console.log(obj);
  } else {
    console.error(error);
  }
});
