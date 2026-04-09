const mongoose = require('mongoose');

const PostSchema = new mongoose.Schema({
  platform: { type: String, required: true }, // e.g., "X", "Reddit"
  externalId: { type: String, required: true, unique: true },
  content: {
    text: { type: String, required: true },
    media: [String], // Array for varying image/video URLs
  },
  metadata: { 
    type: Map, 
    of: mongoose.Schema.Types.Mixed // Handles platform-specific data like "retweets" or "upvotes"
  },
  analysis: {
    sentiment: { type: String, default: "Pending" },
    riskLevel: { type: String, default: "Low" }
  }
}, { timestamps: true });

module.exports = mongoose.model('Post', PostSchema);