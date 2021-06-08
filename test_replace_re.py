import re
#s = 'sdfjoiweng%@$foo$fsoifjoi'
#new_s = re.sub('foo','bar',s)
#print (new_s)
#sdfjoiweng%@$bar$fsoifjoi


s = '''
<networkManagedElementId>%node_logical_name%</networkManagedElementId>
                     <domainNumber>%Domain_number_SyncRef_4%</domainNumber>
<address>%address_router:vr_OAM%/%network_prefix_length:vr_OAM%</address>
'''

print("-----init string---------")
print(s)
print("-------------------------")
#regex3 = '%' + "(\w+)"+'%'
regex3 = '%' + "([\w:]+)"+'%'
variables3 = re.findall(regex3, s)
print(variables3)
for var in variables3:
	print (var)
	new_s = re.sub('%'+var+'%','${'+var+'}',s)
	s = new_s

print("-----after string---------")
print(s)
print("---------------------------")
#new_s = re.sub(regex3,"AAA",s)
#print(new_s)
#<networkManagedElementId>AAA</networkManagedElementId>

