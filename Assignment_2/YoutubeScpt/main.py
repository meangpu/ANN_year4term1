"""
Assignment2
Student name: Nattapong Tangsatheanrapap
613040128-7
"""

from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
import itertools
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import classification_report


def displayConfusionMatrix(cm, cmap=plt.cm.GnBu):
    classes = ["Other Number", "Number 0"]
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title("Confusion Matrix")
    plt.colorbar()
    trick_marks = np.arange(len(classes))
    plt.xticks(trick_marks, classes)
    plt.yticks(trick_marks, classes)
    thresh = cm.max() / 2
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], 'd'),
                 horizontalalignment='center',
                 color='white' if cm[i, j] > thresh else 'black')

    plt.tight_layout()
    plt.ylabel('Actually')
    plt.xlabel('Prediction')
    plt.show()


def display_image(number):
    plt.imshow(number.reshape(28, 28), cmap=plt.cm.get_cmap("Greys"), interpolation="nearest")
    plt.show()


def display_predict(clf, actually_y, x_value):
    print(f"Actually y = {actually_y}")
    print(f"Prediction = {clf.predict([x_value])[0]}")


mnist_raw = loadmat("data/mnist-original.mat")
# data มีข้อมูล 70000 ชุด และขนาด 784 (28*28 Pixel)
# target มีข้อมูล 70000 ชุด เป็นเลข 0-9 คือคำตอบของข้อมูล
mnist = {"data": mnist_raw["data"].T, "target": mnist_raw["label"][0]}

x = mnist["data"]
y = mnist["target"]

# print(mnist["data"].shape)

# แบ่งข้อมูลออกเป็น 60000 กะ 10000 เอาไป train กะ test
# ข้อมูล class 0-9
x_train = x[:60000]
x_test = x[60000:]
y_train = y[:60000]
y_test = y[60000:]

# ทาย 0 กะ ไม่ใช่ 0
# -> มี 10 กลุ่ม
# print(x_test.shape)
predict_number = 50

y_train_0 = (y_train == 0)  # หาค่าทั้งหมดใน y ถ้าเป็น 0 ก็จะเอาออกมา 60000
y_test_0 = (y_test == 0)  # หาค่าทั้งหมดใน y_test ถ้าเป็น 0 ก็จะเอาออกมา 10000

y_train_5 = (y_train == 5)  # หาค่าทั้งหมดใน y ถ้าเป็น 0 ก็จะเอาออกมา 60000
y_test_5 = (y_test == 5)  # หาค่าทั้งหมดใน y_test ถ้าเป็น 0 ก็จะเอาออกมา 10000

sgd_clf = SGDClassifier()

# อันนี้จะแยกข้อมูลออกเป็น 2 กลุ่มเลยคือ ใช่ 0 กะไม่ใช่ 0
sgd_clf.fit(x_train, y_train_0)  # train data x with outcome y that only have 0

# score = cross_val_score(sgd_clf, x_train, y_train_0, cv=3, scoring="accuracy")  # cv คือ ทดลองกี่ครั้ง
# print(score)

y_train_predict = cross_val_predict(sgd_clf, x_train, y_train_0, cv=2)
cm = confusion_matrix(y_train_0, y_train_predict)

y_test_predict = sgd_clf.predict(x_test)

# classes = ["Other number", "Number 0"]
# print(classification_report(y_test_0, y_test_predict, target_names=classes))

plt.figure()
displayConfusionMatrix(cm)

# display_predict(sgd_clf, y_test_0[predict_number], x_test[predict_number])
# display_image(x_test[predict_number])
