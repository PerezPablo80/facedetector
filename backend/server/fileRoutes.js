
const File = require('./file')
exports.createRoutes = function(app){
    const file=new File();
    app.get('/file',function(req,res){
        res.send({message:"Should send file list"})
    });

    app.post('/file',async function(req,res){
        
        if(req.files){
            file.create(req.files,req.body)
        }
        res.send({message:"Should send something",body:req.body})
    });
    app.post('/hola',function(req,res){
        console.log(req.body);
        res.send({msg:'paciencia'})
    })
}