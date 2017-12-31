Author: Nirvan Anjirbag

#Functionalities:
Uses GRPC (Google remote procedural calls) for sending video over the internet. The video is sent from the client to the server. The server processes the received video, generates some results and passes these results back to the client. This code uses bi-directinal streaming. Video is streamed from client to server. Results are streamed from server to client.


#Futurescope:
This can be used to stream live footage from cctv cameras. This video can be processed at some far-away facility and the results can be transferred back. This way a cctv camera feed can be sent to a remote facility. At the facility we can use some heavy computational procedure on it like deep learning and transfer the results back to the place at which the camera is located.

#----------------------------------------------

#Main requirements:

Grpc
openCV
skvideo.io

Grpc:
https://grpc.io/docs/quickstart/python.html

Install Grpc: 
python -m pip install grpcio

Install Grpc tools:
$ python -m pip install grpcio-tools


openCV;
sudo apt-get install libopencv-dev python-opencv


skvideo: 
sudo pip install scikit-video

#--------------------------------------------------------
 
#Video transfer using grpc
We transfer a video from client to server over the internet and send the results back after processing, from server to client.

#usage

First we make the .proto file and place it in the grpcTest/protos folder. We execute the following command from the folder grpcTest.

  python -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/imageTest.proto
  
  This creates the files `imageTest_pb2_grpc.py` and `imageTest_pb2.py` in the folder grpcTest.
  
  We then write the files `imageTest_server.py` and `imageTest_client.py` which use the above 2 generated files.
  
  The client sends the video file via a stream of frames. The server receives these frames and continuously processes each frame and counts the number of people entering the mall. This count is sent back to the client using streaming. 
  
Note: Use internet through LAN for fastest transfer.

To start server, 

   python imageTest_server.py
   
To start client, 

   python imageTest_client.py

#Links for reference

https://grpc.io/docs/tutorials/basic/python.html
https://grpc.io/docs/quickstart/python.html
https://grpc.io/docs/guides/concepts.html
https://grpc.io/docs/guides/concepts.html#bidirectional-streaming-rpc
https://stackoverflow.com/questions/47867440/cv2-imshow-giving-black-screen/47867865#47867865
https://stackoverflow.com/questions/47883841/grpc-not-working-when-i-use-2-computers-instead-of-1/47887825#47887825
