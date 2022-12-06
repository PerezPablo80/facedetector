const path = require('path')
require('dotenv').config()
class File{
    constructor(){
        this.folder = process.env.IMAGE_FOLDER||'./files/'
    }
    list(){
        return ['nom1','nom2']
    }
    async create(files,body){
        console.log('files');
        console.log(files);
        console.log('body')
        console.log(body)
        // var ext =body.previousName.split('.')[1];
        // files.file.mv()
    }
}

module.exports = File;