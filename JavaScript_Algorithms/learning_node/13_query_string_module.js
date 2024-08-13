const querystring = require('querystring');

const url = 'https://www.example.com/p/a/t/h?course=node&lesson=http';

// Isolate query string from url
const queryToParse = url.split('?')[1];
console.log(queryToParse)

// Parse query string into object, then add new property
const parsedQuery = querystring.parse(queryToParse);
parsedQuery.exercise = 'querystring';

// Rebuild query string from object
const modifiedQueryString = querystring.stringify(parsedQuery);