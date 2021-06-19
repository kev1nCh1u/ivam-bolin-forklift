#!/bin/bash
# Program:
#       This program start bolin
# History:
# 2020/11/12	kevin	First release

echo -e "\033[32m
##############################
# ros bolin  #
# by Kevin Chiu 2020         #
##############################
\033[0m"
ws_path="/home/user/ros/kevin_bolin_ws" # 路徑
echo -e "ws_path:" $ws_path "\n"
cd $ws_path
source devel/setup.bash


###########
# 分頁視窗 #
###########
# gnome-terminal --tab -t "分頁名稱" -- bash -ic "指令"
gnome-terminal --tab -t "hokuyo_node" -- bash -ic "cd ~/ros/hokuyo_ws/;source devel/setup.bash;roslaunch hokuyo_node hokuyo_node.launch;exec bash"
sleep 0.2
gnome-terminal --tab -t "hector_slam_launch" -- bash -ic "cd $ws_path;source devel/setup.bash;roslaunch hector_slam_launch tutorial.launch;exec bash"
sleep 0.2
gnome-terminal --tab -t "joystick" -- bash -ic "cd $ws_path;source devel/setup.bash;rosrun JoyStick joystick /dev/input/js0;exec bash"
sleep 0.2
gnome-terminal --tab -t "move_robot" -- bash -ic "cd $ws_path;source devel/setup.bash;rosrun move_robot move_robot /dev/ttyUSB0 115200;exec bash"
sleep 0.2
# gnome-terminal --tab -t "r2000_node" -- bash -ic "cd $ws_path;source devel/setup.bash;rosrun pepperl_fuchs_r2000 r2000_node 192.168.10.100;exec bash"
# sleep 0.2
gnome-terminal --tab -t "AnhungControl" -- bash -ic "cd $ws_path;source devel/setup.bash;rosrun AnhungControl AnhungControl 127.0.0.1 9930;exec bash"
sleep 0.2

exec bash