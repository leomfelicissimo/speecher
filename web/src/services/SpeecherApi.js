async function getImageUrl(sentence) {
  const response = await fetch(`http://localhost:5000/?q=${sentence}`);
  const responseData = await response.json();
  return responseData;
}

export default {
  getImageUrl,
}