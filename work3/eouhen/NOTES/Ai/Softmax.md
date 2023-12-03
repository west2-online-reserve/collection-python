Softmax 函数是一个常用的激活函数，主要用于多分类问题的输出层。给定一个 N 维度的向量，Softmax 函数将每个元素转化为取值在 (0, 1) 之间的概率，并且所有元素的概率之和为 1。

Softmax 函数的定义如下：

对于给定的输入向量  X = \[x_1, x_2, ..., x_N] ，Softmax 函数的输出 σ(X) = \[σ(x_1), σ(x_2), ..., σ(x_N)]  计算如下：

$$
\sigma(x_i) = \frac{e^{x_i}}{\sum_{j=1}^{N} e^{x_j}} \quad \text{for} \quad i = 1, 2, ..., N
$$

其中，σ(x_i) 是输入向量中第  i 个元素经过 Softmax 转换后的概率，而 \( e^{x_i} \) 表示 \( x_i \) 的指数。

Softmax 函数广泛用于神经网络的输出层，特别是在多分类问题中，它将网络的原始输出转化为类别概率分布，便于进行分类决策。

```python
import numpy as np

def softmax(x):
    # 避免数值溢出，将每个元素减去向量中的最大值
    exp_x = np.exp(x - np.max(x))
    
    # 计算 softmax 函数的值，使用 np.sum 对每个元素求和
    return exp_x / np.sum(exp_x, axis=0)
```
1. `exp_x = np.exp(x - np.max(x))`: 计算输入向量 `x` 中每个元素减去向量中的最大值后的指数，这一步是为了避免数值溢出。取最大值是因为指数函数增长非常快，如果输入中的某个元素很大，那么指数的结果会非常大，可能导致数值计算不稳定。

2. `return exp_x / np.sum(exp_x, axis=0)`: 计算 softmax 函数的值。`np.sum(exp_x, axis=0)` 对每个元素求和，然后将每个元素除以这个和，得到最终的 softmax 概率分布。

这个函数可以处理输入向量 `x`，对每个元素进行 softmax 变换，返回一个概率分布。