const express = require("express")
const app = express();
const bodyParser = require("body-parser")
const cors = require("cors")
const fileRoutes = require('./fileRoutes')

// put routes when needed

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended:true}))
app.use(cors())
app.get('/',(req,res)=>{
    res.send({msg:'msg'})
})
fileRoutes.createRoutes(app)

module.exports = app;