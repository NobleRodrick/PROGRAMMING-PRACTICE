const readline = require("readline");
const fs = require("fs");

const myInterface = readline.createInterface({
  input: fs.createReadStream("shoppingList.txt"),
});
const fileStream = fs.createWriteStream("shoppingResults.txt");

let transformData = (line) => {
  fileStream.write(`They were out of: ${line}\n`);
};

myInterface.on("line", transformData);
