"""
Food recognition module using Google Gemini Vision API
"""

import base64
import os
from pathlib import Path

import google.generativeai as genai
from PIL import Image


class FoodRecognizer:
    """Recognize food in images and estimate calorie content using Google Gemini Vision API."""

    def __init__(self, api_key: str):
        """
        Initialize the food recognizer with Google API key.

        Args:
            api_key: Google Generative AI API key
        """
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.5-flash-lite")

    def analyze_image(self, image_path: str) -> dict:
        """
        Analyze an image to determine if it contains food and estimate calories.

        Args:
            image_path: Path to the image file or URL

        Returns:
            A dictionary containing:
            - is_food: bool indicating if the image contains food
            - analysis: str with food type and estimated calories
            - error: str with error message if any
        """
        try:
            # Verify image file exists and is valid
            if not Path(image_path).exists():
                return {
                    "is_food": False,
                    "analysis": "無法讀取圖片檔案",
                    "error": f"File not found: {image_path}",
                }

            # Open and validate image
            image = Image.open(image_path)
            image.verify()

            # Reopen image after verification
            image = Image.open(image_path)

            # Send to Gemini API for analysis
            prompt = """請分析這張圖片：
1. 判斷這是否為食物
2. 如果是食物，請識別食物類型和估計的卡路里含量

請用以下格式回應：
- 如果不是食物：回答「這個不是食物」
- 如果是食物：回答「這是[食物名稱]，大概[數字]卡路里」

只需要回答上述格式，不要提供額外說明。"""

            response = self.model.generate_content([prompt, image])

            analysis_text = response.text.strip()

            # Determine if it's food based on response
            is_food = "不是食物" not in analysis_text

            return {
                "is_food": is_food,
                "analysis": analysis_text,
                "error": None,
            }

        except Exception as e:
            return {
                "is_food": False,
                "analysis": f"分析失敗：{str(e)}",
                "error": str(e),
            }

    def analyze_from_pil(self, image: Image.Image) -> dict:
        """
        Analyze a PIL Image object.

        Args:
            image: PIL Image object

        Returns:
            A dictionary containing:
            - is_food: bool indicating if the image contains food
            - analysis: str with food type and estimated calories
            - error: str with error message if any
        """
        try:
            prompt = """請分析這張圖片：
1. 判斷這是否為食物
2. 如果是食物，請識別食物類型和估計的卡路里含量

請用以下格式回應：
- 如果不是食物：回答「這個不是食物」
- 如果是食物：回答「這是[食物名稱]，大概[數字]卡路里」

只需要回答上述格式，不要提供額外說明。"""

            response = self.model.generate_content([prompt, image])

            analysis_text = response.text.strip()

            # Determine if it's food based on response
            is_food = "不是食物" not in analysis_text

            return {
                "is_food": is_food,
                "analysis": analysis_text,
                "error": None,
            }

        except Exception as e:
            return {
                "is_food": False,
                "analysis": f"分析失敗：{str(e)}",
                "error": str(e),
            }
