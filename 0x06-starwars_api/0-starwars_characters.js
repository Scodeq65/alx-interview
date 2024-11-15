#!/usr/bin/node
/**
 * Script to print all characters of a Star Wars movie
 * Usage: ./0-starwars_characters.js <Movie ID>
 */

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// API URL to retrieve movie information
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a request to get the movie data
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    const characters = data.characters;

    // Fetch each character's name in sequence
    characters.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    });
  } else {
    console.error(`Error: Could not retrieve movie with ID ${movieId}`);
  }
});
