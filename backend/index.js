const express = require("express")
const app = require('./server/server')
const server = require('./server/server')
const path = require('path')
require('dotenv').config()

let port = process.env.PORT || 3000;
app.use('/files',express.static(path.join(__dirname,"files")))
app.listen(port,()=>{
    console.log(`APP listening on port ${port}`)
})