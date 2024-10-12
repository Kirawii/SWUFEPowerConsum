# SWUFEPowerConsum
西南财经大学易校园用电量自动获取

基于python3.9.18的requests库写的简易程序，可以在Linux服务器运行。

balance为剩余电量，会和时间以及变化量储存在同一目录下的csv文件中。

每半小时到一小时随机请求一次，并记录在csv文件中。

已考虑balance增加的情况，change不会考虑负数。

仅供学习使用，请勿以作他用。
