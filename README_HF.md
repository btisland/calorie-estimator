---
title: Calorie Estimator
emoji: 🍔
colorFrom: green
colorTo: blue
sdk: streamlit
sdk_version: "1.31.1"
app_file: app.py
pinned: false
license: mit
---

# 🍔 Food Calorie Estimator

A Streamlit application that uses Google Gemini Vision API to estimate calorie content from food images.

## Features

- 🔍 Identify food types from images
- 📊 Estimate calorie content
- 🚫 Detect non-food images
- 🌏 Chinese (Traditional) interface

## Setup

1. Get a Google Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Add your API key in the Space settings:
   - Go to Settings → Repository secrets
   - Add a new secret named `GOOGLE_API_KEY`
   - Paste your API key

## Usage

1. Upload a food image (JPG, PNG, GIF, or WebP)
2. Wait for AI analysis
3. View the estimated calories and food type

## Tech Stack

- **Streamlit**: Web interface
- **Google Gemini Vision API**: Image analysis and calorie estimation
- **Python 3.10+**: Backend logic

## For Developers

See the [GitHub repository](https://github.com/btisland/Calorie) for development setup and contribution guidelines.

## Note

Calorie estimates are AI-generated and may not be 100% accurate. Use as a reference only.
