#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];

try {
  const text = fs.readFileSync(filePath, 'utf-8');
  console.log(text);
} catch (err) {
  console.log(err);
}
