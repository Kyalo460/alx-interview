#!/usr/bin/node

// import fetch from 'node-fetch';

// const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
// fetch(url)
//   .then(response => {
//     return response.json();
//   })
//   .then(data => {
//     data.characters.forEach(character => {
//       fetch(character)
//         .then(response => {
//           return response.json();
//         })
//         .then(data => {
//           console.log(data.name);
//         })
//         .catch(error => {
//           console.log(error);
//         });
//     });
//   })
//   .catch(error => {
//     console.log(error);
//   });

const request = require('request');

const filmId = process.argv[2];

if (!filmId) {
  console.error('Please provide a film ID as a command-line argument.');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

// Function to make a request and parse JSON
const fetchJson = (url, callback) => {
  request({ url, json: true }, (error, response, body) => {
    if (error) {
      return callback(error);
    }
    callback(null, body);
  });
};

// Fetch film data
fetchJson(url, (error, filmData) => {
  if (error) {
    console.error('Error fetching film data:', error);
    return;
  }

  // Fetch character data
  filmData.characters.forEach(characterUrl => {
    fetchJson(characterUrl, (error, characterData) => {
      if (error) {
        console.error('Error fetching character data:', error);
        return;
      }
      console.log(characterData.name);
    });
  });
});
