#!/usr/bin/env python3
#version 1.1, 20Apr update ham matching_tr
import pandas
import numpy as np
import re
import new_crash
import skt_5g_cd_tool
filename = 'mhweb_data.csv'
dataset = pandas.read_csv(filename,encoding = "ISO-8859-1",low_memory=False)

#data = pandas.read_csv(myfile, encoding='utf-8', quotechar='"', delimiter=',') 
print ("READING file",filename,'...')

#print(dataset)
print("Data dimention:", dataset.shape)

global tr_ids, tr_headings, faulty_sws, corrected_sws, observations, answers
tr_ids = dataset['General.Eriref']
tr_headings = dataset['General.Heading']
faulty_sws = dataset['Node level.Product no & R-Stat']
corrected_sws = dataset['Corrected.Product no & R-State']
observations = dataset['Observation.Observation']
answers = dataset['Answer.Answer']


def filter_column_by_trid(tr, column_header):

	'''
	input:trid and column_header == 'Node level.Product no & R-Stat'
	output:{'CXP 902 4418/12@R62A86', 'CXP 902 4418/12@R62A87', 'CXP 902 4418/12@R62A88'}
	'''
	column_content = dataset[column_header]
	filter_result = set()
	for i, trid in enumerate(tr_ids):
		#chi add string, khong add nan item
		if trid == tr and isinstance(column_content[i], str):
			filter_result.add(column_content[i])
	
	return filter_result
	

def create_tr_sw_dict(column_header):
	tr_dict = {}
	for i, tr in enumerate(tr_ids):
		#sws = filter_column_by_trid(tr, 'Node level.Product no & R-Stat')
		sws = filter_column_by_trid(tr, column_header)
		tr_dict[tr] = sws
	
	return tr_dict

def extract_revision(sw_list):
	'''
	return example:
	{'CXP9024418/12': ['R45D39']}
	{'CXP9024418/6': ['R84A104', 'R86A05'], 'CXP9024418/15': ['R1A62'], 'CXP9024418/12': ['R56A100']}
	
	'''
	result_dict_product_rev = {}
	products =set()
	#find product code
	for sw in sw_list:
		m = re.match('(.*)@(.*)',sw)
		if m:
			product_code = m.group(1)
			product_code = product_code.replace(' ', '')
			product_rev = m.group(2)
			products.add(product_code)
	
	#find revision
	for product in products:
		revs = []
		for sw in sw_list:
			m = re.match('(.*)@(.*)',sw)
			if m:
				product_code = m.group(1)
				product_code = product_code.replace(' ', '')
				product_rev = m.group(2)
				if product_code == product:
					revs.append(product_rev)
		#result_dict_product_rev	[product] = revs
		#chi luu min va max cho de xu ly
		if min(revs) < max(revs):
			result_dict_product_rev	[product] = [min(revs), max(revs)]
		
		if min(revs) == max(revs):
			result_dict_product_rev	[product] = [min(revs)]
	
	sorted(result_dict_product_rev)
	
	return result_dict_product_rev
	

def print_tr(tr):
	print (tr)
	print("observation:")
	print(get_observation(tr))
	
	print("answer:")
	print(get_answer(tr))
	
	print("faulty_sws:")
	print(get_faulty_sw_dict(tr))
	
	print("corrected_sws:")
	print(get_corrected_sw_dict(tr))
	

def get_observation(trid):
	observation = ""
	for i, tr in enumerate(tr_ids):
		if tr == trid:
			observation = observations[i]
			break
	return observation
	

def get_answer(trid):
	answer = ""
	for i, tr in enumerate(tr_ids):
		if tr == trid:
			answer = answers[i]
			break
	return answer
	



			
def get_faulty_sw_dict(tr):
	#return observed_sw
	#return example, a tube (CXP2010045/5 R15B37)
	observed_sw = ("","")
	if tr in tr_faultsw_dict.keys():
		faultsw = tr_faultsw_dict[tr]
		dict_product_rev = extract_revision(faultsw)
		#faulty sw: {'CXP2010045/5': ['R17B29']}
		#vi ly do sw observed/sw fault chi co 1 item
		
		observed_sw = (list(dict_product_rev.keys())[0] , list(dict_product_rev.values())[0][0])
	return observed_sw

def get_corrected_sw_dict(tr):
	correctedsw = tr_corrected_dict[tr]
	dict_product_rev = extract_revision(correctedsw)
	return dict_product_rev

def matching_tr(crash_string, observed_sw):
	'''
	observed_sw is a tube = (product revision) = ('CXP2010045/5', 'R19B31')
	'''
	#remove day time from searching string
	
	crash_string = new_crash.extract_crash_signature(crash_string, False)
	search_pattern = skt_5g_cd_tool.create_python_regex_string(crash_string)
	
	observed_product = observed_sw[0]
	observed_rev = observed_sw[1]
	observed_sw_string = observed_product +'_'+observed_rev
	print('observed_product' , observed_product)
	print('observed_rev' , observed_rev)
	print('observed_sw_string' , observed_sw_string)
	
	#print(crash_string)
	print ("seaching pattern:",search_pattern)
	tr_founds = set()
	for i, observation in enumerate(observations):
		#neu string khong trong thi moi tien hanh match
		if search_pattern!= "":
			#cach nay rat cham
			if re.search(search_pattern, observation):
				tr = tr_ids[i]
				
				#matching dua vao sw level, to filter some TR by sw
				#sw cua TR duoc tim ra
				corrected_sw = get_corrected_sw_dict(tr)
				
				print ('corrected_sw', corrected_sw)
				#corrected_sw {'CXP9024418/12': ['R52C24', 'R52C31'], 'CXP9024418/6': ['R80C106', 'R82A71']}
				
				corrected_product = corrected_sw.keys()
				print ('corrected_product', corrected_product)
				
				
				#new TR tim ra ma co solution roi, thi tien hanh so sanh
				if len(corrected_product) > 0:
					if observed_product in corrected_product:
						print ('extract corrected product and rev')
						corrected_rev = corrected_sw[observed_product]
						min_corrected_sw_string = observed_product+'_'+corrected_rev[0]
						max_corrected_sw_string = observed_product+'_'+corrected_rev[-1]
						
						print ('observed: '+observed_sw_string, 'min: '+ min_corrected_sw_string,'max '+ max_corrected_sw_string)
						#neu observed sw < min corrected sw thi coi nhu chap nhan
						if observed_sw_string <= min_corrected_sw_string:
							tr_founds.add(tr)
				else:
					# neu tr tim ra chua co solution, thi add luon, giet nham con hon bo xot
					tr_founds.add(tr)

	
	return list(tr_founds)


	

def match_all_sign_trmappingtool():
	tr_dict = new_crash.get_tr_mapping_dict()[0]
	i = 1
	for sign, tr in tr_dict.items():
		print ('-'*30)
		print (sign)
		observed_sw = get_faulty_sw_dict(tr)
		#print ("troubleshoot")
		print ("observed_sw", observed_sw)
		
		#observed_sw = (CXP2010045/5 R15B37)
		
		#finding list of matching TR
		matched_tr_list = matching_tr(sign, observed_sw)
		
		print (i, '|', sign, '|', 'origin TR ' + tr, '|' , 'matched:',  matched_tr_list)
		if len(matched_tr_list) > 0:
			print ("Detail of matching TR:")
			for id in matched_tr_list:
				print (id)
				print ("faulty sw:",get_faulty_sw_dict(id))
				print ("corrected sw",get_corrected_sw_dict(id))
		i += 1

def main():
	tr_set = set(tr_ids)
	
	global tr_faultsw_dict
	global tr_corrected_dict
	tr_faultsw_dict = create_tr_sw_dict('Node level.Product no & R-Stat')
	tr_corrected_dict = create_tr_sw_dict('Corrected.Product no & R-State')
	
	#tr_faultsw_dict = {'HY37588': {'CXP 902 4418/6@R80F51'}, 'HY37607': {'CXP 902 4418/12@R57C74'}, 'HY37614': {'CXP 902 4418/12@R57C74'},...}
	
	#tr_corrected_dict = {'HY37588': set(),  'HY34532': {'CXP 102 051/27@R73K09', 'CXP 902 4418/6@R73K16', 'CXP 902 4418/6@R86A05', 'CXP 902 4418/12@R52E42', 'CXP 902 4418/6@R83A92', 'CXP 902 4418/12@R45K10', 'CXP 902 4418/6@R73K14', 'CXP 902 4418/6@R73K15', 'CXP 902 4418/15@R1A62', 'CXP 902 4418/6@R80E41'},   ... }
	
	#test get tr content 
	#trid = input("TR ID:")
	#print_tr(trid)
	
	print ("sw for all tr")
	print ("Total TR in DATABASE:", len(tr_set))
	#for i, tr in enumerate(tr_set):
	#	print (i, '|', tr, '|' , get_faulty_sw_dict(tr), '|', get_corrected_sw_dict(tr))
	
	print("Test matching TR function")

	match_all_sign_trmappingtool()

	
	
	
		
if __name__ == "__main__":
	main()