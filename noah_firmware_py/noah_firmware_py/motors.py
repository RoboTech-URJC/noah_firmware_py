import drive
import rclpy
from rclpy.executors import MultiThreadedExecutor
from rclpy.node import Node
import drive

class NoahMotorsNode(Node):
    def __init__(self):
        super().__init__(
          'NoahMotorsNode',
          allow_undeclared_parameters=True,
          automatically_declare_parameters_from_overrides=True)
        self.get_logger().info("NoahMotorsNode initializated")
        self._md = drive.md25()
        self._md.drive(100,100) # drives both motors at speed 100 using the default mode
    def destroy(self):
        super().destroy_node()

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