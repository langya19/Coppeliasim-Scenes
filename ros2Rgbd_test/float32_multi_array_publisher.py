import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import random


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('float32_multi_array_publisher')
        self.publisher_ = self.create_publisher(Float32MultiArray, 'Float32MultiArray_test', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        length = 320*200
        msg = Float32MultiArray()
        msg.data = [round(self.i + random.random(), 2) for i in range(1, length + 1)] # random.random() 0~0.9
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: %d' % msg.data[0])
        self.i += 1


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
