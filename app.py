"""
Streamlit application for food calorie estimation using Google Gemini Vision API
"""

import os
import sys
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

# Add src directory to Python path for importing modules
sys.path.insert(0, str(Path(__file__).parent / "src"))

from food_recognizer import FoodRecognizer

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="食物卡路里估計器",
    page_icon="🍔",
    layout="wide",
)

# Get API key from environment variable
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    st.error(
        "❌ 錯誤：GOOGLE_API_KEY 未找到。\n\n"
        "請確保：\n"
        "1. 在 `.env` 檔案中設定 GOOGLE_API_KEY\n"
        "2. 或在環境變數中設定 GOOGLE_API_KEY"
    )
    st.stop()

# Initialize food recognizer
@st.cache_resource
def get_recognizer():
    return FoodRecognizer(GOOGLE_API_KEY)

recognizer = get_recognizer()

# Main title and description
st.markdown(
    """
    # 🍔 食物卡路里估計器

    上傳一張食物的照片，AI 將幫你估計卡路里含量
    """
)

# Create columns
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 📸 上傳照片")
    uploaded_file = st.file_uploader(
        "選擇一張圖片",
        type=["jpg", "jpeg", "png", "gif", "webp"],
        label_visibility="collapsed",
    )

with col2:
    st.markdown("### 📊 分析結果")
    result_container = st.empty()

# Process image
if uploaded_file is not None:
    with col1:
        # Display uploaded image
        st.image(uploaded_file, caption="上傳的圖片", use_column_width=True)

    # Save uploaded file temporarily
    import tempfile

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
        tmp_file.write(uploaded_file.getbuffer())
        tmp_file_path = tmp_file.name

    try:
        # Analyze image
        with st.spinner("🤖 正在分析圖片..."):
            result = recognizer.analyze_image(tmp_file_path)

        # Display result
        with col2:
            if result["error"]:
                st.error(f"❌ {result['analysis']}")
            elif result["is_food"]:
                st.success(f"✅ {result['analysis']}")
                st.balloons()
            else:
                st.warning(f"⚠️ {result['analysis']}")

    finally:
        # Clean up temporary file
        os.unlink(tmp_file_path)

# Instructions
with st.expander("ℹ️ 使用說明", expanded=False):
    st.markdown(
        """
        ### 功能
        - ✅ 識別食物類型
        - ✅ 估計卡路里含量
        - ✅ 識別非食物圖片

        ### 支援的圖片格式
        - JPG/JPEG
        - PNG
        - GIF
        - WebP

        ### 提示
        - 確保照片清晰，可以看清食物
        - 單次只能上傳一張圖片
        - 大的圖片會被自動調整大小

        ### 注意
        - 估計的卡路里是基於 AI 分析，可能不完全準確
        - 如果上傳的不是食物照片，系統會回應「這個不是食物」
        """
    )

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 12px;'>
    由 Google Gemini Vision API 提供支援
    </div>
    """,
    unsafe_allow_html=True,
)
