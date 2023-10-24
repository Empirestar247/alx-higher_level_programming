#!/usr/bin/node
const request = require('request');

const episodeId = process.argv[2];

if (parseInt(episodeId) < 8) {
  const url = 'https://swapi-api.hbtn.io/api/films/' + episodeId;

  request(url, (error, response, body) => {
    if (error) {
      return console.log(error);
    }
    console.log(JSON.parse(body).title);
  });
}
