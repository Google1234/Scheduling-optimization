# Scheduling-optimization
问题：已知集装箱中包含的零件和总的零件需求，求最优的调箱方案，使得所需要集装箱数目最少
代码适用于windows平台，如需在mac／Linux平台下使用，需要从https://www.coin-or.org/download/binary/ 下载对应的优化问题求解二进制文件，同时修改optimize.py 中代码
生成.exe 文件：cd 至main.py所在目录，执行 pyinstaller --onefile main.py ,同时在将data文件夹拷贝至main.exe目录
