const { textController } = require('../controllers/serviceController');

const router = require('express').Router();

router.post("/text", textController);


module.exports = router;