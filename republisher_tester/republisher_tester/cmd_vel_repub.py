import rclpy
import time
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data

from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

ROBOTS = [
    [
        'tb01_0332',
        'tb02_0433',
        'tb03_0455',
        'tb04_0526',
        'tb05_1160',
        'tb06_1168',
        'tb07_1458',
        'tb08_1720',
        'tb09_2295',
        'tb10_2300',
        'tb11_1467',
        'tb12_1668',
        'tb13_1730',
        'tb14_1751',
        'tb15_1778',
        'tb16_1802',
        'tb17_0089',
        'tb18_1021',
        'tb19_1030',
        'tb20_2296',
    ],
]

# ROBOTS = [
#     [
#         'tb09_2295',
#         'tb10_2300', 
#     ],
# ]
# ROBOTS = [
#     [
#         'tb01_0332',
#         'tb02_0433',
#         'tb03_0455',
#         'tb04_0526',
#         'tb05_1160',
#     ],
#     [
#         'tb06_1168',
#         'tb07_1458',
#         'tb08_1720',
#         'tb09_2295',
#         'tb10_2300',
#     ],
# ]

class CmdVelRepub(Node):

    def __init__(self):
        super().__init__('cmd_vel_repub')
        self.repub_subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.listener_callback,
            qos_profile_sensor_data)
        self.repub_subscription  # prevent unused variable warning

        self.publishers_ = []
        for group in ROBOTS:
            pubs = []
            for name in group:
                pubs.append(self.create_publisher(Twist, f'/{name}/cmd_vel', 10))
                self.create_subscription(LaserScan,f'/{name}/scan',self.listener_callback2,qos_profile_sensor_data)
            self.publishers_.append(pubs)

    def listener_callback(self, msg):
        for pub_group in self.publishers_:
            for pub in pub_group:
                pub.publish(msg)
                #self.get_logger().info(f'Repub message to {pub.topic_name}')
            #time.sleep(0.1)
            #self.get_logger().info(f'pausing...')

    def listener_callback2(self, msg):
        msg


def main(args=None):
    rclpy.init(args=args)

    cmd_vel_repub = CmdVelRepub()

    rclpy.spin(cmd_vel_repub)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    cmd_vel_repub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
