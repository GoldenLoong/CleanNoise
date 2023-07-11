# CleanNoise

这个代码是基于https://github.com/lllyasviel/AdverseCleaner 而改出来的，作用是对本文件夹内所有Png图片进行降噪。

环境准备

pip install numpy

pip install opencv-contrib-python

运行：
双击“批量降噪-对本文件夹内所有png格式的文件进行降噪 - 副本.bat”


如果你出了什么问题，比如说“ line 4, in <module>
from cv2.ximgproc import guidedFilter”，那么你应该学删了再重装两样东西。
删掉：
pip uninstall opencv-contrib-python opencv-python
再装：
pip install opencv-contrib-python opencv-python 

最后，如果我个人建议全英文路径，不要中文。
