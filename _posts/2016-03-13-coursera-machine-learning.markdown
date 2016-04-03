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

# Model Tuning

## Learning Curve
- Over fitting (High variance)
  - low training error v.s. high validation error
  - Add more training data may help
  - less features

- Under fitting (High bias)
  - more training data not help
  - more features

Please have a look at tables below:

| Tries              | Overfitting | Underfitting |
| ------------------ | ----------- | ------------ |
| more training data | may work    | not work     |
| more features      | not work    | may work     |
| less features      | may work    | not work     |
| high lambda        | may work    | not work     |
| low lambda         | not work    | may work     |

## Cross Validation
- By using cross validation, you can choose different models based on F score.
- By using cross validation, you can try different thresholds by the F score for 2-classification problem.

# Support Vector Machine

# ...
