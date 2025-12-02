# 部署檢查清單

## ✅ 本機開發完成

- [x] 建立 pyproject.toml 並設定所有相依套件
- [x] 建立 FoodRecognizer 模組（使用 Google Gemini Vision API）
- [x] 建立 Streamlit 應用程式前端
- [x] 測試應用程式在本機 (localhost:8501) 成功執行
- [x] 建立 .env 檔案配置本機 Google API Key
- [x] 建立 .gitignore 確保 API Key 不被上傳
- [x] 建立 Dockerfile 供 Hugging Face Spaces 使用
- [x] 建立完整的文件和指南

## 🚀 即將進行：Hugging Face Spaces 部署

### 前置準備

- [ ] 確認你的 Hugging Face 帳號已建立：https://huggingface.co
- [ ] 生成 Hugging Face API Token：https://huggingface.co/settings/tokens
- [ ] 確保 Google API Key 已取得並保存在安全的地方

### 部署步驟

#### 步驟 1: 建立 Hugging Face Space

```
✅ 完成後：
- [ ] 訪問 https://huggingface.co/spaces
- [ ] 點擊「Create new Space」
- [ ] 填寫：
  - Space name: calorie-estimator（或你喜歡的名稱）
  - License: MIT
  - Space SDK: Docker
  - Visibility: Public
- [ ] 建立完成後記錄你的 Space URL：
  https://huggingface.co/spaces/YOUR_USERNAME/calorie-estimator
```

#### 步驟 2: 設定本機 Git Remote

```bash
# 在你的本機終端執行
cd /Users/Joseph/PycharmProjects/Calorie

# 新增 Hugging Face remote
git remote add huggingface https://huggingface.co/spaces/YOUR_USERNAME/calorie-estimator

# 驗證 remote 已新增
git remote -v
```

#### 步驟 3: 推送程式碼到 Hugging Face

```bash
# 推送主分支到 Hugging Face Space
git push huggingface main

# 系統會要求輸入認證
# 用戶名：git
# 密碼：你的 Hugging Face API Token
```

**如果推送失敗**：
```bash
# 可以嘗試清除舊的認證
git config --global credential.helper store
git credential reject https://huggingface.co
# 然後重新執行 push
```

#### 步驟 4: 在 Hugging Face Spaces 設定 API Key Secret

1. 訪問你的 Space：`https://huggingface.co/spaces/YOUR_USERNAME/calorie-estimator`
2. 點擊「Settings」標籤
3. 在左側選擇「Secrets and variables」
4. 點擊「New secret」
5. 設定：
   - **Name**: `GOOGLE_API_KEY`
   - **Value**: 你的 Google Generative AI API Key（從 https://aistudio.google.com/app/apikey 取得）
6. 點擊「Save」

#### 步驟 5: 等待自動部署

- [ ] Space 會自動開始構建（構建時間 2-5 分鐘）
- [ ] 在 Space 頁面可以看到構建日誌
- [ ] 構建完成後會自動重啟應用程式
- [ ] 訪問 Space URL 測試應用程式

## 🧪 測試部署

部署完成後，測試以下功能：

- [ ] 能夠訪問 Space URL
- [ ] 應用程式介面正常載入
- [ ] 可以上傳圖片
- [ ] 系統正確分析食物圖片
- [ ] 系統正確識別非食物圖片

## 📚 有用的資源

- [Hugging Face Spaces 文件](https://huggingface.co/docs/hub/spaces)
- [Streamlit 官方文件](https://docs.streamlit.io/)
- [Google Generative AI 快速入門](https://ai.google.dev/tutorials/python_quickstart)

## 🐛 常見問題排查

### Q: 推送時出現認證錯誤

**A:**
```bash
# 清除儲存的認證
git config --global credential.helper ""
# 重新推送會要求輸入 token
git push huggingface main
```

### Q: Space 構建失敗

**A:**
1. 檢查 Dockerfile 語法
2. 檢查 pyproject.toml 是否有效
3. 查看 Space 的構建日誌找出具體錯誤
4. 確保 .env 檔案不在 git 倉庫中

### Q: 應用程式顯示「API Key 未找到」

**A:**
1. 確認在 Space 設定中正確新增了 GOOGLE_API_KEY secret
2. 檢查 secret 的名稱是否完全相符（區分大小寫）
3. 在 Space 設定中儲存 secret 後，Space 會自動重新構建
4. 等待重新構建完成

### Q: 應用程式無法分析圖片

**A:**
1. 確認 Google API Key 有效且未過期
2. 確認 Google API 配額未耗盡
3. 嘗試使用不同的圖片測試
4. 檢查 Space 的日誌查看詳細錯誤訊息

## 📝 注意事項

- ✅ `.env` 檔案已在 `.gitignore` 中，不會被上傳
- ✅ `.venv` 目錄已在 `.gitignore` 中
- ✅ Dockerfile 使用 `uv` 套件管理器確保快速安裝
- ✅ Streamlit 預設在 port 8501 執行
- ❌ **不要在程式碼中硬寫 API Key**
- ❌ **不要提交 `.env` 檔案到 git**

## ✨ 部署完成！

部署完成後，你的應用程式將：
1. 在 Hugging Face Spaces 上持續執行
2. 可以公開存取（如果設定為 Public）
3. 自動處理 API Key（通過 Secrets）
4. 支援多個使用者同時訪問

祝賀！🎉
