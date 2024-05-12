import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32

from gpiozero import CPUTemperature
from time import sleep
from collections import deque
from time import time
        

class TempPublisher(Node):
    def __init__(self):
        super().__init__('rpi_temp_publisher')

        self.cpu = CPUTemperature()
        self.max_temp_10s = float('-inf')
        self.max_temp_60s = float('-inf')
        self.deque_size = 60 # seconds
        self.temperature_queue = deque(maxlen=self.deque_size)  # Queue to store temperatures for 60 seconds
        self.last_update_time = time()
        
        self.publisher_cpu_temp = self.create_publisher(Float32, 'rpi_cpu_temp', 10)
        self.publisher_max_temp_10s = self.create_publisher(Float32, 'rpi_cpu_max_temp_10s', 10)
        self.publisher_max_temp_60s = self.create_publisher(Float32, 'rpi_cpu_max_temp_60s', 10)
        self.get_logger().info("Printing cpu temperture: Current | max 10s | max60s")

        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        # self.i = 0.0

    def timer_callback(self):
        try:
            self.update_max_temp()
            cpu_temp = self.cpu.temperature
            msg_cpu_temp = Float32()
            msg_cpu_temp.data = cpu_temp
            self.publisher_cpu_temp.publish(msg_cpu_temp)

            msg_max_temp_10s = Float32()
            msg_max_temp_10s.data = self.max_temp_10s
            self.publisher_max_temp_10s.publish(msg_max_temp_10s)

            msg_max_temp_60s = Float32()
            msg_max_temp_60s.data = self.max_temp_60s
            self.publisher_max_temp_60s.publish(msg_max_temp_60s)
        except Exception as e:
            self.get_logger().info("Error reading CPU temperature: {}".format(e))
    
    def update_max_temp(self):
        current_temp = self.cpu.temperature

        # Ensure the deque doesn't exceed its maximum size
        if len(self.temperature_queue) >= self.deque_size:
            self.temperature_queue.popleft()  # Remove the oldest element
        self.temperature_queue.append(current_temp)

        # Update max temp for last 10 seconds
        if len(self.temperature_queue) >= 10:
            self.max_temp_10s = max(list(self.temperature_queue)[-10:])

        # Update max temp for all readings
        self.max_temp_60s = max(list(self.temperature_queue))
        
        self.get_logger().info("{:.1f}\u00b0\t{:.1f}\u00b0\t{:.1f}\u00b0".format(current_temp,
                                                                                       self.max_temp_10s,
                                                                                       self.max_temp_60s
                                                                                       ))
        
        # self.get_logger().info("\nqueue:{}".format(self.temperature_queue))


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
