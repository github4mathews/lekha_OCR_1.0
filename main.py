# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 10:25:26 2015

Project Malayalam OCR - Lekha
-----------------------------

@author: james
"""
import cv2
import sys
import preprocess as pp
import training as train
sys.path.insert(0,'/home/jithin/lekha_OCR_1.0')
import random
def recognize_block(im):
	line = pp.find_lines(im)
	# print len(linene)
	label_list=train.label_unicode()
	i=0
	string='word:'
	for l in line:
		cv2.imwrite('temp/zline_'+str(i)+'.png',l.data)
		string=string+'\n'
		j=0
		for w in l.word_list:
	#		cv2.imwrite('zword_'+str(i)+'_word_'+str(j)+'.png',w.data)
			string=string+' '
			j+=1
			k=0
			c=0
			while(c<len(w.char_list)):
				char= w.char_list[c]
				try:
					if(label_list[int(char.label)]in ['\'',',']):
						char2=w.char_list[c+1]
						if(label_list[int(char2.label)]in ['\'',',']):
							string=string+'\"'
							c+=1
						else:
							string=string+label_list[int(char.label)]
					elif(label_list[int(char.label)]in ['െ','േ','്ര']):
						char2=w.char_list[c+1]
						if(label_list[int(char2.label)]in ['െ','്ര']):
							char3=w.char_list[c+2]
							string=string+label_list[int(char3.label)]
							c+=1
						string=string+label_list[int(char2.label)]
						string=string+label_list[int(char.label)]
						c+=1
					else:
						string=string+label_list[int(char.label)]
				except IndexError:
					string=string+label_list[int(char.label)]
				# cv2.imwrite('output/zcline_'+str(i)+'_word_'+str(j)+'_c_'+str(k)+str(int(w.char_list[c].label))+'.png',w.char_list[c].data)
				k+=1
				c+=1
		i+=1
	return string
url = sys.argv[1]
print 'opening file: '+url
# print "working"
# url='Example/news_paper.png'
img=cv2.imread(url,0)
# cv2.imshow("img",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
if(img==None):
	print url+' does\'nt exist'
	exit()
img = pp.preprocess(img)
im=img
# im,rot = pp.skew_correction(img)
# print "working after between \n"
# cv2.imshow("img",im)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite('temp/'+str(random.randint(0,9))+'input.png',im)
print recognize_block(im)
# print "working after"
