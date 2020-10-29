import pandas
import matplotlib.pyplot as plt
import numpy as np
import os

from time import time, ctime, localtime
from datetime import datetime


# kalibr_bagextractor --bag ./zeiss_data.bag --image-topics /mynteye/left/image_raw --imu-topics /mynteye/imu/data_raw --output-folder ./test_output_zeiss/

data_imu = pandas.read_csv("./test_output_zeiss/imu0.csv")
timestamps_imu = data_imu["timestamp"].tolist()
timestamps_imu_format = []
for tps in timestamps_imu:
    temp = str(tps)[:10]
    temp2 = str(tps)[10:]
    timestamps_imu_format.append(np.double(temp+"."+temp2))
timestamps_imu_format.sort()

list_img = os.listdir("./test_output_zeiss/cam0/")
timestamps_img_format = []
for name in list_img:
    name_time = name.split(".")[0]
    temp = name_time[:10]
    temp2 = name_time[10:]
    timestamps_img_format.append(np.double(temp+"."+temp2))
timestamps_img_format.sort()


# imu time diff
imu_time_diff = [0]
for i in range(len(timestamps_imu_format)-1):
    time_left = timestamps_imu_format[i]
    time_right = timestamps_imu_format[i+1]
    time_diff = (time_right-time_left)*1000
    imu_time_diff.append(time_diff)

# image time diff
img_time_diff = [0]
for i in range(len(timestamps_img_format)-1):
    time_left = timestamps_img_format[i]
    time_right = timestamps_img_format[i+1]
    time_diff = (time_right-time_left)*1000
    img_time_diff.append(time_diff)

print(len(imu_time_diff))
print(len(img_time_diff))

num = 400
plt.subplot(211)
plt.plot(timestamps_img_format[1:num],
         img_time_diff[1:num])
plt.title("Image data captured by MYNTEYE (30Hz)")
plt.xlabel("Image timestamps (unix time)")
plt.ylabel("time diff (ms)")

plt.subplot(212)
plt.plot(timestamps_imu_format[1:num],
         imu_time_diff[1:num])
plt.title("IMU data captured by MYNTEYE (200Hz)")
plt.xlabel("IMU timestamps (unix time)")
plt.ylabel("time diff (ms)")
# plt.show()

plt.show()

