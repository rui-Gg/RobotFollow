import threading
import time
from pynput.mouse import Controller
from pymycobot import *
m = Mercury("/dev/ttyAMA1") #根据串口号修改
if(m.is_power_on() != True):
    m.power_on()

m.set_movement_type(0)  #使用ptp模式运动到初始姿态
angles = [0,0,0,-90,0,90,0]
m.send_angles(angles,10)
coord = m.get_coords()
target = coord.copy();
m.set_movement_type(3)  #切换为速度环融合规划
m.set_vr_mode(1)    #将机械臂内部点位缓存窗口修改为2
# 创建一个鼠标控制器实例
mouse = Controller()

# 记录初始位置
initial_position = None

def capture_mouse_position():
    global initial_position
    st = time.time()
    while True:
        # 获取鼠标的当前坐标
        current_position = mouse.position
        
        # 如果是第一次采样，记录初始位置
        if initial_position is None:
            initial_position = current_position

        # 计算相对于初始位置的偏移量
        offset_position = (current_position[0] - initial_position[0], current_position[1] - initial_position[1])
        target[0] = coord[0] - offset_position[1] * 0.15
        target[1] = coord[1] - offset_position[0] * 0.15
        print(1000*(time.time()-st))
        st = time.time()
        m.send_coords(target, 10, _async=True)  #安全起见初始速度较慢，最快不要小于3
        # 等待10毫秒
        time.sleep(0.01)
        # 参数说明：
        # 	target：目标位置（1*6坐标）
        # 	TI：速度等级，TI越小速度越快，建议>=3
        # 	_async=True：开环接口，指令不等待
        # 	time.sleep(0.01)：发送频率不要超过100hz（10ms）
        print(f'Relative mouse position: {offset_position}')
        

# 创建一个线程以10ms的周期捕捉鼠标坐标
thread = threading.Thread(target=capture_mouse_position)
thread.daemon = True  # 设置为守护线程，以便程序退出时线程自动结束
thread.start()

# 主线程继续运行
try:
    while True:
        time.sleep(1)  # 主线程保持活动状态
except KeyboardInterrupt:
    print("捕捉停止")
