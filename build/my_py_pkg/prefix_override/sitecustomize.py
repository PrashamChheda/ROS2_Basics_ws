import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/prasham/Prasham/GitHub/ros2_basics_ws/install/my_py_pkg'