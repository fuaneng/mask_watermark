import argparse
import os
from PIL import Image
import cv2
import numpy as np
from preprocess_image import preprocess_image
import tensorflow as tf
import neuralgym as ng
from inpaint_model import InpaintCAModel

parser = argparse.ArgumentParser()
parser.add_argument('--input_dir', default='inputdir', type=str,
                    help='The directory of input images.')
parser.add_argument('--output_dir', default='outputdir', type=str,
                    help='The directory to save output images.')
parser.add_argument('--watermark_type', default='mask', type=str,
                    help='The watermark type')
parser.add_argument('--checkpoint_dir', default='model/', type=str,
                    help='The directory of tensorflow checkpoint.')

if __name__ == "__main__":
    FLAGS = ng.Config('inpaint.yml')
    args, unknown = parser.parse_known_args()

    model = InpaintCAModel()

    sess_config = tf.ConfigProto()
    sess_config.gpu_options.allow_growth = True

    # 创建输出目录
    os.makedirs(args.output_dir, exist_ok=True)

    # 处理输入文件夹中的每张图片
    for filename in os.listdir(args.input_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            input_path = os.path.join(args.input_dir, filename)
            output_path = os.path.join(args.output_dir, filename)

            try:
                print(f"Opening image file: {input_path}")
                image = Image.open(input_path)
                print(f"Image size: {image.size}")
            except Exception as e:
                print(f"Error opening image file {input_path}: {e}")
                continue

            input_image = preprocess_image(image, args.watermark_type)

            tf.reset_default_graph()

            if input_image.size != 0:
                with tf.Session(config=sess_config) as sess:
                    input_image = tf.constant(input_image, dtype=tf.float32)
                    output = model.build_server_graph(FLAGS, input_image)
                    output = (output + 1.) * 127.5
                    output = tf.reverse(output, [-1])
                    output = tf.saturate_cast(output, tf.uint8)

                    # 加载预训练模型
                    vars_list = tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES)
                    assign_ops = []
                    for var in vars_list:
                        vname = var.name
                        from_name = vname
                        var_value = tf.contrib.framework.load_variable(
                            args.checkpoint_dir, from_name)
                        assign_ops.append(tf.assign(var, var_value))
                    sess.run(assign_ops)
                    print('Model loaded.')
                    result = sess.run(output)
                    cv2.imwrite(output_path, cv2.cvtColor(
                        result[0][:, :, ::-1], cv2.COLOR_BGR2RGB))
                    print(f"Image saved to {output_path}")
            else:
                print(f"Failed to process image {input_path}.")
