from __future__ import print_function

import grpc
import cv2
import imageTest_pb2
import imageTest_pb2_grpc
import skvideo.io

URL = "/home/nirvan/Desktop/projName/db/DVR_ch7_main_20171015180000_20171015190000.mp4"

def run():
  channel = grpc.insecure_channel('192.168.1.195:50051')
  stub = imageTest_pb2_grpc.ImageTestStub(channel)
  #temp = cv2.imread('/home/nirvan/img_one.png')
  for response in stub.Analyse( generateRequests() ):
      print(str(response.reply))


def generateRequests():
    videogen = skvideo.io.vreader(URL)
    i=0
    cnt = 1
    for frame in videogen:
        
        if(cnt == 5):
            cnt = 1
        else:
            cnt+=1
            continue
        
        frame = cv2.cvtColor( frame, cv2.COLOR_RGB2GRAY )
        frame = bytes(frame)
        yield imageTest_pb2.MsgRequest(img= frame)
    

if __name__ == '__main__':
  run()
