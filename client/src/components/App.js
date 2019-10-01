import React, { Component } from 'react';
import Url from './Url';
import List from './List';

class App extends Component {

  render() {
    return (
      <div className="text-center">
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <h2 className="text-white">AIOHTTP URL SHORTNER</h2>
        <Url />
        <List />
      </div>
    );
  }
}

export default App;
