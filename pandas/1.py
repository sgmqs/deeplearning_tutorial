#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-07 21:17:35
# @Author  : org (928758777@qq.com)
# @Link    : ${link}
# @Version : $Id$

from __future__ import print_function
import pandas as pd
import numpy as np

s 	=	pd.Series([1,2,4,np.nan,5,1])
print("s:",s)

dates	=	pd.date_range('20170101',periods=6)
df = pd.DataFrame(np.random.randn(6,5),index=dates,columns=['A','B','C','D','E'])
print("con:",df['C'])

df2 = pd.DataFrame({'A':1.,
		'B':pd.Timestamp('20160102'),
		'C':pd.Series(1,index=list(range(4)),dtype='float32'),
		'D':np.array([3]*4,dtype='int32'),
		'E':pd.Categorical(["test","train","123","567"]),
		'F':'footer'
	})

print("df2:",df2)
print("df2 type:",df2.dtypes)

print("df index:",df.index)
print("df colums:",df.columns)
print("df.values:",df.values)
print("df.describe:",df.describe)
print("df.T:",df.T)
print("df.sort_index:",df.sort_index(axis=1,ascending=False))
print("df.sort_values:",df.sort_values(by='C'))
