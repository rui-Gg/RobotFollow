# MercuryB1\X1 有严格的上下电顺序，必须遵循 右臂下电→左臂下电→左臂上电→右臂上电 才可以正常使用
# 此脚本帮助用户快速控制机械臂使能
from pymycobot import Mercury

ml = Mercury("/dev/left_arm")
mr = Mercury("/dev/right_arm")

mr.power_off()
ml.power_off()
ml.power_on()
mr.power_on()
    