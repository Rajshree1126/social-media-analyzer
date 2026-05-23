const express = require('express');
const router = express.Router();

const Post = require('../models/Post');

// GET ALL POSTS
router.get('/', async (req, res) => {
  try {
    const posts = await Post.find().sort({ createdAt: -1 });

    res.status(200).json(posts);
  } catch (error) {
    console.error(error);

    res.status(500).json({
      message: 'Server Error'
    });
  }
});

module.exports = router;