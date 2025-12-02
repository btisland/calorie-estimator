# Calorie Estimator

A Streamlit web application that estimates calorie content of food from images using Google Gemini Vision API.

## Features

- 📸 Upload food images to analyze
- 🤖 AI-powered food recognition using Google Gemini Vision
- 📊 Calorie content estimation
- 💬 Friendly response when non-food images are uploaded

## Prerequisites

- Python 3.9 or higher
- Google Generative AI API Key (free from [Google AI Studio](https://aistudio.google.com/app/apikey))
- `uv` package manager

## Setup

### 1. Get Google API Key

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click "Create API Key"
3. Copy your API key

### 2. Configure Environment

Copy the example environment file and add your API key:

```bash
cp .env.example .env
```

Then edit `.env` and add your Google API key:

```
GOOGLE_API_KEY=your_actual_api_key_here
```

### 3. Install Dependencies

This project uses `uv` for dependency management:

```bash
# Install all dependencies (including dev)
uv sync --all-extras

# Or just production dependencies
uv sync
```

## Running Locally

### Option 1: Using the shell script (recommended)

```bash
./streamlit_run.sh
```

### Option 2: Manual activation

```bash
source .venv/bin/activate
streamlit run src/app.py
```

The app will be available at `http://localhost:8501`

## Project Structure

```
Calorie/
├── src/
│   ├── app.py                 # Main Gradio application
│   └── food_recognizer.py     # Food recognition module
├── docs/                      # Documentation (if needed)
├── pyproject.toml            # Project configuration and dependencies
├── .env.example              # Example environment variables
├── .env                      # Local environment variables (not committed)
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

## Deployment to Hugging Face Spaces

### Prerequisites

- Hugging Face account
- Hugging Face API token

### Steps

1. **Create a Space on Hugging Face**
   - Go to [Hugging Face Spaces](https://huggingface.co/spaces)
   - Click "Create new Space"
   - Choose:
     - **Space name**: `calorie-estimator` (or your preferred name)
     - **License**: MIT or your choice
     - **Space SDK**: Select "Docker"
     - **Visibility**: Public (or Private)

2. **Push Code to Space Repository**
   ```bash
   # Add Hugging Face remote
   git remote add huggingface https://huggingface.co/spaces/YOUR_USERNAME/calorie-estimator

   # Push your code (replaces YOUR_USERNAME with your actual username)
   git push huggingface main
   ```

3. **Configure Secrets**
   - Go to your Space page
   - Click on "Settings" → "Secrets and variables"
   - Add a new secret:
     - **Name**: `GOOGLE_API_KEY`
     - **Value**: Your Google Generative AI API key
   - Save and the Space will automatically rebuild and deploy

### Important Notes

- The `GOOGLE_API_KEY` in `.env` is for local development only
- On Hugging Face Spaces, set the secret in the Space settings
- The app uses `python-dotenv` to load `.env` locally, which is safe for production since `.env` is in `.gitignore`

## Environment Variables

- `GOOGLE_API_KEY`: Your Google Generative AI API key (required)

## How It Works

1. User uploads an image to the Gradio interface
2. The image is sent to Google Gemini Vision API
3. The model analyzes the image and:
   - Determines if it contains food
   - If yes: identifies the food type and estimates calories
   - If no: responds with "這個不是食物" (This is not food)
4. The result is displayed to the user

## API Response Format

The app expects responses in this format:
- **If it's food**: "這是[food name]，大概[number]卡路里"
  - Example: "這是番茄醬漢堡，大概450卡路里"
- **If it's not food**: "這個不是食物"

## Troubleshooting

### ImportError for `food_recognizer`

Make sure you're running from the correct directory:
```bash
cd /Users/Joseph/PycharmProjects/Calorie
source .venv/bin/activate
python src/app.py
```

### API Key Not Found

Check that:
1. `.env` file exists in the project root
2. `GOOGLE_API_KEY` is set with a valid key
3. No typos in the variable name

### Rate Limiting

Google's free API tier has rate limits. If you hit the limit, wait a moment before trying again.

## License

MIT
