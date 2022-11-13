import React from "react";

class Welcome extends React.Component {
    constructor(props) {
        super(props);
        this.get_user()
        this.state = {
            url: '',
        }
    }


    get_user = () => {
        fetch(this.props.url).then (
            (response) => response.json().then((json) => {
                this.setState({
                    user:json["user"]
                })
            })
        )
    };
    
    

    render () {
        return (
            <div>
            <table>
                <tr><th>User</th></tr>
                <tr><td>{this.state.user}</td></tr>
            </table>
            </div>
        );
    }
}


export default Welcome