# Yehezkely Nitay 021976808
# ex2.py

# --------------Imports-----------------------------
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sklearn import datasets, svm, metrics
from sklearn import linear_model
from sklearn.cross_validation import cross_val_predict
from sklearn import preprocessing
from sklearn import datasets


#################################################################################
# -------------------------Functoins for Q 21-------------------------------------
#################################################################################


def get_upper_rows(m):
    """
    The function gets a matrix m at size l*l (l must be even!), and returns the:
     sum, the average, the variance
     of theupper l/2 rows.
    :param m: The matrix m.
    :return: A matrix of upper l/2 rows of m.
    """
    l=len(m)
    p=m[:(l//2)]
    return [np.sum(p), np.average(p), np.var(p)]

# ----------------------------------------------------------------------------------
def get_lower_rows(m):
    """
    Same as above but just for the lower rows.
    """
    l=len(m)
    p = m[l//2:]
    return [np.sum(p), np.average(p), np.var(p)]

# ----------------------------------------------------------------------------------
def get_first_cols(m):
    """
    same as above but just for the first cols.
    """
    l=len(m)
    p=m[:,0:l//2]
    return [np.sum(p), np.average(p), np.var(p)]

# ----------------------------------------------------------------------------------
def get_last_cols(m):
    """
    same as above
    """
    l=len(m)
    p=m[:,l//2:]
    return [np.sum(p), np.average(p), np.var(p)]


# ----------------------------------------------------------------------------------
# >>>>>>>>>>>>>>> The features <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -----------------------------------------------------------------------------------

#1
def diff_upper_lower(m):
    """
    The function gets matrix of picture m - and returns the difference between the upper part and the lower of m.
    :param m: The matrix
    :return: The difference between the upper part and the lower of m.
    """
    return (get_upper_rows(m)[0]-get_lower_rows(m)[0])

# ----------------------------------------------------------------------------------

#2
def diff_first_last(m):
    """
    The function gets matrix of picture m - and returns the difference between the first columns and the last columns of m.
    :param m: The matrix
    :return: The difference between the first columns and the last columns of m.
    """
    return (get_first_cols(m)[0]-get_last_cols(m)[0])

# ----------------------------------------------------------------------------------

#3
def ratio_first_last(m):
    """
    The function gets matrix of picture m - and returns the ratio between the first columns and the last columns of m.
    :param m: The matrix
    :return: The ratio (of the sum) between the first columns and the last columns of m.
    """
    if (np.sum(get_last_cols(m)==0)):
        return 0
    return ((np.sum(get_first_cols(m)))/np.sum(get_last_cols(m)))

# ----------------------------------------------------------------------------------

#4
def ratio_upper_lower(m):
    """
    The function gets matrix of picture m - and returns the ratio between the first columns and the last columns of m.
    :param m: The matrix
    :return: The ratio (of the sum) between the first columns and the last columns of m.
    """
    if (np.sum(get_lower_rows(m) == 0 )):
        return 0
    return ((np.sum(get_upper_rows(m)))/np.sum(get_lower_rows(m)))

# ----------------------------------------------------------------------------------

#5
def sum_inside_one(m):
    """
    This function is for only recognize 1 and 0!!
    :param m: A matrix
    :return: The sum of the
    """
    return (np.sum(m[:,1])+np.sum(m[:,len(m)-2]))


# ----------------------------------------------------------------------------------

#6
def max_inside_one(m):
    """
    This function is for only recognize 1 and 0!!
    :param m: A matrix
    :return: The sum of the
    """
    return (max(max(m[:,1]),max(m[:,len(m)-2])))


# ----------------------------------------------------------------------------------

#7
def num_of_zeros_at_center(m):
    """
    This function gets matrix m (8X8) of numbers and return the amount of zeros at the center.
    :param m: The matrix.
    :return: The amount of the zeros at the center.
    """

    b = m[3:5, 3:5]
    return(len(b[np.where(b <= 2)])) #Instead of 0 is better when little bit bigger. This is why I change it...

# ----------------------------------------------------------------------------------

#8
def num_of_large_numbers_at_center(m):
    """
    This function gets matrix m (8X8) of numbers and return the amount of large numbers(>=13) at the center.
    :param m: The matrix.
    :return: The amount of large numbers(>=13) at the center.
    """

    b = m[3:5, 3:5]
    return(len(b[np.where(b >= 13)]))
# ----------------------------------------------------------------------------------

#9
def var_of_up_triangular(m):
    """
    This function gets a matrix 8X8 and returns the variance of the upper triangle matrix.
    :param m: The matrix.
    :return: The function returns the variance of the upper triangle matrix
    """
    return (np.var(np.triu(m)))

# ----------------------------------------------------------------------------------

#10
def var_of_down_triangular(m):
    """
    This function gets a matrix 8X8 and returns the variance of lower triangle matrix.
    :param m: The matrix.
    :return: The function returns the variance of the lower triangle matrix.
    """
    return (np.var(np.tril(m)))
# ----------------------------------------------------------------------------------

#11
def sum_of_m_and_tm(m):
    """
    This function gets a matrix 8X8 and returns the sum of m and m^t.
    :param m: The matrix.
    :return: The function returns the sum of m and m^t.
    """
    t = np.transpose(m)
    return (np.sum(m + t))
# ----------------------------------------------------------------------------------

#12
def var_of_m_and_tm(m):
    """
    This function gets a matrix 8X8 and returns the variance of m and m^t.
    :param m: The matrix.
    :return: the variance of m and m^t.
    """
    t=np.transpose(m)
    return (np.var(m+t))

# ------------------------------------------------------------------------------------
#13
def huge_sum(m):
    """
    :param m: The matrix.
    :return: The total sum of each cell -i-, but (2**i)*m[i].
    """
    sum=0
    x = 1
    for i in m:
        for j in i:
            x = x*2
            sum+=x*j

    return sum

# ------------------------------------------------------------------------------------



# -------------------------Q-20---------------------------------------------------

# This part will be good also for Q21....
# The digits dataset
digits = datasets.load_digits()

# The data that we are interested in is made of 8x8 images of digits, let's
# have a look at the first 4 images, stored in the `images` attribute of the
# dataset.  If we were working from image files, we could load them using
# matplotlib.pyplot.imread.  Note that each image must have the same size. For these
# images, we know which digit they represent: it is given in the 'target' of
# the dataset.
images_and_labels = list(zip(digits.images, digits.target))

# To apply a classifier on this data, we need to flatten the image, to
# turn the data in a (samples, feature) matrix:
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

# Create a classifier: a support vector classifier
classifier = svm.SVC(gamma=0.001)

# We learn the digits on the first half of the digits
classifier.fit(data[:n_samples // 2], digits.target[:n_samples // 2])

# Now predict the value of the digit on the second half:
expected = digits.target[n_samples // 2:]
predicted = classifier.predict(data[n_samples // 2:])

print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(expected, predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))

images_and_predictions = list(zip(digits.images[n_samples // 2:], predicted))

def q20():
    # Represiting the wrong clf
    original = []
    clf = []
    digit_num = []
    print("The wrong identification digits:")
    for i in range((n_samples // 2)):
        if (expected[i] != predicted[i]):
            original.append(expected[i])
            clf.append(predicted[i])
            digit_num.append(i)
            print("Digit:",expected[i],", Comp says:", predicted[i], ", Place at the array:", i)
    wrong = list(zip(original, clf, digit_num))

    # plot it:
    line = 10
    col = int((len(wrong) / line))
    plt.suptitle("Test. mis-classification: expected - predicted")
    for index, (i, j, k) in enumerate(wrong):
        plt.subplot(3, 10, index + 1)
        plt.axis('off')
        plt.imshow(digits.images[(n_samples // 2) + k], cmap=plt.cm.gray_r, interpolation='nearest')
        plt.title(repr(i) + " " + repr(j))
    plt.show()

q20()

# ---------------------------------------------------Q-21--------------------------------------------------------


indices_0_1 = np.where(np.logical_and(digits.target >=0, digits.target<=1))
digits.target[indices_0_1]

print("\n\n\n")
# ---------------------------------------------------------------------------------
# -------------------------The confusion matrix of 0 and 1-------------------------
# up = upper, low= lower, fi=first, la=last

ratio_up_low=[]
ratio_fi_la=[]
diff_fi_la=[]
diff_up_low=[]
sumx=[]
avgx=[]
varx=[]
sum_1=[]
max_1=[]
zeros_at_center=[]
large=[]
tri_up=[]
tri_down=[]
var_of_m_and_t=[]
hugesum=[]

# -------------------------------------q21 - g: 0 and 1--------------------------------------------
def q21g():
    for i, j in (zip(indices_0_1[0], digits.target[indices_0_1])):
        x = digits.images[i]
        ratio_fi_la.append(ratio_first_last(x))
        ratio_up_low.append(ratio_upper_lower(x))
        diff_fi_la.append(diff_first_last(x))
        diff_up_low.append(diff_upper_lower(x))
        sumx.append(np.sum(x))
        varx.append(np.var(x))
        sum_1.append(sum_inside_one(x))
        max_1.append(max_inside_one(x))
        zeros_at_center.append(num_of_zeros_at_center(x))
        large.append(num_of_large_numbers_at_center(x))
        tri_up.append(var_of_up_triangular(x))
        tri_down.append(var_of_down_triangular(x))
        var_of_m_and_t.append(var_of_m_and_tm(x))
        hugesum.append(huge_sum(x))



    # creating the X (feature) matrix
    X = np.column_stack((sumx, varx, zeros_at_center, sum_1, max_1,large, var_of_m_and_t,tri_down,tri_up))
    # scaling the values for better classification performance
    X_scaled = preprocessing.scale(X)  # the predicted outputs
    Y = digits.target[indices_0_1]
    # Training Logistic regression
    logistic_classifier = linear_model.LogisticRegression()
    logistic_classifier.fit(X_scaled, Y)
    # show how good is the classifier on the training data
    expected = Y
    predicted = logistic_classifier.predict(X_scaled)
    print("Logistic regression using [sumx, varx, zeros_at_center, sum_1, max_1,large, var_of_m_and_t,tri_down,tri_up] features:\n%s\n" % (
        metrics.classification_report(
            expected,
            predicted)))
    print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))
    # estimate the generalization performance using cross validation
    predicted2 = cross_val_predict(logistic_classifier, X_scaled, Y, cv=10)
    print("Logistic regression using [sumx, varx, zeros_at_center, sum_1, max_1,large, var_of_m_and_t,tri_down,tri_up] features cross validation:\n%s\n" % (
    metrics.classification_report(expected, predicted2)))
    print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted2))

    # --------------q21 - e: Some graphs of 0 and 1:---------------------------
    # inner function of q21g()

    def q21e():
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        fig.suptitle("Variance, Sum, Amount of zeros at the centers")
        ax.scatter(varx, sumx, zeros_at_center, c=digits.target[indices_0_1])
        ax.set_xlabel('Variance')
        ax.set_ylabel('Sum of matrix')
        ax.set_zlabel('Zeros at canter')
        plt.show()

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        fig.suptitle("Variance, Sum, Amount of large numbers at the centers")
        ax.scatter(varx, sumx, large, c=digits.target[indices_0_1])
        ax.set_xlabel('Variance')
        ax.set_ylabel('Sum of matrix')
        ax.set_zlabel('Large numbers at canter')
        plt.show()

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        fig.suptitle("Variance, Zeros at center, and the variance of m+m^t")
        ax.scatter(zeros_at_center, large, var_of_m_and_t, c=digits.target[indices_0_1])
        ax.set_xlabel('Zeros_at_center')
        ax.set_ylabel('Large numbers at the center')
        ax.set_zlabel('Variance of m and m^t')
        plt.show()

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        fig.suptitle("Zeros at center, The variance of the lower triangular matrix, and the variance of m")
        ax.scatter(zeros_at_center, tri_down, varx, c=digits.target[indices_0_1])
        ax.set_xlabel('Zeros_at_center')
        ax.set_ylabel('The variance of the lower triangular matrix')
        ax.set_zlabel('Variance of m')
        plt.show()

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        fig.suptitle("Zeros at center, The variance of the lower triangular matrix, The Huge Sum")
        #I didn't use hugesum[] at the 0-1 section, but I put it here because its gives good seperation.
        ax.scatter(zeros_at_center, tri_down, hugesum, c=digits.target[indices_0_1])
        ax.set_xlabel('Zeros_at_center')
        ax.set_ylabel('The variance of the lower triangular matrix')
        ax.set_zlabel('The "HugeSum" of m')
        plt.show()

    #q21e()


q21g()

# -------------------------q21 - h: The confusion matrix of all numbers-------------------------
ratio_up_low=[]
ratio_fi_la=[]
diff_fi_la=[]
diff_up_low=[]
sumx=[]
avgx=[]
varx=[]
sum_1=[]
max_1=[]
zeros_at_center=[]
large=[]
tri_up=[]
tri_down=[]
var_of_m_and_t=[]
sum_of_n_and_tm=[]
hugesum=[]


def q21h():
    for i, j in (zip(np.arange(0,len(digits.target)), digits.target)):
        x = digits.images[i]
        ratio_fi_la.append(ratio_first_last(x))
        ratio_up_low.append(ratio_upper_lower(x))
        diff_fi_la.append(diff_first_last(x))
        diff_up_low.append(diff_upper_lower(x))
        sumx.append(np.sum(x))
        varx.append(np.var(x))
        sum_1.append(sum_inside_one(x))
        max_1.append(max_inside_one(x))
        zeros_at_center.append(num_of_zeros_at_center(x))
        large.append(num_of_large_numbers_at_center(x))
        tri_up.append(var_of_up_triangular(x))
        tri_down.append(var_of_down_triangular(x))
        var_of_m_and_t.append(var_of_m_and_tm(x))
        sum_of_n_and_tm.append(sum_of_m_and_tm(x))
        hugesum.append(huge_sum(x))

    # creating the X (feature) matrix
    X = np.column_stack((hugesum, varx, tri_down ,tri_up ,ratio_up_low ,var_of_m_and_t ,sum_1 ,max_1 ,zeros_at_center ,large))
    # scaling the values for better classification performance
    X_scaled = preprocessing.scale(X)  # the predicted outputs
    Y = digits.target
    # Training Logistic regression
    logistic_classifier = linear_model.LogisticRegression()
    logistic_classifier.fit(X_scaled, Y)
    # show how good is the classifier on the training data
    expected = Y
    predicted = logistic_classifier.predict(X_scaled)
    print("Logistic regression using [hugesum, varx, tri_down ,tri_up ,ratio_up_low ,var_of_m_and_t ,sum_1 ,max_1 ,zeros_at_center ,large] features:\n%s\n" % (
        metrics.classification_report(
            expected,
            predicted)))
    print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))
    # estimate the generalization performance using cross validation
    predicted2 = cross_val_predict(logistic_classifier, X_scaled, Y, cv=10)
    print("Logistic regression using [hugesum, varx, tri_down ,tri_up ,ratio_up_low ,var_of_m_and_t ,sum_1 ,max_1 ,zeros_at_center ,large] features cross validation:\n%s\n" % (
        metrics.classification_report(expected, predicted2)))
    print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted2))


q21h()

# -----------------------------------------------End Of File---------------------------------------------------------------------------