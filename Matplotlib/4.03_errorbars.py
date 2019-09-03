#!/usr/bin/env python
# coding: utf-8

'Visulizing Errors'
# error report is as important if not more import than accurate computational reporting. For instance the hubble constant
# e.g., the expansion rate of the Universe suggests a value of 71 (km/s)/Mpc and you recieved a value of 74 (km/s)/Mpc with
# a given method. Is this information correct and are the values consistent? It is impossible to know. Now consider enhancing
# you computations to report uncertanties. The current standard is 71 'plus or minus' 2.5 (km/s)/Mpc and any method has
# measured a value of 74 'plus or minus' 5 (km/s)/Mpc. This is consistant and can be quantitatively answered.

'Basic Errorbars'
# it is possible to create an errorbr with a single Matplotlib function call

# setting up the enviroment
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

x = np.linspace(0, 10, 50)
dy = 0.8
y = np.sin(x) + dy * np.random.rand(50)
plt.errorbar(x, y, yerr=dy, fmt='.k');
# fmt is a code for format controlling the appearance of lines and points

# that are many options to customize the aesthetics of an errorbar plot. This is useful in crowded plots
plt.errorbar(x, y, yerr=dy, fmt='o', color='black',
             ecolor='lightgray', elinewidth=3, capsize=0);
# it is possible to specify the horizontal errorbar (xerr), one-sided errorbars, and other variants

'Continuous Errors'
# when it is desired to show continuous errorbar quantities then it is possible to combine plt.plt and plt.fill_between

# performing a simple Gaussian process regression with Scikit-learn's API. This is a method of fitting a very flexible
# non-parametric function to data with a continuous measure of the undertantiy.

# as sklern.gaussian_process import GaussianProcess has been depreceated and the method has changed I will need to learn
# how to implement the GaussianProcessRegressor method.

'''
What do I know right now?
doc on the method: https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html?fbclid=IwAR0KszS4J35_9IAovbNlGuk8VnVADKIschdVFz34Xe5O2oEIXUNUCnwuvlA#sklearn.gaussian_process.GaussianProcessRegressor
visulization reference: https://l.facebook.com/l.php?u=https%3A%2F%2Fmedium.com%2Fdistrict-data-labs%2Fvisual-diagnostics-for-more-informed-machine-learning-7ec92960c96b%3Ffbclid%3DIwAR1cE1UhsK2q8YO0H8cu7z7gHdkfZ55at-q7R80mUvE2arGd6qrDFA-uOag&h=AT11qKGKPMmEK8_mC4YcziEIoE7RCslbRqlz9MlbZA_yoUsQwlVKtxnIgzzlZoPgw47kPnzTcsh1oAvhsklVDApe7OwNDJF6IdgGib8Mgr4wOkmbm_59hXZTuvgXHpbEdy3o_V7hFY-VteK5PgYGgZYk

GaussianProcess was deprecated in 0.18 and removed in 0.20 , we need to use GaussianProcessRegressor instead.
It's a cubic correlation according to the image, in GaussianProcess we can set the trend to either cubic, linear, quadratic but in Regressor it is constant.
for regressors metrics for error rate are Mean squared error, absolute error and F2 score.
absolute error is the difference between the predicted values and true values. F2 score determines how likely your model gonna predict well in future.
'''

## from sklearn.gaussian_process import GaussianProcess # old method sklearn <= 0.20 (current version is 0.21.3)
from sklearn import gaussian_process # is this the correct method?

# define the model and draw some data
model = lambda x: x * np.sin(x)
xdata = np.array([1, 3, 5, 6, 8])
ydata = model(xdata)

# Compute the Gaussian process fit
## gp = GaussianProcess(corr='cubic', theta0=1e-2, thetaL=1e-4, thetaU=1E-1,
##                      random_start=100)
## gp.fit(xdata[:, np.newaxis], ydata)

xfit = np.linspace(0, 10, 1000)
## yfit, MSE = gp.predict(xfit[:, np.newaxis], eval_MSE=True)
## dyfit = 2 * np.sqrt(MSE) # 2*sigma ~ 95% confidence

# it is impossible to visualize the data as it stands and I will need to research how to implement this method

# visulizing the result
plt.plot(xdata, ydata, 'or')
plt.plot(xfit, yfit, '-', color='gray')

plt.fill_between(xfit, yfit, - dyfit, yfit + dyfit,
                 color='gray', alpha=0.2)
plt.xlim(0, 10);
# the fill_between function is having an x value passed then the lower y-bound, then the upper y-bound, and the result
# is that the area between these regions is filled
