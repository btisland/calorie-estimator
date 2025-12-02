# 🚀 快速開始指南

## 5 分鐘快速上手

### 第 1 步：取得 Google API Key（2 分鐘）

1. 訪問 [Google AI Studio](https://aistudio.google.com/app/apikey)
2. 點擊「Create API Key」
3. 複製你的 API Key（看起來像 `AIzaSy...`）

### 第 2 步：配置 API Key（1 分鐘）

編輯 `.env` 檔案，在第一行貼上你的 API Key：

```
GOOGLE_API_KEY=AIzaSy... (你複製的 key)
```

儲存檔案。

### 第 3 步：執行應用（2 分鐘）

```bash
# 啟動應用
./streamlit_run.sh
```

或者：

```bash
source .venv/bin/activate
streamlit run src/app.py
```

應用會在 `http://localhost:8501` 啟動 🎉

### 第 4 步：測試應用

1. 在瀏覽器中訪問 `http://localhost:8501`
2. 上傳一張食物的照片
3. 看到卡路里估計結果！

---

## 部署到 Hugging Face Spaces（5 分鐘）

### 步驟 1：建立 Space

1. 訪問 [Hugging Face Spaces](https://huggingface.co/spaces)
2. 點擊「Create new Space」
3. 填寫：
   - **Space name**: `calorie-estimator`
   - **License**: `MIT`
   - **Space SDK**: `Docker`
   - **Visibility**: `Public`

### 步驟 2：推送程式碼

```bash
git remote add huggingface https://huggingface.co/spaces/YOUR_USERNAME/calorie-estimator
git push huggingface main
# 輸入 Hugging Face Token 當被提示時
```

### 步驟 3：設定 API Key

1. 進入你的 Space 設定頁面
2. 點擊「Settings」→「Secrets and variables」
3. 新增 secret：
   - **Name**: `GOOGLE_API_KEY`
   - **Value**: 你的 Google API Key

4. 儲存 - Space 會自動重新部署 ✨

---

## 🎯 就這樣！

應用程式現在：
- ✅ 在本機執行（http://localhost:8501）
- ✅ 在 Hugging Face Spaces 上部署（https://huggingface.co/spaces/YOUR_USERNAME/calorie-estimator）

---

## 遇到問題？

查看詳細文件：

- **本機設定**: `docs/SETUP_GUIDE.md`
- **部署指南**: `docs/HUGGINGFACE_DEPLOYMENT.md`
- **部署檢查清單**: `docs/DEPLOYMENT_CHECKLIST.md`
- **專案總結**: `PROJECT_SUMMARY.md`

---

## 快速命令參考

```bash
# 啟動應用
./streamlit_run.sh

# 或
source .venv/bin/activate
streamlit run src/app.py

# 更新相依套件
uv sync --all-extras

# 查看 Git 狀態
git status

# 推送到 Hugging Face
git push huggingface main

# 查看遠端倉庫
git remote -v
```

---

祝你使用愉快！🍔🤖
