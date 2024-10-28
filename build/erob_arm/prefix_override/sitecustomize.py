import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/erobman/IGH_EtherCAT/eRob_arm/install/erob_arm'
