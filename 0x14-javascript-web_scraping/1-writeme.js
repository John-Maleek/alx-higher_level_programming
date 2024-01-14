#!/usr/bin/node
const fs = require("fs");
const filePath = process.argv[2];
const textToWrite = process.argv[3];

try {
  fs.writeFileSync(filePath, textToWrite, "utf-8");
  return;
} catch (err) {
  console.log(err);
}
