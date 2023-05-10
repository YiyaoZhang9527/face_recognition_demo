git clone https://github.com/davisking/dlib.git
cd dlib
mkdir build; cd build; cmake ..; cmake --build .
cd ..
python3 setup.py install
cd ..
pip install face_recognition
pip install opencv-python
mkdir images
cd images