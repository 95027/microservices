const axios = require('axios');
const FormData = require('form-data');

const textController = async (req, res, next) => {
    try {
        const { input } = req.body;
        const response = await axios.post(`${process.env.GEN_AI_SERVER}/text`, { input });
        res.status(200).json({ message: "Text generated", data: response.data });
    } catch (error) {
        next(error);
    }

}

const audioController = async (req, res, next) => {
    try {
        if (!req.file) {
            return res.status(400).json({ message: "file is required" });
        }
        const form = new FormData();

        form.append("file", req.file.buffer, {
            filename: req.file.originalname,
            contentType: req.file.mimetype,
        });

        form.append("prompt", req.body.prompt);

        const response = await axios.post(
            `${process.env.GEN_AI_SERVER}/audio`,
            form,

        );
        res.status(200).json({ message: "Text generated from audio", data: response.data });
    } catch (error) {
        next(error);
    }
}


module.exports = {
    textController,
    audioController
}