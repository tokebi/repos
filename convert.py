#!/usr/bin/python
# -*- coding: sjis -*-

import codecs
import json
import math
import os.path

# sw_dra/xlsm�́u�����X�^�[�v�V�[�g
inf = open("txt.txt", "r")
#outf = open("out.tsv", "w")
outf = open("swSkill.py", "w")

outf.write('#!/usr/bin/python' + "\n")
outf.write('# -*- coding: sjis -*-' + "\n")
outf.write('' + "\n")
outf.write('class SwSkill:' + "\n")
outf.write('	def getSkillsMap(self):' + "\n")
outf.write('		return {' + "\n")
skill_ids = {}
for line in inf:
	itemList = line[:-1].split('\t')
	nameList = itemList[0].split("�E")
	name = nameList[0]
	if len(nameList) == 2:
		name = nameList[1] + nameList[0]
	if name == "���O":
		continue;
	#outf.write(name  + "\t")	# ���O
	#outf.write(itemList[9]  + "\t")	# ���[�_�X�L��
	#outf.write(itemList[10] + "\t")	# �X�L���P
	#outf.write(itemList[11] + "\t")	# �X�L���Q
	#outf.write(itemList[12] + "\t")	# �X�L���R
	#outf.write(itemList[19] + "\t")	# �X�L���Pno
	#outf.write(itemList[20] + "\t")	# �X�L���Qno
	#outf.write(itemList[21] + "\t")	# �X�L���Rno
	outf.write('			#' + itemList[18] +',' + "\n")
	if itemList[23] != "":
		if itemList[23] in skill_ids:
			# ���ɓ������O�̃����X�^�[��������
			skill_ids[itemList[23]] += 1
			#print("�d��:" + itemList[23])
		else:
			skill_ids[itemList[23]] = 1
			outf.write('			"' + itemList[23] + '" :{' + "\n")
			outf.write('				"name":"' + '"' + "\n") # ���[�_�X�L����
			outf.write('				,"comment":"' + itemList[9] + '"' + "\n")
			outf.write('				,"rate":' + '0' + ' # �{��' + "\n")
			outf.write('				,"num":'  + '0' + '     # �U����' + "\n")
			outf.write('				,"usemin:":' + '0' + "\n")
			outf.write('				,"usemax":'  + '0' + "\n")
			outf.write('				,"lvmax":'  + '0' "\n")
			outf.write('			},' + "\n")
	if itemList[19] != "":
		if itemList[19] in skill_ids:
			# ���ɓ������O�̃����X�^�[��������
			skill_ids[itemList[19]] += 1
			print("�d��:" + itemList[19])
		else:
			skill_ids[itemList[19]] = 1
			outf.write('			"' + itemList[19] + '" :{' + "\n")
			outf.write('				"name":"' + itemList[25] +'"' + "\n") # �X�L���P��
			outf.write('				,"comment":"' + itemList[10] + '"' + "\n")
			outf.write('				,"rate":' + '1' + ' # �{��' + "\n")
			outf.write('				,"num":'  + '1' + '     # �U����' + "\n")
			outf.write('				,"usemin:":' + '1' + "\n")
			outf.write('				,"usemax":'  + '1' + "\n")
			outf.write('				,"lvmax":"'  + itemList[30] + '"' + "\n")
			outf.write('			},' + "\n")
	if itemList[20] != "":
		if itemList[20] in skill_ids:
			# ���ɓ������O�̃����X�^�[��������
			skill_ids[itemList[20]] += 1
			print("�d��:" + itemList[20])
		else:
			skill_ids[itemList[20]] = 1
			outf.write('			"' + itemList[20] + '" :{' + "\n")
			outf.write('				"name":"' + itemList[26] +'"' + "\n") # �X�L���Q��
			outf.write('				,"comment":"' + itemList[11] + '"' + "\n")
			outf.write('				,"rate":' + '1' + ' # �{��' + "\n")
			outf.write('				,"num":'  + '1' + '     # �U����' + "\n")
			outf.write('				,"usemin:":' + '1' + "\n")
			outf.write('				,"usemax":'  + '1' + "\n")
			outf.write('				,"lvmax":"'  + itemList[31] + '"' + "\n")
			outf.write('			},' + "\n")
	if itemList[21] != "":
		if itemList[21] in skill_ids:
			# ���ɓ������O�̃����X�^�[��������
			skill_ids[itemList[21]] += 1
			print("�d��:" + itemList[21])
		else:
			skill_ids[itemList[21]] = 1
			outf.write('			"' + itemList[21] + '" :{' + "\n")
			outf.write('				"name":"' + itemList[27] +'"' + "\n") # �X�L���R��
			outf.write('				,"comment":"' + itemList[12] + '"' + "\n")
			outf.write('				,"rate":' + '1' + ' # �{��' + "\n")
			outf.write('				,"num":'  + '1' + '     # �U����' + "\n")
			outf.write('				,"usemin:":' + '1' + "\n")
			outf.write('				,"usemax":'  + '1' + "\n")
			outf.write('				,"lvmax":"'  + itemList[32] + '"' + "\n")
			outf.write('			},' + "\n")
	if itemList[22] != "":
		if itemList[22] in skill_ids:
			# ���ɓ������O�̃����X�^�[��������
			skill_ids[itemList[22]] += 1
			print("�d��:" + itemList[22])
		else:
			skill_ids[itemList[22]] = 1
			outf.write('			"' + itemList[22] + '" :{' + "\n")
			outf.write('				"name":"' + itemList[28] +'"' + "\n") # �X�L���S��
			outf.write('				,"comment":"' + '"' + "\n")
			outf.write('				,"rate":' + '1' + ' # �{��' + "\n")
			outf.write('				,"num":'  + '1' + '     # �U����' + "\n")
			outf.write('				,"usemin:":' + '1' + "\n")
			outf.write('				,"usemax":'  + '1' + "\n")
			outf.write('				,"lvmax":"'  + itemList[33] + '"' + "\n")
			outf.write('			},' + "\n")
outf.write('		}' +"\n")
inf.close()

