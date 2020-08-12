import concurrent.futures
import time, datetime, re
def current_time_stamp():
	return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

count = 0

def read_file(filename, target_count):
	global count
	while count < target_count:
		time.sleep(5)  #nghi 3s, doc file 1 lan
		print(current_time_stamp(), "start reading file")
		
		temp_count = 0
		with open(filename) as infile:
			lines = [line.strip() for line in infile.readlines()]
			for line in lines:
				if "finish" in line:
					temp_count += 1
		count = temp_count
		print(current_time_stamp(), "end reading file")
		
		print(current_time_stamp(),"count inside readfile func", count)
		
	
def func(text, id):
	global count
	print(current_time_stamp(),"start to call func", id)
	for i in range(3):
		
		print("func id:", id , text)
		count += 1
		print(current_time_stamp(),"count",count)
		time.sleep(3)
		
	print(current_time_stamp(),"end func", id)

no_of_thread = 1

print(current_time_stamp(),"Start test ThreadPoolExecutor")
print(" init count:", count)
with concurrent.futures.ThreadPoolExecutor(max_workers=no_of_thread) as executor:
	for id in range(no_of_thread):
		#executor.submit(func, "hello world", id)
		executor.submit(read_file, "running.txt", 5)  #target, count toi 5

print(current_time_stamp(),"End test ThreadPoolExecutor")
print(" end count:", count)