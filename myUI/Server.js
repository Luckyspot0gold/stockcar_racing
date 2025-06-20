const express = require('express');
const app = express();
const port = 3000;

// Serve static files from 'public' directory
app.use(express.static('public'));

app.get('/', (req, res) => {
  res.send('Racing game loading...');
});

app.listen(port, () => {
  console.log(`Crypto Racing Server running on port ${port}`);
});
