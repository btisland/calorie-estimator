# 本機設定指南

## 1️⃣ 取得 Google API Key

### 步驟

1. 開啟瀏覽器訪問 [Google AI Studio](https://aistudio.google.com/app/apikey)
2. 使用你的 Google 帳號登入（如果還沒登入）
3. 點擊左側的「Create API Key」
4. 選擇「Create API key in new project」
5. 複製顯示的 API Key（看起來像：`AIzaSy...`）

### 重要！

- **不要分享你的 API Key** 給任何人
- 這個 Key 已經在 `.gitignore` 中，不會被上傳到 GitHub
- 如果不小心洩露，可以在 Google Cloud 控制台重新生成

## 2️⃣ 設定本機環境

### 編輯 `.env` 檔案

在專案根目錄找到 `.env` 檔案，將 `GOOGLE_API_KEY=` 後面填入你的 API Key：

```
GOOGLE_API_KEY=AIzaSy... (你的真實 key)
```

## 3️⃣ 執行應用程式

```bash
# 進入專案目錄
cd /Users/Joseph/PycharmProjects/Calorie

# 啟動虛擬環境
source .venv/bin/activate

# 執行應用程式
python src/app.py
```

你應該會看到類似的輸出：

```
Running on http://0.0.0.0:7860
Gradio app is running at http://localhost:7860
```

## 4️⃣ 在瀏覽器中測試

1. 打開瀏覽器，訪問 `http://localhost:7860`
2. 你應該能看到「食物卡路里估計器」的介面
3. 嘗試上傳一張食物的照片
4. 點擊「分析」按鈕

## 測試建議

### 用來測試的圖片源

- 手機相機：拍一張你周圍的食物
- Google 圖片搜尋：搜尋「food photography」
- 其他圖片：確保有清晰的食物

### 測試場景

1. **正常食物**：漢堡、披薩、沙拉等
   - 預期結果：「這是[食物名稱]，大概[數字]卡路里」

2. **非食物圖片**：汽車、建築、貓等
   - 預期結果：「這個不是食物」

## 常見問題

### Q: 執行時出現 `ModuleNotFoundError: No module named 'food_recognizer'`

**A:** 確保：
1. 你在 `/Users/Joseph/PycharmProjects/Calorie` 目錄下
2. 虛擬環境已啟動 (應看到 `(.venv)` 在終端提示符前)
3. 執行的是 `python src/app.py`（不是 `python app.py`）

### Q: API Key 不被識別

**A:** 檢查：
1. `.env` 檔案是否在專案根目錄
2. `GOOGLE_API_KEY=` 後面有你的真實 key（沒有空格或引號）
3. 重啟 Python 應用程式

### Q: 出現「分析失敗」訊息

**A:** 可能原因：
- Google API 配額已用完（免費額度限制）
- API Key 無效或已過期
- 網路連線問題
- 圖片格式不支援

### Q: 慢或超時

**A:** 這是正常的，因為：
- 首次請求可能需要 5-10 秒
- 圖片較大時會更慢
- Google API 伺服器繁忙時會慢

## 下一步：Hugging Face Spaces 部署

設定完成並在本機成功執行後，參考 README.md 中的「Deployment to Hugging Face Spaces」部分進行部署。

主要步驟：
1. 在 Hugging Face 建立 Space
2. 推送程式碼到該 Space 的 git 倉庫
3. 在 Space 設定頁面新增 `GOOGLE_API_KEY` secret
4. 自動部署完成
