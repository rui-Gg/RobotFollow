# 鼠标&MercuryX1联动说明

## 控制效果

**位置环**

<img src="../../resource\X1.gif">

**速度环**

<img src="../../resource\Basespeed.gif">

## 使用前的准备

#### 更新pymycobot固件

	pip install pynput	#安装鼠标库

	cd mouse_follow\X1
	pip install pymycobot-3.8.1b1-py3-none-any.whl


#### 更新MercuryX1固件

	Mercury_firmware\MercuryX1_left_v1.1.0_20250224.bin
	Mercury_firmware\MercuryX1_right_v1.1.0_20250224.bin

#### 固件烧录方法如下：

<video controls src="../../resource/MercuryX1固件烧录方法.mp4" title=""></video>

#### 后续我们会将该固件更新至官网的mystudio中，目前需要手动更新

	mouse.py 位置环控制

	speed.py 速度环控制

## mouse.py脚本说明

	ml = Mercury("/dev/left_arm") #left arm
	mr = Mercury("/dev/right_arm") #right arm

切换为FUSION模式

	ml.set_movement_type(2)
	mr.set_movement_type(2)

	print(ml.get_movement_type())
	print(mr.get_movement_type())

#### 注意！如果此处显示出错，或未成功切换至mode=2，需要确认 *使用前准备* 是否正常完成！

设置VR模式

	ml.set_vr_mode(1)
	mr.set_vr_mode(1)

循环将采样点发送给Mercury

	while 1:
		TI = 5
        ml.send_base_coords(target, TI, _async=True)
		time.sleep(0.01)

## 参数说明：	
**m.send_base_coords(mercury_list, TI, _async=True)**
	
	mercury_list：目标位置（1*6坐标）

	TI：速度等级，TI越小速度越快，建议>=3

	_async=True：开环接口，指令不等待
	
	time.sleep(0.01)：发送频率不要超过100hz（10ms）