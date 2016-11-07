#!/usr/bin/python
# -*- coding: sjis -*-

import codecs
import json
import math
import os.path
import xlrd
import sys

ROW_LSKILL_COMMENT	= "E9"
ROW_SKILL1_COMMENT	= "E10"
ROW_SKILL2_COMMENT	= "E11"
ROW_SKILL3_COMMENT	= "E12"
ROW_SKILL4_COMMENT	= "E13"
ROW_MONSTER_KIND	= "E17"
ROW_KIND_MONSTER	= 18
ROW_SKILL1_NO		= "E19"
ROW_SKILL2_NO		= "E20"
ROW_SKILL3_NO		= "E21"
ROW_SKILL4_NO		= "E22"
ROW_LSKILL_NO		= "E23"
ROW_SKILL1_NAME		= "E25"
ROW_SKILL2_NAME		= "E26"
ROW_SKILL3_NAME		= "E27"
ROW_SKILL4_NAME		= "E28"
ROW_SKILL1_MAXLV	= "E30"
ROW_SKILL2_MAXLV	= "E31"
ROW_SKILL3_MAXLV	= "E32"
ROW_SKILL4_MAXLV	= "E33"
ROW_LSKILL_RATE		= 0
ROW_SKILL1_RATE		= 1
ROW_SKILL2_RATE		= 1
ROW_SKILL3_RATE		= 1
ROW_SKILL4_RATE		= 1
ROW_LSKILL_NUM		= 0
ROW_SKILL1_NUM		= 1
ROW_SKILL2_NUM		= 1
ROW_SKILL3_NUM		= 1
ROW_SKILL4_NUM		= 1
ROW_LSKILL_USEMIN	= 0
ROW_SKILL1_USEMIN	= 1
ROW_SKILL2_USEMIN	= 1
ROW_SKILL3_USEMIN	= 1
ROW_SKILL4_USEMIN	= 1
ROW_LSKILL_USEMAX	= 0
ROW_SKILL1_USEMAX	= 1
ROW_SKILL2_USEMAX	= 1
ROW_SKILL3_USEMAX	= 1
ROW_SKILL4_USEMAX	= 1

def getCellNum(row, cellnum, defval):
	ret = ""
	if isinstance(cellnum, str) and cellnum[:1] == "E":
		ret = inb.cell(row, int(cellnum[1:])).value
		if not isinstance(ret, str):
			ret = str(int(inb.cell(row, int(cellnum[1:])).value))
	else:
		ret = str(cellnum)
	if ret == "":
		ret = defval
	return ret

def outputSkill(row, skillno_in, name_in, comment_in, rate_in, num_in, usemin_in, usemax_in, lvmax_in):
	skillno		= getCellNum(row, skillno_in, "")
	name		= getCellNum(row, name_in, "")
	comment		= getCellNum(row, comment_in, "1")
	rate		= getCellNum(row, rate_in, "1")
	num			= getCellNum(row, num_in, "1")
	usemin		= getCellNum(row, usemin_in, "1")
	usemax		= getCellNum(row, usemax_in, "1")
	lvmax		= getCellNum(row, lvmax_in, "9999")
	
	if skillno != "":
		if skillno in skill_ids:
			# 既に同じ名前のスキルがあったら
			skill_ids[skillno] += 1
			#print("重複:" + itemList[23])
		else:
			skill_ids[skillno] = 1
			outf.write('			"' + skillno + '" :{' + "\n")
			outf.write('				"name":"' + name +'"' + "\n")			# スキル名
			outf.write('				,"comment":"' + comment + '"' + "\n")	# スキル詳細
			outf.write('				,"rate":' + rate + "\n")				# 倍率
			outf.write('				,"num":'  + num + "\n")					# 攻撃回数
			outf.write('				,"usemin:":' + usemin + "\n")			# 再利用最小
			outf.write('				,"usemax":'  + usemax + "\n")			# 再利用最大
			outf.write('				,"lvmax":'  + lvmax + "\n")				# レベルＭＡＸ
			outf.write('			},' + "\n")

# sw_dra/xlsmの「モンスター」シート
book = xlrd.open_workbook('C:\\Users\\hhara\\OneDrive\\sw_dra.xlsm')
inb = book.sheet_by_name('モンスター')
# 最終行を取得
maxrow = inb.nrows

#inf = open("txt.txt", "r")
#outf = open("out.tsv", "w")
outf = open("swSkill.py", "w")

outf.write('#!/usr/bin/python' + "\n")
outf.write('# -*- coding: sjis -*-' + "\n")
outf.write('' + "\n")
outf.write('class SwSkill:' + "\n")
outf.write('	def getSkillsMap(self):' + "\n")
outf.write('		return {' + "\n")
skill_ids = {}
#for line in inf:
for row in range(2, maxrow):
	#itemList = line[:-1].split('\t')
	#nameList = itemList[0].split("・")
	#name = nameList[0]
	#if len(nameList) == 2:
	#	name = nameList[1] + nameList[0]
	#if name == "名前":
	#	continue;
	#outf.write(name  + "\t")	# 名前
	#outf.write(itemList[9]  + "\t")	# リーダスキル
	#outf.write(itemList[10] + "\t")	# スキル１
	#outf.write(itemList[11] + "\t")	# スキル２
	#outf.write(itemList[12] + "\t")	# スキル３
	#outf.write(itemList[19] + "\t")	# スキル１no
	#outf.write(itemList[20] + "\t")	# スキル２no
	#outf.write(itemList[21] + "\t")	# スキル３no
	#print("row=" + str(row))
	outf.write('			#' + inb.cell(row, ROW_KIND_MONSTER).value +',' + "\n")
	#                skillno,       name             comment           , rate           , num           , usemin           , usemax           , lvmax
	outputSkill(row, ROW_LSKILL_NO, ""             , ROW_LSKILL_COMMENT, ROW_LSKILL_RATE, ROW_LSKILL_NUM, ROW_LSKILL_USEMIN, ROW_LSKILL_USEMAX, 1)
	outputSkill(row, ROW_SKILL1_NO, ROW_SKILL1_NAME, ROW_SKILL1_COMMENT, ROW_SKILL1_RATE, ROW_SKILL1_NUM, ROW_SKILL1_USEMIN, ROW_SKILL1_USEMAX, ROW_SKILL1_MAXLV)
	outputSkill(row, ROW_SKILL2_NO, ROW_SKILL2_NAME, ROW_SKILL2_COMMENT, ROW_SKILL2_RATE, ROW_SKILL2_NUM, ROW_SKILL2_USEMIN, ROW_SKILL2_USEMAX, ROW_SKILL2_MAXLV)
	outputSkill(row, ROW_SKILL3_NO, ROW_SKILL3_NAME, ROW_SKILL3_COMMENT, ROW_SKILL3_RATE, ROW_SKILL3_NUM, ROW_SKILL3_USEMIN, ROW_SKILL3_USEMAX, ROW_SKILL3_MAXLV)
	outputSkill(row, ROW_SKILL4_NO, ROW_SKILL4_NAME, ROW_SKILL4_COMMENT, ROW_SKILL4_RATE, ROW_SKILL4_NUM, ROW_SKILL4_USEMIN, ROW_SKILL4_USEMAX, ROW_SKILL4_MAXLV)
outf.write('		}' +"\n")
#inf.close()
sys.exit()

