import React from "react";



class StoreRegister extends React.Component {
    constructor(props) {
        super (props);
        this.state = {
            url: ''
        }
    }

    getAndSendInput = () => {
        const storeName = document.getElementById('storeName').value
        const companyName = document.getElementById('companyName').value
        const storeImage = document.getElementById('storeImage').value
        const storeEmail = document.getElementById('storeEmail').value
        const payPalEmail = document.getElementById('payPalEmail').value
        this.setState({storeName: storeName,companyName: companyName,storeImage: storeImage, storeEmail: storeEmail,payPalEmail: payPalEmail})
        fetch(this.props.url, {
            method: "POST",
            body: JSON.stringify ({
                'storeName':storeName,
                'companyName':companyName,
                'storeImage':storeImage,
                'storeEmail':storeEmail,
                'payPalEmail':payPalEmail
            }),
            headers: {
                'Content-type': 'application/json; charset=UTF-8'
            }, 
        })          
    }


    render () {
        return (
            <div>
            <label>Store Name</label>
            <input type={"text"} name={"storeName"} id={"storeName"}  ></input>
            <br></br>
            <label>Company Name</label>
            <input type={"text"} name={"companyName"} id={"companyName"} ></input>
            <br></br>
            <label>Store Image</label>
            <input type={"file"} name={"storeImage"} id={"storeImage"}></input>
            <br></br>
            <label>Store Email</label>
            <input type={"email"} name={"storeEmail"} id={"storeEmail"} ></input>
            <br></br>
            <label>Pay Pal Email</label>
            <input type={"email"} name={"payPalEmail"} id={"payPalEmail"}></input>
            <br></br>
            <button onClick={() => this.getAndSendInput()}>Register</button>
            </div>
        )
    }
}


export default StoreRegister