import React, { useEffect, useState } from 'react';
import { Input, Image, Header, Icon } from 'semantic-ui-react';
import styled from 'styled-components';
import SpeecherApi from './services/SpeecherApi';

const Container = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  width: 50%;
  height: 100%;
`;

const SentenceInput = styled(Input)`
  width: 100%;
  font-size: 14px;
  margin: 20px 0px;
`;

const App = () => {
  const [sentence, setSentence] = useState('');
  const [imageUrl, setImageUrl] = useState('');
  const [search, setSearch] = useState('');
  const KEY_ENTER = 'Enter';

  useEffect(() => {
    async function fetchData() {
      const data = await SpeecherApi.getImageUrl(sentence);
      const imageUrl = data && data.url;
      console.log(imageUrl);
      setImageUrl(imageUrl);
    }

    if (sentence) {
      fetchData();
    }
  }, [search]);

  return (
    <Container>
      <Header as='h1' icon>
        <Icon name="microphone" />
        Speecher
        <Header.Subheader>Enquanto você escreve (no futuro fala), as imagens aparecem</Header.Subheader>
      </Header>
      <SentenceInput
        type="text"
        icon="search"
        placeholder="Digite uma frase..."
        size="large"
        value={sentence}
        onChange={e => setSentence(e.target.value)}
        onKeyUp={e => e.key === KEY_ENTER && setSearch(sentence)}
      />
      {imageUrl && (
        <Image src={imageUrl} alt="speecher image" fluid rounded />
      )}
    </Container>
  );
}

export default App;
