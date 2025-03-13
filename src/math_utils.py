#這裡注意到Py的型別問題，因此我們給出Type Hint(類型提示)，告訴coding的人這裡應該帶入什麼型別，但不是強制
# x : float 表示預期 x 為浮點數
# -> float 表示回傳值為浮點數
# 使用三引號(PEP257規範)
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
    return x * x

if __name__ == "__main__":
    try:
        num = float(input("輸入一個數字:")) 
        print(f"{num}的平方為:{square(5)}")
    except ValueError:
        print("無效輸入!")