# 📱 食物卡路里估計器 - 專案總結

## 專案概述

這是一個使用 **Google Gemini Vision API** 的 AI 應用程式，可以分析食物圖片並估計其卡路里含量。

- **前端框架**: Streamlit
- **AI 引擎**: Google Generative AI (Gemini Vision)
- **部署平台**: Hugging Face Spaces (Docker)
- **開發語言**: Python 3.10+
- **套件管理**: uv

## 專案結構

```
Calorie/
├── src/                          # 應用程式源代碼
│   ├── app.py                   # Streamlit 主應用程式
│   └── food_recognizer.py       # 食物辨識模組（Google API 整合）
├── docs/                        # 文件
│   ├── SETUP_GUIDE.md          # 本機設定指南
│   ├── HUGGINGFACE_DEPLOYMENT.md # 部署指南
│   └── DEPLOYMENT_CHECKLIST.md   # 部署檢查清單
├── pyproject.toml              # 專案設定和相依套件
├── uv.lock                     # 鎖定的相依版本
├── Dockerfile                  # Docker 容器設定
├── .env.example                # 環境變數範本
├── .env                        # 本機環境變數（不被 commit）
├── .gitignore                  # Git 忽略規則
├── streamlit_run.sh            # Streamlit 啟動腳本
├── README.md                   # 專案說明文件
└── PROJECT_SUMMARY.md          # 本檔案
```

## 核心功能

### 1. 食物辨識 (`src/food_recognizer.py`)

```python
recognizer = FoodRecognizer(api_key)
result = recognizer.analyze_from_pil(image)
# 返回：
# {
#   "is_food": bool,
#   "analysis": "這是[食物名稱]，大概[卡路里]卡路里",
#   "error": None or error message
# }
```

**特點**：
- 使用 Google Gemini 1.5 Flash 模型
- 支援 PIL Image 和檔案路徑
- 自動判斷是否為食物
- 估計卡路里含量

### 2. Streamlit 應用 (`src/app.py`)

**功能**：
- 📸 圖片上傳介面
- 🤖 AI 實時分析
- 📊 結果展示（成功/警告/錯誤）
- 💾 自動快取識別器以提高效能

**特點**：
- 支援拖放上傳
- 支援多種圖片格式（JPG, PNG, GIF, WebP）
- 環境變數自動載入
- 響應式設計

## 相依套件

```toml
# 核心套件
streamlit==1.31.1              # Web UI 框架
google-generativeai==0.6.0     # Google AI API 整合
pillow==10.2.0                 # 圖片處理
python-dotenv==1.0.0           # 環境變數管理

# 開發套件
pytest==7.4.4                  # 測試框架
black==24.1.1                  # 程式碼格式化
ruff>=0.2.2                    # 程式碼檢查
```

## 使用流程

### 本機開發

```bash
# 1. 進入專案
cd /Users/Joseph/PycharmProjects/Calorie

# 2. 啟用虛擬環境
source .venv/bin/activate

# 3. 設定 Google API Key 到 .env
# GOOGLE_API_KEY=your_api_key_here

# 4. 啟動應用
streamlit run src/app.py
# 或
./streamlit_run.sh

# 5. 訪問 http://localhost:8501
```

### Hugging Face Spaces 部署

```bash
# 1. 在 Hugging Face 建立 Docker Space
# https://huggingface.co/spaces

# 2. 新增遠端倉庫
git remote add huggingface https://huggingface.co/spaces/YOUR_USERNAME/space-name

# 3. 推送程式碼
git push huggingface main

# 4. 在 Space 設定中新增 secret：GOOGLE_API_KEY

# 5. Space 自動構建和部署（2-5 分鐘）
```

## API Key 配置

### Google Generative AI API Key

1. 訪問 [Google AI Studio](https://aistudio.google.com/app/apikey)
2. 登入 Google 帳號
3. 點擊「Create API Key」
4. 複製 API Key

**本機**: 設定到 `.env` 檔案
```
GOOGLE_API_KEY=AIzaSy...
```

**Hugging Face Spaces**: 通過 Space Settings → Secrets 設定

## 開發注意事項

### 不要做的事

❌ 在程式碼中硬寫 API Key
❌ 提交 `.env` 檔案到 git
❌ 在 commit message 中包含敏感訊息
❌ 修改虛擬環境中的套件（使用 pyproject.toml）

### 應該做的事

✅ 使用環境變數存放 API Key
✅ 使用 `.env` 檔案管理本機配置
✅ 使用 uv 管理套件依賴
✅ 定期更新套件版本（檢查相容性）

## 套件管理流程

### 安裝新套件

```bash
# 1. 編輯 pyproject.toml 新增套件
# 例如：dependencies = [..., "package-name==version"]

# 2. 同步相依
uv sync --all-extras

# 3. 測試應用
streamlit run src/app.py

# 4. 提交變更
git add pyproject.toml uv.lock
git commit -m "Add new package"
```

### 更新現有套件

```bash
# 更新特定套件版本在 pyproject.toml，然後執行
uv sync --all-extras
```

## 測試

### 單元測試（未來實作）

```bash
pytest tests/
```

### 本機功能測試

1. **食物圖片**：測試 AI 能否識別並估計卡路里
2. **非食物圖片**：確認系統回應「這個不是食物」
3. **各種格式**：測試 JPG、PNG、GIF、WebP

## 效能最佳化

- ✅ 使用 `@st.cache_resource` 快取 FoodRecognizer 實例
- ✅ 使用 Google Gemini 1.5 Flash（快速推論）
- ✅ 自動清理臨時檔案

## 部署檢查清單

在部署到 Hugging Face 之前：

- [ ] 本機應用程式成功執行
- [ ] `GOOGLE_API_KEY` 正確設定
- [ ] `.env` 檔案不在 git 倉庫
- [ ] Dockerfile 已建立
- [ ] `pyproject.toml` 和 `uv.lock` 已提交
- [ ] README.md 已更新
- [ ] Git history 乾淨（無臨時提交）

## 常見問題

### Q: 如何更新應用程式？

A: 編輯 `.py` 檔案，測試完成後提交：
```bash
git add .
git commit -m "Update: description"
git push huggingface main
```
Hugging Face 會自動重新構建和部署。

### Q: 如何檢查 API 額度？

A: 訪問 [Google Cloud Console](https://console.cloud.google.com)，查看 API 配額。

### Q: 能否離線使用？

A: 不行，需要網路連線連接 Google API。

### Q: 支援多語言嗎？

A: 目前的 prompt 使用中文，但可以透過修改 `food_recognizer.py` 的 prompt 支援其他語言。

## 未來改進

- [ ] 新增歷史記錄功能
- [ ] 支援多語言界面
- [ ] 新增營養成分詳細分析
- [ ] 新增批次圖片上傳
- [ ] 新增使用者帳號系統
- [ ] 新增圖片存儲和檢索

## 技術棧

| 功能 | 技術 |
|------|------|
| Web UI | Streamlit |
| AI 模型 | Google Gemini Vision 1.5 Flash |
| 圖片處理 | Pillow |
| 套件管理 | uv |
| 容器化 | Docker |
| 部署平台 | Hugging Face Spaces |
| 版本控制 | Git |

## 許可證

MIT License - 詳見 LICENSE 檔案

## 聯繫和支援

遇到問題？

1. 檢查 `docs/` 目錄中的指南
2. 查看 GitHub Issues（如果有）
3. 查閱相關官方文件

## 致謝

- Google Generative AI Team
- Streamlit Community
- Hugging Face
