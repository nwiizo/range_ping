#!/usr/bin/env python3

import sys
import time
import ipaddress
import os
import re

def setting_ip():
    start_ip = str(input("start_ip:"))
    range_ip = input("range_ip:")
    set_ip = []
    for n in range(int(range_ip)):
        target_ip = str(ipaddress.IPv4Address(start_ip) + n)
        set_ip.append(target_ip)
    return set_ip

def setting_cmd(target_ip = setting_ip()):
    cmd = []
    for n in target_ip:
        target_path = str("ping -c 1 " + n +" > /dev/null 2>&1")
        cmd.append(target_path)
    return cmd



def task_route(cmd = setting_cmd()):
    pro_list=[[]]
    for i,n in enumerate(cmd):
        cmd_chk = os.system(n)
        sys.stdout.flush()
        if cmd_chk == 0:
            pro_list.append("OK")
        else:
            pro_list.append("OK")

    return pro_list


def main():
    print('  m mm   mmm   m mm    mmmm   mmm          mmmm   mmmmm  m mm    mmmm ')
    print('  #"  " "   #  #"  #  #" "#  #"  #         #" "#    #    #"  #  #" "# ')
    print('  #     m"""#  #   #  #   #  #""""         #   #    #    #   #  #   # ')
    print('  #     "mm"#  #   #  "#m"#  "#mm"         ##m#"  mm#mm  #   #  "#m"# ')
    print('                       m  #                #                     m  # ')
    print('                        ""         """"""  "      v0.1            ""  ')
    chk = task_route()
    cmd = setting_cmd()
    for cmd,c in zip(cmd,chk[1:]):
        print(cmd.split(" ")[3],c)
        sys.stdout.flush()
    


if __name__ == '__main__':
        main()
