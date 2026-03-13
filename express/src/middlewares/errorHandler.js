const errorHandler = async (err, req, res, next) => {
    if (err) {
        console.log(err);
        const status = err?.status || 500;
        const msg = err?.response?.data?.message || err?.response?.data?.detail || err?.message || "Internal server error";
        return res.status(status).json({ message: msg });
    }
    next();
}

module.exports = errorHandler;