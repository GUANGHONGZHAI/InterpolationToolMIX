利用wrf-chem模型进行大气污染物数值模拟，获取排放清单数据后，将各种排放数据插值到我们的wrfinput文件是不可或缺的一步。
由清华大学开发的Mix数据是目前亚洲地区广泛使用的人为排放数据，但是网络上的插值代码主要针对于同门的MEIC数据，使用时需要微调。
这里完善了Hao lyu老师的代码https://github.com/IncubatorShokuhou/meic2wrf_hourly，为大家提供一个相对简单易行的MIX数据插值工具。
首先我们在官网下载数据后，需要使用split.py脚本按月份和排放部门对数据进行拆分
准备好拆分后的数据，wrfinput_d0i数据后就可以使用mix.py脚本一步产生排放源的.nc文件
