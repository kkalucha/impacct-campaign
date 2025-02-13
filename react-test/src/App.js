import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {

  constructor() {
    super();
    this.state = {
      message: "Hello World",
      data: null
    }
  }

  fetchData = () => {

    fetch('http://impacct-test.herokuapp.com/getall')
      .then(response => response.json())
      .then(data => this.setState({ data }));

      console.log(this.state.data);
    //fetch('http://localhost:5000/api/simplelist').then(response => response.json()).then(data =>console.log(response))
      // Do something with response

    /*
    fetch('',{mode: 'no-cors'})
        .then(response => response.json())
        .then(data => console.log(data));
    */
  }
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            {this.state.message}
          </p>
          <button onClick={this.fetchData}>Click me</button>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div>
    );
  }
}

export default App;
