#!/usr/bin/python
# -*- coding: sjis -*-

import math
import swRuneSet
import swEffectType
import swMonstersName
import swNotOutputMonster
import swAttribute
import swMonsterType
import swSkill

class SwMaster:
	def __init__(self):
		self.__runeSetMap         = swRuneSet         .SwRuneSet()         .getMap()
		self.__swEffectTypeMap    = swEffectType      .SwEffectType()      .getMap()
		self.__swMonstersNameMap  = swMonstersName    .SwMonstersName()    .getMap()
		self.__swNotOutputMonster = swNotOutputMonster.SwNotOutputMonster().getMap()
		self.__swAttribute        = swAttribute       .SwAttribute()       .getMap()
		self.__swMonsterType      = swMonsterType     .SwMonsterType()     .getMap()
		self.__swSkill            = swSkill           .SwSkill()           .getMap()

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
	# モンスターの日本語名のハッシュを返す
	#
	def getMonsterName(self, id, attribute_id):
		# 文字列に変換
		str_id = str(int(id))
		# "122"  : "スライム",だが、水スライムだと 12201となるため計算する
		if str_id in self.__swMonstersNameMap:
			return self.__swMonstersNameMap[str_id]
		else:
			return self.__swMonstersNameMap[str(int(math.floor(id) / 100))] + \
				"(" + self.__swAttribute[attribute_id] + ")"

	#
	# 出力対象外のモンスターのハッシュを返す
	#
	def isNotOutputMonster(self, tmon):
		#return self.__swNotOutputMonster
		for mon in self.__swNotOutputMonster:
			if tmon[0:len(mon)] in mon:
				#print("対象外:" + mon)
				return True
		return False
	#
	# 属性名を日本語で返す
	#
	def getAttributeName(self, id):
		return self.__swAttribute[id]

	#
	# モンスターの攻撃種類を返す
	#
	def getMonsterType(self, id):
		if id in self.__swMonsterType:
			return self.__swMonsterType[id]
		else:
			return "未設定"

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






