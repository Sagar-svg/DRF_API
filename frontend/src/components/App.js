import React, {Component, Fragment} from 'react';
import ReactDOM, { render } from 'react-dom';
import Header from './layout/Header';
import List from './layout/List';


class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
          data: [],
          loaded: false,
          placeholder: "Loading"
        };
      }

      componentDidMount() {
        fetch("http://127.0.0.1:8000/api/python")
          .then(response => {
            if (response.status > 400) {
              return this.setState(() => {
                return { placeholder: "Something went wrong!" };
              });
            }
            return response.json();
          })
          .then(data => {
            this.setState(() => {
              return {
                data,
                loaded: true
              };
            });
          });
      }
    
  
       
  

 
      render() {
          const {data, loaded} = this.state;
        return (
            <div>
            
            {data}   
          </div>
        );
      }
  
}

export default App;

ReactDOM.render(<App />, document.getElementById('app'));