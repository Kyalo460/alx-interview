#!/usr/bin/node

import fetch from 'node-fetch';

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
fetch(url)
  .then(response => {
    return response.json();
  })
  .then(data => {
    data.characters.forEach(character => {
      fetch(character)
        .then(response => {
          return response.json();
        })
        .then(data => {
          console.log(data.name);
        })
        .catch(error => {
          console.log(error);
        });
    });
  })
  .catch(error => {
    console.log(error);
  });
