import numpy as np
from PIL import Image
import cv2


def preprocess_image(image, watermark_type):
    image_type: str = ''
    preprocessed_mask_image = np.array([])
    
    # Convert image to RGB if necessary and convert to numpy array
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = np.array(image)
    image_h = image.shape[0]
    image_w = image.shape[1]
    aspectRatioImage = image_w / image_h
    print("image size: {}".format(image.shape))

    # Determine image type based on aspect ratio
    if image_w >= image_h:
        image_type = "landscape"
    else:
        image_type = "potrait"

    # Load and process mask image
    mask_image = Image.open(
        "mask/mask.png".format(watermark_type, image_type))
    if mask_image.mode != "RGB":
        mask_image = mask_image.convert("RGB")
    mask_image = np.array(mask_image)
    print("mask image size: {}".format(mask_image.shape))

    aspectRatioMaskImage = mask_image.shape[1] / mask_image.shape[0]
    upperBoundAspectRatio = 1.05 * aspectRatioMaskImage
    lowerBoundAspectRatio = 0.95 * aspectRatioMaskImage

    # Resize mask image to match input image size if aspect ratio is compatible
    if lowerBoundAspectRatio <= aspectRatioImage <= upperBoundAspectRatio:
        preprocessed_mask_image = cv2.resize(mask_image, (image_w, image_h))
        print(preprocessed_mask_image.shape)
    else:
        print("Image size not supported!!!")

    # Check if preprocessed_mask_image is not empty
    if preprocessed_mask_image.size != 0:
        # Ensure that both images have the same shape
        assert image.shape == preprocessed_mask_image.shape, \
            f"Shape mismatch: image shape {image.shape}, preprocessed mask shape {preprocessed_mask_image.shape}"
        
        grid = 8
        image = image[:image_h//grid*grid, :image_w//grid*grid, :]
        preprocessed_mask_image = preprocessed_mask_image[:image_h //
                                                          grid*grid, :image_w//grid*grid, :]
        image = np.expand_dims(image, 0)
        preprocessed_mask_image = np.expand_dims(preprocessed_mask_image, 0)
        input_image = np.concatenate([image, preprocessed_mask_image], axis=2)
        return input_image

    else:
        return preprocessed_mask_image
