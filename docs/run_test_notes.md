run_tests.py 說明筆記
 
這是一份為了說明 `run_tests.py` 這支測試整合腳本的文件。
如果你剛學會寫單元測試、遇到模組找不到、指令太長、資料夾結構無法掌握等問題，這份筆記是為了解決這些問題而寫下的。

---
 
## 第一步：導入所需模組
```
import os
import sys
import unittest
```
這些模組都是 Python 內建的，不需要另外安裝：
 
os：處理系統路徑
 
sys：調整 Python 的模組搜尋路徑
 
unittest：Python 標準的測試工具
 
 
 
---
 
## 第二步：記住 run_tests.py 的絕對位置並補上模組路徑
```
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)
```
這段的作用是讓 Python 能正確找到你的 `/src` 模組。否則當你執行 `tests/test_*.py` 時，很可能會出現 `No module named 'src'` 的錯誤。
 
補充說明：
 
假設你專案的結構如下：

```
my_project/
├── src/
│   └── math_utils.py
├── tests/
│   └── test_math_utils.py
└── run_tests.py
```

執行 `os.path.abspath(__file__)` 的結果可能會是：
 
`C:\Users\me\Desktop\my_project\run_tests.py`
 
而 `os.path.dirname(...)` 會拿掉檔名，只保留：
 
`C:\Users\me\Desktop\my_project`
 
這樣就能讓 Python 從根目錄開始找模組，不會漏掉 `src/`
 
 
---
 
## 第三步：使用 unittest 掃描測試檔案
```
loader = unittest.TestLoader()
suite = loader.discover(start_dir="tests", pattern="test_*.py")
```
這段的意思是：
 
從 `tests/` 資料夾開始找
 
所有檔名開頭是 `test_` 且副檔名為 `.py` 的檔案都會被抓進來
 
整理成一份「待執行的測試清單」

---
 
第四步：執行測試並顯示結果
```
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
```
`TextTestRunner` 是 `unittest` 內建的測試執行器
 
`verbosity=2` 會列出每一個測試的詳細執行情況
 
測試結束後，結果會顯示每筆測試是否通過或失敗
 
 
範例輸出可能像這樣：
``` 
test_add (tests.test_math_utils.TestMathUtils) ... ok
test_square (tests.test_math_utils.TestMathUtils) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.002s
 
OK
 
``` 
---
 
## 第五步：將測試結果交給自動化系統判斷
```
if result.wasSuccessful():
    sys.exit(0)
else:
    sys.exit(1)
``` 
這段的功能是讓系統（像是 GitHub Actions 或 Jenkins）知道這次測試有沒有成功。
 
`0` 代表測試全部通過
 
`1` 代表至少有一項測試失敗
 
 
這是將來你接入 CI/CD 流程時非常重要的一段邏輯。
 
 
---
 
執行方式
 
請在專案根目錄下執行：
 
`python run_tests.py`
 
 
---
 
小結
 
這支程式的目的是「集中執行所有測試」
 
減少路徑錯誤、指令過長等問題
 
也方便日後與 CI/CD 串接
 
最終也可以寫進 README，幫助別人快速了解如何執行你的測試流程