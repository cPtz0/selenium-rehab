import os
import sys
import unittest

# 將根目錄加進sys path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,project_root)

# 尋找tests/ 下的unittests模組
loader = unittest.TestLoader()
suite = loader.discover(start_dir="tests",pattern="test_*.py")

# 執行並輸出結果
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

# 未來延展部分(這裡已經可以讓程式自行結束)CI/CD可判斷是否成功
if result.wasSuccessful():
    sys.exit(0)
else:
    sys.exit(1)