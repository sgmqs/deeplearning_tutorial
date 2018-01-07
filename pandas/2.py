#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-07 21:48:20
# @Author  : org (928758777@qq.com)
# @Link    : ${link}
# @Version : $Id$

from __future__ import print_function
import pandas as pd
import numpy as np

dates =	pd.date_range('20170101',periods=6)
df =	pd.DataFrame(np.random.randn(6,5),index=dates,columns=['A','B','C','D','E'])
print("A:",df['A'])
print("df coum:",df[0:3],df['20170102':'20170104'])

#select by lable :loc
print("select by lable:",df.loc['20170103'])
print("selec a ,b:",df.loc[:,['A','B']])
print("selec ab:",df.loc['20170102',['A','B']])

#select by position :iloc
print("select by position:iloc:",df.iloc[2])
print("select position:",df.iloc[3,0])
print("selec position 3:",df.iloc[3:5,0:3])
# print("selec position 4:",df.iloc[1,2,4,5],[0,3])

#mixed selection:ix
print("selec maxed:",df.ix[:3,['A','B']])
#boolean indexing
print("boolean index:",df[df.A>0])