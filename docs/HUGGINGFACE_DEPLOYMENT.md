# Hugging Face Spaces 部署指南

## 概述

Hugging Face Spaces 是免費的應用程式託管平台。我們的 Streamlit 應用程式已經完全支援 Spaces 部署，使用 Docker 容器化。

## 前置要求

1. **Hugging Face 帳號**：訪問 [huggingface.co](https://huggingface.co) 註冊
2. **Hugging Face API Token**：在帳號設定中生成
3. **本機已測試**：確保應用程式在本機能正常執行

## 部署步驟

### Step 1: 建立 Hugging Face Space

1. 登入 [Hugging Face](https://huggingface.co)
2. 進入 [Spaces 頁面](https://huggingface.co/spaces)
3. 點擊「Create new Space」按鈕
4. 填寫以下資訊：
   - **Space name**: `calorie-estimator`（或你喜歡的名稱，例如 `food-calorie-counter`）
   - **License**: 選擇 `mit`（或其他你偏好的開源協議）
   - **Space SDK**: **重要！選擇「Docker」**（不是 Streamlit，我們用 Docker 執行）
   - **Visibility**: 選擇「Public」（或「Private」如果你想保密）

5. 點擊「Create Space」
6. 等待 Space 建立完成

### Step 2: 獲取 Hugging Face Token

1. 進入 [Account Settings](https://huggingface.co/settings/tokens)
2. 點擊「New token」
3. 設定以下：
   - **Name**: 例如 `calorie-push`
   - **Type**: 選擇「Write」（允許推送程式碼）
   - **Expiration**: 選擇「Never」或適當的期限
4. 點擊「Generate token」並複製 token（看起來像：`hf_...`）

### Step 3: 設定本機 Git 和推送程式碼

在你的本機終端執行以下命令：

```bash
# 進入專案目錄
cd /Users/Joseph/PycharmProjects/Calorie

# 設定你的 Hugging Face 認證
# 當提示輸入 username 時，輸入 "git"
# 當提示輸入 password 時，貼上你的 Hugging Face Token
git config --global credential.helper store
git credential approve

# 或者使用 Hugging Face CLI 工具
huggingface-cli login
# 輸入你的 token 當被提示時

# 新增 Hugging Face 遠端倉庫
git remote add huggingface https://huggingface.co/spaces/YOUR_HUGGINGFACE_USERNAME/calorie-estimator

# 推送程式碼到 Spaces
git push huggingface main
```

⚠️ **替換 `YOUR_HUGGINGFACE_USERNAME` 為你的 Hugging Face 用戶名**

### Step 4: 在 Spaces 設定 API Key Secret

1. 進入你在 Hugging Face 上建立的 Space
2. 點擊「Settings」（設定）標籤
3. 在左側選擇「Secrets and variables」
4. 點擊「New secret」
5. 填寫：
   - **Name**: `GOOGLE_API_KEY`
   - **Value**: 貼上你的 Google API Key

6. 點擊「Save」

**重要**：不要把 API Key 放在 `.env` 檔案或程式碼中提交到 Hugging Face！使用 Secrets 確保安全。

### Step 5: 應用程式會自動部署

1. 設定 secret 後，Spaces 會自動重新構建應用程式
2. 過程可能需要 2-5 分鐘
3. 完成後，你會在 Space 頁面上看到一個連結

## 驗證部署

1. 訪問你的 Space URL（例如：`https://huggingface.co/spaces/YOUR_USERNAME/calorie-estimator`）
2. 應該能看到應用程式的介面
3. 嘗試上傳一張圖片並分析

## 檔案結構說明

Hugging Face Spaces Docker 部署會自動識別以下檔案：

- **`Dockerfile`**: Docker 容器設定（Spaces 會自動執行這個來構建容器）
- **`src/app.py`**: 主應用程式入口（在 Docker 中執行）
- **`pyproject.toml`**: 相依套件定義（Docker 構建時會安裝）
- **`uv.lock`**: 鎖定的相依套件版本（確保可重現的構建）
- **`.env`**: 本機開發用（不會被上傳，Spaces 使用 secrets 代替）
- **`.gitignore`**: Git 忽略規則

## Spaces 的環境特性

- **Python 版本**: 通常是 3.9 或更高
- **虛擬環境**: Spaces 自動管理
- **端口**: 應用程式自動在正確的端口運行
- **時間限制**: 30 分鐘無活動時應用程式會暫停

## 常見問題

### Q: 推送程式碼時認證失敗

**A:**
```bash
# 清除舊的認證並重新設定
git config --global credential.helper store
git credential reject https://huggingface.co
# 然後再執行 push，會提示輸入 token
git push huggingface main
```

### Q: Spaces 顯示「Build failed」

**A:** 檢查：
1. `.env` 檔案是否被提交（應該在 `.gitignore` 中）
2. `pyproject.toml` 語法是否正確
3. 查看 Spaces 構建日誌找出具體錯誤

### Q: API Key 不被識別

**A:** 確保：
1. 在 Spaces 設定中正確設定了 `GOOGLE_API_KEY` secret
2. 設定後 Spaces 已重新構建（等待幾分鐘）
3. API Key 沒有多餘的空格或特殊字元

### Q: 應用程式很慢

**A:**
- 首次啟動 Space 時會較慢（cold start）
- 30 分鐘無使用會暫停，下次訪問需要重新啟動
- 這是 Hugging Face 免費方案的限制

## 自訂 Spaces 頁面

如果想自訂 Space 的外觀和說明：

1. 在專案根目錄建立 `README.md`（我們已經有了）
2. 在 Space 設定中編輯 README
3. 可以新增徽章、截圖等

## 更新應用程式

當你修改程式碼並想更新 Spaces 上的版本：

```bash
# 在本機進行修改和測試
# 然後提交並推送
git add .
git commit -m "Update: your change description"
git push huggingface main
```

Spaces 會自動重新構建並部署。

## 安全注意事項

✅ **DO**:
- 使用 Spaces Secrets 存放 API Key
- 在 `.gitignore` 中排除 `.env` 檔案
- 定期檢查 API 使用情況

❌ **DON'T**:
- 在程式碼中硬寫 API Key
- 提交 `.env` 檔案到 git
- 在網路上分享你的 API Key

## 成本

- Hugging Face Spaces 免費方案提供基本資源
- 不需要信用卡即可使用
- 有 30 分鐘無活動暫停的限制

## 支援資源

- [Hugging Face Spaces 文件](https://huggingface.co/docs/hub/spaces)
- [Gradio 官方文件](https://www.gradio.app/docs)
- [Google Generative AI 文件](https://ai.google.dev/tutorials/python_quickstart)
