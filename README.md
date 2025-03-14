# selenium-rehab

- 建立 feature 分支開發
- 提交 PR 並進行模擬 Code Review 修正
- 合併至 main 並刪除分支
- 建立版本標籤並發布 GitHub Release
- 專案結構調整為 `src/`, `tests/`, `docs/`
 
## 執行測試
```bash
python run_test.py
```
## 功能列表
 
- `add(x, y)`: 加法（含例外處理）
- `subtract(x, y)`: 減法（含例外處理）
- `square(x)`: 計算平方（含例外處理）
- `divide(x, y)`: 除法（含例外處理）
- `sqrt(x)`: 開根號（含例外處理）
- `factorial(n)`: 階乘計算（支援遞迴 / 防呆）

## 備註
 
後續預計加入單元測試、更多數學函式擴充與簡易 API 接口練習，逐步建立功能模組化與測試習慣。