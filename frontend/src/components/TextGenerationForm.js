import React, { useState } from 'react';
import axios from 'axios';

const TextGenerationForm = () => {
  const [seed, setSeed] = useState('');
  const [numWords, setNumWords] = useState('');
  const [generatedText, setGeneratedText] = useState('');
  const [output, setOutput] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('/predict', { seed, numWords, generatedText });
      setOutput(response.data.output);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type="text" value={seed} onChange={e=> setSeed(e.target.value)} name="enginesize" placeholder="Engine Size" required="required"/>
        <input type="text" value={numWords} onChange={e=> setNumWords(e.target.value)} name="cylinders" placeholder="Cylinders" required="required"/>
        <input type="text" value={generatedText} onChange={e=> setGeneratedText(e.target.value)} name="fuel" placeholder="Fuel" required="required"/>

        <button type="submit" class="btn">Predict</button>
      </form>

      {output && (
        <div>
          <h3>Prediction :</h3>
          <p>{output}</p>
        </div>
      )}
    </div>
  );
};

export default TextGenerationForm;