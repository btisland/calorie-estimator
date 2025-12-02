# 📄 檔案總覽

## 專案結構概覽

```
Calorie/
├── 源代碼 (src/)
│   ├── app.py                    # 🌐 Streamlit Web 應用主檔
│   └── food_recognizer.py        # 🤖 Google Gemini Vision API 整合模組
│
├── 配置檔案
│   ├── pyproject.toml            # 📦 專案配置和相依套件定義
│   ├── uv.lock                   # 🔒 鎖定的相依版本
│   ├── Dockerfile                # 🐳 Docker 容器設定
│   ├── .env.example              # 📋 環境變數範本
│   ├── .env                      # 🔐 本機環境變數（不提交）
│   ├── .gitignore                # 🚫 Git 忽略規則
│   └── streamlit_run.sh          # 🚀 應用啟動腳本
│
├── 文件資料夾 (docs/)
│   ├── SETUP_GUIDE.md            # 🔧 本機設定詳細指南
│   ├── HUGGINGFACE_DEPLOYMENT.md # ☁️ Hugging Face 部署完整指南
│   ├── HUGGINGFACE_TOKEN_GUIDE.md # 🔑 Token 使用說明
│   └── DEPLOYMENT_CHECKLIST.md   # ✅ 部署前檢查清單
│
├── 根目錄文件
│   ├── README.md                 # 📖 專案主說明檔
│   ├── QUICKSTART.md             # ⚡ 5 分鐘快速開始指南
│   ├── PROJECT_SUMMARY.md        # 🎯 專案詳細總結
│   ├── NEXT_STEPS.md             # 🚀 下一步行動清單
│   └── FILES_OVERVIEW.md         # 📄 本檔案
│
└── 虛擬環境和其他
    ├── .venv/                    # 🐍 Python 虛擬環境（已設置）
    ├── .git/                     # 📚 Git 版本控制
    └── .idea/                    # 💻 IDE 設定
```

---

## 每個檔案的詳細說明

### 源代碼 (src/)

#### `app.py` - Streamlit Web 應用

**用途**: 應用程式的主要 Web 介面

**主要功能**:
- 頁面配置和標題設定
- 圖片上傳介面
- AI 分析結果展示
- 使用說明摺疊面板
- 環境變數自動載入

**何時修改**: 需要改變 UI 或添加新功能

---

#### `food_recognizer.py` - AI 辨識模組

**用途**: 整合 Google Gemini Vision API

**主要類別**: `FoodRecognizer`

**方法**:
- `__init__(api_key)` - 初始化模組
- `analyze_image(file_path)` - 分析本地檔案
- `analyze_from_pil(image)` - 分析 PIL Image 物件

**何時修改**: 需要改變 AI 提示或使用不同的 Google 模型

---

### 配置檔案

#### `pyproject.toml` - 專案配置

**用途**: 定義專案元資料和相依套件

**主要部分**:
- `[project]` - 專案基本資訊
- `dependencies` - 生產環境套件
- `[project.optional-dependencies]` - 開發環境套件

**何時修改**:
- 安裝新套件時
- 更新套件版本時
- 變更 Python 最低版本時

**修改流程**:
1. 編輯 `pyproject.toml`
2. 執行 `uv sync --all-extras`
3. 測試應用
4. 提交 `pyproject.toml` 和 `uv.lock`

---

#### `uv.lock` - 相依套件鎖定檔

**用途**: 鎖定所有相依套件的確切版本

**重要性**: 確保不同環境中使用相同版本，避免相容性問題

**何時修改**: 不要手動修改，由 `uv sync` 自動生成

---

#### `Dockerfile` - Docker 容器設定

**用途**: 定義 Docker 容器的構建和執行方式

**主要步驟**:
1. 使用 Python 3.12 slim 基礎映像
2. 安裝系統相依
3. 複製專案檔案
4. 安裝 Python 相依
5. 設定 Streamlit 環境變數
6. 啟動應用

**何時修改**:
- 需要額外的系統套件時
- 需要改變啟動命令時
- 需要不同的 Python 版本時

**注意**: Hugging Face 會自動使用此檔案構建容器

---

#### `.env.example` - 環境變數範本

**用途**: 展示應該配置哪些環境變數

**內容**:
```
GOOGLE_API_KEY=your_key_here
```

**何時修改**: 新增環境變數時更新此檔案，並提交到 Git

---

#### `.env` - 本機環境變數

**用途**: 儲存你的本機 API Key

**內容**:
```
GOOGLE_API_KEY=AIzaSy... (你的真實 key)
```

**重要**:
- 已在 `.gitignore` 中，不會被上傳
- 本機開發時需要此檔案
- Hugging Face Spaces 使用 Secrets 代替

---

#### `.gitignore` - Git 忽略規則

**用途**: 定義哪些檔案不應被 Git 追蹤

**包含**:
- `.env` 檔案（包含 API Key）
- 虛擬環境 `.venv`
- `__pycache__` 目錄
- IDE 設定檔
- 測試快取

**何時修改**: 添加新的臨時文件類型時

---

#### `streamlit_run.sh` - 啟動腳本

**用途**: 簡化應用啟動

**使用方法**:
```bash
./streamlit_run.sh
```

**做的事**:
1. 啟動虛擬環境
2. 執行 Streamlit 應用

**何時修改**: 很少需要修改

---

### 文件資料夾 (docs/)

#### `SETUP_GUIDE.md` - 本機設定指南

**適用場景**:
- 初次設定本機開發環境
- 遇到套件安裝問題
- 需要詳細設定步驟

**包含**:
- Google API Key 取得步驟
- 環境變數設定
- 應用執行方法
- 常見問題排查

---

#### `HUGGINGFACE_DEPLOYMENT.md` - 部署指南

**適用場景**:
- 想要部署應用到線上
- 需要 Hugging Face 詳細說明
- 遇到部署問題

**包含**:
- 建立 Space 步驟
- 獲取 Hugging Face Token
- 推送程式碼步驟
- Secret 配置
- 常見部署問題

---

#### `HUGGINGFACE_TOKEN_GUIDE.md` - Token 說明

**適用場景**:
- 不知道什麼是 Hugging Face Token
- 需要建立或更新 Token
- 遇到認證問題

**包含**:
- Token 的用途
- 如何建立 Token
- 如何使用 Token
- Token 安全最佳實踐

---

#### `DEPLOYMENT_CHECKLIST.md` - 部署檢查清單

**適用場景**:
- 準備部署到 Hugging Face
- 想確保沒有遺漏任何步驟
- 需要系統化的部署流程

**包含**:
- 部署前準備
- 逐步部署指南
- 部署後驗證
- 常見問題快速解答

---

### 根目錄文件

#### `README.md` - 專案主說明檔

**適用對象**: 所有人

**包含**:
- 專案概述
- 功能說明
- 安裝指南
- 本機執行說明
- 部署指南
- 環境變數說明

**何時更新**: 重要功能變更或新增時

---

#### `QUICKSTART.md` - 5 分鐘快速開始

**適用對象**: 想快速上手的人

**包含**:
- 5 分鐘內使用應用
- 5 分鐘內部署到線上
- 快速命令參考

**特點**: 最簡潔的指南，只有必要步驟

---

#### `PROJECT_SUMMARY.md` - 專案詳細總結

**適用對象**: 想深入了解項目的人

**包含**:
- 專案概述
- 核心功能詳解
- 使用流程
- API 配置
- 開發注意事項
- 技術棧
- 未來改進方向

---

#### `NEXT_STEPS.md` - 下一步行動清單

**適用對象**: 已完成設定，需要後續指引的人

**包含**:
- 立即行動清單
- 部署步驟概覽
- 參考文件指引
- 後續改進建議
- 學習資源

---

### 虛擬環境和版本控制

#### `.venv/` - Python 虛擬環境

**用途**: 隔離專案的 Python 套件環境

**大小**: ~500MB（包含所有套件）

**何時使用**:
```bash
source .venv/bin/activate  # 啟動
deactivate                 # 停用
```

**何時修改**: 使用 `uv sync` 自動管理，不手動編輯

---

#### `.git/` - 版本控制

**用途**: 儲存 Git 歷史記錄

**何時使用**:
```bash
git status     # 查看狀態
git add .      # 加入變更
git commit -m "message"  # 提交
git push       # 推送
```

---

## 檔案修改頻率

| 頻率 | 檔案 |
|------|------|
| 經常 | `src/app.py`, `src/food_recognizer.py` |
| 偶爾 | `pyproject.toml`, 文件檔 |
| 很少 | `Dockerfile`, `uv.lock` |
| 不應修改 | `.venv/`, `.git/` |
| 本機私密 | `.env` |

---

## 提交到 Git 前的檢查清單

```
□ .env 檔案 NOT 在 Git 中（已在 .gitignore）
□ 虛擬環境 .venv/ NOT 在 Git 中
□ __pycache__ 目錄 NOT 在 Git 中
□ 修改的檔案有清晰的提交訊息
□ 測試已確認應用正常執行
□ README 或相關文件已更新（如有重要變更）
□ pyproject.toml 和 uv.lock 同時提交（新增套件時）
```

---

## 推送到 Hugging Face 時需要的檔案

✅ 必需:
- `src/app.py`
- `src/food_recognizer.py`
- `pyproject.toml`
- `uv.lock`
- `Dockerfile`
- `README.md`

❌ 不會上傳:
- `.env` (在 .gitignore 中)
- `.venv/` (虛擬環境)
- `.git/` (本地)

---

## 檔案大小參考

| 檔案/資料夾 | 大小 |
|-----------|------|
| `.venv/` | ~500MB |
| `.git/` | ~1MB |
| `src/` | ~10KB |
| `docs/` | ~50KB |
| 其他檔案 | ~30KB |

---

## 常見修改場景

### 想改變 UI
編輯 `src/app.py`

### 想改變 AI 提示詞
編輯 `src/food_recognizer.py` 中的 `prompt`

### 想新增套件
1. 編輯 `pyproject.toml`
2. 執行 `uv sync --all-extras`
3. 測試應用

### 想改變 Streamlit 設定
編輯 `src/app.py` 中的 `st.set_page_config()`

### 想改變 Docker 設定
編輯 `Dockerfile`

---

## 何時需要推送到 Hugging Face

修改後，執行以下命令推送：

```bash
git add .
git commit -m "描述你的變更"
git push huggingface main
```

Hugging Face 會自動：
1. 拉取新程式碼
2. 執行 Dockerfile 構建
3. 部署新版本（2-5 分鐘）

---

總共 **17 個檔案**，所有都是必要的！📦
