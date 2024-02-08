import logo from './logo.svg';
import './App.css';
import TextGenerationForm from './components/TextGenerationForm';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <TextGenerationForm className="App-link">AI Application</TextGenerationForm>
      </header>
    </div>
  );
}

export default App;
