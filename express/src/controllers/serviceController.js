const axios = require('axios');

const textController = async (req, res, next) => {
    try {
        const { input } = req.body;
        const response = await axios.post(`${process.env.GEN_AI_SERVER}/text`, { input });
        res.status(200).json({ message: "Text generated", data: response.data });
    } catch (error) {
        next(error);
    }

}


module.exports = {
    textController
}