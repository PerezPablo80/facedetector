const express = require("express")
const app = express();
const bodyParser = require("body-parser")
const cors = require("cors")
const fileUpload = require('express-fileupload')
const fileRoutes = require('./fileRoutes')

//force body to be in json format
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended:true}))

//allows cross origin
app.use(cors())

//for files, needed express-fileupload
app.use(fileUpload({createParentPath:true}))

// put routes when needed
fileRoutes.createRoutes(app)

module.exports = app;