---
layout: post
title:  "Coursera Machine Learning"
---

# Linear Regression
- Cost function is a convex function, mean of sum square error.
- Normal equation v.s. gradient method.
- When there are many features, normal equation have to solve a inverse of a matrix.

# Logistics Regression
- Linear regression could not get good result for 2-classification problem.
- It turns classification problem into splitting points with super plane after introducing sigmoid function.
- It will become a non-convex function if using square error as cost function (that is one of reasons sigmoid function be introduced).
- Logistics regression could be non-linear classifier if adding more features (like polynomial features), but that can be very expensive to train (that is why neural network is introduced).
- Logistics regression could also be used to make a multi-classification by using one-vs-all method.

# Regularization
- over fitting = high variance, under fitting = high bias.
- high lambda regularization = under fitting, low lambda = overfitting.
- Regularization could be used to reduce overfitting.
- Add many unrelated features will make you overfitting.

# Neural Network

- Chain rule
- Dynamic programming

# Model Tuning

## Learning Curve
- Learning curve is two curves, one is for train error with different size of train data while the other is the cross
validation error with same set of validation set (it is same with test data set if it is not used to adjust lambda).

- Regularization is helpful to adjust the learning curve, so you can select lambda based on a cross validation set.

- Using a very large training set makes it unlikely for model to overfit the training data.

- Over fitting (High variance).
  - low training error v.s. high validation error.
  - Add more training data may help.
  - less features may help.

- Under fitting (High bias).
  - more training data not help.
  - more features may help.

Please have a look at table below:

| Tries              | Overfitting | Underfitting |
| ------------------ | :---------: | -----------: |
| more training data | may work    | not work     |
| more features      | not work    | may work     |
| less features      | may work    | not work     |
| high lambda        | may work    | not work     |
| low lambda         | not work    | may work     |

## Cross Validation
- By using cross validation, you can choose different models based on F score.
- By using cross validation, you can try different thresholds by the F score for 2-classification problem.

# Support Vector Machine
- Adjust C and sigma.
  - C is just like 1/lambda.
    - low C => high lambda => avoid overfitting (overfitting means not optimal largest margin).
    - high C => low lambda => avoid underfitting (underfitting means line is put not correctly).
- Get top predictors according to weights if the svm model is linear.

# K-Means
- Optimization cost function.
  - Easy to debug.
  - Avoid local minimum value.
- How to choose number of clusters.
  - Draw curve based on error and number of clusters, and then choose `elbow` point.
  - Use a cost function based follow-up optimization.
- Apply on image compression.
  - Compress a 24bit images to a 16 color's image.
  - 16 clustering on the pixels in the image.

# PCA
- Minimize the sum error of the projection distance.
  - Projection, so it is different with linear regression.
- Choose K.
  - 99% of variance is retrained.
  - Use diagonal matrix after SVD.
- Applying.
  - Compress => good.
  - Speed up => good.
  - Visualization with 2d/3d data => good.
  - Avoid overfitting => bad.

# Scale on the large data
- Batch gradient descent.
- Stochastic gradient descent.
- Mini-batch gradient descent.
- online learning setting <-> SGD.
  - Example: learning the predicted click-through rate (CTR).
- Map/Reduce could be applied in forward / backprop for nerual network.

# Anomaly Detection
- small number of -1(anomaly), large number of +1(non-anomaly).
- test data are not large enough to show everything possible.
- application.
  - fraud detection.
  - manufacturing.
  - monitoring machines in data center.
- have new features to make feature like a Gaussian.
  - log(x + c).
  - x^(1/c).
- v.s. Multivariate Gaussian.
  - Original Model, need x1/x2 to capture relation between two features while Multivariate doesn't need.
  - Multivariate is expensive to compute.

# Recommenter Systems
- Content based system (defined features on movies, like romantic and action).
- Collaborative filtering (user based).
  - Need to provide what user like (like how many he likes action and romantic).
  - Iteration, theta -> x -> theta -> x ...
  - Minimize (x,theta) at the same time.
    - Define a J(x, theta).
  - This is also a "Low Rank Matrix Factorization".
  - Mean Normalization.
    - For users who are not giving any scores on the movie, average scores will be given. Otherwise, the scores of these users will turn out to be zeros.
- No bias unit.
  - bias unit is already included in the feature, that means it will automatically learn x0 = 1.

# Photo OCR (Photo Optical Character Recoginition)
- Text detection
- Character segmentation
- Character recognition
