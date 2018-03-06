import tensorflow as tf

matrix1 = tf.constant([[3., 3.]])
matrix2 = tf.constant([[2.], [2.]])

preduct = tf.matmul(matrix1, matrix2)

sess_ = tf.InteractiveSession()

tf.global_variables_initializer().run()
print preduct.eval()

sess_.close()