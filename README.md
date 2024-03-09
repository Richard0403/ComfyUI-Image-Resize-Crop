# ImageCrop 裁剪图片到目标尺寸， 可放大可缩小

**使用背景**

很多模型只能生成1024x1024、1360x768这种固定尺寸，喂入想要的尺寸，生成的图不尽人意， 
使用其他扩图方式，比较繁琐，性能较差，所以自己开发了该节点，用于图片尺寸转换。

**功能**： 

放大、缩小、裁剪（自动选择中间位置裁切）

**使用方式**

1. 在ComfyUI的 `custom_nodes` 文件夹中clone代码:

```
git clone https://github.com/Richard0403/ComfyUI-Image-Resize-Crop.git
```
 
2. 在ComfyUi中，双击搜索“ImageResizeCrop”

**原理**

1. 主要使用PIL的Image功能，根据目标尺寸的设置，对图片进行缩小放大。
2. 若目标尺寸和输入尺寸不一致，会把图片缩放到和目标尺寸相近大小后， 在图片中心进行裁剪。

**效果图**

![image](https://github.com/Richard0403/ComfyUI-Image-Resize-Crop/assets/14147304/128d4c48-a5dd-4aeb-b867-90bf991de041)
