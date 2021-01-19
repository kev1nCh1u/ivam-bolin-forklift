# BOLIN 插車

## chmod

    sudo chmod 777 /dev/ttyACM0

## ros run
    cd ~/ros/kevin_bolin_ws/

    catkkin_make

    . devel/setup.bash
    rosrun JoyStick joystick /dev/input/js0
    roslaunch JoyStick joystick.launch  //or

    . devel/setup.bash
    rosrun move_robot move_robot /dev/ttyACM0 38400
    roslaunch move_robot move_robot.launch  //or

    . devel/setup.bash
    rosrun pepperl_fuchs_r2000 r2000_node 192.168.10.100
    roslaunch pepperl_fuchs_r2000 pepperl_fuchs_master.launch  //or

    . devel/setup.bash
    roslaunch hector_slam_launch tutorial.launch

    . devel/setup.bash
    rosrun AnhungControl AnhungControl 192.168.72.224 9930
    roslaunch AnhungControl anhung_control.launch  //or

## ros launch
    roslaunch hector_slam_launch tutorial.launch
    roslaunch bolin_forklift bin_forklift.launch

## debug
    python src/test/UDP_Send/udp_send.py
    
    "Mr;1,0,1.68822,0.432922,1.71258,diff,0,0.5,ivam_3F;2,3,2.46556,-4.44588,1.73435,diff,0,0.5,ivam_3F,2;E"
    "Mr;1,0,1.73,0.43,1.74,diff,0,0.5,ivam_3F;2,3,2.48,-5.01,1.74,diff,0,0.5,ivam_3F,2;E"

    "Mr;1,0,3.18,-3.50,1.75,diff,0,0.5,ivam_3F;3,13,2.92,-1.39,1.73,diff,0,0.5,ivam_3F;4,13,3.10,-2.179,1.58,diff,0,0.5,ivam_5F;5,3,3.19,-0.88,1.58,diff,0,0.5,ivam_5F,2;E"

    rosrun hokuyo_node hokuyo_node
    rosrun move_robot move_robot /dev/ttyUSB0 115200

    rostopic pub -r 5 Send_Pose geometry_msgs/PoseStamped // tab

## ssh
    ssh 192.168.72.152
    sudo service ssh start
    scp -r /home/user/ros/kevin_bolin_ws/src user@192.168.72.152:/home/user/ros/kevin_bolin_ws/
    scp -r /home/user/ros/kevin_bolin_ws/src user@192.168.72.22:/home/user/ros/kevin_bolin_ws/

## git
    git clone ssh://user@192.168.72.152:/home/user/ros/bolin_ws/src.git
    git remote add laptop ssh://user@192.168.72.152:/home/user/ros/bolin_ws/src.git

## 問題
