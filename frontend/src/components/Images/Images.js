import React from "react";
import axios from "axios";

class Image extends React.Component{
    constructor(props){
        super(props);
        this.state={
            images:[],
            names:[],
            message:"",
            status:"",
            hasData:false
        }
    }
    componentDidMount(){
        axios.get(url).then((res)=>{

        }).catch((e)=>{

        })
    }
    imageCards(){}
    render(){
        {this.state.hasData?this.imageCards(): <h1>Cargando</h1>}
    }
}