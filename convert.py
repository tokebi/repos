#!/usr/bin/python
# -*- coding: sjis -*-

import codecs
import json
import math
import os.path
import xlrd
import sys

LSKILL_COMMENT	= "E9"
SKILL1_COMMENT	= "E10"
SKILL2_COMMENT	= "E11"
SKILL3_COMMENT	= "E12"
SKILL4_COMMENT	= "E13"
DUMMY			= "E14"
DUMMY			= "E15"
DUMMY			= "E16"
MONSTER_KIND	= "E17"
KIND_MONSTER	= 18
KAKU_MONSTER	= "E19"
KIND_ATTACK		= "E20"
DUMMY			= "E21"
SKILL1_NO		= "E22"
SKILL2_NO		= "E23"
SKILL3_NO		= "E24"
SKILL4_NO		= "E25"
LSKILL_NO		= "E26"
DUMMY			= "E27"
SKILL1_NAME		= "E28"
SKILL2_NAME		= "E29"
SKILL3_NAME		= "E30"
SKILL4_NAME		= "E31"
DUMMY			= "E32"
SKILL1_MAXLV	= "E33"
SKILL2_MAXLV	= "E34"
SKILL3_MAXLV	= "E35"
SKILL4_MAXLV	= "E36"
LSKILL_RATE		= 0
SKILL1_RATE		= "E39"
SKILL2_RATE		= "E40"
SKILL3_RATE		= "E41"
SKILL4_RATE		= "E42"
LSKILL_NUM		= 0
SKILL1_NUM		= 1
SKILL2_NUM		= 1
SKILL3_NUM		= 1
SKILL4_NUM		= 1
LSKILL_USEMIN	= 0
SKILL1_USEMIN	= "E47"
SKILL2_USEMIN	= "E48"
SKILL3_USEMIN	= "E49"
SKILL4_USEMIN	= "E50"
LSKILL_USEMAX	= 0
SKILL1_USEMAX	= "E43"
SKILL2_USEMAX	= "E44"
SKILL3_USEMAX	= "E45"
SKILL4_USEMAX	= "E46"

def getCellNum(row, cellnum, defval):
	ret = ""
	if isinstance(cellnum, str) and cellnum[:1] == "E":
		try:
			ret = inb.cell(row, int(cellnum[1:])).value
		except:
			ret = ""
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
		#print("出力対象" + skillno)
		if skillno in skill_ids:
			# 既に同じ名前のスキルがあったら
			skill_ids[skillno] += 1
			#print("重複:" + skillno)
		else:
			#print("出力" + skillno)
			skill_ids[skillno] = 1
			outf.write('			"' + skillno + '" :{' + "\n")
			outf.write('				"name":"' + name +'"' + "\n")			# スキル名
			outf.write('				,"comment":"' + comment + '"' + "\n")	# スキル詳細
			outf.write('				,"rate":"' + rate + '"' + "\n")			# 倍率
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
outf.write('	#' + "\n")
outf.write('	# スキルハッシュを返す' + "\n")
outf.write('	#' + "\n")
outf.write('	def getMap(self):' + "\n")
outf.write('		return {' + "\n")
skill_ids = {}

for row in range(2, maxrow):
	#print("row=" + str(row))
	outf.write('			#' + inb.cell(row, KIND_MONSTER).value +',' + "\n")
	#                skillno,       name   , comment       , rate       , num       , usemin       , usemax       , lvmax
	outputSkill(row, LSKILL_NO, ""         , LSKILL_COMMENT, 0          , 0         , 0            , 0            , 1)
	outputSkill(row, SKILL1_NO, SKILL1_NAME, SKILL1_COMMENT, SKILL1_RATE, SKILL1_NUM, SKILL1_USEMIN, SKILL1_USEMAX, SKILL1_MAXLV)
	outputSkill(row, SKILL2_NO, SKILL2_NAME, SKILL2_COMMENT, SKILL2_RATE, SKILL2_NUM, SKILL2_USEMIN, SKILL2_USEMAX, SKILL2_MAXLV)
	outputSkill(row, SKILL3_NO, SKILL3_NAME, SKILL3_COMMENT, SKILL3_RATE, SKILL3_NUM, SKILL3_USEMIN, SKILL3_USEMAX, SKILL3_MAXLV)
	outputSkill(row, SKILL4_NO, SKILL4_NAME, SKILL4_COMMENT, SKILL4_RATE, SKILL4_NUM, SKILL4_USEMIN, SKILL4_USEMAX, SKILL4_MAXLV)
outf.write('		}' +"\n")
#inf.close()
sys.exit()

