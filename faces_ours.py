import cv2

image_name = input("Enter name of image file or type exit to end process: ")
# open the image
img = cv2.imread(image_name)

# face cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# face detection function
def detect_face(img):
    
    face_img = img.copy()
    
    face_rects = face_cascade.detectMultiScale(face_img, scaleFactor=1.3, minNeighbors=3)
    
    for (x,y,w,h) in face_rects:
    	cv2.rectangle(face_img, (x,y), (x+w,y+h), (0,0,255), 2)
	
    print(face_rects, len(face_rects))
    amount_of_faces = len(face_rects)
    file = open("output.txt", "w")
    file.write(str(amount_of_faces))
    file.close()
    return face_img

# apply the face detection function
face_img = detect_face(img)


# display the result
cv2.imshow('Original Image', img)
cv2.imshow('Detected Face', face_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


