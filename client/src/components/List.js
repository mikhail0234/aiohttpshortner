import React, { Component } from 'react';
import axios from 'axios';


class List extends Component {
    constructor() {
        super();
        this.state = {
            status: false,
            data: {},
        }
        this.onSubmit = this.onSubmit.bind(this);
        this.getList = this.getList.bind(this);
        this.apiUrl = 'http://0.0.0.0:8080/';
    }

    onSubmit(event) {
        this.setState({ data: {} });
        this.setState({ status: 302 });
        event.preventDefault();
        this.getList();
    }

    getList() {
        const postRequest = {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        }

        console.log("postRequest",postRequest);
        axios.get(this.apiUrl, postRequest)
        .then((response) => {
            const data = response.data;
            console.log("data",data);
        this.setState({data: data});
        // this.setState({status: true});
        })
        .catch(error => {
            console.log(error);
            this.setState({data: 'Что-то пошло не так!.'});
            this.setState({status: 500});
        })
    }

    componentDidMount() {
    }

    render() {
        const listState = this.state.data;
        const listStatus = this.state.status;
        let views = <div className="text-white">Подождите</div>
        if(Object.keys(listState).length === 0) {
            views = <div className="text-white">Загурзите список</div>
        }
        if(listStatus === true) {
            views = <div className="text-white">{listState}</div>
        }

        return (
            <div className="text-center">
                {views}
                <button onClick={this.onSubmit}>
                  Загрузить
                </button>

            </div>
        );
    }
}

export default List;
