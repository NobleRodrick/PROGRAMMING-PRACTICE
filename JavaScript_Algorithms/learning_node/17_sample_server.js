const http = require('http');

// Handle GET Request
const handleGetRequest = (req, res) => {
  const options = {
    hostname: 'static-assets.codecademy.com',
    path: '/Courses/Learn-Node/http/data.json',
    method: 'GET'
  }

  const request = http.request(options, (response) => {
    let data = '';

    response.on('data', (chunk) => {
      data += chunk;
    });

    response.on('end', (chunk) => {
      res.end(data);
    });
  });

  request.end()
}

// Creates server instance
const server = http.createServer((req, res) => {
  const { method } = req;
 
  switch(method) {
    case 'GET':
      return handleGetRequest(req, res);
    default:
      throw new Error(`Unsupported request method: ${method}`);
  }
});

// Starts server listening on specified port
server.listen(4001, () => {
  const { address, port } = server.address();
  console.log(`Server is listening on: http://${address}:${port}`);
});