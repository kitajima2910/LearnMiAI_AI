from numpy import loadtxt
from sklearn.model_selection import train_test_split
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
import os

# FIX: Your CPU Supports Instructions that this TensorFlow Binary was not Compiled to use AVX2
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 1.load dữ liệu chia Train, Val và Test
dataset = loadtxt('pima-indians-diabetes.data.csv', delimiter=',')

X = dataset[:, 0:8]
Y = dataset[:, 8]

X_train_val, X_test, Y_train_val, Y_test = train_test_split(X, Y, test_size=0.2)
X_train, X_val, Y_train, Y_val = train_test_split(X_train_val, Y_train_val, test_size=0.2)

# 2. Xây dựng model
# 2.1 Sequential model
model = Sequential(
    [
        layers.Dense(16, input_dim=8, activation='relu'),
        layers.Dense(8, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ]
)

# 2.2 Summary model
model.summary()

# 2.3 Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 2.4 Train model
model.fit(
    X_train,
    Y_train,
    epochs=100,
    batch_size=8,
    validation_data=(X_val, Y_val)
)

# 2.5 Save model
model.save('diabetes.h5')
