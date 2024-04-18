#!/usr/bin/node
// prints all characters of a Star Wars movie

const arg = process.argv[2];
// create url using arg
const url = `https://swapi-api.alx-tools.com/api/films/${arg}/`;

const request = require('request');
// list to store promises
const characterPromise = [];
request(url,
  function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const data = JSON.parse(body);
      const movieCharacters = data.characters;
      // loop through characters link
      movieCharacters.forEach((item) => {
        const characterName = new Promise((resolve, reject) => {
          request(item, (error, response, body) => {
            if (error) {
              reject(error);
            } else {
              const data = JSON.parse(body);
              resolve(data.name);
            }
          });
        });
        // append each promise
        characterPromise.push(characterName);
      });
      // use promise.all() to wait for all promise to settle
      Promise.all(characterPromise)
        .then(names => {
          // print names in order
          names.forEach(name => {
            console.log(name);
          });
        })
        .catch(error => {
          console.error(error);
        });
    }
  });
