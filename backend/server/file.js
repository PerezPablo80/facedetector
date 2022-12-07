const fs = require('fs')
const path = require('path')
require('dotenv').config()
class File{
    constructor(){
        this.folder = process.env.IMAGE_FOLDER||'./files/'
    }
    async list(){
        var lst=[];
        const files = fs.readdirSync(this.folder);
        files.forEach((file)=>{
            lst.push(file)
        })
        return {status:true,list:lst};
    }
    async emptyFolder(){
        const files = fs.readdirSync(this.folder);
        try{
            files.forEach((file)=>{
                fs.unlink(this.folder+file,(err)=>{
                    if(err) console.log(`error with file ${file} and error:${err}`)
                })
            })
            return {status:true,message:'empty ok'}    
        }catch(e){
            return {status:false,message:e}
        }
    }
    async create(files,body){
        try{
            var ext =files.file.name.split('.')[1];
            let name=files.file.name;
            files.file.mv(this.folder+name);
            return {status:true,message:'Creacion correcta'};
        }catch(e){
            console.log("ERRRORRRR en create")
            console.log(e)
            return {status:false,message:'Creacion incorrecta'};
            
        }
    }
    async update(filename,newName){
     fs.rename(this.folder+filename,this.folder+newName,function(err){
        if(err) {
            console.log('error updating::',err)
            return false;
        }
        return true;
     })   
    }
}

module.exports = File;