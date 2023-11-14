#!/usr/bin/node

exports.addMeMaybe = function (var1, callBack) {
  var1 = var1 + 1;
  callBack(var1);
}
