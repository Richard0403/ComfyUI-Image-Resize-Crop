# ImageCrop 裁剪图片到目标尺寸， 可放大可缩小

**使用背景**

很多模型只能生成1024x1024、1360x768这种固定尺寸，喂入想要的尺寸，生成的图不尽人意， 
使用其他扩图方式，比较繁琐，性能较差，所以自己开发了该节点，用于图片尺寸转换。

功能： 放大、缩小、裁剪（自动选择中间位置裁切）


1. 在ComfyUI的 `custom_nodes` 文件夹中clone代码:

```
git clone https://github.com/Richard0403/ComfyUI-Image-Resize-Crop.git
```

2. 在ComfyUi中，双击搜索“ImageResizeCrop”