import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
import tf2_ros

class MapFrameBroadcaster(Node):
    def __init__(self):
        super().__init__('world_frame_broadcaster')
        self.broadcaster = tf2_ros.StaticTransformBroadcaster(self)
        self.broadcast_world_frame()

    def broadcast_world_frame(self):
        t = TransformStamped()
        
        # Since this is the root frame, it has no parent.
        t.header.frame_id = 'world'  # No parent frame
        t.child_frame_id = 'map'
        
        # Set the timestamp to the current time
        t.header.stamp = self.get_clock().now().to_msg()
        
        # Set the position of the world frame (origin)
        t.transform.translation.x = 0.0
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.0
        
        # Set the orientation of the world frame (identity quaternion)
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0
        
        # Broadcast the static transformation
        self.broadcaster.sendTransform(t)

def main(args=None):
    rclpy.init(args=args)
    node = MapFrameBroadcaster()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()