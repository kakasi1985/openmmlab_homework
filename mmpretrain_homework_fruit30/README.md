

 ## 此项目为本人openmmlab训练营第5天MMPretrain课程课后作业。
    题目：基于 ResNet50 的水果分类

    背景：使用基于卷积的深度神经网络 ResNet50 对 30 种水果进行分类

    任务

    划分训练集和验证集
    按照 MMPreTrain CustomDataset 格式组织训练集和验证集
    使用 MMPreTrain 算法库，编写配置文件，正确加载预训练模型
    在水果数据集上进行微调训练
    使用 MMPreTrain 的 ImageClassificationInferencer 接口，对网络水果图像，或自己拍摄的水果图像，使用训练好的模型进行分类
    需提交的验证集评估指标（不能低于 60%）

    mmpretrain_fruit30.ipynb为主程序，mmpretrain/projects/fruits为算法配置文件，测试集评估指标、网上下载的水果图片预测结果截图在mmpretrain/workout目录中。