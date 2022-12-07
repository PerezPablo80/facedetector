const express = require("express")
const app = require('./server/server')
const server = require('./server/server')
const path = require('path')
require('dotenv').config()

//get port from env or default in 3000
let port = process.env.PORT || 3000;

//allows access to folder files by: url:port/files/file_name
app.use('/files',express.static(path.join(__dirname,"files")))
app.listen(port,()=>{
    console.log(`APP listening on port ${port}`)
})