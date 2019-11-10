

all:
	g++ Principal.cpp HuMomentsExtractor.cpp -L/home/vlarobbyk/aplicaciones/Librerias/opencv-4.0.0/opencv4-installation/lib/ -I/home/vlarobbyk/aplicaciones/Librerias/opencv-4.0.0/opencv4-installation/include/opencv4/ -lopencv_core -lopencv_highgui -lopencv_imgproc -lopencv_imgcodecs -o huM.bin
	
run:
	./huM.bin
