from Young.Young_finger import Young_Finger
from nakano.image_processing import load_image_grayscale


YF = Young_Finger(3, 6, 15, -5)
img = load_image_grayscale("../features_detection/fingerprint.png")
YF.load_ndarray(img)
YF.far_generation(1)
YF.show()
# YF.show_cv2()
YF.far_generation(3)
YF.show()


