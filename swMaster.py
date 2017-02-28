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
	# �����X�^�[�̓��{�ꖼ��Ԃ�
	#
	def getMonsterName(self, id, attribute_id):
		if id in self.__swMonstersNameMap:
			return self.__swMonstersNameMap[id][0]

	#
	# �����X�^�[�̊o�����̖���Ԃ�
	#
	def getKakuseiName(self, id):
		if id in self.__swMonstersNameMap:
			return self.__swMonstersNameMap[id][1]

	#
	# �����X�^�[�̍U����ނ�Ԃ�
	#
	def getMonsterTypeName(self, id):
		if id in self.__swMonstersNameMap:
			return self.__swMonstersNameMap[id][2]

	#
	# �o�͑ΏۊO�̃����X�^�[��Ԃ�
	#
	def isNotOutputMonster(self, tmon):
		for mon in self.__swNotOutputMonster:
			if tmon[0:len(mon)] in mon:
				return True
		return False

	#
	# ����������{��ŕԂ�
	#
	def getAttributeName(self, id):
		return self.__swAttribute[id]

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

	#
	# �X�L���{����Ԃ�
	#
	def getSkillRate(self, id):
		ret = ""
		if id in self.__swSkill:
			ret = self.__swSkill[id]["rate"]
		return ret

class SwRuneSet:
	#
	# ���[���ݒu�̃n�b�V����Ԃ�
	#
	def getMap(self):
		return {
			1: "��",
			2: "��",
			3: "�v",
			4: "�n",
			5: "��",
			6: "�W",
			7: "�E",
			8: "��",
			10: "��",
			11: "�z",
			13: "�\",
			14: "��",
			15: "��",
			16: "��",
			17: "��",
			18: "�j",
			19: "��", # ���u�F�����̍U���́{�P�O��
			20: "��", # ���ӁF�����̖h��{�V��
			21: "��", # ���g�F�����̗̑́{�V��
			22: "��", # �����F�����̓I���{�P�O��
			23: "��", # �����F�����̒�R�{�P�O��
			24: "��", # ���u�F�����̍U���{�V��
		}

class SwEffectType:
	#
	# ���ʖ��̃n�b�V����Ԃ�
	#
	def getMap(self):
		return {
			0:  "",
			1:  "��",
			2:  "��%",
			3:  "�U",
			4:  "�U%",
			5:  "�h",
			6:  "�h%",
			8:  "��",
			9:  "�N��",
			10: "�_��",
			11: "��R",
			12: "�I��"
		}

class SwAttribute:
	#
	# ����������{��n�b�V����Ԃ�
	#
	def getMap(self):
		return {
			1: "��",
			2: "��",
			3: "��",
			4: "��",
			5: "��"
		}