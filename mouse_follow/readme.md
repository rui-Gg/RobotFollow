# 鼠标&MercuryA1联动说明

## 控制效果
<img src="../resource\mouse.gif">

## 使用前的准备

#### 更新pymycobot固件(version=b66及之后的版本)

	pip install pynput	#安装鼠标库
	pip install pymycobot==3.5.0b66
	pip show pymycobot


#### 更新Mercury固件(get_modified_version=37及之后的版本)

	Mercury_firmware\MercuryA1_0122_v37.bin

#### 固件烧录方法如下：

<video controls src="../resource/MercuryA1固件烧录方法.mp4" title=""></video>

#### 后续我们会将该固件更新至官网的mystudio中，目前需要手动更新

## 文件说明

	mouse.py 坐标跟随
	mouse_joint.py 角度跟随

**完成使用前准备后，直接运行mouse.py脚本即可**

## mouse.py脚本说明

**首先需要修改为Mercury对应串口，一般为/dev/ttyAMA1**

	m = Mercury("/dev/ttyAMA1") #根据串口号修改

切换为速度融合模式

	ml.set_movement_type(3)
	mr.set_movement_type(3)

	print(ml.get_movement_type())
	print(mr.get_movement_type())

#### 注意！如果此处显示出错，或未成功切换至mode=3，需要确认 *使用前准备* 是否正常完成！

设置VR模式

	ml.set_vr_mode(1)
	mr.set_vr_mode(1)

循环将采样点发送给Mercury

	while 1:
		mc.send_angles(mercury_list, TI, _async=True)
		time.sleep(0.01)

## 参数说明：	

**m.send_angles(mercury_list, TI, _async=True)**
	
	mercury_list：目标位置（1*7关节角度）

	TI：速度等级，TI越小速度越快，建议>=3

	_async=True：开环接口，指令不等待
	
	time.sleep(0.01)：发送频率不要超过100hz（10ms）


**m.send_coords(mercury_list, TI, _async=True)**
	
	mercury_list：目标位置（1*6坐标）

	TI：速度等级，TI越小速度越快，建议>=3

	_async=True：开环接口，指令不等待
	
	time.sleep(0.01)：发送频率不要超过100hz（10ms）