import cv2

class ShirorekhaDetection:

    def regenrating_image(address, filename):
        print("Detecting lines from ")
        destination = "".join([address, filename])

        #Reading the image
        img = cv2.imread(destination)
        print(address)

        # Convert to Gray Scale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #Gaussian GaussianBlur for noise reduction (5,5) 0 => default
        gray = cv2.GaussianBlur(gray, (5, 5), 0) 

        # OTSU threshold seems best threshold for line detection
        th, threshed = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

        # find and draw the upper boundary of each lines
        # UPPER and LOWER BOUNDARY and CROPPING
        hist = cv2.reduce(threshed, 1, cv2.REDUCE_AVG).reshape(-1)  # matrix reduced to single column (avg of every row)
        # print(hist)
        th_H = 100
        th_L = 25
        H, W = img.shape[:2]
        uppers = [y for y in range(H - 1) if hist[y] <= th_H < hist[y + 1]]
        for y in uppers:
            cv2.line(rotated, (0,y), (W, y), (255,0,255), 1)

        # save image with lines
        cv2.imwrite("result.png", rotated)

        for y in uppers:
            crp = threshed[y:y + 25, ]
            cv2.imwrite(address + "result_%d.jpg" % y, crp)


