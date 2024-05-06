import rclpy 
from rclpy.node import Node 
from std_msgs.msg import String

class SimplePublisher(Node):
    def __init__(self):
        super().__init__("simple_publisher")
        self.pub = self.create_publisher(String, "chatter", 10) # defined in Node class
        self.counter = 0
        self.frequency = 1.0 # frequency (Hz)
        
        self.get_logger().info(f"Publishing at {self.frequency} Hz")

        self.timer = self.create_timer(self.frequency, self.timerCallback)

    def timerCallback(self):
        msg = String()
        msg.data = f"Hello ROS2 --counter: {self.counter}"

        self.pub.publish(msg)
        self.counter += 1

def main():
    rclpy.init()
    simple_publisher = SimplePublisher()
    rclpy.spin(simple_publisher) # keep node active

    simple_publisher.destroy_node() # graceful ctrl-c exit
    rclpy.shutdown()


if __name__=="__main__":
    main()