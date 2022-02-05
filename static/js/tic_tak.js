'use strict';


class Timer extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      seconds: 0
    };
  }

  tick() {
    this.setState(state => ({
      seconds: state.seconds + 1
    }));
  }

  componentDidMount() {
    this.interval = setInterval(() => this.tick(), 1000);
  }

  componentWillUnmount() {
    clearInterval(this.interval);
  }

  render() {
    return /*#__PURE__*/React.createElement("div", null, "\u0421\u0435\u043A\u0443\u043D\u0434\u044B: ", this.state.seconds);
  }

}

ReactDOM.render( /*#__PURE__*/React.createElement(Timer, null), document.getElementById('root'));


/*function Welcome(props) {
  return <h1>Привет, {props.name}</h1>;
}

const element = <Welcome name="Алиса" />;
ReactDOM.render(
  element,
  document.getElementById('root')
);
*/
/*function App(props) {
  return React.createElement('h1', null, 'Hello world');
};

ReactDOM.render(
  React.createElement(App),
  document.getElementById('root')
 );
*/
/*
'use strict';

const e = React.createElement;

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    if (this.state.liked) {
      return 'You liked this.';
    }

    return e(
      'button',
      { onClick: () => this.setState({ liked: true }) },
      'Like'
    );
  }
}

const domContainer = document.querySelector('#like_button_container');
ReactDOM.render(e(LikeButton), domContainer);
*/