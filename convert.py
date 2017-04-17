#!/usr/bin/python
# -*- coding: sjis -*-

import codecs
import json
import math
import os.path
import xlrd
import sys

class ConvertSkill:
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

	def getCellNum(self, row, cellnum, defval):
		ret = ""
		if isinstance(cellnum, str) and cellnum[:1] == "E":
			try:
				ret = self.inb.cell(row, int(cellnum[1:])).value
			except:
				ret = ""
			if not isinstance(ret, str):
				ret = str(int(self.inb.cell(row, int(cellnum[1:])).value))
			if cellnum == self.LSKILL_NO:
				ret = "L" + ret
		else:
			ret = str(cellnum)
		if ret == "":
			ret = defval
		return ret

	def outputSkill(self, row, skillno_in, name_in, comment_in, rate_in, num_in, usemin_in, usemax_in, lvmax_in):
		skillno		= self.getCellNum(row, skillno_in, "")
		name		= self.getCellNum(row, name_in, "")
		comment		= self.getCellNum(row, comment_in, "")
		rate		= self.getCellNum(row, rate_in, "")
		num			= self.getCellNum(row, num_in, "1")
		usemin		= self.getCellNum(row, usemin_in, "1")
		usemax		= self.getCellNum(row, usemax_in, "1")
		lvmax		= self.getCellNum(row, lvmax_in, "9999")
		
		if skillno != "":
			#print("出力対象" + skillno)
			if skillno in self.skill_ids:
				# 既に同じ名前のスキルがあったら
				self.skill_ids[skillno] += 1
				#print("重複:" + skillno)
			else:
				#print("出力" + skillno)
				self.skill_ids[skillno] = 1
				self.outf.write('			"' + skillno + '" :{' + "\n")
				self.outf.write('				"name":"' + name +'"' + "\n")			# スキル名
				self.outf.write('				,"comment":"' + comment + '"' + "\n")	# スキル詳細
				self.outf.write('				,"rate":"' + rate + '"' + "\n")			# 倍率
				self.outf.write('				,"num":'  + num + "\n")					# 攻撃回数
				self.outf.write('				,"usemin:":' + usemin + "\n")			# 再利用最小
				self.outf.write('				,"usemax":'  + usemax + "\n")			# 再利用最大
				self.outf.write('				,"lvmax":'  + lvmax + "\n")				# レベルＭＡＸ
				self.outf.write('			},' + "\n")

	def __init__(self):
		self.outf = open("swSkill.py", "w")
		self.inb = book.sheet_by_name('モンスター')
		self.skill_ids = {}

	def main(self, book):
		# 最終行を取得
		maxrow = self.inb.nrows

		self.outf.write('#!/usr/bin/python' + "\n")
		self.outf.write('# -*- coding: sjis -*-' + "\n")
		self.outf.write('' + "\n")
		self.outf.write('class SwSkill:' + "\n")
		self.outf.write('	#' + "\n")
		self.outf.write('	# スキルハッシュを返す' + "\n")
		self.outf.write('	#' + "\n")
		self.outf.write('	def getMap(self):' + "\n")
		self.outf.write('		return {' + "\n")

		for row in range(2, maxrow):
			self.outf.write('			#' + self.inb.cell(row, self.KIND_MONSTER).value +',' + "\n")
			#                skillno,       name             , comment            , rate            , num            , usemin            , usemax            , lvmax
			self.outputSkill(row, self.LSKILL_NO, ""              , self.LSKILL_COMMENT, 0               , 0              , 0                 , 0                 , 1)
			self.outputSkill(row, self.SKILL1_NO, self.SKILL1_NAME, self.SKILL1_COMMENT, self.SKILL1_RATE, self.SKILL1_NUM, self.SKILL1_USEMIN, self.SKILL1_USEMAX, self.SKILL1_MAXLV)
			self.outputSkill(row, self.SKILL2_NO, self.SKILL2_NAME, self.SKILL2_COMMENT, self.SKILL2_RATE, self.SKILL2_NUM, self.SKILL2_USEMIN, self.SKILL2_USEMAX, self.SKILL2_MAXLV)
			self.outputSkill(row, self.SKILL3_NO, self.SKILL3_NAME, self.SKILL3_COMMENT, self.SKILL3_RATE, self.SKILL3_NUM, self.SKILL3_USEMIN, self.SKILL3_USEMAX, self.SKILL3_MAXLV)
			self.outputSkill(row, self.SKILL4_NO, self.SKILL4_NAME, self.SKILL4_COMMENT, self.SKILL4_RATE, self.SKILL4_NUM, self.SKILL4_USEMIN, self.SKILL4_USEMAX, self.SKILL4_MAXLV)
		self.outf.write('		}' +"\n")
		self.outf.close()

class ConvertMonster:
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
	KAKU_MONSTER	= 19
	KIND_ATTACK		= 20
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
	MONSTER_ID		= 38
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

	def __init__(self):
		self.outf = open("swMonstersName.py", "w")
		self.inb = book.sheet_by_name('モンスター')
		self.skill_ids = {}

	def main(self, book):
		# 最終行を取得
		maxrow = self.inb.nrows

		self.outf.write('#!/usr/bin/python' + "\n")
		self.outf.write('# -*- coding: sjis -*-' + "\n")
		self.outf.write('' + "\n")
		self.outf.write('class SwMonstersName:' + "\n")
		self.outf.write('	#' + "\n")
		self.outf.write('	# モンスターの日本語名のハッシュを返す' + "\n")
		self.outf.write('	#' + "\n")
		self.outf.write('	def getMap(self):' + "\n")
		self.outf.write('		return {' + "\n")
		self.outf.write('#pythonソース' + "\n")

		lines = []
		for row in range(2, maxrow):
			if self.inb.cell(row, self.MONSTER_ID).value == "":
				continue
			id    = str(int(self.inb.cell(row, self.MONSTER_ID).value))
			name  = self.inb.cell(row, self.KIND_MONSTER).value
			kname = self.inb.cell(row, self.KAKU_MONSTER).value
			kind  = self.inb.cell(row, self.KIND_ATTACK).value
			
			try:
				#10101: ["フェアリー(水)","エルーシャ","サポート系"],
				line = "			"
				line = line + id + ": "
				line = line + '["' + name
				line = line + '","' + kname
				line = line + '","' + kind
				line = line + '"],'
				lines.append(line)
			except:
				print("変換エラー：id=" + id )
		for line in sorted(lines):
			self.outf.write(line +"\n")
		self.outf.write('		}' +"\n")
		self.outf.close()
	
if __name__ == "__main__":
	# sw_dra/xlsmの「モンスター」シート
	book = xlrd.open_workbook('C:\\Users\\hhara\\OneDrive\\sw_dra.xlsm')
	a = ConvertSkill()
	a.main(book)
	b = ConvertMonster()
	b.main(book)