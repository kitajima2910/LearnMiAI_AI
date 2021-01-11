from tensorflow.keras.models import load_model
from numpy import loadtxt
from sklearn.model_selection import train_test_split
import os
import numpy

# FIX: Your CPU Supports Instructions that this TensorFlow Binary was not Compiled to use AVX2
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 1.load dữ liệu chia Train, Val và Test
dataset = loadtxt('pima-indians-diabetes.data.csv', delimiter=',')

X = dataset[:, 0:8]
Y = dataset[:, 8]

X_train_val, X_test, Y_train_val, Y_test = train_test_split(X, Y, test_size=0.2)
X_train, X_val, Y_train, Y_val = train_test_split(X_train_val, Y_train_val, test_size=0.2)

# load model
model = load_model('diabetes.h5')

loss, acc = model.evaluate(X_test, Y_test)
print('Loss: ', loss)
print('Acc: ', acc)

# đưa dữ liệu vào check
X_new = [1, 199, 60, 23, 999, 30.1, 0.911, 59]

X_new = numpy.expand_dims(X_new, axis=0)

X_predict = model.predict(X_new)

if X_predict <= 0.5:
    result = 'Không tiểu đường(0)'
else:
    result = 'Tiểu đường(1)'

print('Gia tri du doan: ', result)
