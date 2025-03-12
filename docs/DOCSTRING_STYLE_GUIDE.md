# Python Docstring & Type Hint 樣式指南（個人風格初稿）
 
本指南為個人專案中所使用的 Python 函式撰寫格式，旨在提升可讀性、可維護性與可擴充性。
 
## 1. 函式定義格式範例
 
```python
def square(x: float) -> float:
    """
    計算正方形面積的函式。
 
    此函式為初階示範用，未來可提供模組化擴增及標準模板參照。
    傳入錯誤參數時（如 str、bool）將 raise ValueError。
 
    Args:
        x (float): 傳入正方形邊長，用於計算正方形面積。
 
    Returns:
        float: x 的平方，亦即正方形的面積。
 
    Raises:
        ValueError: 當輸入為非數值型態時會觸發此錯誤。
 
    Example:
        >>> square(5)
        25.0
    """
    if not isinstance(x, (int, float)):
        raise ValueError("參數必須為數值")
    return x * x
 