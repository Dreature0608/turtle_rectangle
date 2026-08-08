#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class TurtleRect(Node):
    def __init__(self):
        super().__init__('turtle_rect')
        # 创建发布者，控制乌龟移动
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        time.sleep(1)  # 等待1秒，让乌龟窗口准备好

    # 直走函数：speed速度(米/秒)，distance距离(米)
    def go_straight(self, speed, distance):
        msg = Twist()
        msg.linear.x = speed
        duration = distance / speed  # 需要走多少秒
        end_time = time.time() + duration
        while time.time() < end_time:
            self.pub.publish(msg)
            time.sleep(0.05)  # 每0.05秒发一次命令
        self.stop()  # 停下来

    # 转弯函数：speed角速度(弧度/秒)，angle角度(弧度, 90度=1.57)
    def turn(self, speed, angle):
        msg = Twist()
        msg.angular.z = speed
        duration = angle / speed
        end_time = time.time() + duration
        while time.time() < end_time:
            self.pub.publish(msg)
            time.sleep(0.05)
        self.stop()

    def stop(self):
        self.pub.publish(Twist())  # 发布一个空命令，让乌龟停下
        time.sleep(0.1)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleRect()
    
    # 画长方形：长边2米，短边1米
    # 速度0.5米/秒，转90度(1.57弧度)用1.0弧度/秒的速度
    node.go_straight(0.5, 2.0)   # 走长边
    node.turn(1.0, 1.57)         # 左转90度
    node.go_straight(0.5, 1.0)   # 走短边
    node.turn(1.0, 1.57)         # 左转90度
    node.go_straight(0.5, 2.0)   # 走长边
    node.turn(1.0, 1.57)         # 左转90度
    node.go_straight(0.5, 1.0)   # 走短边
    node.turn(1.0, 1.57)         # 左转90度 (回到起点)

    print("长方形画完了！")
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
