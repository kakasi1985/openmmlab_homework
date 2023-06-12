## 此项目为本人openmmlab训练营第7天MMDetection课程课后作业。

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
