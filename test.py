# import os
import tensorflow as tf

# from distutils.version import LooseVersion


# Check TensorFlow Version
# assert LooseVersion(tf.__version__) >= LooseVersion('1.0'), 'Please use TensorFlow version 1.0 or newer.  You are using {}'.format(tf.__version__)
# print('TensorFlow Version: {}'.format(tf.__version__))

# for k, v in os.environ.items():
#     print(k+" "+v)
#
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

