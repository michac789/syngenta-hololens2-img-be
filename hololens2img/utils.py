import base64


def convert_image_to_base64(image_url):
    path = f"C:/My Files/REPOSITORY SEASON2/syngenta-hololens2-img-be{image_url}"
    try:
        with open(path, "rb") as image_file:
            image_data = image_file.read()
            image_base64 = base64.b64encode(image_data).decode('utf-8')
            return image_base64
    except FileNotFoundError:
        return None
