const path = require('path')
require('dotenv').config()
class File{
    constructor(){
        this.folder = process.env.IMAGE_FOLDER||'./files/'
    }
    list(){
        
    }
    async create(files,body){
        var ext =files.file.name.split('.')[1];
        let name=ext?ext:'';
        name =files.file.name+name;
        files.file.mv(this.folder+name);
    }
}

module.exports = File;