import express from 'express';
import  { fileURLToPath } from 'url';
import path from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = process.env.PORT || 3000;

// Define the directory for static files
const staticDir = path.join(__dirname, 'app');

// Serve static files
app.use(express.static(staticDir));

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
