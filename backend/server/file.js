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
        return lst;
    }
    async create(files,body){
        try{
            var ext =files.file.name.split('.')[1];
            let name=ext?ext:'';
            name =files.file.name+name;
            files.file.mv(this.folder+name);
            return true;
        }catch(e){
            return false;
        }
    }
}

module.exports = File;