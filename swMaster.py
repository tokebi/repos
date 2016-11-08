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
	# ���[���Z�b�g����Ԃ�
	#
	def getRuneSetName(self, id):
		return self.__runeSetMap[id]

	#
	# ���ʖ���Ԃ�
	#
	def getEffectTypeName(self, id):
		return self.__swEffectTypeMap[id]

	#
	# �����X�^�[�̓��{�ꖼ�̃n�b�V����Ԃ�
	#
	def getMonsterName(self, id, attribute_id):
		# ������ɕϊ�
		str_id = str(int(id))
		# "122"  : "�X���C��",�����A���X���C������ 12201�ƂȂ邽�ߌv�Z����
		if str_id in self.__swMonstersNameMap:
			return self.__swMonstersNameMap[str_id]
		else:
			return self.__swMonstersNameMap[str(int(math.floor(id) / 100))] + \
				"(" + self.__swAttribute[attribute_id] + ")"

	#
	# �o�͑ΏۊO�̃����X�^�[�̃n�b�V����Ԃ�
	#
	def isNotOutputMonster(self, tmon):
		#return self.__swNotOutputMonster
		for mon in self.__swNotOutputMonster:
			if tmon[0:len(mon)] in mon:
				#print("�ΏۊO:" + mon)
				return True
		return False
	#
	# ����������{��ŕԂ�
	#
	def getAttributeName(self, id):
		return self.__swAttribute[id]

	#
	# �����X�^�[�̍U����ނ�Ԃ�
	#
	def getMonsterType(self, id):
		if id in self.__swMonsterType:
			return self.__swMonsterType[id]
		else:
			return "���ݒ�"

	#
	# �X�L���̃��x��MAX��Ԃ�
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






