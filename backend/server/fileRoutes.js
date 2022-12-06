
const File = require('./file')
exports.createRoutes = function(app){
    const file=new File();
    app.get('/file',async function(req,res){
        let lst=await file.list();
        let rta={lst:lst,message:"Should send file list"};
        console.log(rta)
        res.send(rta)
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