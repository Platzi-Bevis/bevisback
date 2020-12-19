const express = require('express')
const app = express();
const port = 3002;
const swagger = require('./swagger');

app.use(express.json());
app.use('/', swagger);

app.listen(port, () => console.log(`Server listening on port ${port}!`))
