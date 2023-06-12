# openmmlab_homework
my openmmlab ai learning homework.

# 此项目为本人openmmlab训练营作业
### 目录ear_pred_kakasi1985为训练营第3天MMPose课程课后作业。
	题目：基于RTMPose的耳朵穴位关键点检测
	背景：根据中医的“倒置胎儿”学说，耳朵的穴位反映了人体全身脏器的健康，耳穴按摩可以缓解失眠多梦、内分泌失调等疾病。耳朵面积较小，但穴位密集，涉及耳舟、耳轮、三角窝、耳甲艇、对耳轮等三维轮廓，普通人难以精准定位耳朵穴位。
	任务：
	1.Labelme标注关键点检测数据集（子豪兄已经帮你完成了）
	2.划分训练集和测试集（子豪兄已经帮你完成了）
	3.Labelme标注转MS COCO格式（子豪兄已经帮你完成了）
	4.使用MMDetection算法库，训练RTMDet耳朵目标检测算法，提交测试集评估指标
	5.使用MMPose算法库，训练RTMPose耳朵关键点检测算法，提交测试集评估指标
	6.用自己耳朵的图像预测，将预测结果发到群里
	7.用自己耳朵的视频预测，将预测结果发到群里
	需提交的测试集评估指标（不能低于baseline指标的50%）

    项目的算法库mmcls、mmdet、mmpose均为源码安装，为了省上传空间，删除了大部分源码，只保留作业的配置文件和数据集文件，以及项目开发中生成的文件，大多文件为省空间已删除原文件，换成原文件结构截图。RTMDet、RTMPose算法的训练集、测试集评估指标截图在目录“训练集与测试集评估指标截图”中，耳朵目标检测预测程序生成的图片与视频放在目录“耳朵目标检测预测图片与视频”中，耳朵穴位关键点检测程序生成的图片与视频放在目录“耳朵穴位关键点检测图片与视频”中。

 ### 目录mmpretrain_homework_fruit30为训练营第5天MMPretrain课程课后作业。
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

 ### 目录MMDetection_homework为训练营第7天MMDetection课程课后作业。
 作业：基于 RTMDet 的气球检测

背景：熟悉目标检测和 MMDetection 常用自定义流程。

任务：

基于提供的 notebook，将 cat 数据集换成气球数据集
按照视频中 notebook 步骤，可视化数据集和标签
使用MMDetection算法库，训练 RTMDet 气球目标检测算法，可以适当调参，提交测试集评估指标
用网上下载的任意包括气球的图片进行预测，将预测结果发到群里
按照视频中 notebook 步骤，对 demo 图片进行特征图可视化和 Box AM 可视化，将结果发到群里
需提交的测试集评估指标（不能低于baseline指标的50%）
目标检测 RTMDet-tiny 模型性能不能 65 mAP
数据集
气球数据集可以直接下载 https://download.openmmlab.com/mmyolo/data/balloon_dataset.zip

同时也欢迎各位选择更复杂的数据集进行训练，可以选用一下 10 类的饮料数据集。
https://github.com/TommyZihao/Train_Custom_Dataset/tree/main/%E7%9B%AE%E6%A0%87%E6%A3%80%E6%B5%8B/%E7%9B%AE%E6%A0%87%E6%A3%80%E6%B5%8B%E6%95%B0%E6%8D%AE%E9%9B%86

rtmdet_balloon.ipynb为主程序，mmdetection/rtmdet_tiny_1xb12-40e_balloon.py为算法配置文件，测试集评估指标截图在根目录下 rmdet训练的模型在balloon数据集上的测试指标截图.png，网上下载的气球图片预测结果截图在MMDetection_homework\气球检测结果图片目录中。