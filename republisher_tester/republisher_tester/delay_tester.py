import rclpy
import time
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data

from nav_msgs.msg import Odometry


class DelayTester(Node):

    def __init__(self):
        super().__init__('delay_tester')
        self.repub_subscription = self.create_subscription(
            Odometry,
            '/donatello/odom',
            self.repub_listener_callback,
            qos_profile_sensor_data)
        self.repub_subscription  # prevent unused variable warning

        self.orig_subscription = self.create_subscription(
            Odometry,
            '/donatello/_do_not_use/odom',
            self.orig_listener_callback,
            qos_profile_sensor_data)
        self.orig_subscription  # prevent unused variable warning

    def repub_listener_callback(self, msg):
        self.get_logger().info(f'Repub message at {time.time()} from time stamp {msg.header.stamp}')

    def orig_listener_callback(self, msg):
        self.get_logger().info(f'Orig  message at {time.time()} from time stamp {msg.header.stamp}')


def main(args=None):
    rclpy.init(args=args)

    delay_tester = DelayTester()

    rclpy.spin(delay_tester)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    delay_tester.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
