from string import Template
data = {"nodename":"viettel1"}


f = open("/mnt/c/cygwin/home/ephucle/tool_script/python/pythonlab/script_creater/template/5G_relation/4_1_gNB_NRNetwork", "r")
input_file_content = f.read()  #<class 'str'>

print("type(input_file_content):",type(input_file_content))
print(input_file_content)
src = Template(input_file_content)
result = src.substitute(data)

print("type(result):", type(result))
print(result)


output_text_file = open("outfile.txt", "w")
output_text_file.write(result)
output_text_file.close()