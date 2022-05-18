import face_recognition
import cv2
import datetime
import numpy as np
from conexao import mydb, mycursor


# pegar a data e hora atual
currentDateTime = datetime.datetime.now()

# captura de video
video_capture = cv2.VideoCapture(0)
 
# carrega a imagem para reconhecimento
michael_image = face_recognition.load_image_file("img/michael.png")
michael_face_encoding = face_recognition.face_encodings(michael_image)[0]

obama_image = face_recognition.load_image_file("img/obama.png")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

mandela_image = face_recognition.load_image_file("img/mandela.png")
mandela_face_encoding = face_recognition.face_encodings(mandela_image)[0]

# identifica o nome da pessoa que foi reconhecida
known_face_encodings = [
    michael_face_encoding,
    obama_face_encoding,
    mandela_face_encoding
]
known_face_names = [
    "Michael Sants",
    "Barack Obama",
    "Nelson Mandela"
]


face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:

            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Desconhecido"
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                 # CONTADOR DE LINHAS 
                contador = "SELECT COUNT(*) from entradas where nome LIKE '"+name+"' "
                mycursor.execute(contador)
                result=mycursor.fetchone()
                number_of_rows=result[0]
                if(number_of_rows < 1):
                    sql = "INSERT INTO entradas (id, nome, entrada) VALUES (%s, %s, %s)"
                    val = ("",name, currentDateTime)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    
    process_this_frame = not process_this_frame
    face_names.append(name)


    for (top, right, bottom, left), name in zip(face_locations, face_names):

        top *= 4
        right *= 4
        bottom *= 4
        left *= 4


        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)


        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)


    cv2.imshow('Video', frame)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cv2.destroyAllWindows()
