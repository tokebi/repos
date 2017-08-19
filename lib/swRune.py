#!/usr/bin/python
# -*- coding: sjis -*-

import math

from lib.swMaster import SwMaster

class SwRune():
	def __init__(self, rune):
		self.__mst = SwMaster.getInstance()
		self.__data = {}
		for k, v in rune.items():   # for/if文では文末のコロン「:」を忘れないように
			if k in {
				"base_value"
				,"class"
				,"extra"
				,"occupied_id"
				,"occupied_type"
				,"prefix_eff"
				,"pri_eff"
				,"rank"
				,"rune_id"
				,"sec_eff"
				,"sell_value"
				,"set_id"
				,"slot_no"
				,"upgrade_curr"
				,"upgrade_limit"
				,"wizard_id"
			}:
				self.__data[k] = rune[k]
			else:
				print(k)
				sys.exit()
		self.__data["unit_id"] = ""
		self.__data["unit_master_id"] = ""
		self.__data["reaDo"] = 0

	#
	# 星を返す
	#
	def getClass(self):
		return self.__data["class"]

	#
	# サブオプを返す
	#
	def getPrefixEff(self):
		return self.__data["prefix_eff"]

	#
	# メインオプを返す
	#
	def getPriEff(self):
		return self.__data["pri_eff"]

	#
	# IDを取得
	#
	def getRuneId(self):
		return self.__data['rune_id']

	#
	# 強化数を返す
	#
	def getSecEff(self):
		return self.__data["sec_eff"]

	#
	# 売値を返す
	#
	def getSellValue(self):
		return self.__data["sell_value"]

	#
	# ルーンのセット名称を返す
	#
	def getRuneSetName(self):
		return self.__mst.getRuneSetName(self.__data['set_id'])

	#
	# 装備スロットを取得
	#
	def getSlotNo(self):
		return self.__data['slot_no']

	#
	# 強化数を返す
	#
	def getUpgradeCurr(self):
		return self.__data["upgrade_curr"]

	#
	# 所持しているマスターIDを返す
	#
	def getUnitMasterId(self):
		return self.__data["unit_master_id"]

	#
	# 所持しているIDを設定
	#
	def setId4Shoji(self, unitId, MasterId):
		self.__data["unit_id"] = unitId
		self.__data["unit_master_id"] = MasterId

	#
	# ルーンの効果名称を返す
	#
	def getEffectTypeName(self, key):
		if key == "pri":
			return self.__mst.getEffectTypeName(self.__data["pri_eff"][0])
		elif key == "pre":
			return self.__mst.getEffectTypeName(self.__data["prefix_eff"][0])
		elif key in {0, 1, 2, 3}:
			return self.__mst.getEffectTypeName(self.__data["sec_eff"][key][0])
		else:
			print("not EffectTypeName key = " + str(key))

	#
	# ルーンの効果値を返す
	#
	def getEffectValue(self, key):
		if key == "pri":
			return self.__data["pri_eff"][1]
		elif key == "pre":
			if self.__data["prefix_eff"][0] == 0 and self.__data["prefix_eff"][1] == 0:
				return ""
			else:
				return self.__data["prefix_eff"][1]
		elif key in {0, 1, 2, 3}:
			return self.__data["sec_eff"][key][1]
		else:
			print("not getEffectValue key = " + str(key))

	#
	# ルーンの練磨値を返す
	#
	def getRenmaEffectValue(self, key):
		if key in {0, 1, 2, 3}:
			return self.__data["sec_eff"][key][3]
		else:
			print("not getEffectValue key = " + str(key))

	#
	# レア度を返す
	#
	def getReaDo(self):
		return self.__data["reaDo"]

	#
	# レア度を設定
	#
	def setReaDo(self, val):
		self.__data["reaDo"] = val

	#  0: ("",""),
	#  1: ("HP flat", "HP +%s"),
	#  2: ("HP%", "HP %s%%"),
	#  3: ("ATK flat", "ATK +%s"),
	#  4: ("ATK%", "ATK %s%%"),
	#  5: ("DEF flat", "DEF +%s"),
	#  6: ("DEF%", "DEF %s%%"),
	#  7: "UNKNOWN",  # ?
	#  8: ("SPD", "SPD +%s"),
	#  9: ("CRate", "CRI Rate %s%%"),
	# 10: ("CDmg", "CRI Dmg %s%%"),
	# 11: ("RES", "Resistance %s%%"),
	# 12: ("ACC", "Accuracy %s%%")
	def getEfficiency(self):
		sum = 0
		for eff in [self.__data['prefix_eff']] + self.__data['sec_eff']:
			typ = eff[0]
			if len(eff) == 2:
				value = eff[1]
			else:
				value = eff[1]+eff[3]
			max = 0
			if typ in [2, 4, 6, 11, 12]:
				max = 40.0
			elif typ == 8 or typ == 9:
				max = 30.0
			elif typ == 10:
				max = 35.0
			if max > 0:
				sum += (value / max)
		sum += 1 if self.__data['class'] == 6 else 0.85
		return sum / 2.8

	#
	# 売りコメントを返す
	#
	def getUriComment(self):
		uri = ""
		uricomment = ""
		if self.__data["reaDo"] == 6: # レア
			if self.__data["sec_eff"][0][0] in [1,3,5]: # 1:体、3:攻、5:防
				uri = "売"
				uricomment = "1番実数"
			if self.__data["sec_eff"][1][0] in [1,3,5]:
				uri = "売"
				uricomment = "2番実数"
			if self.__data["slot_no"] in [2,4,6]:
				uri = ""
				uricomment = ""
			if uri == "":
				if self.__data["sec_eff"][0][0] == 8 or self.__data["sec_eff"][1][0] == 8:# 速度
					if self.__data["class"] == 5 and \
						((self.__data["sec_eff"][0][0] == 8 and self.__data["sec_eff"][0][1] == 3) or \
						 (self.__data["sec_eff"][1][0] == 8 and self.__data["sec_eff"][1][1] == 3)):# 速度:3
						uri = "売"
						uricomment = "速度3"
					else:
						uri = ""
						uricomment = ""
				elif self.__data["slot_no"] in [2,4,6]: # スロットが2,4,6
					uri = ""
					uricomment = ""
				elif self.__data["sec_eff"][0][0] in [9, 10] and self.__data["sec_eff"][1][0] in [9, 10]: # 9:クリ、10:ダメ
					uri = ""
					uricomment = ""
				else:
					uri = "売3"
					uricomment = "速度なし、クリなし、ダメなし"
		if self.__data["reaDo"] == 9: # ヒーロー
			if self.__data["sec_eff"][0][0] in [1,3,5]:
				uri = "売4"
				uricomment = "1番実数"
			if self.__data["sec_eff"][1][0] in [1,3,5]:
				uri = "売5"
				uricomment = "2番実数"
			if self.__data["sec_eff"][2][0] in [1,3,5]:
				uri = "売6"
				uricomment = "3番実数"
			if self.__data["slot_no"] in [2,4,6]:
				uri = ""
				uricomment = ""
			if uri != "":
				if self.__data["sec_eff"][0][0] == 8:
					uri = ""
					uricomment = ""
				if self.__data["sec_eff"][1][0] == 8:
					uri = ""
					uricomment = ""
				if self.__data["sec_eff"][2][0] == 8:
					uri = ""
					uricomment = ""
		return [uri,uricomment]

	#
	# ランクを返す
	#
	def getRank(self):
		return len(self.__data["sec_eff"])

	#
	# サブオプ強化残数を返す
	#
	def getNokoriSumOpKyoka(self):
		dest = math.floor(self.getReaDo()/3)
		now  = math.floor(self.getUpgradeCurr()/3)
		zan  = dest - now
		if (zan == -1):
			zan = 0
		return zan
