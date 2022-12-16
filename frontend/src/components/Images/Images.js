import React from "react";
import axios from "axios";
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Col from "react-bootstrap/esm/Col";
import Row from "react-bootstrap/Row"
import ToggleButtonGroup from 'react-bootstrap/ToggleButtonGroup';
import ToggleButton from "react-bootstrap/esm/ToggleButton";

class Image extends React.Component{
    constructor(props){
        super(props);
        this.state={
            images:[],
            names:[],
            radioButton:false,
            typeOfData:'Desconocidos',
            message:"",
            status:"",
            updatables:[],
            hasData:false
        }
    }
    componentDidMount(){
        this.loadData()
    }
    loadData(tip=""){
        let url=process.env.REACT_APP_SERVER_PYTHON||'http://192.168.1.111:2999/';
        if(tip.length===0)
            tip=this.state.typeOfData
        url=url+'file/'+tip;
        axios.get(url).then((res)=>{
            console.log(res.data);
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
        let val=updatables[name];
        let url=process.env.REACT_APP_SERVER_PYTHON||'http://192.168.1.111:2999/';
        url=url+'file/';
        val=val+"."+name.split(".")[1];
        let body={previousName:name,actualName:val};
        axios.put(url,body).then((res)=>{
            console.log(res.data);
            
        }).catch((e)=>{
            console.log('ERROR on update::',e)
        })
    }
    updateData(event,name){
        let value=event.target.value;
        let updatables=this.state.updatables;
        updatables[name]=value;
        this.setState({updatables:updatables})
        updatables=this.state.updatables;
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
                
                    // }else{ //esto no deberia ir, solo para pruebas
                }
                extra =(
                    <div key={"div_img_"+key}>
                        <Form.Control key={"input_"+key} onChange={((e)=>{this.updateData(e,name)})} type="text" id={name}></Form.Control>
                        <Button className="text-center" variant="success" onClick={()=>{this.updateImage(name)}}>Nombrar</Button>
                    </div>
                )

                return <Col key={"col_image_"+key} >
                <Card style={{width:'16rem',padding:"7px"}}  key={"card_"+key}>
                    <Card.Img variant="top" src={url+name} key={"card_img_"+key}/>
                    <Form.Label className="text-center">{img.split('.')[0]}</Form.Label>
                    {extra}
                    
                </Card>
                </Col>
            })
        }
        return <>No hay datos</>
    }
    toggleChange =()=>{
        let val=this.state.radioButton;
        val=!val;
        let tod='Desconocidos'
        if(val){
            
            tod='Conocidos'
        }else{
        }
        this.setState({radioButton:val,typeOfData:tod})
        this.loadData(tod);
    };    
    //Toggle button for Known and unknown cards
    toggle(){
        return (
            <Form.Check type="switch" label={this.state.typeOfData} onChange={this.toggleChange}/>      
        )
    }
    render(){
        return (<div className="container">
            {this.toggle()}
        <Row md={2} sm={1} lg={3} xl={4} style={{padding:"5px"}}>
        {this.state.hasData?this.imageCards(): <h1>Cargando</h1>}
        </Row>
    </div>) 
        
        
    }
}
export default Image;