#!/usr/bin/python
# -*- coding: sjis -*-

import math
import swRuneSet
import swEffectType
import swMonstersName
import swNotOutputMonster
import swAttribute
import swSkill

class SwMaster:
	def __init__(self):
		self.__runeSetMap         = swRuneSet         .SwRuneSet()         .getMap()
		self.__swEffectTypeMap    = swEffectType      .SwEffectType()      .getMap()
		self.__swMonstersNameMap  = swMonstersName    .SwMonstersName()    .getMap()
		self.__swNotOutputMonster = swNotOutputMonster.SwNotOutputMonster().getMap()
		self.__swAttribute        = swAttribute       .SwAttribute()       .getMap()
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
	# モンスターの日本語名を返す
	#
	def getMonsterName(self, id, attribute_id):
		if id in self.__swMonstersNameMap:
			return self.__swMonstersNameMap[id][0]

	#
	# モンスターの覚醒名称名を返す
	#
	def getKakuseiName(self, id):
		if id in self.__swMonstersNameMap:
			return self.__swMonstersNameMap[id][1]

	#
	# モンスターの攻撃種類を返す
	#
	def getMonsterTypeName(self, id):
		if id in self.__swMonstersNameMap:
			return self.__swMonstersNameMap[id][2]

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
