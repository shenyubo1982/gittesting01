## pool下的__init__.py
#from pool import versions ##绝对导入
## 或 import pool.futures

from . import versions ## 推荐使用相对导入
import pool.futures
##from . import versions ##相对导入
## .代表当前文件所在的目录，..代表当前目录的上一级目录，依次类推
#pool下的__init__.py


##针对包内模块之间的互相导入，推荐使用相对导入，强调：
# 1.相对导入只能在包内部使用，用相对导入不同目录下的模块是非法的。
# 2.无论是用import，form import，只要是在导入时带点的，
#   点的左侧必须是包，否则语法错误


