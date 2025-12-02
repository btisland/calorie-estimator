# 🔑 Hugging Face Token 指南

## 你為什麼需要 Hugging Face Token？

是的，你需要提供一個 Hugging Face API Token 來推送程式碼到 Hugging Face Spaces。這是用於：

1. **身份驗證** - 證明你的身份
2. **授權** - 確認你有權推送到該 Space
3. **安全** - 防止未授權的程式碼上傳

---

## 如何取得 Hugging Face Token

### 第 1 步：訪問 Token 設定

1. 登入 [Hugging Face](https://huggingface.co)
2. 點擊右上角的個人頭像
3. 選擇「Settings」
4. 點擊左側的「Access Tokens」

或直接訪問：https://huggingface.co/settings/tokens

### 第 2 步：建立新 Token

1. 點擊「New token」按鈕
2. 填寫 token 資訊：
   - **Name**: 例如 `calorie-push`（描述用途）
   - **Type**: 選擇「Write」（允許推送程式碼）
   - **Expiration**: 選擇「Never」或設定期限

3. 點擊「Generate token」

### 第 3 步：複製 Token

新建立的 token 會顯示在頁面上，看起來像：

```
hf_aBcDeFgHiJkLmNoPqRsT
```

**重要**：將這個 token **複製並保存在安全的地方**。關閉頁面後將無法再次查看。

---

## 如何使用 Token 推送程式碼

### 方法 1：Git 提示時直接輸入（推薦）

```bash
git push huggingface main
```

當被提示時：
- **Username**: 輸入 `git`
- **Password**: 貼上你的 Hugging Face Token

```
Username for 'https://huggingface.co': git
Password for 'https://git:***@huggingface.co': hf_aBcDeFgHiJkLmNoPqRsT
```

### 方法 2：使用 Git Credential Storage

如果你不想每次都輸入，可以儲存認證：

```bash
# 設定 Git 使用 credential helper
git config --global credential.helper store

# 執行 push - 會提示輸入認證
git push huggingface main

# 此後 Git 會記憶你的認證
```

### 方法 3：使用 Hugging Face CLI

```bash
# 安裝 Hugging Face CLI（如果還沒安裝）
pip install huggingface-hub

# 登入
huggingface-cli login
# 輸入你的 token

# 之後就可以推送
git push huggingface main
```

---

## 🔐 Token 安全最佳實踐

### 應該做的事 ✅

- ✅ 定期更新 token
- ✅ 對每個用途使用不同的 token
- ✅ 設定 token 過期時間
- ✅ 使用「Write」權限而不是「Admin」
- ✅ 將 token 安全地儲存（密碼管理器）

### 不應該做的事 ❌

- ❌ 與他人分享你的 token
- ❌ 在程式碼或 Git 歷史中暴露 token
- ❌ 使用過期的 token
- ❌ 給予超過必要的權限（例如只需要 Write，別給 Admin）
- ❌ 在公開場合（截圖、貼文）洩露 token

---

## 如果洩露了 Token

### 立即行動

1. 訪問 [Hugging Face Settings](https://huggingface.co/settings/tokens)
2. 找到被洩露的 token
3. 點擊「Delete」刪除它
4. **立即建立新的 token**
5. 更新你的認證設定

### 驗證安全

Hugging Face 會自動監控可疑活動。如果發現異常：
- 更改密碼
- 檢查最近的 Space 活動
- 聯繫 Hugging Face Support

---

## Token 相關的常見錯誤

### 錯誤 1：「Authentication failed」

**原因**: Token 不正確或已過期

**解決**:
```bash
# 清除舊的認證
git config --global credential.helper ""
git credential reject https://huggingface.co

# 重新輸入 token
git push huggingface main
```

### 錯誤 2：「Permission denied」

**原因**: Token 權限不足或指向錯誤的帳號

**解決**:
1. 確認 token 有「Write」權限
2. 確認使用的是你自己的帳號
3. 重新建立 token 並重試

### 錯誤 3：「Repository not found」

**原因**: Space URL 不正確

**解決**:
```bash
# 檢查 remote URL
git remote -v

# 應該顯示類似:
# huggingface https://huggingface.co/spaces/YOUR_USERNAME/space-name (fetch)
# huggingface https://huggingface.co/spaces/YOUR_USERNAME/space-name (push)

# 如果不正確，更新 remote
git remote set-url huggingface https://huggingface.co/spaces/YOUR_USERNAME/space-name

# 重新推送
git push huggingface main
```

---

## 關於 API Key（Google）vs Token（Hugging Face）的區別

這個專案涉及兩個不同的 key：

| | Google API Key | Hugging Face Token |
|---|---|---|
| 用途 | 調用 Google 的 AI 服務 | 推送程式碼到 Hugging Face |
| 位置 | `.env` 檔案和 Space Secrets | Git 認證 |
| 可見 | Secrets（隱藏） | 輸入時可見 |
| 權限 | 讀取權限 | 寫入權限 |
| 過期 | 不過期 | 可設定過期 |

---

## 快速參考

```bash
# 生成新 token
訪問: https://huggingface.co/settings/tokens

# 推送程式碼
git push huggingface main

# 當提示時輸入
Username: git
Password: <paste your token>

# 驗證 remote
git remote -v

# 更新 remote URL
git remote set-url huggingface <new-url>
```

---

## 更多資源

- [Hugging Face Security](https://huggingface.co/docs/hub/security)
- [Git Credentials 設定](https://git-scm.com/docs/git-credential)
- [Hugging Face API Documentation](https://huggingface.co/docs/hub/api)

---

## 需要幫助？

如果在使用 token 時遇到問題：

1. 檢查 token 是否正確（複製沒有多餘空格）
2. 確認 token 有「Write」權限
3. 嘗試刪除舊 token 並建立新的
4. 查看 [Hugging Face Support](https://huggingface.co/contact)

---

**重要**: Token 就像密碼，保護好它！🔐
