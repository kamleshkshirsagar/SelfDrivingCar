import tensorflow as tf
#Code to tensorflow x = 10 y = 2 z = x/y - 1
x= tf.constant(10,tf.int32)
y= tf.constant(2,tf.int32)
z=tf.subtract(tf.divide(x,y),tf.cast(tf.constant(1),tf.float64))

#Print value of Z
with tf.Session() as sess:
    output=sess.run(z)
    print(output)