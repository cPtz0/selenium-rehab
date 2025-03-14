#這裡注意到Py的型別問題，因此我們給出Type Hint(類型提示)，告訴coding的人這裡應該帶入什麼型別，但不是強制
# x : float 表示預期 x 為浮點數
# -> float 表示回傳值為浮點數
# 使用三引號(PEP257規範)
import math
def square(x : float) -> float:
    """
    計算正方形面積的函式

    此函式為初階示範用，未來提供給模組化擴增及標準模板參照
    傳入錯誤參數時，如 str或bool將raise ValueError

    Args:
        x(float): 傳入正方形邊長,用於計算正方形面積。
 
    Returns:
        float: x 的平方,即正方形面積
 
    Raises:
        ValueError: 當輸入為非數值型態則會觸發此錯誤。
 
    使用案例:
        >>> square(5)
        25.0
    """
    if not isinstance(x,(int,float)):
        raise ValueError("請輸入數值!")
    return x * x
def add(x : float , y : float) -> float:
    """
    計算兩數相加之和

    Args:
        x(float): 傳入第一個參數,用於相加。
        y(float): 傳入第二個參數,用於相加。
 
    Returns:
        float: x + y 的和
 
    Raises:
        ValueError: 當輸入為非數值型態則會觸發此錯誤。
 
    Example:
        >>> add(1,2)
        3
    """
    if not isinstance(x,(int,float)):
        raise ValueError("請輸入數值!")
    if not isinstance(y,(int,float)):
        raise ValueError("請輸入數值!")
    return x + y

def subtract(x : float , y : float) -> float:
    """
    計算兩數相減之解

    Args:
        x(float): 傳入第一個參數,用於相減。
        y(float): 傳入第二個參數,用於相減。
 
    Returns:
        float: x - y 的解
 
    Raises:
        ValueError: 當輸入為非數值型態則會觸發此錯誤。
 
    Example:
        >>> subtract(3,2)
        1
    """
    if not isinstance(x,(int,float)):
        raise ValueError("請輸入數值!")
    return x - y

def divide(x : float , y : float) -> float:
    """
    計算兩數相除之解

    Args:
        x(float): 傳入第一個參數,作為被除數。
        y(float): 傳入第二個參數,作為除數。
 
    Returns:
        float: x / y 的解
 
    Raises:
        ValueError: 當輸入為非數值型態則會觸發此錯誤
        ZeroDivisonError: 當除數為0,即 y = 0 時

    Example:
        >>> divide(4,2)
        2
    """
    if not isinstance(x,(int,float)):
        raise ValueError("請輸入數值!")
    if y == 0:
        raise ZeroDivisionError("除數不可為0")
    
    return x / y

def sqrt(x : float) -> float:
    """
    計算一數之平方根

    Args:
        x(float): 傳入第一個參數,作為開根號數。
 
    Returns:
        float: x開根號 的解
 
    Raises:
        ValueError: 當輸入為非數值型態或 x < 0則會觸發此錯誤

    Example:
        >>> sqrt(9)
        3
    """
    if not isinstance(x,(int,float)):
        raise ValueError("請輸入數值!")
    if x < 0:
        raise ValueError("無法開根號小於0之數")
    
    return  math.sqrt(x) 

def factorial(x : int) -> int:
    """
    傳入一個非負整數n,回傳n的階乘結果。

    Args:
        x (int): 傳入一參數,計算階乘。
 
    Returns:
        int: x 的階乘結果
 
    Raises:
        ValueError: 當輸入為負數或非整數，則會觸發此錯誤。
 
    使用案例:
        >>> factorial(5)
        120
    """
    if not isinstance(x,int) or x < 0:
        raise ValueError("請輸入正整數!")
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1) 

if __name__ == "__main__":
    try:
        num = float(input("輸入一個數字:")) 
        num1 = float(input("輸入一個數字:")) 
        print(f"{num1} + {num} 為:{add(num,num1)}")
    except ValueError as ve: 
        print(f"輸入錯誤{ve}")
    except Exception as e:
        print(f"預期外錯誤{e}")
    