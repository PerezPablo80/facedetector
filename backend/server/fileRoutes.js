
// const file = require('./file')
exports.createRoutes = function(app){
    app.get('/file',function(req,res){
        res.send({message:"Should send file list"})
    });
    app.get('/ff',function(req,res){
        res.send({message:"Should send ff"})
    });
}