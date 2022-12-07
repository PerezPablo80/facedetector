
const File = require('./file')
exports.createRoutes = function(app){
    const file=new File();
    //GET ALL files from folder given in environment 
    app.get('/file',async function(req,res){
        let lst=await file.list();
        res.send(rta)
    });
    // EMPTY the folder given in envirnment
    app.get('/emptyFolder',async function(req,res){
        let rta=await file.emptyFolder();
        res.send(rta)
    })
    // SAVE FILE with given name
    app.post('/file',async function(req,res){
        if(req.files){
            let resp=await file.create(req.files,req.body)
            res.send(resp);
        }else res.send({message:"No files on post",status:false})
    });
    //UPDATE file name given by oldName and newName in body.
    app.put('/file',async function(req,res){
        let resp=await file.update(req.body.oldName,req.body.newName);
        res.send(resp)
    })
}