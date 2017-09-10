# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 13:00:35 2017

@author: XiaoY
"""

import pandas as pd # 导入pandas库

names = pd.Series(['小明', '小红', '小黑', '小刚']) # 创建Series
print(names) # 打印该结构数据
'''
其输出为：
0    小明
1    小红
2    小黑
3    小刚
dtype: object
'''
infos = [['小明', 27, 178], ['小红', 24, 170], ['小黑', 28, 180]]
infos_ser = pd.Series(infos) # 传入多维列表，仍然是把第一个元素(列表)作为Series的第一个数据
print(infos_ser)
'''
0    [小明, 27, 178]
1    [小红, 24, 170]
2    [小黑, 28, 180]
dtype: object
'''

ages = [27, 24, 28]
ages_ser = pd.Series(ages, index=['小明', '小红', '小黑']) # 设置索引使用index
print(ages_ser)
'''
dtype: object
小明    27
小红    24
小黑    28
dtype: int64
'''

print(ages_ser.dtype) # 获取Series存储的元素的数据类型
print(ages_ser.shape) # 获取Series的形状，即多少行多少列
print(ages_ser.index) # 获取Series的索引
print(ages_ser.values) # 获取Series的数据
'''
int64
(3,) # 3行没有列
Index(['小明', '小红', '小黑'], dtype='object')
[27 24 28]
'''

print(ages_ser[0]) # 通过默认的序号获取元素
print(ages_ser['小明']) # 通过索引名获取元素
print(ages_ser['小明':'小红']) # 通过切片获取元素

ages_ser[0] = 10 # 通过默认的的序号修改
ages_ser['小红'] = 18 # 通过索引标签修改
print(ages_ser)
'''
小明    10
小红    18
小黑    28
dtype: int64
'''

ages_ser.index.name = '姓名' # 给索引命名
ages_ser.name = '姓名与年龄' # 给Series命名
print(ages_ser)
'''
姓名
小明    10
小红    18
小黑    28
Name: 姓名与年龄, dtype: int64
'''
print(ages_ser.unique()) # 去除Series存储数据的重复值并返回
print(ages_ser.value_counts()) # 获取各元素的计数
print(ages_ser.isin([1, 10, 2])) # 判断Series的元素是否含在参数集合中，返回bool类型的Series
'''
[10 18 28]
10    1
18    1
28    1
Name: 姓名与年龄, dtype: int64
姓名
小明     True
小红    False
小黑    False
Name: 姓名与年龄, dtype: bool
'''

# 使用多维列表创建DataFrame
infos = [['小明', 27, 178], ['小红', 24, 170], ['小黑', 28, 180]]
infos_df_1 = pd.DataFrame(infos)
print(infos_df_1)
'''
    0   1    2
0  小明  27  178
1  小红  24  170
2  小黑  28  180
'''

# 带索引创建DataFrame，index设置行索引，columns设置列索引
infos_df_2 = pd.DataFrame(infos, index=[1,2,3], columns=['姓名', '年龄', '身高'])
infos_df_2.index.name = 'ID' # 给行索引命名
print(infos_df_2)
'''
    姓名  年龄   身高
ID             
1   小明  27  178
2   小红  24  170
3   小黑  28  180
'''

# 使用字典创建DataFrame，字典的键会变为列名
infos_dict = {'姓名':['小明', '小红', '小黑'], '年龄':[27, 24, 28], '身高':[178, 170, 180]}
infos_df_3 = pd.DataFrame(infos_dict)
print(infos_df_3)
'''
   姓名  年龄   身高
0  小明  27  178
1  小红  24  170
2  小黑  28  180
'''
tmp = infos_df_3['姓名'] # 获取姓名列
print(tmp)
tmp = infos_df_3[['姓名', '身高']] # 获取多列
print(tmp)
tmp = infos_df_3.年龄 # 获取年龄列
print(tmp)

infos_df_3.index = ['第1个人', '第2个人', '第3个人']
print(infos_df_3)
'''
      姓名  年龄   身高
第1个人  小明  27  178
第2个人  小红  24  170
第3个人  小黑  28  180
'''
tmp = infos_df_3.loc['第3个人', '身高'] # 通过索引标签获取数据
print(tmp)
tmp = infos_df_3.iloc[0, 0] # 通过索引位置获取数据
print(tmp)
#tmp = infos_df_3.ix['第2个人', 1] # 混合使用
print(tmp)
'''
180
小明
24
'''
tmp = infos_df_3.loc[:, '年龄'] # 获取年龄列
print(tmp)
tmp = infos_df_3.loc['第1个人', :] # 获取第一个人的一行
print(tmp)
tmp = infos_df_3.iloc[0:2, :]
print(tmp)
'''
第1个人    27
第2个人    24
第3个人    28
Name: 年龄, dtype: int64

姓名     小明
年龄     27
身高    178
Name: 第1个人, dtype: object

      姓名  年龄   身高
第1个人  小明  27  178
第2个人  小红  24  170
'''

tmp = infos_df_3.xs('第1个人') # 获取一行
print(tmp)
tmp = infos_df_3.xs('姓名', axis=1) # 改变axis=1，即可获取列
print(tmp)
'''
姓名     小明
年龄     27
身高    178
Name: 第1个人, dtype: object
第1个人    小明
第2个人    小红
第3个人    小黑
Name: 姓名, dtype: object
'''

print(infos_df_3)
'''
      姓名  年龄   身高
第1个人  小明  27  178
第2个人  小红  24  170
第3个人  小黑  28  180
'''
infos_df_3['姓名'] = '小刚' # 修改姓名列的数据为小刚
print(infos_df_3)
'''
      姓名  年龄   身高
第1个人  小刚  27  178
第2个人  小刚  24  170
第3个人  小刚  28  180
'''
infos_df_3.iloc[:, 0] = ['小明', '小红', '小黑'] # 修改姓名列的数据为列表中各元素
print(infos_df_3)
'''
      姓名  年龄   身高
第1个人  小明  27  178
第2个人  小红  24  170
第3个人  小黑  28  180
'''
infos_df_3.iloc[0:2, 0:2] = 0 # 修改选取的元素为0
print(infos_df_3)
'''
      姓名  年龄   身高
第1个人   0   0  178
第2个人   0   0  170
第3个人  小黑  28  180
'''
infos_df_3.iloc[0:2, 0:2] = ['小明', 27] # 获取前两行前两列，按行进行修改
print(infos_df_3)
'''
      姓名  年龄   身高
第1个人  小明  27  178
第2个人  小明  27  170
第3个人  小黑  28  180
'''
infos_df_3.iloc[0:2, 0:2] = [['小明', 27], ['小红', 24]] # 修改前两行前两列为多维列表中的数据
print(infos_df_3)
'''
      姓名  年龄   身高
第1个人  小明  27  178
第2个人  小红  24  170
第3个人  小黑  28  180
'''

print(infos_df_3.dtypes) # 获取数据类型
print(infos_df_3.shape) # 获取形状
print(infos_df_3.ndim) # 获取维度的个数
print(infos_df_3.size) # 获取元素总数
'''
姓名    object
年龄     int64
身高     int64
dtype: object
(3, 3)
2
9
'''

print(infos_df_3)
'''
      姓名  年龄   身高
第1个人  小明  27  178
第2个人  小红  24  170
第3个人  小黑  28  180
'''
# 使用insert可以在指定位置处插入一列
infos_df_3.insert(loc=3, column='地址', value=['上海', '杭州', '北京'])
print(infos_df_3)
'''
      姓名  年龄   身高  地址
第1个人  小明  27  178  上海
第2个人  小红  24  170  杭州
第3个人  小黑  28  180  北京
'''
# 插入一列数据
infos_df_3.loc[:, '学校'] = ['清华', '北大', '北大']
print(infos_df_3)
'''
      姓名  年龄   身高  地址  学校
第1个人  小明  27  178  上海  清华
第2个人  小红  24  170  杭州  北大
第3个人  小黑  28  180  北京  北大
'''
# 插入一行数据
infos_df_3.loc['第4个人', :] = ['小刚', 28, 190, '上海', '清华']
print(infos_df_3)
'''
      姓名    年龄     身高  地址  学校
第1个人  小明  27.0  178.0  上海  清华
第2个人  小红  24.0  170.0  杭州  北大
第3个人  小黑  28.0  180.0  北京  北大
第4个人  小刚  28.0  190.0  上海  清华
'''
# 使用drop可以删除列或行，指定axis=0即为删除行，axis=1删除列。原数据不会改变，返回删除后得到的数据
print(infos_df_3.drop('第4个人', axis=0)) # 删除第4个人行
'''
      姓名    年龄     身高  地址  学校
第1个人  小明  27.0  178.0  上海  清华
第2个人  小红  24.0  170.0  杭州  北大
第3个人  小黑  28.0  180.0  北京  北大
'''
print(infos_df_3.drop('学校', axis=1)) # 删除学校列
'''
      姓名    年龄     身高  地址
第1个人  小明  27.0  178.0  上海
第2个人  小红  24.0  170.0  杭州
第3个人  小黑  28.0  180.0  北京
第4个人  小刚  28.0  190.0  上海
'''
del infos_df_3['学校'] # 删除学校列，这种操作会改变原数据
print(infos_df_3)
'''
      姓名    年龄     身高  地址
第1个人  小明  27.0  178.0  上海
第2个人  小红  24.0  170.0  杭州
第3个人  小黑  28.0  180.0  北京
第4个人  小刚  28.0  190.0  上海
'''
index_dict = {'第1个人':'小明', '第2个人':'小红', '第3个人':'小黑', '第4个人':'小刚'}
print(infos_df_3.rename(index=index_dict))
'''
    姓名    年龄     身高  地址
小明  小明  27.0  178.0  上海
小红  小红  24.0  170.0  杭州
小黑  小黑  28.0  180.0  北京
小刚  小刚  28.0  190.0  上海
'''
columns_dict = {'姓名':'name', '年龄':'age', '身高':'height', '地址':'addr'}
print(infos_df_3.rename(columns=index_dict))
'''
      姓名    年龄     身高  地址
第1个人  小明  27.0  178.0  上海
第2个人  小红  24.0  170.0  杭州
第3个人  小黑  28.0  180.0  北京
第4个人  小刚  28.0  190.0  上海
'''
print(infos_df_3.reindex(index=['第2个人', '第3个人', '第1个人'], columns=['姓名', '地址']))
'''
      姓名  地址
第2个人  小红  杭州
第3个人  小黑  北京
第1个人  小明  上海
'''

print(infos_df_3)
print(infos_df_3+infos_df_3)
'''
      姓名    年龄     身高  地址
第1个人  小明  27.0  178.0  上海
第2个人  小红  24.0  170.0  杭州
第3个人  小黑  28.0  180.0  北京
第4个人  小刚  28.0  190.0  上海
        姓名    年龄     身高    地址
第1个人  小明小明  54.0  356.0  上海上海
第2个人  小红小红  48.0  340.0  杭州杭州
第3个人  小黑小黑  56.0  360.0  北京北京
第4个人  小刚小刚  56.0  380.0  上海上海
'''
print(infos_df_3.sum())
'''
姓名    小明小红小黑小刚
年龄         107
身高         718
地址    上海杭州北京上海
dtype: object
'''
print(infos_df_3.sum(axis=1))
'''
第1个人    205.0
第2个人    194.0
第3个人    208.0
第4个人    218.0
dtype: float64
'''
import numpy as np
infos_df_3.iloc[0, 0] = np.nan
print(infos_df_3)
'''
       姓名    年龄     身高  地址
第1个人  NaN  27.0  178.0  上海
第2个人   小红  24.0  170.0  杭州
第3个人   小黑  28.0  180.0  北京
第4个人   小刚  28.0  190.0  上海
'''
print(infos_df_3.isnull()) # notnull与之相反操作
'''
         姓名     年龄     身高     地址
第1个人   True  False  False  False
第2个人  False  False  False  False
第3个人  False  False  False  False
第4个人  False  False  False  False
'''
print(infos_df_3.fillna(0)) # 指定值0填充NaN
'''
      姓名    年龄     身高  地址
第1个人   0  27.0  178.0  上海
第2个人  小红  24.0  170.0  杭州
第3个人  小黑  28.0  180.0  北京
第4个人  小刚  28.0  190.0  上海
'''
# 使用下一个数据进行填充，ffill为上一个，axis控制行或者列
print(infos_df_3.fillna(method='bfill', axis=0))
'''
      姓名    年龄     身高  地址
第1个人  小红  27.0  178.0  上海
第2个人  小红  24.0  170.0  杭州
第3个人  小黑  28.0  180.0  北京
第4个人  小刚  28.0  190.0  上海
'''
print(infos_df_3.dropna()) # 移除缺失值，默认移除行，可以通过axis控制行或者列
'''
      姓名    年龄     身高  地址
第2个人  小红  24.0  170.0  杭州
第3个人  小黑  28.0  180.0  北京
第4个人  小刚  28.0  190.0  上海
'''
print(infos_df_3.dropna(axis=1, how='all')) # how参数控制是含有就进行移除还是全是Nan才进行移除
'''
       姓名    年龄     身高  地址
第1个人  NaN  27.0  178.0  上海
第2个人   小红  24.0  170.0  杭州
第3个人   小黑  28.0  180.0  北京
第4个人   小刚  28.0  190.0  上海
'''
def drop_nan(arg): # lambda x:'缺失值' if pd.isnull(x) else x
    '''
    这是处理函数
    '''
    if pd.isnull(arg):
        return '缺失值'
    return arg
# 使用applymap可以对个元素进行处理
print(infos_df_3.applymap(drop_nan))
'''
       姓名    年龄     身高  地址
第1个人  缺失值  27.0  178.0  上海
第2个人   小红  24.0  170.0  杭州
第3个人   小黑  28.0  180.0  北京
第4个人   小刚  28.0  190.0  上海
'''


info_base = pd.DataFrame(infos_dict) # 基本信息表
infos_dict_2 = {'姓名':['小明', '小红', '小黑'], '地址':['上海', '杭州', '上海']}
info_other = pd.DataFrame(infos_dict_2) # 其他信息表
print(info_base)
print(info_other)
'''
   姓名  年龄   身高
0  小明  27  178
1  小红  24  170
2  小黑  28  180
   地址  姓名
0  上海  小明
1  杭州  小红
2  上海  小黑
'''
print(pd.merge(info_base, info_other)) # 合并两张表
'''
   姓名  年龄   身高  地址
0  小明  27  178  上海
1  小红  24  170  杭州
2  小黑  28  180  上海
'''

print(pd.concat([info_base, info_base]))
'''
   姓名  年龄   身高
0  小明  27  178
1  小红  24  170
2  小黑  28  180
0  小明  27  178
1  小红  24  170
2  小黑  28  180
'''

info_data = pd.DataFrame({"姓名": ["小明", '小红', '小K', '小L', '小Y', '小U', '小T', '小N'], \
    "年龄": [23,24,23,24,23,25,24,25], \
    "身高": [178, 190,178,179,190,178, 190,178], \
    "学校": ['清华', '清华', '北大', '清华', '北大', '清华', '北大', '清华']})
print(info_data)
"""
   姓名  学校  年龄   身高
0  小明  清华  23  178
1  小红  清华  24  190
2  小K  北大  23  178
3  小L  清华  24  179
4  小Y  北大  23  190
5  小U  清华  25  178
6  小T  北大  24  190
7  小N  清华  25  178
"""
grpby = info_data.groupby(["学校"]) # 以学校进行分组，因为只有两种学校，所以会分为两组
print(grpby)
'''
<pandas.core.groupby.DataFrameGroupBy object at 0x00000266E2FA3A58>
'''
print(grpby.sum()) # 对每组数据进行求和操作
'''
     年龄   身高
学校          
北大   70  558
清华  121  903
'''
import numpy as np
print(grpby.agg([np.mean, np.sum])) # 使用agg可以进行多种操作
'''
           年龄          身高     
         mean  sum   mean  sum
学校                            
北大  23.333333   70  186.0  558
清华  24.200000  121  180.6  903
'''
def op(df, arg=0):
    return df.sort_values(['年龄']).iloc[0:2]
print(grpby.apply(op)) # 对每个分组进行自定义操作
'''
      姓名  年龄   身高
学校               
北大 2  小K  23  178
   4  小Y  23  190
清华 0  小明  23  178
   1  小红  24  190
'''

print(pd.pivot_table(info_data, index=['学校'], values=['年龄'], columns=['姓名'], aggfunc='sum', fill_value=0)) # -> grpby.mean()
'''
    年龄                            
姓名  小K  小L  小N  小T  小U  小Y  小明  小红
学校                                
北大  23   0   0  24   0  23   0   0
清华   0  24  25   0  25   0  23  24
'''

table_txt = pd.read_table('../../data/chapter_4/table.txt')
print(table_txt.shape)
print(table_txt)
'''
(4, 4)
   name gender  age  edu
0   Sim      M   27  YJS
1    Xu      F   25  YJS
2  Wang      F   26   BK
3    Wu      M   32   BK
'''





































