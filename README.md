The module renders an image reducing noise and cropping out lines from an image of sanskrit or any ancient Indian language.

input : image path and filename.
output: An image with recognised lines and cropped image of every line.

Input image is assumed to be non-skew for skewed or rotated images apply rotation before passing the image.

Thresholding value for upper and lower line is used 100 and 25 after certain experiments on test cases. These values can be changed to improve efficiency for a particular dataset.
