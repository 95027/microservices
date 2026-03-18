const { textController, audioController } = require('../controllers/serviceController');
const upload = require('../utils/multer');

const router = require('express').Router();

router.post("/text", textController);
router.post("/audio", upload.single("audio"), audioController);


module.exports = router;