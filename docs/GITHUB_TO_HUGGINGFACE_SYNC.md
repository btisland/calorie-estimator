# GitHub to Hugging Face Space 自動同步設定指南

## 概述

本指南說明如何設定 GitHub Actions，實現從 GitHub 自動同步到 Hugging Face Space 的工作流程。

```
本機端 → GitHub → (自動) → Hugging Face Space
```

---

## 前置準備

### 需要準備的東西

1. GitHub 帳號
2. Hugging Face 帳號
3. Hugging Face Access Token（需要 write 權限）
4. 本機已安裝 Git

---

## 步驟 1：準備專案結構

### 1.1 調整專案檔案結構

```bash
Calorie/
├── .github/
│   └── workflows/
│       └── sync-to-hf.yml          # GitHub Actions 設定檔
├── src/
│   ├── app.py                      # 原本的 Streamlit app
│   └── food_recognizer.py          # 食物辨識模組
├── app.py                          # Hugging Face Space 入口（新增）
├── requirements.txt                # 相依套件（給 HF 用）
├── pyproject.toml                  # 專案設定（給本地開發用）
├── .env.example                    # 環境變數範例
├── .gitignore                      # Git 忽略規則
├── README.md                       # 開發者文件（給 GitHub）
└── README_HF.md                    # HF Space 文件（含 YAML metadata）
```

### 1.2 建立 Hugging Face Space 專用的 README

檔案：`README_HF.md`

```markdown
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

See the [GitHub repository](https://github.com/YOUR_USERNAME/calorie-estimator) for development setup and contribution guidelines.

## Note

Calorie estimates are AI-generated and may not be 100% accurate. Use as a reference only.
```

---

## 步驟 2：建立 GitHub Repository

### 2.1 在 GitHub 網站上建立新的 Repository

1. 前往 https://github.com/new
2. 填寫資訊：
   - **Repository name**: `calorie-estimator`（或您想要的名稱）
   - **Description**: "AI-powered food calorie estimator using Google Gemini Vision API"
   - **Visibility**: Public 或 Private（您的選擇）
   - **不要**勾選 "Initialize this repository with a README"（因為我們已經有了）
3. 點擊 "Create repository"

### 2.2 從本機推送到 GitHub

```bash
# 進入專案目錄
cd /Users/Joseph/PycharmProjects/Calorie

# 如果還沒初始化 Git（通常已經有了）
git init

# 加入 GitHub remote（替換 YOUR_USERNAME）
git remote add origin https://github.com/YOUR_USERNAME/calorie-estimator.git

# 確認 remote 設定
git remote -v

# 加入所有檔案
git add .

# 建立初始 commit
git commit -m "Initial commit: Food calorie estimator with Streamlit and Gemini API"

# 推送到 GitHub（如果是新建立的 repo）
git branch -M main
git push -u origin main
```

### 2.3 使用 Personal Access Token（如果需要）

如果推送時要求認證，建議使用 **Fine-grained tokens**（更安全）：

1. 前往 GitHub Settings → Developer settings → Personal access tokens → **Fine-grained tokens**
2. 點擊 "Generate new token"
3. 填寫資訊：
   - **Token name**: `calorie-estimator-push`
   - **Expiration**: 選擇到期時間（建議 90 天或 1 年）
   - **Repository access**: 選擇 **"Only select repositories"**
   - 選擇您的 `calorie-estimator` repository
   - **Permissions** → **Repository permissions**:
     - Contents: **Read and write** （允許推送程式碼）
     - Workflows: **Read and write** （允許推送 workflow 檔案）⚠️ 重要！
     - Metadata: **Read-only** （自動勾選）
4. 點擊 "Generate token" 並複製 token

⚠️ **重要說明**：
- **Workflows 權限**是用來推送 `.github/workflows/` 檔案到 GitHub
- 如果沒有這個權限，推送時會出現錯誤：`refusing to allow a Personal Access Token to create or update workflow`
- 這與 GitHub Actions 執行無關，只是本機推送需要
5. 推送時使用：
   ```bash
   git push https://YOUR_USERNAME:YOUR_TOKEN@github.com/YOUR_USERNAME/calorie-estimator.git main
   ```

**為什麼使用 Fine-grained tokens？**
- ✅ 只授權特定 repository
- ✅ 最小權限原則
- ✅ 更安全，即使洩漏也只影響單一 repo

---

## 步驟 3：設定 GitHub Actions

### 3.1 建立 Workflow 檔案

建立目錄和檔案：

```bash
mkdir -p .github/workflows
```

檔案：`.github/workflows/sync-to-hf.yml`

```yaml
name: Sync to Hugging Face Space

on:
  push:
    branches:
      - main  # 當推送到 main 分支時觸發

jobs:
  sync:
    runs-on: ubuntu-latest

    steps:
      # 步驟 1: 檢出程式碼
      - name: Checkout repository
        uses: actions/checkout@v3
        with:
          fetch-depth: 0  # 拉取完整的 Git 歷史
          lfs: true       # 如果使用 Git LFS

      # 步驟 2: 設定 Git 使用者資訊
      - name: Configure Git
        run: |
          git config --global user.email "github-actions[bot]@users.noreply.github.com"
          git config --global user.name "github-actions[bot]"

      # 步驟 3: 準備 Hugging Face Space 專用檔案
      - name: Prepare files for Hugging Face
        run: |
          # 複製 HF 專用的 README（覆蓋原本的 README.md）
          cp README_HF.md README.md

          # 確保必要檔案存在
          ls -la

      # 步驟 4: 推送到 Hugging Face Space
      - name: Push to Hugging Face Space
        env:
          HF_TOKEN: ${{ secrets.HF_TOKEN }}
          HF_USERNAME: ${{ secrets.HF_USERNAME }}
          SPACE_NAME: calorie-estimator
        run: |
          # 加入 Hugging Face remote
          git remote add huggingface https://$HF_USERNAME:$HF_TOKEN@huggingface.co/spaces/$HF_USERNAME/$SPACE_NAME || true

          # 確保在正確的分支
          git checkout main

          # 提交變更（如果有的話）
          git add README.md
          git diff --quiet && git diff --staged --quiet || git commit -m "Update from GitHub: $(git log -1 --pretty=%B)"

          # 推送到 Hugging Face
          git push huggingface main --force
```

### 3.2 更簡化的版本（推薦新手使用）

如果上面的版本太複雜，可以用這個簡化版：

```yaml
name: Sync to Hugging Face Space

on:
  push:
    branches:
      - main

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0

      - name: Push to Hugging Face
        env:
          HF_TOKEN: ${{ secrets.HF_TOKEN }}
        run: |
          git push https://YOUR_HF_USERNAME:$HF_TOKEN@huggingface.co/spaces/YOUR_HF_USERNAME/calorie-estimator main --force
```

記得替換：
- `YOUR_HF_USERNAME`：您的 Hugging Face 使用者名稱

---

## 步驟 4：設定 GitHub Secrets

### 4.1 取得 Hugging Face Access Token

1. 前往 https://huggingface.co/settings/tokens
2. 點擊 "New token"
3. 填寫：
   - **Name**: `github-actions-sync`
   - **Role**: 選擇 "Write"
4. 點擊 "Generate a token"
5. **複製 token**（只會顯示一次！）

### 4.2 在 GitHub 設定 Secrets

1. 前往您的 GitHub repository
2. 點擊 "Settings" 標籤
3. 左側選單選擇 "Secrets and variables" → "Actions"
4. 點擊 "New repository secret"
5. 新增以下 secrets：

   **Secret 1:**
   - Name: `HF_TOKEN`
   - Value: 您剛剛複製的 Hugging Face Access Token
   - 點擊 "Add secret"

   **Secret 2:（如果使用完整版 workflow）**
   - Name: `HF_USERNAME`
   - Value: 您的 Hugging Face 使用者名稱（例如：`josephchou`）
   - 點擊 "Add secret"

---

## 步驟 5：提交並測試

### 5.1 提交 GitHub Actions 設定

```bash
# 加入 workflow 檔案
git add .github/workflows/sync-to-hf.yml

# 加入 HF README（如果有建立）
git add README_HF.md

# 提交
git commit -m "Add GitHub Actions workflow for Hugging Face sync"

# 推送到 GitHub
git push origin main
```

### 5.2 查看執行狀態

1. 前往您的 GitHub repository
2. 點擊 "Actions" 標籤
3. 您應該會看到 "Sync to Hugging Face Space" workflow 正在執行
4. 點擊進入查看詳細日誌

### 5.3 確認同步成功

1. 前往您的 Hugging Face Space: https://huggingface.co/spaces/josephchou/calorie-estimator
2. 檢查檔案是否已更新
3. 查看 Space 是否自動重新建置

---

## 日常使用流程

設定完成後，您的工作流程變成：

```bash
# 1. 在本機修改程式碼
vim src/app.py

# 2. 測試功能
./streamlit_run.sh

# 3. 提交變更
git add .
git commit -m "Update feature X"

# 4. 推送到 GitHub
git push origin main

# 5. GitHub Actions 會自動：
#    - 觸發 workflow
#    - 推送到 Hugging Face Space
#    - Hugging Face 自動重新建置
```

**您只需要推送到 GitHub，其他都自動完成！**

---

## 進階設定

### 僅在特定條件下同步

如果您想要更細緻的控制，可以修改觸發條件：

```yaml
on:
  push:
    branches:
      - main
    paths:
      - 'src/**'           # 只有 src 目錄變更時
      - 'app.py'
      - 'requirements.txt'
      - 'README_HF.md'
```

### 同步前執行測試

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          pip install uv
          uv sync
      - name: Run tests
        run: pytest

  sync:
    needs: test  # 只有測試通過才同步
    runs-on: ubuntu-latest
    # ... (同上)
```

---

## 故障排除

### 問題 1: GitHub Actions 推送失敗

**錯誤訊息**: `fatal: could not read Username`

**解決方法**:
- 檢查 `HF_TOKEN` secret 是否正確設定
- 檢查 token 是否有 write 權限

### 問題 2: 推送成功但 Hugging Face 沒有更新

**可能原因**:
- Hugging Face Space 建置中（等待幾分鐘）
- 查看 Space 的 Logs 是否有錯誤

**解決方法**:
- 前往 Space 頁面查看建置狀態
- 檢查 requirements.txt 是否正確

### 問題 3: README 沒有更新

**原因**: 使用簡化版 workflow 沒有替換 README

**解決方法**:
1. 使用完整版 workflow
2. 或直接把 HF 的 YAML metadata 加到主 README.md 最上方

---

## 安全性建議

1. **永遠不要**將 token 直接寫在程式碼中
2. **使用 GitHub Secrets** 儲存敏感資訊
3. **定期更換** Hugging Face Access Token
4. **最小權限原則**：token 只給需要的權限（write）

---

## 參考資源

- [GitHub Actions 官方文件](https://docs.github.com/en/actions)
- [Hugging Face Spaces 文件](https://huggingface.co/docs/hub/spaces)
- [Git 基礎教學](https://git-scm.com/book/zh-tw/v2)

---

## 總結

設定完成後的工作流程：

```
本機開發 → git push → GitHub → (自動) → Hugging Face Space
```

您只需要專注在開發和推送到 GitHub，其他都自動化了！
