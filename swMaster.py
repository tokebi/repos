#!/usr/bin/python
# -*- coding: sjis -*-

import math
from swMonstersName     import SwMonstersName
from swNotOutputMonster import SwNotOutputMonster
from swSkillMaster      import SwSkillMaster

class SwMaster:
	__instance = None
	__runeSetMap         = None
	__swEffectTypeMap    = None
	__swAttribute        = None
	__swMonstersNameMap  = None
	__swNotOutputMonster = None
	__swSkill            = None

	def __new__(cls, *args, **keys):
		if cls.__instance is None:
			cls.__instance = object.__new__(cls)
			cls.__runeSetMap         = SwRuneSet()         .getMap()
			cls.__swEffectTypeMap    = SwEffectType()      .getMap()
			cls.__swAttribute        = SwAttribute()       .getMap()
			cls.__swMonstersNameMap  = SwMonstersName()    .getMap()
			cls.__swNotOutputMonster = SwNotOutputMonster().getMap()
			cls.__swSkill            = SwSkillMaster()     .getMap()
		return cls.__instance

	@classmethod
	def getInstance(cls):
		if not cls.__instance:
			cls.__instance = cls()
		return cls.__instance
		
	#
	# ルーンセット名を返す
	#
	def getRuneSetName(self, id):
		return self.__runeSetMap[id]

	#
	# 効果名を返す
	#
	def getEffectTypeName(self, id):
		return self.__swEffectTypeMap[id]

	#
	# モンスターの日本語名を返す
	#
	def getMonsterName(self, id, attribute_id):
		if id in self.__swMonstersNameMap:
			return self.__swMonstersNameMap[id]["name"]

	#
	# モンスターの覚醒名称名を返す
	#
	def getKakuseiName(self, id):
		if id in self.__swMonstersNameMap:
			return self.__swMonstersNameMap[id]["kname"]

	#
	# モンスターの攻撃種類を返す
	#
	def getMonsterTypeName(self, id):
		if id in self.__swMonstersNameMap:
			return self.__swMonstersNameMap[id]["kind"]

	#
	# モンスターのリーダスキルを返す
	#
	def getLSkillComment(self, id):
		if id in self.__swMonstersNameMap:
			return self.__swMonstersNameMap[id]["lskill"]

	#
	# 出力対象外のモンスターを返す
	#
	def isNotOutputMonster(self, tmon):
		for mon in self.__swNotOutputMonster:
			if tmon[0:len(mon)] in mon:
				return True
		return False

	#
	# 属性名を日本語で返す
	#
	def getAttributeName(self, id):
		return self.__swAttribute[id]

	#
	# スキルのレベルMAXを返す
	#
	def getSkillMaxLev(self, id):
		if id in self.__swSkill:
			lvmax = self.__swSkill[id]["lvmax"]
			if lvmax != "":
				return lvmax
			else:
				return "9999"
		else:
			return id

	#
	# スキル倍率を返す
	#
	def getSkillRate(self, id):
		ret = ""
		if id in self.__swSkill:
			ret = self.__swSkill[id]["rate"]
		return ret

	#
	# スキルコメントを返す
	#
	def getSkillComment(self, id):
		ret = ""
		if id in self.__swSkill:
			ret = self.__swSkill[id]["comment"]
		if ret == "":
			ret = str(id)
		return ret
		
	#
	# スキル略称を返す
	#
	def getSkillRyaku(self, id):
		ret = ""
		if id in self.__swSkill:
			ret = self.__swSkill[id]["ryaku"]
		return ret

class SwRuneSet:
	#
	# ルーン設置のハッシュを返す
	#
	def getMap(self):
		return {
			1: "元",
			2: "守",
			3: "迅",
			4: "刃",
			5: "激",
			6: "集",
			7: "忍",
			8: "猛",
			10: "絶",
			11: "吸",
			13: "暴",
			14: "果",
			15: "意",
			16: "保",
			17: "反",
			18: "破",
			19: "闘", # 闘志：味方の攻撃力＋１０％
			20: "決", # 決意：味方の防御＋７％
			21: "高", # 高揚：味方の体力＋７％
			22: "命", # 命中：味方の的中＋１０％
			23: "根", # 根性：味方の抵抗＋１０％
			24: "闘", # 闘志：味方の攻撃＋７％
		}

class SwEffectType:
	#
	# 効果名のハッシュを返す
	#
	def getMap(self):
		return {
			0:  "",
			1:  "体",
			2:  "体%",
			3:  "攻",
			4:  "攻%",
			5:  "防",
			6:  "防%",
			8:  "速",
			9:  "クリ",
			10: "ダメ",
			11: "抵抗",
			12: "的中"
		}

class SwAttribute:
	#
	# 属性名を日本語ハッシュを返す
	#
	def getMap(self):
		return {
			1: "水",
			2: "火",
			3: "風",
			4: "光",
			5: "闇"
		}