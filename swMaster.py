#!/usr/bin/python
# -*- coding: sjis -*-

import math
from swMonstersName     import SwMonstersName
from swNotOutputMonster import SwNotOutputMonster
from swSkill            import SwSkill

class SwMaster:
	def __init__(self):
		self.__runeSetMap         = SwRuneSet()         .getMap()
		self.__swEffectTypeMap    = SwEffectType()      .getMap()
		self.__swAttribute        = SwAttribute()       .getMap()
		self.__swMonstersNameMap  = SwMonstersName()    .getMap()
		self.__swNotOutputMonster = SwNotOutputMonster().getMap()
		self.__swSkill            = SwSkill()           .getMap()

	#
	# [Zbg¼ðÔ·
	#
	def getRuneSetName(self, id):
		return self.__runeSetMap[id]

	#
	# øÊ¼ðÔ·
	#
	def getEffectTypeName(self, id):
		return self.__swEffectTypeMap[id]

	#
	# X^[Ìú{ê¼ðÔ·
	#
	def getMonsterName(self, id, attribute_id):
		if id in self.__swMonstersNameMap:
			return self.__swMonstersNameMap[id][0]

	#
	# X^[ÌoÁ¼Ì¼ðÔ·
	#
	def getKakuseiName(self, id):
		if id in self.__swMonstersNameMap:
			return self.__swMonstersNameMap[id][1]

	#
	# X^[ÌUíÞðÔ·
	#
	def getMonsterTypeName(self, id):
		if id in self.__swMonstersNameMap:
			return self.__swMonstersNameMap[id][2]

	#
	# oÍÎÛOÌX^[ðÔ·
	#
	def isNotOutputMonster(self, tmon):
		for mon in self.__swNotOutputMonster:
			if tmon[0:len(mon)] in mon:
				return True
		return False

	#
	# ®«¼ðú{êÅÔ·
	#
	def getAttributeName(self, id):
		return self.__swAttribute[id]

	#
	# XLÌxMAXðÔ·
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

class SwRuneSet:
	#
	# [ÝuÌnbVðÔ·
	#
	def getMap(self):
		return {
			1: "³",
			2: "ç",
			3: "v",
			4: "n",
			5: "",
			6: "W",
			7: "E",
			8: "Ò",
			10: "â",
			11: "z",
			13: "\",
			14: "Ê",
			15: "Ó",
			16: "Û",
			17: "½",
			18: "j",
			19: "¬", # ¬uF¡ûÌUÍ{PO
			20: "", # ÓF¡ûÌhä{V
			21: "", # gF¡ûÌÌÍ{V
			22: "½", # ½F¡ûÌI{PO
			23: "ª", # ª«F¡ûÌïR{PO
			24: "¬", # ¬uF¡ûÌU{V
		}

class SwEffectType:
	#
	# øÊ¼ÌnbVðÔ·
	#
	def getMap(self):
		return {
			0:  "",
			1:  "Ì",
			2:  "Ì%",
			3:  "U",
			4:  "U%",
			5:  "h",
			6:  "h%",
			8:  "¬",
			9:  "N",
			10: "_",
			11: "ïR",
			12: "I"
		}

class SwAttribute:
	#
	# ®«¼ðú{ênbVðÔ·
	#
	def getMap(self):
		return {
			1: "",
			2: "Î",
			3: "",
			4: "õ",
			5: "Å"
		}