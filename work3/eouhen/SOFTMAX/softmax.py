# Author : AnnieHathaway
import numpy as np

def softmax(x):
    # 避免数值溢出，将每个元素减去向量中的最大值
    exp_x = np.exp(x - np.max(x))
    # 计算 softmax 函数的值，使用 np.sum 对每个元素求和
    return exp_x / np.sum(exp_x, axis=0)

#input = input("请输入向量")
input_vector = np.array([[1, 2, 3], [4, 5, 6]])
output_vector = softmax(input_vector)

print("Input Vector Shape:", input_vector.shape)
print("Output Vector Shape:", output_vector.shape)
print("Softmax Output:", output_vector)