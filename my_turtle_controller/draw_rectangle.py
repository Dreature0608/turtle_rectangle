import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class TurtleRect(Node):
    def __init__(self):
        super().__init__('turtle_rect')
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        time.sleep(1)  

    def go_straight(self, speed, distance):
        msg = Twist()
        msg.linear.x = speed
        duration = distance / speed  
        end_time = time.time() + duration
        while time.time() < end_time:
            self.pub.publish(msg)
            time.sleep(0.05)  
        self.stop()  


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
        self.pub.publish(Twist())  
        time.sleep(0.1)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleRect()

    node.go_straight(0.5, 2.0)   
    node.turn(1.0, 1.57)         
    node.go_straight(0.5, 1.0)   
    node.turn(1.0, 1.57)         
    node.go_straight(0.5, 2.0)   
    node.turn(1.0, 1.57)        
    node.go_straight(0.5, 1.0)   
    node.turn(1.0, 1.57)         

    print("长方形画完了！")
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
