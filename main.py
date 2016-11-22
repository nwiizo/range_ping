#!/usr/bin/env python3

import sys
import time
import ipaddress
import os

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
		target_path = str("ping -c 1 " + n)
		cmd.append(target_path)
	return cmd



def task_route(cmd = setting_cmd()):
	pro_list=[]
	for n in cmd:
		cmd_chk = os.system(n)
		sys.stdout.flush()
		if cmd_chk == 0:
			pro_list.append(":(*´ω`)")
		else:
			pro_list.append(":(TдT)")

	return pro_list


def main():
	chk = task_route()
	cmd = setting_cmd()
	for cmd,c in zip(cmd,chk):
		print(cmd[10:],c)
		sys.stdout.flush()


	
if __name__ == '__main__':
		main()
