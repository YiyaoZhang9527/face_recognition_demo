import face_recognition
import cv2
import os
import numpy as np

def norm_l2(x):
    return np.sqrt(sum(x**2))

def face(path):
    #存储知道人名列表
    known_names=[] 
    #存储知道的特征值
    known_encodings=[]
    for image_name in os.listdir(path):
        load_image = face_recognition.load_image_file(path+image_name) #加载图片
        BGR_image = cv2.cvtColor(load_image,cv2.COLOR_RGB2BGR)
        image_face_encoding = face_recognition.face_encodings(BGR_image)[0] #获得128维特征值
        known_names.append(image_name.split(".")[0])
        known_encodings.append(image_face_encoding)
    # print(known_encodings)
    
    #打开摄像头，0表示内置摄像头
    video_capture = cv2.VideoCapture(0) 
    process_this_frame = True
    while True:
        ret, frame = video_capture.read()
        # frame = cv2.cvtColor(BGRframe, cv2.COLOR_BGR2RGB)
        # opencv的图像是BGR格式的，而我们需要是的RGB格式的，因此需要进行一个转换。
        rgb_frame = frame
        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_frame)#获得所有人脸位置
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations) #获得人脸特征值
            face_names = [] #存储出现在画面中人脸的名字
            for face_encoding in face_encodings:         
                #matches = face_recognition.compare_faces(known_encodings, face_encoding,tolerance=0.5)
                
                # l2 范数表示特征距离
                tolerance=0.4
                matches = [norm_l2(known_encoding-face_encoding) <= tolerance for known_encoding in  known_encodings]
                # 余弦相似度测试效果
                #matches = [np.cos(known_encoding,face_encoding) <= tolerance for known_encoding in  known_encodings]
                
                if True in matches:
                    print(matches)
                    print(f"known_names: {known_names}")
                    first_match_index = matches.index(True)
                    print('first_match_index:',first_match_index)
                    name = known_names[first_match_index]
                else:
                    name="unknown"
                face_names.append(name)

        process_this_frame = not process_this_frame

        # 将捕捉到的人脸显示出来
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2) # 画人脸矩形框
            # 加上人名标签
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX 
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        
        # cv2.imshow('frame', cv2.cvtColor(frame,cv2.COLOR_RGB2BGR))
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    face("./images/") #存放已知图像路径