from rembg import remove
from PIL import Image
import torch
import numpy as np


# Tensor to PIL
def tensor2pil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))


# Convert PIL to Tensor
def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)


class ImageResizeCrop:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "target_width": ("INT", {
                    "default": 1920,
                    "max": 4096,
                    "min": 0,
                    "step": 1,
                    "display": "number"
                }),
                "target_height": ("INT", {
                    "default": 1080,
                    "max": 4096,
                    "min": 0,
                    "step": 1,
                    "display": "number"
                }),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "crop_image"
    CATEGORY = "image"

    def crop_image(self, image, target_width, target_height):

        image = tensor2pil(image)
        origin_width = image.width
        origin_height = image.height

        # 先扩大图片到目标尺寸之上
        expand_factor = max(target_width / origin_width, target_height / origin_height)
        resized_image = image.resize((int(image.width * expand_factor),
                                      int(image.height * expand_factor)), Image.LANCZOS)

        resized_width = resized_image.width
        resized_height = resized_image.height

        crop_side_width = (resized_width - target_width) / 2
        crop_side_height = (resized_height - target_height) / 2
        box = (int(crop_side_width), int(crop_side_height),
               int(crop_side_width) + target_width, int(crop_side_height) + target_height)
        crop_image = resized_image.crop(box)

        result_image = pil2tensor(crop_image)

        return (result_image,)


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "ImageResizeCrop": ImageResizeCrop
}
