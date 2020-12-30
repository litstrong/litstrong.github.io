---
layout: post
title:  "拉格朗日乘数"
date:   2020-12-30 00:15:50 -0800
categories: math
---
拉格朗日乘数法可解一类约束最优化问题，它将最优化问题的维度增加一维后，巧妙地将问题转换为求解一个
函数的极值点。有趣的是，该极值点同时还是该函数的马鞍点。

# 约束最优化

求解一个函数的最大值或者最小值被称为最优化问题，我们知道对于无约束的最优化问题，可以通过寻找
导数为 0 的点。而实际情况最优化往往伴有若干约束条件。以下是一个
简化的约束最优化问题

$$
\begin{align}
  \text{optimize } & f(x),\\
\text{subject to } & g(x) = 0.\\
\end{align}
$$

下面会介绍以及简单证明拉格朗日乘数法可以用来解决该类问题。该类解法可以泛化到不等式以及非线性的约束条件，
只要满足 [KKT][kkt-wiki] 条件。

# 拉格朗日乘数法

引入 $$ \lambda $$ 并构建 $$ L $$ 函数

$$
L(x, \lambda) = f(x) + \lambda * g(x),
$$

再寻找使得 $$ L $$ 函数导数为 0 的 $$ (x^*, \lambda^*) $$

$$
\nabla L(x^*, \lambda^*) = 0.
$$

则 $$ x^* $$ 便是可以使 $$ f(x) $$ 在约束 $$ g(x)= 0 $$ 下最优的解。

## 证明

核心的引理是，如果对应的解 $$ x^* $$ 存在的话，则该解一定满足

$$
\nabla f(x^*) = \lambda * \nabla g(x^*).
$$

反证法。如下图所示，假设 $$ x_0 $$ 是最优解，如果 $$ \nabla f(x_0) \neq \nabla g(x_0) $$，
沿着 $$ g(x)=0 $$ 向两侧移动，定是沿着与 $$ \nabla g(x_0) $$ 相垂直的方向（图中的虚线）。
又因为 $$ \nabla f(x_0) \neq \nabla g(x_0) $$，一定能从 $$ A $$ 或者 $$ B $$ 点中找到一
侧方向并向该方向移动一个小增量使得 $$ f (x_0 + dx) $$ 更优。

![lagrange-multiplier](/assets/images/lagrange-multiplier.png){: .center}

## 马鞍点

首先，举一个简单的例子来理解为什么 $$ L $$ 函数最优解 $$ (x_*, \lambda_*) $$ 属于马鞍点。
假设我们需要优化以下问题

$$
\begin{align}
  \text{minimize } & f(x) = x^2,\\
\text{subject to } & g(x) = x = 0.\\
\end{align}
$$

然后，我们构建对应的拉格朗日函数

$$
\begin{align}
L(x, \lambda) &= f(x) + \lambda (x - 0)\\
              &= x^2 + \lambda * x.
\end{align}
$$

$$ L(x, \lambda) $$ 在 $$ x $$ 和 $$ \lambda $$ 都为 0 时，可取到最小值 0。
根据以下两点并结合下图，可知该点很可能为马鞍点：

* 当 $$ x = 0 $$ 时，$$ \lambda $$ 任意取值 $$ L $$ 都为常数；
* $$ \frac{\partial L}{\partial \lambda} = x $$ 表明在 $$ x = 0 $$ 的领域一侧梯度大于 0，一侧梯度小于 0。

<!-- TODO: centralize below plot.  -->
{% include charts/lagrange-multiplier.html %}

较严谨的方法可以使用 [二阶导数验证][saddle-test-wiki] ，该验证通过判定对应的 Hessian 矩阵的
行列式的正负来判断马鞍点。以下是 $$ L $$ 对应的 Hessian 矩阵

$$
H(L) =
\begin{bmatrix}
\frac{\partial^2 f}{\partial x^2} & \frac{\partial g}{\partial x} \\
\frac{\partial g}{\partial x} & 0\\
\end{bmatrix},
$$

则

$$
|H(L)| = -(\frac{\partial g}{\partial x})^2.
$$

当 $$ \frac{\partial g}{\partial x} \neq 0 $$ 时，
$$ |H(L)| < 0 $$，对应求解出的点为马鞍点。

# 与 Ridge Regression 的关联

给定 $$ (A, b) $$ 对应的线性回归问题，最小二乘法最小化损失函数

$$ L(x) = ||Ax - b||, $$

为了避免过拟合，
会在损失函数中引入惩罚项 $$ \lambda * ||x|| $$

$$ L(x, \lambda) = ||Ax - b|| + \lambda * ||x||. $$

该方法便称为 [Ridge Regression][ridge-wiki]。下面证明 Ridge Regression 问题等价于以下
带约束的最优化问题

$$
\begin{align}
  \text{minimize } & f(x) = ||Ax - b||\\
\text{subject to } & g(x) \leq c\\
                   & g(x) = ||x||.\\
\end{align}
$$

首先，根据拉格朗日乘数法，定义以上问题的拉格朗日函数为

$$
L'(x, l) = ||Ax - b|| + l * (||x|| - c)
$$

根据 KKT 条件，该约束最优化问题的解需要满足

$$ \nabla L' = \nabla L(x, l) = 0, $$

$$ ||x|| - c = 0. $$

当 $$ l=\lambda $$，且 $$ c = ||x^*||_\lambda $$ 约束最优化 $$ L' $$ 的解与 $$ L $$
的解等价，反之同理。详细的证明请参考 [Suzanna][suzyahyah-blog] 的博客以及 [这里][stack-overflow]。

[kkt-wiki]: https://en.wikipedia.org/wiki/Karush%E2%80%93Kuhn%E2%80%93Tucker_conditions
[saddle-test-wiki]: https://en.wikipedia.org/wiki/Second_partial_derivative_test
[suzyahyah-blog]: https://suzyahyah.github.io/math/optimization/2018/07/20/Constrained-unconstrained-form-Ridge.html
[stack-overflow]: https://math.stackexchange.com/questions/335306/why-are-additional-constraint-and-penalty-term-equivalent-in-ridge-regression
[ridge-wiki]: https://en.wikipedia.org/wiki/Tikhonov_regularization
