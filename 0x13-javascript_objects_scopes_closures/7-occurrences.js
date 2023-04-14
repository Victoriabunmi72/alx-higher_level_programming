#!/usr/bin/node

exports.nboccurences = function (list, searchElement) {
  return (list.filter(data => data === searchElement).length);
};
