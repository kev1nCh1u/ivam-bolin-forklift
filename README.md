# BOLIN 插車

## chmod
    sudo chmod 777 /dev/ttyACM0

## ros launch
    roslaunch hector_slam_launch tutorial.launch
    roslaunch roslaunch launch_start start.launch

## ros run
    cd ~/ros/kevin_bolin_ws/

    catkin_make

    . devel/setup.bash

    rosrun JoyStick joystick /dev/input/js0
    rosrun move_robot move_robot /dev/ttyACM0 38400
    rosrun pepperl_fuchs_r2000 r2000_node 192.168.10.100
    roslaunch hector_slam_launch tutorial.launch
    rosrun AnhungControl AnhungControl 192.168.72.224 9930

## debug
    rostopic pub -r 5 Send_Pose geometry_msgs/PoseStamped // tab

    python src/test/UDP_Send/udp_send.py
    
    "Mr;1,0,1.73,0.43,1.74,diff,0,0.5,ivam_3F;2,3,2.48,-5.01,1.74,diff,0,0.5,ivam_3F,2;E" #line

    "Mr;1,0,3.18,-3.50,1.75,diff,0,0.5,ivam_3F;3,13,2.92,-1.39,1.73,diff,0,0.5,ivam_3F;4,13,3.10,-2.179,1.58,diff,0,0.5,ivam_5F;5,3,3.19,-0.88,1.58,diff,0,0.5,ivam_5F,2;E"

    "Mr;1,0,-0.17,-0.44,0.10,diff,1,0.5,ivam_3F;2,1,3.61,0.35,1.68,diff,0,0.5,ivam_3F;3,3,4.01,-3.44,1.68,diff,0,0.5,ivam_3F,2;E" #one turn

    "Mr;1,0,-0.17,-0.44,0.10,diff,1,0.5,ivam_3F;2,1,3.61,0.35,1.68,diff,1,0.5,ivam_3F;3,1,4.01,-3.44,1.68,diff,0,0.5,ivam_3F;4,3,1.31,-3.73,0.12,diff,0,0.5,ivam_3F,2;E" #two turn

    "Mr;1,0,-0.17,-0.44,0.10,diff,1,0.5,ivam_3F;2,1,3.61,0.35,1.68,diff,0,0.5,ivam_3F;3,1,3.77,-0.85,-1.46,diff,1,0.5,ivam_3F;4,1,4.01,-3.44,1.68,diff,1,0.5,ivam_3F;5,1,1.31,-3.73,0.12,diff,0,0.5,ivam_3F;6,3,0.72,-0.358,-1.45,diff,0,0.5,ivam_3F,2;E" #o turn

    "Mr;1,0,-0.95, -0.30,-3.02,diff,0,0.5,ivam_3F;2,3,1.49,-0.90,-0.32,diff,0,0.5,ivam_3F;3,19,1.49,-0.90,-0.32,diff,0,0.5,ivam_3F;4,3, 1.01,-2.98,1.69,diff,0,0.5,ivam_3F,2;E" #switch_test

    "F;10;E" #倒車
    "F;11;E" #前進
    

## ssh
    ssh 192.168.72.152
    sudo service ssh start
    scp -r /home/user/ros/kevin_bolin_ws/src user@192.168.72.152:/home/user/ros/kevin_bolin_ws/
    scp -r /home/user/ros/kevin_bolin_ws/src user@192.168.72.22:/home/user/ros/kevin_bolin_ws/

## git
    git clone ssh://user@192.168.72.152:/home/user/ros/bolin_ws/src.git
    git remote add laptop ssh://user@192.168.72.152:/home/user/ros/bolin_ws/src.git

## problem
