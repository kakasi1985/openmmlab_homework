### 目录MMagic_homework为训练营第11天MMagic代码课程课后作业。
作业：ControlNet 的 N 种玩法
假设你是某装修公司的设计师，客户发了你毛坯房的照片，想让你设计未来装修好的效果图。 先将毛坯房照片，用 OpenCV 转为 Canny 边缘检测图，然后输入 ControlNet，用 Prompt 咒语控制生成效果。 将毛坯房图、Canny 边缘检测图、咒语 Prompt、ControlNet 生成图，做成一页海报，发到群里。

毛胚房装修-ControlNet-Canny.ipynb为主程序，mmagic/configs/controlnet/controlnet-canny.py为ControlNet模型的算法配置文件，咒语prompt为'Room with nordic style.'。
客户毛胚房图片放在mmagic/data/maopei/maopei3.jpg
<img decoding="async" src="mmagic/data/maopei/maopei3.jpg" width="50%">
输出的canny边缘线稿放在mmagic/output/control_0.png
<img decoding="async" src="mmagic//output/control_0.png" width="50%">
输出的装修效果图片放在mmagic/output/sample_0.png
<img decoding="async" src="mmagic/output/sample_0.png" width="50%">
