# 本文件为控制文件，命名为：MercuryControl.py
import threading
from pymycobot import Mercury
import time
from exoskeleton_api import Exoskeleton

obj = Exoskeleton(port="/dev/ttyACM2")  #根据实际串口修改
ml = Mercury("/dev/left_arm")
mr = Mercury("/dev/right_arm")

if(ml.is_power_on() != True):
    ml.power_on()
if(mr.is_power_on() != True):
    mr.power_on()
    
# 设置双臂为速度融合模式
ml.set_movement_type(3)
mr.set_movement_type(3)

print(ml.get_movement_type())
print(mr.get_movement_type())

ml.set_vr_mode(1)
mr.set_vr_mode(1)
# 设置夹爪运行模式
ml.set_gripper_mode(0)
mr.set_gripper_mode(0)


# 1 左臂，2 右臂
def control_arm(arm):
    while True:
        if arm == 1:
            arm_data = obj.get_arm_data(1)
            print("l: ", arm_data)
            mc = ml
        elif arm == 2:
            arm_data = obj.get_arm_data(2)
            print("r: ", arm_data)
            mc = mr
        else:
            raise ValueError("error arm")
        # 由于外骨骼各关节转向、零点与部分机械臂构型不同，在此设置映射关系(根据各关节实际控制转向、位置设置)
        mercury_list = [
            arm_data[0], -arm_data[1], arm_data[2], -arm_data[3], arm_data[4],
            135 + arm_data[5], arm_data[6]
        ]
        if arm_data[9] == 0:
            mc.set_gripper_state(1, 100)
        elif arm_data[10] == 0:
            mc.set_gripper_state(0, 100)
        mc.send_angles(mercury_list, 5, _async =True)
        # print(time.time())
        time.sleep(0.01)


# # 左臂
threading.Thread(target=control_arm, args=(1, )).start()
# 右臂
threading.Thread(target=control_arm, args=(2, )).start()