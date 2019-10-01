import React, { Component } from 'react';
import axios from 'axios';


class Url extends Component {
    constructor() {
        super();
        this.state = {
            status: false,
            data: {},
        }
        this.onSubmit = this.onSubmit.bind(this);
        this.getUrl = this.getUrl.bind(this);
        this.apiUrl = 'http://0.0.0.0:8080/new';
    }

    onSubmit(event) {
        this.setState({ data: {} });
        this.setState({ status: 302 });
        event.preventDefault();
        const urlLink =  this.url.value;
        this.getUrl(urlLink);
    }

    getUrl(urlLink) {
        const postRequest = {
            method: 'POST',
            url: urlLink,
            // requestData,
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        }
        console.log("postRequest",postRequest);
        axios.post(this.apiUrl, postRequest)
        .then((response) => {
            const data = response.data;
            console.log("data",data);
        this.setState({data: data});
        this.setState({status: true});
        })
        .catch(error => {
            console.log(error);
            this.setState({data: 'Что-то пошло не так!'});
            this.setState({status: 500});
        })
    }


    componentDidMount() {
    }
    render() {
        const urlState = this.state.data;
        const urlStatus = this.state.status;
        let views = <div className="text-white">Подождите</div>
        if(Object.keys(urlState).length === 0) {
            views = <div className="text-white"></div>
        }
        if(urlStatus === true) {
            views = <div className="text-white">{urlState}</div>
        }

        return (
            <div className="text-center">
                 <form ref={(input) => this.urlForm = input} className="form-signin" onSubmit={this.onSubmit}>
                    <div className="form-group">
                     <input ref={(input) => this.url = input} type="text" placeholder="Вставьте вашу ссылку" className="form-control form-control-lg" />
                    </div>
                </form>
                {views}
            </div>
        );
    }
}

export default Url;
