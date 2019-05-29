import React, { useEffect, useState } from 'react';
import styled from 'styled-components';
import SpeecherApi from './services/SpeecherApi';

const Container = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  width: 100%;
  height: 100%;
`;

const Button = styled.button`
  width: 80px;
  font-size: 14px;
`;

const SentenceInput = styled.input`
  height: 20px;
  width: 50%;
  padding: 10px;
  font-size: 14px;
  margin: 20px 0px;
`;

const Image = styled.img`
  margin-top: 20px;
`;

function App() {
  const [sentence, setSentence] = useState('');
  const [imageUrl, setImageUrl] = useState('');
  const [search, setSearch] = useState('');

  useEffect(() => {
    async function fetchData() {
      const data = await SpeecherApi.getImageUrl(sentence);
      const imageUrl = data && data.url;
      console.log(imageUrl);
      setImageUrl(imageUrl);
    }

    fetchData();
  }, [search]);

  return (
    <Container>
      <SentenceInput
        type="text"
        value={sentence}
        onChange={e => setSentence(e.target.value)}
      />
      <Button onClick={() => setSearch(sentence)}>Buscar</Button>
      {imageUrl && <Image height="40%" src={imageUrl} alt="speecher image" /> }
    </Container>
  );
}

export default App;
