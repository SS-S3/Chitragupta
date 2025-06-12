// src/app.js
const express = require('express');
const cors = require('cors');
require('dotenv').config();

const app = express();
app.use(cors());
app.use(express.json());

// Import routes
const taskRoutes = require('./routes/task.routes');
app.use('/api/tasks', taskRoutes);

module.exports = app;
