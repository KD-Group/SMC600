# SMC600

[![Build status](https://ci.appveyor.com/api/projects/status/iyix3p3fnhmfkmy3?svg=true)](https://ci.appveyor.com/project/Wingsgo/smc600)

## 安装方式
```
pip install SMC600
```

## 雷塞SMC600系列运动控制程序说明

1. X/Y轴: 10000个脉冲走4mm(默认值)
2. Z轴: 10000个脉冲走1mm(默认值)
3. 返回位置: 返回位置有两个类型，一个是脉冲值，一个是编码器，对于脉冲值，发送10000个脉冲，返回10000个脉冲，对于编码器
，通过set_counter_inmode，默认位0,10000个脉冲返回2500个脉冲，如果设置为3，则乘以4倍，返回10000个脉冲

## 示例
```
from SMC600 import smc600


# 1. 连接设备（网卡连接）
smc600.board_init_e(0, 0, 2, '192.168.0.1', 0)
# 2. 设置x轴当量脉冲为1
smc600.set_equiv_e(0, 0, 1)
# 3. 设置x轴编码器计数方式为3，即发送10000个脉冲，编码器也返回10000个脉冲
smc600.set_counter_inmode_e(0, 0, 3)
# 4. 设置x轴alm信号
smc600.set_alm_mode_e(0, 0, 0, 0, 0)
# 5. 设置x轴的伺服使能端口输出
smc600.write_sevon_pin_e(0, 0, 0)
# 6. x轴按照15000的速度移动10000个脉冲(绝对坐标模式)
speed = 15000
position = 10000
smc600.set_pulse_outmode_e(0, 0, 0)
smc600.set_profile_e(0, 0, 500.0, speed, 0.1, 0.1, 500)
smc600.set_s_profile_e(0, 0, 0, 0.0)
smc600.pmove_e(0, 0, position, 1)
# 7. 检查x轴是否在移动
is_movting = (smc600.check_done(0, 0) == 0) # 0代表运动中，1代表停止
# 8. x轴回原点(正向)
smc600.set_pulse_outmode_e(0, 0, 0)
smc600.set_home_profile_e(0, 0, 500.0, speed, 0.1, 0.1)
smc600.set_homemode_e(0, 0, 1, 1, 2, 1)
smc600.home_move_e(0, 0)
# 9. x轴急停
smc600.stop_e(0, 0, 1)
# 10. 获取x轴脉冲位置
pos = smc600.new_doublep()
ret = smc600.get_position(0, 0, pos)
res = smc600.doublep_value(pos) if ret == 0 else 0
smc600.delete_doublep(pos)
# 11. 获取x轴编码器位置
pos = smc600.new_doublep()
ret = smc600.get_encoder_unit(0, 0, pos)
res = smc600.doublep_value(pos) if ret == 0 else 0
smc600.delete_doublep(pos)
```

## 函数说明
### 函数名: smc_board_init

**功能：控制器链接初始化函数，分配系统资源**
**参数**：

- ConnectNo 指定链接号（0-7），默认值 0
- Type 链接类型：1-串口，2-网口
- Pconnectstring 链接字符串，对应与控制器的 IP 地址或相应的 COM 口
- Baud 波特率，默认值 115200
- 返回值：0： 链接成功，非 0： 链接失败错误码

### 函数名: set_alm_mode_e

**功能：设置指定轴的 ALM 信号**

**参数**：

- ConnectNo 指定链接号：0-7,默认值 0
- axis 指定轴号，取值范围：0-控制器最大轴数-1
- enableALM 信号使能，0：禁止，1：允许
- alm_logicALM 信号的有效电平，0：低有效，1：高有效
- alm_actionALM 信号的制动方式，0：立即停止（只支持该方式）

### 函数名: write_sevon_pin_e

**功能：控制指定轴的伺服使能端口的输出**

**参数**：

- ConnectNo 指定链接号：0-7,默认值 0
- axis 指定轴号，取值范围：0-控制器最大轴数-1
- on_off 设置伺服使能端口电平，0：低电平，1：高电平
- 返回值：错误代码

### 函数名: set_equiv_e

**功能：设置脉冲当量值**

**参数**

- ConnectNo 指定链接号：0-7,默认值 0
- axis 指定轴号，取值范围：0-控制器最大轴数-1
- equiv 脉冲当量，单位：pulse/unit
- 返回值：错误代码

### 函数名: get_equiv_e

**功能：返回脉冲当量值设置**

**参数**

- ConnectNo 指定链接号：0-7,默认值 0
- axis 指定轴号，取值范围：0-控制器最大轴数-1
- equiv 返回脉冲当量设置值
- 返回值：错误代码

### 函数名: set_backlash_unit_e

**功能：设置反向间隙值**
**参数**

- ConnectNo 指定链接号：0-7,默认值 0
- axis 指定轴号，取值范围：0-控制器最大轴数-1
- backlash 反向间隙值，单位：unit
- 返回值：错误代码

### 函数名: get_backlash_unit_e

**功能：读取反向间隙值设置**
**参数**

- ConnectNo 指定链接号：0-7,默认值 0
- axis 指定轴号，取值范围：0-控制器最大轴数-1
- backlash 返回反向间隙设置值
- 返回值：错误代码

### 函数名: set_pulse_outmode_e

**功能: 设置指定轴的脉冲输出模式**

**参数**：

- ConnectNo 指定链接号：0-7,默认值 0
- axis 指定轴号，取值范围：0-控制器最大轴数-1
- out_mode 脉冲输出方式选择

### 函数名: set_homemode_e

**功能：设置回原点模式**
**参数**

- ConnectNo 指定链接号：0-7,默认值 0
- axis 指定轴号，取值范围：0-控制器最大轴数-1
- home_dir 回原点方向，0：负向，1：正向 (均使用正向)
- vel_mode 回原点速度模式，默认值：1
- Mode 回原点模式：2 (二次回零)
- Source 回零计数源，0：指令位置计数器，1：编码器计数器 (使用1)

### 函数名: home_move_e

**功能：回原点运动**
**参数**

- ConnectNo 指定链接号：0-7,默认值 0
- axis 指定轴号，取值范围：0-控制器最大轴数-1
- 返回值：错误代码

### 函数名: set_home_profile_e

**功能：设置回原点速度参数**
**参数**

- ConnectNo 指定链接号：0-7,默认值 0
- axis 指定轴号，取值范围：0-控制器最大轴数-1
- Low_Vel 设置回原点起始速度
- High_Vel 设置回原点运行速度
- Tacc 设置回原点加速、减速时间，单位：s
- Tdec 保留值 0
- 返回值：错误代码

### 函数名: check_done

**功能：检测连续插补运行状态**
**参数**

- ConnectNo 指定链接号：0-7,默认值 0
- Crd 坐标系号，取值范围：0~1
- 返回值：运动状态，0：运行中，1：停止

### 函数名: set_profile_e

**功能：设置单轴运动速度曲线（时间模式）**

**参数**：

- ConnectNo 指定链接号：0-7,默认值 0
- axis 指定轴号，取值范围：0-控制器最大轴数-1
- Min_Vel 起始速度，单位：unit/s
- Max_Vel 最大速度，单位：unit/s
- Tacc 加速时间，单位：s
- Tdec 减速时间，单位：s
- Stop_Vel 停止速度，单位：unit/s

### 函数名: set_s_profile_e

**功能：设置单轴速度曲线 S 段参数值**

**参数**

- ConnectNo 指定链接号：0-7,默认值 0
- axis 指定轴号，取值范围：0-控制器最大轴数-1
- s_mode 保留参数，固定值为 0
- s_para S 段时间，单位：s；范围：0~1 s

### 函数名: pmove_e

**功能：定长运动**

**参数**

- ConnectNo 指定链接号：0 - 7, 默认值 0
- axis 指定轴号，取值范围：0 - 控制器最大轴数 - 1
- Dist 目标位置，单位：unit +向上 -向下
- posi_mode 运动模式，0：相对坐标模式，1：绝对坐标模式

### 函数名: set_position_e

**功能：设置当前指令位置计数器值**
**参数**

- ConnectNo 指定链接号：0-7,默认值 0
- axis 指定轴号，取值范围：0-控制器最大轴数-1
- Pos 位置值，单位：unit

### 函数名: get_position

**功能：读取当前指令位置计数器值**

**参数**

- ConnectNo 指定链接号：0-7,默认值 0
- axis 指定轴号，取值范围：0-控制器最大轴数-1
- pos 返回当前位置值，单位：unit

### 函数名: set_encoder_unit_e

**功能：设置指定轴编码器脉冲计数值**
**参数**

- ConnectNo 指定链接号：0-7,默认值 0
- axis 指定轴号，取值范围：0-控制器最大轴数-1
- encoder_value 编码器计数值，单位：unit

### 函数名: get_encoder_unit_e

**功能：读取指定轴编码器脉冲计数值**
**参数**

- ConnectNo 指定链接号：0-7,默认值 0
- axis 指定轴号，取值范围：0-控制器最大轴数-1
- pos 返回编码器位置值，单位：unit

### 函数名: set_counter_inmode_e

**功能：设置编码器的计数方式**
**参数**

- ConnectNo 指定链接号：0-7,默认值 0
- axis 指定轴号，取值范围：0-控制器最大轴数-1
- mode 编码器的计数方式：
    - 0：非 A/B 相(脉冲/方向)
    - 1：1×A/B
    - 2：2×A/B
    - 3：4×A/B

### 函数名: get_counter_inmode_e

**功能：读取编码器的计数方式**
**参数**

- ConnectNo 指定链接号：0-7,默认值 0
- axis 指定轴号，取值范围：0-控制器最大轴数
- mode 返回编码器的计数方式
- 返回值：错误代码

### 函数名: stop_e

short smc_stop(WORD ConnectNo,WORD axis,WORD stop_mode)
**功能：指定轴停止运动**
**参数**

- ConnectNo 指定链接号：0-7,默认值 0
- axis 指定轴号，取值范围：0-控制器最大轴数-1
- stop_mode 制动方式，0：减速停止，1：立即停止
- 返回值：错误代码

### 函数名: emg_stop_e

**功能：紧急停止所有轴**
**参数**

- ConnectNo 指定链接号：0-7,默认值 0
- 返回值：错误代码 

### 函数名: read_org_pin
**功能：读取指定轴的 ORG 端口电平**
**参数**
- ConnectNo 指定链接号：0-7,默认值 0 
- axis 指定轴号，取值范围：0-控制器最大轴数-1 
- 返回值：ORG 端口电平，0：低电平，1：高电平

### 函数名: read_elp_pin
**功能：读取指定轴的正硬限位端口电平**
**参数**
- ConnectNo 指定链接号：0-7,默认值 0 
- axis 指定轴号，取值范围：0-控制器最大轴数-1 
- 返回值：EL+端口电平，0：低电平，1：高电平

### 函数名: read_eln_pin
**功能：读取指定轴的负硬限位端口电平**
**参数**
- ConnectNo 指定链接号：0-7,默认值 0 
- axis 指定轴号，取值范围：0-控制器最大轴数-1 
- 返回值：EL-端口电平，0：低电平，1：高电平

### 函数名: axis_io_status
**功能：读取指定轴有关运动信号的状态**
**参数**
- ConnectNo 指定链接号：0-7,默认值 0 
- axis 指定轴号，取值范围：0-控制器最大轴数-1
- 返回值：见表 3.2

| 位号  | 信号名称 |                 描述                  |
|:---:|:----:|:-----------------------------------:|
|  0  | ALM  |     1：表示伺服报警信号 ALM 为 ON； 0：OFF      |
|  1  | EL+  |     1：表示正硬限位信号 +EL 为 ON； 0：OFF      |
|  2  | EL-  |      1：表示负硬限位信号–EL 为 ON； 0：OFF      |
|  3  | EMG  |      1：表示急停信号 EMG 为 ON； 0：OFF       |
|  4  | ORG  |      1：表示原点信号 ORG 为 ON； 0：OFF       |
|  6  | SL+  |      1：表示正软限位信号+SL 为 ON； 0：OFF      |
|  7  | SL-  |     1：表示负软件限位信号-SL 为 ON； 0：OFF      |
|  8  | INP  |     1：表示伺服到位信号 INP 为 ON； 0：OFF      |
|  9  |  EZ  |        1：表示 EZ 信号为 ON； 0：OFF        |
| 10  | RDY  |                 保留                  |1：表示伺服准备信号 RDY 为 ON（SMC100 控制器专用）|
| 11  | DSTP | 1：表示减速停止信号 DSTP 为 ON（SMC100 控制器专用）； |
| 其他位 |  保留  |                                     |