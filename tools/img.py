import os
from PIL import Image


def get_all_files(directory):
    all_files = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.abspath(os.path.join(dirpath, filename))
            _, ext = os.path.splitext(file_path)
            all_files.append([file_path, ext.lower() == ".webp"])
    return all_files


def get_webp_output(path, aspect_ratio) -> dict:
    file_name, file_extension = os.path.splitext(path)
    ret = {}

    def update_new_width(new_width):
        ret.update(
            {
                (
                    new_width,
                    int(new_width * aspect_ratio),
                ): f"{file_name}_{new_width}{file_extension}"
            }
        )

    update_new_width(320)
    update_new_width(640)
    update_new_width(1280)
    return ret


def convert_jpg_to_webp(input_path, output_path, quality=60):
    # 打开 JPG 图像
    with Image.open(input_path) as img:
        # 将图像转换为 RGB 模式（确保兼容性）
        img = img.convert("RGB")
        # 保存为 WebP 格式，设置质量
        img.save(output_path, "WEBP", quality=quality)


def resize_webp_output(path, is_webp):
    if not is_webp:
        name, ext = os.path.splitext(path)
        old_path = path
        path = f"{name}.webp"
        convert_jpg_to_webp(old_path, path, 80)
        print(f"Image convert to webp:{old_path}")

    with Image.open(path) as img:
        # 计算新的高度以保持纵横比
        aspect_ratio = img.height / img.width

        path_output_dict = get_webp_output(path, aspect_ratio)

        for new_size, path_output in path_output_dict.items():
            # 调整图像大小
            resized_img = img.resize(new_size, Image.LANCZOS)

            # 保存调整大小后的图像为 WebP 格式
            resized_img.save(path_output, "WEBP", quality=70, lossless=False)

    print(f"Image resized and saved successfully:{path}")


if __name__ == "__main__":
    directory = "assets\images\painting\膠彩\水母漂流記\過程"
    files = get_all_files(directory)
    for path_list in files:
        resize_webp_output(path_list[0], path_list[1])
