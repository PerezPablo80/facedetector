import React from "react";
import axios from "axios";
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

class Image extends React.Component{
    constructor(props){
        super(props);
        this.state={
            images:[],
            names:[],
            message:"",
            status:"",
            updatables:[],
            hasData:false
        }
    }
    componentDidMount(){
        let url=process.env.REACT_APP_SERVER_PYTHON||'http://192.168.1.111:2999/';
        url=url+'file/unknownn';
        axios.get(url).then((res)=>{
            console.log('llega')
            console.log(res.data)
            this.setState({
                images:res.data.images,
                hasData:true
            })
        }).catch((e)=>{
            console.log('ERROR did mount::',e)
        })
    }
    updateImage(name){
        let updatables=this.state.updatables;
        console.log(updatables);
        console.log(updatables[name])
    }
    updateData(event,name){
        let value=event.target.value;
        let updatables=this.state.updatables;
        updatables[name]=value;
        this.setState({updatables})
    }
    imageCards(){
        let url=process.env.REACT_APP_SERVER_PYTHON||'http://192.168.1.111:2999/';
        url=url+'static/';
        if(this.state.hasData){
            return this.state.images.map((img,key)=>{
                let name=img;
                let extra="";
                if(img.includes('aa_')){
                    img=img.replace('aa_','');
                
                    // }else{
                    extra =(
                        <>
                            <Form.Control key={"input_"+key} onChange={((e)=>{this.updateData(e,name)})} type="text" id={name}></Form.Control>
                            <Button className="text-center" variant="success" onClick={this.updateImage(name)}>Nombrar</Button>
                        </>
                    )
                }

                return <Card style={{width:'18rem'}} key={"card_"+key}>
                    <Card.Img variant="top" src={url+name} key={"card_img_"+key}/>
                    <Form.Label className="text-center">{img.split('.')[0]}</Form.Label>
                    {extra}
                    
                </Card>
            })
        }
        return <>Hola</>
    }
    render(){
        return (<div className="container">
        {this.state.hasData?this.imageCards(): <h1>Cargando</h1>}
    </div>) 
        
        
    }
}
export default Image;