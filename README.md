# BOLIN 插車

## chmod

    sudo chmod 777 /dev/ttyACM0

## start command
    cd ros/bolin_ws/

    . devel/setup.bash
    roslaunch hector_slam_launch tutorial.launch

    . devel/setup.bash
    rosrun JoyStick joystick /dev/input/js0

    . devel/setup.bash
    rosrun move_robot move_robot /dev/ttyACM0 38400

    . devel/setup.bash
    rosrun pepperl_fuchs_r2000 r2000_node "192.168.10.100"

    . devel/setup.bash
    rosrun AnhungControl AnhungControl "192.168.72.224" 9930

## debug
    python src/test/UDP_Send/udp_send.py

## ssh
    ssh 192.168.72.152
    scp -r /home/user/ros/bolin_ws/src user@192.168.72.152:/home/user/kevin_bolin_ws/

## 問題
