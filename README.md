# SWUFEPowerConsum
西南财经大学易校园用电量自动获取

需要自己抓取相关api，此项目不提供任何api和cookies。

基于python3.9.18的requests库写的简易程序，可以在Linux服务器运行。

在太高版本的python上无法运行，因为高版本python删除了cgi库，导致requests库出现错误。

balance为剩余电量，会和时间以及变化量储存在同一目录下的csv文件中。

每半小时到一小时随机请求一次，并记录在csv文件中。

已考虑balance增加的情况，change不会考虑负数。

-更新了自动邮件提醒，会在剩余电量低于20度的时候向指定邮箱发送邮件。
-更新了服务器重启后继续调用csv文件继续计算的设计，不用担心中断运行。
