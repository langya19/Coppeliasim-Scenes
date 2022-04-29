import rclpy
import sys
import cv2
import os
import numpy as np
from sensor_msgs.msg import Image
from rclpy.node import Node
from cv_bridge import CvBridge, CvBridgeError


class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('rgb_img_publisher')
        self.publisher_ = self.create_publisher(Image, '/monocular/camera/rgb', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.a = 960
        self.b = 540


    def timer_callback(self):
        image_path = "/home/hx/Desktop/image/pic.jpg"
        bridge = CvBridge()
        image = cv2.imread(image_path)
        image = cv2.resize(image, (self.a, self.b))
        self.publisher_.publish(bridge.cv2_to_imgmsg(image,"bgr8"))
        self.a -= 50
        self.b -= 20
        self.get_logger().info('Publishing: "%d, %d"' % (self.a, self.b))


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()        
