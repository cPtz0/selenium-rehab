# Mock 筆記補充：模擬 `datetime.now()` 的注意事項
 
## 關於 `datetime` 的雙重命名問題
 
Python 的 `datetime` 模組中，本身就有一個叫做 `datetime` 的 class（類別）：
 
```python
# 結構類似於：
datetime.datetime.now()
```

如果我們在原始檔案中寫：
``` 
from datetime import datetime
now = datetime.now()
```
這樣會將 datetime class 直接帶入命名空間。

---
 
Patch 時容易出錯的寫法
 
如果在測試中這樣寫：
```
@patch("src.time_utils.datetime")
```
其實是嘗試整個替換 datetime 這個 class 本身
 
→ 而不是它裡面的 .now() 方法或其回傳物件
→ 這會導致測試中的錯誤，例如：
``` 
'int' object is not callable

AttributeError: 'MagicMock' object has no attribute 'hour'
``` 
---
 
解法建議
 
✅ 建議 1：改成完整的 import

# 原始檔改寫為：
```
import datetime
 
now = datetime.datetime.now()
```
✅ 建議 2：在測試中 patch 正確的層級
```
@patch("src.time_utils.datetime.datetime")
```
這樣才會準確地「模擬 datetime.datetime.now() 的行為」。
 
 
---
 
備忘錄（超重要）
 
> 「 patch 的對象，一定要跟原始檔案中用到的 '那個名字' 完全一致，不然就會亂套！」

---
 
延伸觀察
 
這個問題之所以容易踩雷，是因為 datetime 模組與它內部的 class 同名，
再加上 Python 的 import 是「名稱綁定」，不是「物件實體替換」，
因此 patch 要精準命中，不然就會不知所云。
 
---
 