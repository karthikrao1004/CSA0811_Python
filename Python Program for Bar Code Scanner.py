import cv2
from pyzbar.pyzbar import decode

def read_barcodes(frame):
    barcodes = decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 400, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 1.0, (255, 255, 255), 1)
        print(f"Bar/QR code data: {barcode_info}")

    return frame

def main():
    # Use camera to capture video
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        frame = read_barcodes(frame)
        cv2.imshow('Barcode/QR Code Reader', frame)

        if cv2.waitKey(1) & 0xFF == 27:  # Press Esc to exit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
