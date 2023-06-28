const express = require("express");
const router = express.Router();

router.get("/", (req, res, next) => {
	res.render("error", { error: req.query.error });
});

module.exports = router;
