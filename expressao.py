def is_substring_expr(str1,str2):
	str2 = str2.split('*')
	if len(str1) < len(str2[0]) + len(str2[1]):
		return False
	word1 = ''
	word2 = ''
	for c in str1:
		word1 += c
		if len(word1) == len(str2[0]):
			if word1 != str2[0]: return False
	for c in range(len(str1) - len(str2[1]),len(str1)):
		word2 += str1[c]
		if len(word2) == len(str2[1]):
			if word2 != str2[1]: return False
	return True
