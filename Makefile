

dl_sdk: 
	./get_sdk

swig-python3: dl_sdk
	mkdir -p leap3_lib
	cp -a SDK/LeapSDK/lib/x64/libLeap.so SDK/LeapSDK/lib/Leap.py SDK/LeapSDK/samples/Sample.py leap3_lib/
	wget http://tinyurl.com/leap-i-patch -O Leap.i.diff
	patch -p0 SDK/LeapSDK/include/Leap.i < Leap.i.diff
	2to3 -nw leap3_lib/Sample.py 
	swig -c++ -python -o /tmp/LeapPython.cpp -interface LeapPython SDK/LeapSDK/include/Leap.i
	g++ -fPIC -I/usr/include/python3.7m -I./SDK/LeapSDK/include /tmp/LeapPython.cpp SDK/LeapSDK/lib/x64/libLeap.so -shared -o leap3_lib/LeapPython.so

all: swig-python3
