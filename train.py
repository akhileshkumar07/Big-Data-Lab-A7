import keras
from keras import layers

'''Load the MNIST dataset'''    
num_classes = 10
(X_train, Y_train), (X_test, Y_test) = keras.datasets.mnist.load_data()
# Reshape the input data
x_train = X_train.reshape(60000, -1)
x_test = X_test.reshape(10000, -1)
# Normalize pixel values to range between 0 and 1
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0
# Convert labels to one-hot encoding
y_train = keras.utils.to_categorical(Y_train, num_classes)
y_test = keras.utils.to_categorical(Y_test, num_classes)

'''Neural Network Model'''
model = keras.Sequential()
model.add(layers.Dense(256, activation='relu', input_shape=(784,)))
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

history = model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))
# Save the trained model
model.save("mnist_model.keras")
# Print the final training and validation accuracy
print('Train Accuracy: ', history.history['accuracy'][-1])
print('Validation Accuracy: ', history.history['val_accuracy'][-1])