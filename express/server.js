const express = require('express');
require('dotenv').config();
const routes = require('./src/routes/serviceRoutes');
const errorHandler = require('./src/middlewares/errorHandler');

const app = express();

app.use(express.json());

app.use(express.urlencoded({ extended: true }));

app.get("/", (req, res, next) => {
    res.send("Welcome");
});

app.use("/v1", routes);

app.use(errorHandler);

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => console.log(`server is running on ${PORT}`));