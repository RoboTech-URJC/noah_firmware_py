import rclpy
from rclpy.executors import MultiThreadedExecutor
from rclpy.node import Node
from noah_firmware_py.drive import md25
from geometry_msgs.msg import Twist

MAX_VEL_VALUE = 127

class NoahMotorsNode(Node):
    def __init__(self):
        super().__init__(
          'NoahMotorsNode',
          allow_undeclared_parameters=True,
          automatically_declare_parameters_from_overrides=True)
        self.get_logger().info("NoahMotorsNode initializated")
        self._md = md25()
        self._cmd_vel_sub = self.create_subscription(
          Twist,
          'cmd_vel',
          self._cmd_vel_cb,
          10)
        # self._md.drive(100,100) # drives both motors at speed 100 using the default mode
    def destroy(self):
        super().destroy_node()
    def _cmd_vel_cb(self, msg):
        linear_vel = 0.0
        angular_vel = 0.0
        if msg.linear.x > 1.0:
            linear_vel = 1.0
        elif msg.linear.x < -1.0:
            linear_vel = -1.0
        else:
            linear_vel = msg.linear.x

        if msg.angular.z > 1.0:
            angular_vel = 1.0
        elif msg.angular.z < -1.0:
            angular_vel = -1.0
        else:
            angular_vel = msg.angular.z

        # linear_vel = 1 - linear_vel # 0.1 rapido - 0.9 lento.

        right = int(MAX_VEL_VALUE * (1.0 * linear_vel + angular_vel * 0.2 / 2.0))
        left = int(MAX_VEL_VALUE * (1.0 * linear_vel - angular_vel * 0.2 / 2.0))

        if msg.linear.x == 0.0 and msg.angular.z == 0.0:
            self._md.stop()
        else:
            self._md.drive(left, right)

def main(args=None):
    rclpy.init(args=args)
    node = NoahMotorsNode()
    try:
        executor = MultiThreadedExecutor()
        rclpy.spin(node, executor=executor)
    except KeyboardInterrupt:
        pass

    node.destroy()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
