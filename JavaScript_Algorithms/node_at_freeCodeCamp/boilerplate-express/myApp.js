let dotenv = require("dotenv");
let express = require('express');
let app = express();

// configuring or loading the dotenv
dotenv.config();


console.log("Hello World");
app.get("/", (req, res) => {
	res.send("Hello Express");
});

app.get("/", (req, res) => {
	res.sendFile(path.join(__dirname, "views", "index.html"));
});

app.get("/json", (req, res) => {
	let message = "Hello json";
	if (process.env.MESSAGE_STYLE === "uppercase"){
		message = message.toUpper();
	}
	res.json({"message": message});
});





























 module.exports = app;
