## Introduction
Using gRPC (Google remote procedural calls) for transferring video over the internet and receiving the results back. The video is sent from the server to the client. The client processes the received video, generates some results and passes these results back to the client. This code uses bi-directinal streaming. Video is streamed from server to client. Results are streamed back from client to server.


## Use
This is used to stream live footage from cctv cameras. Video from a CCTV camera is transferred in real-time to a distant proccessing facility. This is because computationally intensive hardware is not located near the camera. At the facility we can use some heavy computational procedure on it like deep learning and transfer the results back to the place at which the camera is located. 

In this code, I've performed 'people counting' on the video. The video from the camera is transferred via gRPC. The client, running on another machine, receives this video via the internet. The client performs people counting on the video is real-time and continously transfers the results back i.e the number of people counted till now. 


## Main requirements:

Grpc
openCV
skvideo.io

Grpc: https://grpc.io/docs/quickstart/python.html

Install Grpc: 
```python -m pip install grpcio```

Install Grpc tools:
```$ python -m pip install grpcio-tools```

Install openCV:
```sudo apt-get install libopencv-dev python-opencv```

Install skvideo: 
```sudo pip install scikit-video```


## usage

First we make the .proto file and place it in the ```grpcTest/protos folder```. We execute the following command from the folder grpcTest.

  ```python -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/imageTest.proto```
  
  This creates the files ```imageTest_pb2_grpc.py``` and ```imageTest_pb2.py``` in the folder grpcTest.
  
  We then write the files ```imageTest_server.py``` and ```imageTest_client.py``` which use the above 2 generated files.
  
The client sends the video file via a stream of frames. The server receives these frames and continuously processes each frame and counts the number of people entering the mall. This count is sent back to the client using streaming. 
  
Note: Use internet through LAN for fastest transfer.

To start server, 

  ```python imageTest_server.py```
   
To start client, 

   ```python imageTest_client.py```

## Links for reference

https://grpc.io/docs/tutorials/basic/python.html
https://grpc.io/docs/quickstart/python.html
https://grpc.io/docs/guides/concepts.html
https://grpc.io/docs/guides/concepts.html#bidirectional-streaming-rpc
https://stackoverflow.com/questions/47867440/cv2-imshow-giving-black-screen/47867865#47867865
https://stackoverflow.com/questions/47883841/grpc-not-working-when-i-use-2-computers-instead-of-1/47887825#47887825
