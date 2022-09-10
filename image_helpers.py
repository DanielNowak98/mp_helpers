import cv2

'''
image_helpers

author @DanielNowak98
'''

class Image:

    def __init__(self):
        pass
    
    def convert_image_bgr_to_rgb(self, image):
        """
        Converts the image from BGR to RGB.
        """
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    def convert_image_rgb_to_bgr(self, image):
        """
        Converts the image from RGB to BGR.
        """
        return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)


    def flip_image(self, image):
        """
        Flips the image.
        """
        return cv2.flip(image, 1)
    
    def get_image_size(self, image):
        """
        Returns the size of the image.
        """
        return image.shape
    
    def get_image_width(self, image):
        """
        Returns the width of the image.
        """
        return image.shape[1]
    
    def get_image_height(self, image):
        """
        Returns the height of the image.
        """
        return image.shape[0]
    
    def get_image_channels(self, image):
        """
        Returns the number of channels in the image.
        """
        return image.shape[2]
    
    def get_image_data(self, image):
        """
        Returns the image data.
        """
        return image.data
    