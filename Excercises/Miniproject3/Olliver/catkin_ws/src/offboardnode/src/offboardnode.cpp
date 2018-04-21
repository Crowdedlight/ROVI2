/*
 * Originally from: https://dev.px4.io/ros-mavros-offboard.html
 */
#include <ros/ros.h>
#include <geometry_msgs/PoseStamped.h>
#include <mavros_msgs/CommandBool.h>
#include <mavros_msgs/SetMode.h>
#include <mavros_msgs/State.h>
#include <std_msgs/Int16.h>
#include <std_msgs/Float32.h>
mavros_msgs::State current_state;
int x_pos_global;
int y_pos_global;
float theta_global;
void state_cb(const mavros_msgs::State::ConstPtr& msg){
    current_state = *msg;
}
void x_pos_cb(const std_msgs::Int16::ConstPtr& msg){
    x_pos_global = (*msg).data;
}
void y_pos_cb(const std_msgs::Int16::ConstPtr& msg){
    y_pos_global = (*msg).data;
}
void theta_cb(const std_msgs::Float32::ConstPtr& msg){
    theta_global = (*msg).data;
}
int main(int argc, char **argv)
{
    ros::init(argc, argv, "offb_node");
    ros::NodeHandle nh;
    ros::Subscriber state_sub = nh.subscribe<mavros_msgs::State>
            ("mavros/state", 10, state_cb);
    ros::Subscriber x_pos_sub = nh.subscribe<std_msgs::Int16>
            ("/markerlocator/x_pose", 10, x_pos_cb);
    ros::Subscriber y_pos_sub = nh.subscribe<std_msgs::Int16>
            ("/markerlocator/y_pose", 10, y_pos_cb);
    ros::Subscriber theta_sub = nh.subscribe<std_msgs::Float32>
            ("/markerlocator/theta", 10, theta_cb);
    ros::Publisher local_pos_pub = nh.advertise<geometry_msgs::PoseStamped>
            ("mavros/setpoint_position/local", 10);
    ros::ServiceClient arming_client =
            nh.serviceClient<mavros_msgs::CommandBool>
            ("mavros/cmd/arming");
    ros::ServiceClient set_mode_client =
            nh.serviceClient<mavros_msgs::SetMode>
            ("mavros/set_mode");
    //the setpoint publishing rate MUST be faster than 2Hz
    ros::Rate rate(20.0);
    // wait for FCU connection
    while(ros::ok() && current_state.connected){
        ros::spinOnce();
        rate.sleep();
    }
    geometry_msgs::PoseStamped pose;
    pose.pose.position.x = 0;
    pose.pose.position.y = 0;
    pose.pose.position.z = 2;

    //send a few setpoints before starting, or else you won't be able to switch to offboard mode
    for(int i = 100; ros::ok() && i > 0; --i){
        local_pos_pub.publish(pose);
        ros::spinOnce();
        rate.sleep();
    }
    mavros_msgs::SetMode offb_set_mode;
    offb_set_mode.request.custom_mode = "OFFBOARD";
    mavros_msgs::CommandBool arm_cmd;
    arm_cmd.request.value = true;
    ros::Time last_request = ros::Time::now();
    int counter = 0;
    while(ros::ok()){
        if( current_state.mode != "OFFBOARD" &&
                (ros::Time::now() - last_request > ros::Duration(5.0))){
            if( set_mode_client.call(offb_set_mode) &&
                    offb_set_mode.response.mode_sent){
                ROS_INFO("Offboard enabled");
            }
            last_request = ros::Time::now();
        } else {
            if( !current_state.armed &&
                    (ros::Time::now() - last_request > ros::Duration(5.0))){
                if( arming_client.call(arm_cmd) &&
                        arm_cmd.response.success){
                    ROS_INFO("Vehicle armed");
                }
                last_request = ros::Time::now();
            }
        }
        counter++;
        if (counter > 100) {
            pose.pose.position.x = x_pos_global;
            pose.pose.position.y = y_pos_global;
            pose.pose.position.z = 2;
        }
        std::cout << "x-pose: " << x_pos_global << " y-pose: " << y_pos_global << " theta: " << theta_global << std::endl;
        local_pos_pub.publish(pose);
        ros::spinOnce();
        rate.sleep();
    }
    return 0;
}
