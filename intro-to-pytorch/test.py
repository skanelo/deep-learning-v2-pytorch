import tensorflow as tf

print(tf.__version__)

x = tf.Variable(10)
y = tf.constant(5)

x.assign_add(1)

print(x+y)