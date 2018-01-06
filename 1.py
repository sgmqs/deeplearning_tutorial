# -*- coding: utf-8 -*-
# @Date    : 2017-12-05 23:01:10
# @Author  : org (928758777@qq.com)
# @Link    : ${link}
# @Version : $Id$

import os
import tensorflow as tf
import numpy as np

x_data	=	np.float32(np.random.rand(2,100))
y_data 	=	np.dot([0.100,0.200],x_data)+0.300


b 	=	tf.Variable(tf.zeros([1]))
W 	=	tf.Variable(tf.random_uniform([1,2],-1.0,1.0))
y 	=	tf.matmul(W,x_data)+b


loss 	=	tf.reduce_mean(tf.square(y-y_data))
optimizer 	=	tf.train.GradientDescentOptimizer(0.5)
train 	=	optimizer.minimize(loss)


init 	=	tf.global_variables_initializer()


sess 	=	tf.Session()
sess.run(init)


for step in range(0,201):
	sess.run(train)
	if step %2==0:
		print(step,sess.run(W),sess.run(b))






