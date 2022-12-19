# Yehezkely Nitay 021976808
# ex3_1

# -------------------------------------Imports------------------------------
import numpy as np
import matplotlib.pyplot as plt

from scipy.ndimage import convolve
from sklearn import linear_model, datasets, metrics
from sklearn.model_selection import train_test_split
from sklearn.neural_network import BernoulliRBM
from sklearn.pipeline import Pipeline
from sklearn.metrics import precision_score
from sklearn.preprocessing import label_binarize
import time




# Making the array of the numbers
sqrs=[]
for _ in range(2,21):
    sqrs.append(_**2)


##############################################################################
# Setting up

def nudge_dataset(X, Y):
    """
    This produces a dataset 5 times bigger than the original one,
    by moving the 8x8 images in X around by 1px to left, right, down, up
    """
    direction_vectors = [
        [[0, 1, 0],
         [0, 0, 0],
         [0, 0, 0]],

        [[0, 0, 0],
         [1, 0, 0],
         [0, 0, 0]],

        [[0, 0, 0],
         [0, 0, 1],
         [0, 0, 0]],

        [[0, 0, 0],
         [0, 0, 0],
         [0, 1, 0]]]

    shift = lambda x, w: convolve(x.reshape((8, 8)), mode='constant',
                                  weights=w).ravel()
    X = np.concatenate([X] +
                       [np.apply_along_axis(shift, 1, X, vector)
                        for vector in direction_vectors])
    Y = np.concatenate([Y for _ in range(5)], axis=0)
    return X, Y

# Load Data
digits = datasets.load_digits()
X = np.asarray(digits.data, 'float32')
X, Y = nudge_dataset(X, digits.target)
X = (X - np.min(X, 0)) / (np.max(X, 0) + 0.0001)  # 0-1 scaling

X_train, X_test, Y_train, Y_test = train_test_split(X, Y,
                                                    test_size=0.2,
                                                    random_state=0)

# Models we will use
logistic = linear_model.LogisticRegression()
rbm = BernoulliRBM(random_state=0, verbose=True)




classifier = Pipeline(steps=[('rbm', rbm), ('logistic', logistic)])

###############################################################################
# Training

# Hyper-parameters. These were set by cross-validation,
# using a GridSearchCV. Here we are not performing cross-validation to
# save time.
rbm.learning_rate = 0.06
rbm.n_iter = 20
# More components tend to give better prediction performance, but larger
# fitting time
logistic.C = 6000.0

# Now we will train with different number of components.

avg_p=[]
time_diff=[]

# --------------------------------------- q1----------------------------------------------
def q1():
    def q1a(i):
        """
        The function is calculate the time of RBM-Logistic Pipeline method.
        :param i: the components.
        :return: Prints the time of the procedure and the average.
        """
        # Training RBM-Logistic Pipeline
        t0 = time.clock()
        rbm.n_components = i
        classifier.fit(X_train, Y_train)

        # Training Logistic regression

        logistic_classifier = linear_model.LogisticRegression(C=100.0)
        logistic_classifier.fit(X_train, Y_train)
        t1 = time.clock()
        time_diff.append(t1 - t0)

        # I print it twice to see if there is a difference.
        ap = precision_score(Y_test, classifier.predict(X_test), average='macro')
        print("AVG is: ", ap)
        avg_p.append(ap)
        ap = precision_score(Y_test, classifier.predict(X_test), average=None)
        print("AVG is: ", np.average(ap))

    for k in sqrs:
        q1a(k)
        print(k)
        print("X_train shape is: ", X_train.shape)
        print("X_test.shape() is: ", X_test.shape)
        print("rbm.transform(X_train) shape is: ", (rbm.transform(X_train)).shape)
        print("rbm.intercept_hidden_ is: ", rbm.intercept_hidden_.shape)
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        # Plotting
        plt.figure(figsize=(4.2, 4))
        for i, comp in enumerate(rbm.components_):
            plt.subplot(k, k, i + 1)
            plt.imshow(comp.reshape((8, 8)), cmap=plt.cm.gray_r,
                       interpolation='nearest')
            plt.xticks(())
            plt.yticks(())
        plt.suptitle(repr(k * k) + ' components extracted by RBM', fontsize=16)
        plt.subplots_adjust(0.08, 0.02, 0.92, 0.85, 0.08, 0.23)
        plt.show()

q1()

# --------------------------------------- q2 -------------------------------------------------------------
def q2():
    # Plotting graph 1:
    plt.title("Average precision vs. number of components")
    plt.xlabel("components")
    plt.ylabel("Average precision")
    plt.plot(sqrs, avg_p, 'g', [2, 400], [0.77, 0.77], 'b')
    plt.show()
    # Plotting graph 2:
    plt.plot(sqrs, time_diff, 'b')
    plt.title("The average time us, the number of components")
    plt.xlabel("Number of components")
    plt.ylabel("Time diff")
    plt.show()

 q2()


# ------------------------------------ End Of File ----------------------------------------------------------