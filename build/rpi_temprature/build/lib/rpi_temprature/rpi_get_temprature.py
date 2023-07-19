import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32

from gpiozero import CPUTemperature
from time import sleep

def rpi_cpu_temp_func():
    cpu = CPUTemperature()
    cpu_temp = cpu.temperature
    if cpu_temp > 82:
        high_alert = ". CPU temp is HIGH !!!"
    else:
        high_alert = ""

    # print("RPI cpu temp: {:.2f} degC{}".format(cpu_temp, high_alert))
    return cpu_temp

class TempPublisher(Node):
    def __init__(self):
        super().__init__('rpi_temp_publisher')
        self.publisher_ = self.create_publisher(Float32, 'rpi_cpu_temp', 10)
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        # self.i = 0.0

    def timer_callback(self):
        msg = Float32()
        msg.data = rpi_cpu_temp_func()
        self.publisher_.publish(msg)
        # self.get_logger().info('Publishing: "%s"' % msg.data)
        # self.i += 1.0

def main(args=None):    
    rclpy.init(args=args)

    rpi_temp_publisher = TempPublisher()

    rclpy.spin(rpi_temp_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    rpi_temp_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
