#!/usr/bin/python
# -*- coding: sjis -*-

from lib.swMaster import SwMaster

class SwSkill():
	def __init__(self, skills):
		self.__mst = SwMaster.getInstance()
		self.__data = skills

	#
	# スキルIDを取得
	#
	def getId(self):
		return self.__data[0]

	#
	# スキルIDを取得
	#
	def getIdStr(self):
		return str(self.__data[0])
		
	#
	# スキルレベルを取得
	#
	def getLevel(self):
		return self.__data[1]

	#
	# スキルレベルMAXを取得
	#
	def getSkillMaxLev(self):
		return self.__mst.getSkillMaxLev(self.getIdStr())
	
	#
	# スキル倍率を取得
	#
	def getSkillRate(self):
		return self.__mst.getSkillRate(self.getIdStr())

	#
	# スキル略称を取得
	#
	def getSkillRyaku(self):
		return self.__mst.getSkillRyaku(self.getIdStr())

	#
	# スキルコメントを取得
	#
	def getSkillComment(self):
		return self.__mst.getSkillComment(self.getIdStr())

