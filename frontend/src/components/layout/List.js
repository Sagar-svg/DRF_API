import React, { Component } from 'react'

export class List extends Component {
    componentDidMount(){
        const apiUrl = 'http://127.0.0.1:8000/api/python';
        fetch(apiUrl)
        .then((response) => response.json())
        .then((data) => console.log(data));
        
    }

    render() {
        
        return (
            <ul>
              {this.state.data.data.map(contact => {
                return (
                  <li >
                    {contact.videoId} - {contact.title}
                  </li>
                );
              })}
            </ul>
          );
            
    }
}

export default List
