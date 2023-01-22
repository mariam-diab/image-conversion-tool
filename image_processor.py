from PIL import Image
import imghdr

class image_processor:
    def __init__(self):
        self._image = None
        self._file_format = None

    def open_image(self, file_path):
        file_format = imghdr.what(file_path)
        if file_format not in image_adapter._adapters.keys():
            raise ValueError("Invalid file format")
        adapter = image_adapter.get_adapter(file_format)
        self._image = adapter.open_image(file_path)
        self._file_format = file_format

    def save_image(self, file_path, width, height):
        if self._image is None:
            raise ValueError("No selected image")
        width = int(width)
        height = int(height)
        if self._file_format in image_adapter._adapters.keys():
            self._image = self._image.resize((width, height))
            adapter = image_adapter.get_adapter(self._file_format)
            adapter.save_image(self._image, file_path)


class image_adapter:
    _adapters = {}
    @classmethod
    def register_adapter(cls, file_format, adapter):
        cls._adapters[file_format] = adapter
    @classmethod
    def get_adapter(cls, file_format):
        return cls._adapters[file_format]

class jpeg_adapter(image_adapter):
    def open_image(self, file_path):
        image = Image.open(file_path)
        return image
    def save_image(self, image, file_path):
        image = image.convert("RGB")
        image.save(file_path, format='JPEG')
image_adapter.register_adapter("jpeg", jpeg_adapter())


class png_adapter(image_adapter):
    def open_image(self, file_path):
        image = Image.open(file_path)
        return image
    def save_image(self, image, file_path):
        image.save(file_path, format='PNG')
image_adapter.register_adapter("png", png_adapter())


class bitmap_adapter(image_adapter):
    def open_image(self, file_path):
        image = Image.open(file_path)
        return image
    def save_image(self, image, file_path):
        image.save(file_path, format='BMP')
image_adapter.register_adapter("bmp", bitmap_adapter())


class gif_adapter(image_adapter):
    def open_image(self, file_path):
        image = Image.open(file_path)
        return image
    def save_image(self, image, file_path):
        image.save(file_path, format='GIF')
image_adapter.register_adapter("gif", gif_adapter())


class eps_adapter(image_adapter):
    def open_image(self, file_path):
        image = Image.open(file_path)
        return image
    def save_image(self, image, file_path):
        image.save(file_path, format='EPS')
image_adapter.register_adapter("eps", eps_adapter())


class raw_adapter(image_adapter):
    def open_image(self, file_path):
        image = Image.open(file_path)
        return image
    def save_image(self, image, file_path):
        image.save(file_path, format='RAW')
image_adapter.register_adapter("raw", raw_adapter())


class tiff_adapter(image_adapter):
    def open_image(self, file_path):
        image = Image.open(file_path)
        return image
    def save_image(self, image, file_path):
        image.save(file_path, format='TIFF')
image_adapter.register_adapter("tiff", tiff_adapter())




