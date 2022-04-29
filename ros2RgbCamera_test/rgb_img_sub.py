import rclpy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError
from rclpy.node import Node

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('rgb_img_subscriber')
        self.subscription = self.create_subscription(
            Image,
            '/monocular/camera/rgb',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.count = 0

    def listener_callback(self, data):
        bridge = CvBridge()
        cv_image = bridge.imgmsg_to_cv2(data,"bgr8")
        cv2.imshow("lala",cv_image)
        self.count += 1
        self.get_logger().info("receive: %d" % self.count)
        cv2.waitKey(20)


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()