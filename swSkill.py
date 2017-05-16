#!/usr/bin/python
# -*- coding: sjis -*-

import swMaster

class SwSkill():
	def __init__(self, skills):
		self.mst = swMaster.SwMaster.getInstance()
		self.data = skills

	#
	# スキルIDを取得
	#
	def getId(self):
		return self.data[0]

	#
	# スキルIDを取得
	#
	def getIdStr(self):
		return str(self.data[0])
		
	#
	# スキルレベルを取得
	#
	def getLevel(self):
		return self.data[1]

	#
	# スキルレベルMAXを取得
	#
	def getSkillMaxLev(self):
		return self.mst.getSkillMaxLev(self.getIdStr())
	
	#
	# スキル倍率を取得
	#
	def getSkillRate(self):
		return self.mst.getSkillRate(self.getIdStr())

	#
	# スキル略称を取得
	#
	def getSkillRyaku(self):
		return self.mst.getSkillRyaku(self.getIdStr())

	#
	# スキルコメントを取得
	#
	def getSkillComment(self):
		return self.mst.getSkillComment(self.getIdStr())










