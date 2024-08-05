基于水印蒙版去除固定水印

## 水印去除

![pytorch](https://img.shields.io/badge/tensorflow-v1.15.0-green.svg?style=plastic)

该项目是基于深度学习生成式图像修复任务，借鉴于generative_inpainting项目，[link地址为](https://github.com/JiahuiYu/generative_inpainting)

在本项目中我借鉴了他发布深度神经网络预训练模型中有关于门控卷积构建了自由形式的图像修复模块，结合了手动绘制水印蒙版德约束方法进行了对既有水印的图像进行固定水印去除工作。

## 处理效果
![7_cr](https://github.com/user-attachments/assets/649b212c-c0b4-476b-8ae1-4b1601a1cf55)
<img s![img](https://github.com/user-attachments/assets/478c58b9-3fb3-4dcf-8cdc-7c012b910211)
rc="https://img2.imgtp.com/2024/05/29/nCg9zRI2.png" width="45%"/> <img src="https://img2.imgtp.com/2024/05/29/uTbExtzv.png" width="45%"/> 
<img src="https://img2.imgtp.com/2024/05/29/LVRWkwHD.png" width="45%"/> <img src="https://img2.imgtp.com/2024/05/29/YnLpyvbl.png" width="45%"/> 
<img src="https://img2.imgtp.com/2024/05/29/P4HPNlWe.jpg" width="45%" /> <img src="https://img2.imgtp.com/2024/05/29/QRrMfUvq.jpg" width="45%" /> 
<img src="https://img2.imgtp.com/2024/05/29/KB4tfT8p.jpg" width="45%" /> <img src="https://img2.imgtp.com/2024/05/29/JLAoHgGL.jpg" width="45%" /> 

## 安装依赖

- 克隆项目到本地C盘

      git clone https://github.com/fuaneng/removal_watermark.git

  本项目是基于neuralgym项目而展开的图像深度学习模块，所以不支持 Tensorflow 2x version，基于neuralgym库没有更新的原因所以只能支持Tensorflow 1.15.0 version (`建议使用最新版的anaconda拉取python3.7的虚拟环境之后再进行安装以下库`).
 
 - 安装 [anaconda](https://www.anaconda.com/download/success) 并运行anaconda prompt

 - 创建python虚拟依赖环境

           conda create -n py37env python=3.7

   如果你拉取虚拟环境遇到困难也可以直接将我打包好的环境放在“C:\Users\你的电脑名字\anaconda3\envs\py37env\”内

      环境包下载请点击☛ [py37env.7z](https://drive.google.com/file/d/1nIxLdnhY6fii0reo7PHYu2rMKX_OrFZ7/view?usp=sharing)

      ！注意！如果你拉取了我的环境包则无需安装其他依赖项了,将下载好的模型放入model\即可直接执行指令

 - 进入虚拟环境虚拟依赖环境

      conda activate py37env

 - 进入项目路径

      #将项目放在桌面的示例指令
   
       cd C:\Users\123\Desktop\removal_watermark

----------------------------------------------------------

- 拉取 Tensorflow 1x 可以自由选择gpu版本或者cpu版本

      pip install tensorflow==1.15.0

      pip install tensorflow-gpu==1.15.0
      conda install tensorflow-gpu==1.15.0

- 其他依赖项

      pip install -r requirements.txt

- 安装 tensorflow toolkit [neuralgym](https://github.com/JiahuiYu/neuralgym).

      pip install git+https://github.com/JiahuiYu/neuralgym
  
----------------------------------------------------------------------

- 下载预训练模型 [请点击这里](https://drive.google.com/drive/folders/1Gt-jJRlqDMTLQCdzIuzlF7n_7QGkCbCd?usp=sharing) 将其放在 `model/` 文件夹

## 执行指令

- 一切准备就绪之后你可以执行 `main.py/main_pichul.py` 脚本了

      # 执行单张图片去水印
      python main.py --input_dir inputdir --output_dir outputdir --checkpoint_dir model/ --watermark_type mask

      # 批量执行
      python main_pichul.py --input_dir inputdir --output_dir outputdir --checkpoint_dir model/ --watermark_type mask

