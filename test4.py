import new_crash

sw_filter_list = set([
	'CXP9024418/12_R54B47' , 'CXP9024418/12_R55B26', 'CXP9024418/12_R57C74', 'CXP9024418/12_R60B28' , 
	'CXP9024418/6_R77B39' , 'CXP9024418/6_R80F30' , 'CXP9024418/6_R80F51',
	'CXP9024418/6_R85C59(gNB)' , 'CXP9024418/6_R85C103(gNB)'
	])
	

check1 = new_crash.check_if_crash_in_new_sw({'CXP9024418/6_R73E32', 'CXP9024418/12_R57C74', 'CXP9024418/6_R80C90(gNB)', 'CXP9024418/6_R73C96', 'CXP9024418/12_R54B47'}, sw_filter_list)

print (check1)


check2 = new_crash.check_if_crash_in_new_sw({'CXP9024418/6_R73E32'}, sw_filter_list)

print (check2)