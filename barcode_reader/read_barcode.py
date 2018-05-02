import cv2
import numpy as np
from pyzbar.pyzbar import decode


def read_barcode():
    """
    A function that turns on webcam, trys to detect barcode appearing in the
    view of the webcam and returns the detected barcode.

    Returns:
        (barcode_data, barcode_type): bardcode_data is a Python Bytes object
    """
    cap = cv2.VideoCapture(0)
    
    detected_barcodes = set()
    while(True):
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        res = decode(np.array(gray))
        if not res or len(res) >= 2:
            continue
        temp_barcode = (res[0].data, res[0].type)
        if temp_barcode in detected_barcodes:
            barcode = temp_barcode
            break
        detected_barcodes.add(temp_barcode)
        
    cap.release()
    cv2.destroyAllWindows()
    return temp_barcode
