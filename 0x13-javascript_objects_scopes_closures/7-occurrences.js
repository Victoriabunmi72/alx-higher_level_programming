#!/usr/bin/node

const nboccurences = (list, searchElement) => list.filter((element) => searchElement === element).length;

module.exports = { nboccurences };
