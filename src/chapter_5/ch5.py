# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 22:24:05 2017

@author: XiaoY
"""

import numpy as np
import matplotlib as mpl # 导入matplotlib库
import matplotlib.pyplot as plt # 主要的绘图子库

'''
# matplotlib的所有配置保存在下面的字典中，修改字典对应的值即为修改配置
print(mpl.rcParams)
print(mpl.get_configdir())   # 获取配置文件夹
print(mpl.matplotlib_fname())   # 获取当前使用的配置文件路径

mpl.rcParams['font.family'] = 'SimHei'   # 修改字体支持中文，解决中文乱码
mpl.rcParams['backend'] = 'TkAgg'   # 修改后端，解决Qt5平台错误
mpl.rcParams['axes.unicode_minus'] = False # 解决负号显示为方块
'''
'''
上述的配置只在当前执行文件中生效，可以直接在配置文件修改，永久生效
Anaconda3\Lib\site-packages\matplotlib\mpl-data\matplotlibrc   # matplotlib默认配置文件，修改配置后永久有效
> font.family : SimHei   # 解决中文乱码
> backend : TkAgg   # 解决 Qt5 平台报错
> axes.unicode_minus : False   # 解决负号是方块
mpl.rc_params()   # 重新读取配置，以字典形式返回
'''
figure = plt.figure() # 创建画布
'''
# 创建坐标系，参数表示画布中可以放置2行3列坐标系，即6个坐标系，当前选用的是第1个
axes_plot = figure.add_subplot(2, 3, 1) # 可缩写为axes_plot = figure.add_subplot(231)
axes_plot.plot([1,2,3,4], [1,2,3,4])
'''
'''
# 直接使用plt及逆行绘制图形
# 下面会自动创建画布和坐标系，之后直接使用当前坐标系进行绘制
plt.plot([1,2,3,4], [1,2,3,4], color='r', linestyle='--', label='直线')
plt.xticks([1,2,3,4])
plt.title('使用plt绘制折线图')
plt.text(2, 2, '这是(2,2)')
plt.legend()

plt.show()
'''
'''
import numpy as np
x_scatter = np.random.randn(20)
y_scatter = np.random.randn(20)

axes_scatter = figure.add_subplot(2, 3, 2)
axes_scatter.scatter(x_scatter, y_scatter, marker='o', c=['r', 'b', 'k'], cmap=plt.cm.hot)
axes_scatter.set_title('scatter')
axes_scatter.annotate('annotate_10', xy=[x_scatter[10], y_scatter[10]], xytext=[0.2,0.2], arrowprops=dict(facecolor='g'))
'''
'''
axes_bar = figure.add_subplot(2,3,3)
x_bar = np.linspace(1,5,5)
y_bar = np.linspace(1,5,5)
axes_bar.bar(x_bar, y_bar, align='center')
for x_t, y_t in zip(x_bar, y_bar):
    axes_bar.text(x=x_t, y=y_t+0.01, s='%.0f' % y_t, ha='center', va= 'bottom')
axes_bar.set_title('bar')
'''
'''
axes_hist = figure.add_subplot(2,3,4)
x_hist = np.random.randn(1000)
axes_hist.hist(x_hist, bins=50, normed=True)
axes_hist.set_title('hist')
'''
'''
plt.pie([1,2,3], explode=[0.1, 0, 0])
'''
'''
plt.boxplot([1,2,3,4,5,2,3,4,20])
'''
'''
print(mpl.projections.get_projection_names())   # 获取当前画布支持的作图类型
# import mpl_toolkits.mplot3d
from mpl_toolkits.mplot3d import Axes3D   # 导入 3D 库
print(mpl.projections.get_projection_names())

figure = plt.figure()
axes = figure.add_subplot(111, projection='3d')
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
x, y = np.meshgrid(X, Y)
r = np.sqrt(x**2 + y**2)
z = np.sin(r)
axes.plot_surface(x, y, z, rstride=1, cstride=1, cmap='rainbow')
'''
from mpl_toolkits.mplot3d import Axes3D
axes_plot_surface = figure.add_subplot(111,projection='3d')
x_sf = np.linspace(-2, 2, 100)
y_sf = np.linspace(-2, 2, 100)
X_sf, Y_sf = np.meshgrid(x_sf, y_sf)
z = np.sin(np.sqrt(X_sf**2+Y_sf**2))
axes_plot_surface.plot_surface(X_sf, Y_sf, z, cmap=plt.cm.hot)
axes_plot_surface.contourf(X_sf, Y_sf, z, zdir='z', offset=-1, cmap=plt.cm.hot)
axes_plot_surface.set_zlim(-1, 2)
axes_plot_surface.set_title('surface')

plt.show()











































