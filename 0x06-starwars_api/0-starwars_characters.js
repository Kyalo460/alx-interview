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

import fetch from 'node-fetch';

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

const fetchJson = async (url) => {
  const response = await fetch(url);
  if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
  return response.json();
};

const main = async () => {
  try {
    const filmData = await fetchJson(url);
    for (const characterUrl of filmData.characters) {
      const characterData = await fetchJson(characterUrl);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
};

main();
