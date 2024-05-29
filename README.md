去除固定水印

## 水印去除

![version](https://img.shields.io/badge/version-v1.0.0-green.svg?style=plastic)
![pytorch](https://img.shields.io/badge/tensorflow-v1.15.0-green.svg?style=plastic)
![license](https://img.shields.io/badge/license-CC_BY--NC-green.svg?style=plastic)

该项目是基于深度学习生成式图像修复任务，借鉴于generative_inpainting项目，[link地址为](https://github.com/JiahuiYu/generative_inpainting)

在本项目中我借鉴了他发布深度神经网络预训练模型中有关于门控卷积构建了自由形式的图像修复模块，结合了手动绘制水印蒙版德约束方法进行了对既有水印的图像进行固定水印去除工作。

## 处理效果

<img src="https://img2.imgtp.com/2024/05/29/nCg9zRI2.png" width="45%"/> <img src="https://img2.imgtp.com/2024/05/29/uTbExtzv.png" width="45%"/> 
<img src="https://img2.imgtp.com/2024/05/29/LVRWkwHD.png" width="45%"/> <img src="https://img2.imgtp.com/2024/05/29/YnLpyvbl.png" width="45%"/> 
<img src="https://img2.imgtp.com/2024/05/29/P4HPNlWe.jpg" width="45%" /> <img src="https://img2.imgtp.com/2024/05/29/QRrMfUvq.jpg" width="45%" /> 
<img src="https://img2.imgtp.com/2024/05/29/KB4tfT8p.jpg" width="45%" /> <img src="https://img2.imgtp.com/2024/05/29/JLAoHgGL.jpg" width="45%" /> 

## 运行

- 克隆项目到本地C盘

      git clone https://github.com/fuaneng

- 本项目是基于neuralgym项目而展开的图像深度学习模块，所以不支持 Tensorflow 2x version，基于neuralgym库没有更新的原因所以只能支持Tensorflow 1.15.0 version (`建议使用最新版的anaconda拉取python3.7的虚拟环境之后再进行安装以下库`).

 - 创建python虚拟依赖环境
      conda create -n py311env python=3.7

 - 进入虚拟环境虚拟依赖环境

      conda activate py37env

 - 进入项目路径

      cd watermark-removal

- 拉取 Tensorflow 1x 可以自由选择gpu版本或者cpu版本

      pip install tensorflow==1.15.0

      pip install tensorflow-gpu==1.15.0
      conda install tensorflow-gpu==1.15.0

- 其他依赖项

      pip install -r requirements.txt

- 安装 tensorflow toolkit [neuralgym](https://github.com/JiahuiYu/neuralgym).

      pip install git+https://github.com/JiahuiYu/neuralgym

- 下载预训练模型 [link](https://drive.google.com/drive/folders/1xRV4EdjJuAfsX9pQme6XeoFznKXG0ptJ?usp=sharing) 将其放在 `model/` 文件夹(如果发现模型文件带有txt后缀，请将其删除： `checkpoint.txt` → `checkpoint`)

执行指令

- 一切准备就绪之后你可以执行 `main.py/main_pichul.py` 脚本了

      python main.py --input_dir inputdir --output_dir outputdir --checkpoint_dir model/ --watermark_type mask

      python main_pichul.py --input_dir inputdir --output_dir outputdir --checkpoint_dir model/ --watermark_type mask

