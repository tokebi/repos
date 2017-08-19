#!/usr/bin/python
# -*- coding: sjis -*-

import codecs
import json
import math
import os.path
import xlrd
import sys

class ConvertSkill:
	#LSKILL_COMMENT	= "E9"
	SKILL1_COMMENT	= "E11"
	SKILL2_COMMENT	= "E12"
	SKILL3_COMMENT	= "E13"
	SKILL4_COMMENT	= "E14"
	#DUMMY			= "E14"
	#DUMMY			= "E15"
	#DUMMY			= "E16"
	#MONSTER_KIND	= "E17"
	KIND_MONSTER	= 1
	#KAKU_MONSTER	= "E19"
	#KIND_ATTACK		= "E20"
	#DUMMY			= "E21"
	SKILL1_NO		= "E19"
	SKILL2_NO		= "E20"
	SKILL3_NO		= "E21"
	SKILL4_NO		= "E22"
	#LSKILL_NO		= "E26"
	#DUMMY			= "E27"
	SKILL1_NAME		= "E24"
	SKILL2_NAME		= "E25"
	SKILL3_NAME		= "E26"
	SKILL4_NAME		= "E27"
	#DUMMY			= "E28"
	SKILL1_MAXLV	= "E29"
	SKILL2_MAXLV	= "E30"
	SKILL3_MAXLV	= "E31"
	SKILL4_MAXLV	= "E32"
	#LSKILL_RATE		= 0
	SKILL1_RATE		= "E34"
	SKILL2_RATE		= "E35"
	SKILL3_RATE		= "E36"
	SKILL4_RATE		= "E37"
	#LSKILL_NUM		= 0
	SKILL1_NUM		= 1
	SKILL2_NUM		= 1
	SKILL3_NUM		= 1
	SKILL4_NUM		= 1
	#LSKILL_USEMAX	= 0
	SKILL1_USEMAX	= "E38"
	SKILL2_USEMAX	= "E39"
	SKILL3_USEMAX	= "E40"
	SKILL4_USEMAX	= "E41"
	#LSKILL_USEMIN	= 0
	SKILL1_USEMIN	= "E42"
	SKILL2_USEMIN	= "E43"
	SKILL3_USEMIN	= "E44"
	SKILL4_USEMIN	= "E45"

	def getCellNum(self, row, cellnum, defval):
		ret = ""
		if isinstance(cellnum, str) and cellnum[:1] == "E":
			try:
				ret = self.inb.cell(row, int(cellnum[1:])).value
			except:
				ret = ""
			if not isinstance(ret, str):
				ret = str(int(self.inb.cell(row, int(cellnum[1:])).value))
			#if cellnum == self.LSKILL_NO:
			#	ret = "L" + ret
		else:
			ret = str(cellnum)
		if ret == "":
			ret = defval
		#print(str(cellnum) + "=" + str(ret))
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
		#sys.exit()
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
				self.outf.write('				,"ryaku":"' + self.getRyaku(comment) + '"' + "\n")	# スキル略称
				self.outf.write('				,"rate":"' + rate + '"' + "\n")			# 倍率
				self.outf.write('				,"num":'  + num + "\n")					# 攻撃回数
				self.outf.write('				,"usemin:":' + usemin + "\n")			# 再利用最小
				self.outf.write('				,"usemax":'  + usemax + "\n")			# 再利用最大
				self.outf.write('				,"lvmax":'  + lvmax + "\n")				# レベルＭＡＸ
				self.outf.write('			},' + "\n")

	def getRyaku(self, comment):
		ryaku = ""
		
		ryaku = ryaku + self.RyakuTikan(comment, '1ターン', "1T")
		ryaku = ryaku + self.RyakuTikan(comment, '2ターン', "2T")
		ryaku = ryaku + self.RyakuTikan(comment, '3ターン', "3T")
	
		ryaku = ryaku + self.RyakuTikan(comment, '持続的にダメージ', "持続")
		ryaku = ryaku + self.RyakuTikan(comment, 'ミス発生率を高め', "ミス")
		ryaku = ryaku + self.RyakuTikan(comment, '攻撃力を強化'    , "攻↑")
		ryaku = ryaku + self.RyakuTikan(comment, '気絶'            , "気絶")
		ryaku = ryaku + self.RyakuTikan(comment, '15％ずつ回復'    , "全15%回復")
		
		ryaku = ryaku + self.RyakuTikan(comment, '18％', "18%")
		ryaku = ryaku + self.RyakuTikan(comment, '24％', "24%")
		ryaku = ryaku + self.RyakuTikan(comment, '50％', "50%")
		ryaku = ryaku + self.RyakuTikan(comment, '75％', "75%")
		ryaku = ryaku + self.RyakuTikan(comment, '80％', "80%")
		return ryaku

	def RyakuTikan(self, comment, moto, saki):
		ret = ""
		if comment.find(moto) > -1:
			ret = saki
		return ret

	def __init__(self):
		self.outf = open("../swSkillMaster.py", "w")
		self.inb = book.sheet_by_name('モンスター')
		self.skill_ids = {}

	def main(self, book):
		# 最終行を取得
		maxrow = self.inb.nrows

		self.outf.write('#!/usr/bin/python' + "\n")
		self.outf.write('# -*- coding: sjis -*-' + "\n")
		self.outf.write('' + "\n")
		self.outf.write('class SwSkillMaster:' + "\n")
		self.outf.write('	#' + "\n")
		self.outf.write('	# スキルハッシュを返す' + "\n")
		self.outf.write('	#' + "\n")
		self.outf.write('	def getMap(self):' + "\n")
		self.outf.write('		return {' + "\n")

		for row in range(2, maxrow):
			self.outf.write('			#' + self.inb.cell(row, self.KIND_MONSTER).value +',' + "\n")
			#                skillno,       name             , comment            , rate            , num            , usemin            , usemax            , lvmax
			#self.outputSkill(row, self.LSKILL_NO, ""              , self.LSKILL_COMMENT, 0               , 0              , 0                 , 0                 , 1)
			self.outputSkill(row, self.SKILL1_NO, self.SKILL1_NAME, self.SKILL1_COMMENT, self.SKILL1_RATE, self.SKILL1_NUM, self.SKILL1_USEMIN, self.SKILL1_USEMAX, self.SKILL1_MAXLV)
			self.outputSkill(row, self.SKILL2_NO, self.SKILL2_NAME, self.SKILL2_COMMENT, self.SKILL2_RATE, self.SKILL2_NUM, self.SKILL2_USEMIN, self.SKILL2_USEMAX, self.SKILL2_MAXLV)
			self.outputSkill(row, self.SKILL3_NO, self.SKILL3_NAME, self.SKILL3_COMMENT, self.SKILL3_RATE, self.SKILL3_NUM, self.SKILL3_USEMIN, self.SKILL3_USEMAX, self.SKILL3_MAXLV)
			self.outputSkill(row, self.SKILL4_NO, self.SKILL4_NAME, self.SKILL4_COMMENT, self.SKILL4_RATE, self.SKILL4_NUM, self.SKILL4_USEMIN, self.SKILL4_USEMAX, self.SKILL4_MAXLV)
		self.outf.write('		}' +"\n")
		self.outf.close()

class ConvertMonster:
	MONSTER_ID      = 0
	KIND_MONSTER	= 1
	KAKU_MONSTER	= 2
	KIND_ATTACK		= 5
	LSKILL_COMMENT	= 10
	BASE_STAR		= 51
	BASE_CON		= 52
	BASE_ATK		= 53
	BASE_DEF		= 54
	BASE_SPD		= 55
	BASE_CRI		= 56
	BASE_DMG		= 57
	BASE_TEK		= 58
	BASE_TEI		= 59

	def __init__(self):
		self.outf = open("../swMonstersName.py", "w")
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

		lines = []
		for row in range(2, maxrow):
			if self.inb.cell(row, self.MONSTER_ID).value == "":
				continue
			id    = str(int(self.inb.cell(row, self.MONSTER_ID).value))
			name  = self.inb.cell(row, self.KIND_MONSTER).value
			kname = self.inb.cell(row, self.KAKU_MONSTER).value
			kind  = self.inb.cell(row, self.KIND_ATTACK).value
			lskill= self.inb.cell(row, self.LSKILL_COMMENT).value
			baseStar= self.inb.cell(row, self.BASE_STAR).value
			baseCon = self.inb.cell(row, self.BASE_CON).value
			baseAtk = self.inb.cell(row, self.BASE_ATK).value
			baseDef = self.inb.cell(row, self.BASE_DEF).value
			baseSpd = self.inb.cell(row, self.BASE_SPD).value
			baseCri = self.inb.cell(row, self.BASE_CRI).value
			baseDmg = self.inb.cell(row, self.BASE_DMG).value
			baseTek = self.inb.cell(row, self.BASE_TEK).value
			baseTei = self.inb.cell(row, self.BASE_TEI).value
			monster = Monster(baseCon*15, baseAtk, baseDef, baseStar)
			
			if not isinstance(lskill, str):
				lskill = ""
			try:
				#10101: ["フェアリー(水)","エルーシャ","サポート系"],
				line = "			"
				line = line + id + ": {" + "\n"
				line = line + '				"name":"'  + name  + '"' + "\n"
				line = line + '				,"kname":"' + kname + '"' + "\n"
				line = line + '				,"kind":"'  + kind  + '"' + "\n"
				line = line + '				,"lskill":"'  + lskill + '"' + "\n"
				line = line + '				,"con":'  + str(monster.calculate_actual_stat(baseCon)*15) + '' + "\n"
				line = line + '				,"atk":'  + str(monster.calculate_actual_stat(baseAtk)) + '' + "\n"
				line = line + '				,"def":'  + str(monster.calculate_actual_stat(baseDef)) + '' + "\n"
				line = line + '				,"spd":'  + str(int(baseSpd)) + '' + "\n"
				line = line + '				,"cri":'  + str(int(baseCri)) + '' + "\n"
				line = line + '				,"dmg":'  + str(int(baseDmg)) + '' + "\n"
				line = line + '				,"tek":'  + str(int(baseTek)) + '' + "\n"
				line = line + '				,"tei":'  + str(int(baseTei)) + '' + "\n"
				
				line = line + '			},'
				lines.append(line)
			except:
				print("変換エラー：id=" + id )
				import traceback
				traceback.print_exc()
				import sys
				sys.exit()
		#for line in sorted(lines):
		for line in lines:
			self.outf.write(line +"\n")
		self.outf.write('		}' +"\n")
		self.outf.close()
	
class Monster:
	def __init__(self, base_hp, base_attack, base_defense, base_stars):
		self.base_hp      = base_hp
		self.base_attack  = base_attack
		self.base_defense = base_defense
		self.base_stars   = base_stars
	#
	# _calculate_actual_statを呼び出すラッパー
	#
	def calculate_actual_stat(self, stat):
		return self._calculate_actual_stat(stat, 6, 40)
	#
	# header.models.pyの180行目の関数をそのまま移植
	#
	def _calculate_actual_stat(self, stat, grade, level):
		max_lvl = 10 + grade * 5
		
		weight = float(self.base_hp / 15 + self.base_attack + self.base_defense)
		base_value = round((stat * (105 + 15 * self.base_stars)) / weight, 0)
		
		# Magic multipliers taken from summoner's war wikia calculator. Used to calculate stats for lvl 1 and lvl MAX
		magic_multipliers = [
			{'1': 1.0, 'max': 1.9958},
			{'1': 1.5966, 'max': 3.03050646},
			{'1': 2.4242774, 'max': 4.364426603},
			{'1': 3.4914444, 'max': 5.941390935},
			{'1': 4.7529032, 'max': 8.072330795},
			{'1': 6.4582449, 'max': 10.97901633},
		]
		
		stat_lvl_1 = round(base_value * magic_multipliers[grade - 1]['1'], 0)
		stat_lvl_max = round(base_value * magic_multipliers[grade - 1]['max'], 0)
		
		if level == 1:
			return int(stat_lvl_1)
		elif level == max_lvl:
			return int(stat_lvl_max)
		else:
			# Use exponential function in format value=ae^(bx)
			# a=stat_lvl_1*e^(-b)
			from math import log, exp
			b_coeff = log(stat_lvl_max / stat_lvl_1) / (max_lvl - 1)
			
			return int(round((stat_lvl_1 * exp(-b_coeff)) * exp(b_coeff * level)))

if __name__ == "__main__":
	# sw_dra/xlsmの「モンスター」シート
	book = xlrd.open_workbook('C:\\Users\\hhara\\OneDrive\\sw_dra.xlsm')
	a = ConvertSkill()
	a.main(book)
	b = ConvertMonster()
	b.main(book)