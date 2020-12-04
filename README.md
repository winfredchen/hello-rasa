# hello-rasa
rasa聊天机器人实例, [代码的详细介绍](https://51fhd.com/dev/hello-rasa/)
1. 一个最简单的web聊天机器人
2. 获取天气聊天机器人

**效果**

![image](./img/image-20201204130901875.png)

### 案例1：一个最简单的web聊天机器人

**组成**

1. rasa 核心
2. web 聊天页面

**运行**
1. rasa核心
```bash
cd rasa001_basic
rasa run --cors "*" #带允许跨域参数
```
2. web 聊天页面：用web服务器打开rasa001_basic/rasa_basic.html


### 案例2：获取天气聊天机器人

对话的大体目标，两个问句。第一次提出查天气，第二次说明具体的城市

```bash
hi
hi how may i assit you?

tell me today's weather?
which city you want to check for?

shanghai
the temperature is 27 degree
```

**组成**

1. rasa 核心
2. custom action - 获取天气
3. web 聊天页面

**运行** 
1. rasa核心
```bash
cd rasa002_weather
rasa run --cors "*" #带允许跨域参数
```
2. custom action运行
```bash
# 再开一个命令行窗口
rasa run actions
```
3. web 聊天页面：用web服务器打开rasa002_weather/rasa_weather.html
