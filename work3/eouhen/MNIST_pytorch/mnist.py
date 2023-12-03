# Author : AnnieHathaway
# 1.加载必要的库
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
# 2.定义超参数
BATCH_SIZE = 16 # 每批处理的数据
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
EPOCHS = 10 # 训练数据集的轮次

# 3.构建pipeline，对图像做处理
pipeline = transforms.Compose([
    transforms.ToTensor(), # 将图片转换成tensor
    transforms.Normalize((0.1307,), (0.3081,)) # 归一化
])

# 4.下载、加载数据
from torch.utils.data import DataLoader

# 下载数据集
train_set = datasets.MNIST("data", train=True, download=True, transform=pipeline)
test_set = datasets.MNIST("data", train=False, download=True, transform=pipeline)

# 加载数据
train_loader = DataLoader(train_set, batch_size=BATCH_SIZE, shuffle=True)
test_loader = DataLoader(test_set, batch_size=BATCH_SIZE, shuffle=True)
# 5.构建网络模型
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 10, 5) # 1：灰度图片的通道 10：输出通道（卷积核个数） 5：Kernel大小
        self.conv2 = nn.Conv2d(10, 20, 3) # 10：输入通道 20：输出通道 3：Kernel大小
        self.fc1 = nn.Linear(20*10*10, 500) # 20*10*10：输入通道 500：输出通道
        self.fc2 = nn.Linear(500, 10) # 500：输入通道 10：输出通道

    def forward(self, x):
        input_size = x.size(0)  # batch_size
        x  = self.conv1(x) # 进行卷积操作 输入：batch_size*1*28*28; 输出：batch_size*10*24*24 （24=28-5+1 步长默认为1）
        x = F.relu(x) # 激活函数 保持shape不变，输出：batch_size*10*24*24
        x = F.max_pool2d(x, 2,2) # 进行池化操作 输入：batch_size*10*24*24 输出：batch_size*10*12*12

        x = self.conv2(x)  # 进行卷积操作 输入：batch_size*10*12*12 输出：batch_size*20*10*10 （10=12-3+1）
        x = F.relu(x)

        x = x.view(input_size, -1) # 拉平 -1：自动计算维度20*10*10=2000

        x = self.fc1(x)  # 全连接层 输入：batch_size*2000 输出：batch_size*500
        x = F.relu(x)

        x = self.fc2(x) # 全连接层 输入：batch_size*500 输出：batch_size*10

        output = F.log_softmax(x, dim=1) # 计算分类后每个数字的概率值

        return output
# 6.定义优化器
model = Model().to(DEVICE)
optimizer = optim.Adam(model.parameters())
# 7.定义训练方法
def train(model, device, train_loader, optimizer, epoch):
    # 模型训练
    model.train()
    for batch_index, (data, target) in enumerate(train_loader):
        # 部署到DEVICE上
        data, target = data.to(device), target.to(device)
        # 梯度初始化为0
        optimizer.zero_grad()
        # 训练后的结果
        output = model(data)
        # 计算损失
        loss = F.cross_entropy(output, target)
        # 反向传播
        loss.backward()
        # 参数优化
        optimizer.step()
        if batch_index % 6000 == 0:
            print("Train Epoch : {} \t Loss : {:.6f}".format(epoch, loss.item()))
# 8.定义测试方法
def test(model, device, test_loader):
    # 模型验证
    model.eval()
    # 正确率
    correct = 0.0
    # 测试损失
    test_loss = 0.0
    with torch.no_grad():
        for data, target in test_loader:
            # 部署到DEVICE上
            data, target = data.to(device), target.to(device)
            # 测试数据
            output = model(data)
            # 计算测试损失
            test_loss += F.cross_entropy(output, target).item()
            # 找到概率值最大的下标(找到每一行最大值的下标)
            pred = output.argmax(dim=1)
            # 或pred = output.max(1, keepdim=True)[1] 返回：值，索引（索引的index为1）
            # 或pred = torch.max(output, dim=1)
            # 累计正确率
            correct += pred.eq(target.view_as(pred)).sum().item()
        test_loss /= len(test_loader.dataset)
        print("Test —— Average loss : {:.4f}, Accuracy : {:.3f}\n".format(
            test_loss, 100.0 * correct / len(test_loader.dataset)))
# 9.调用方法
for epoch in range(1, EPOCHS + 1):
    train(model, DEVICE, train_loader, optimizer, epoch)
    test(model, DEVICE, test_loader)