#!/usr/bin/python
# -*- coding: sjis -*-

import swMaster

class SwSkill():
	def __init__(self, skills):
		self.mst = swMaster.SwMaster.getInstance()
		self.data = skills

	#
	# �X�L��ID���擾
	#
	def getId(self):
		return self.data[0]

	#
	# �X�L��ID���擾
	#
	def getIdStr(self):
		return str(self.data[0])
		
	#
	# �X�L�����x�����擾
	#
	def getLevel(self):
		return self.data[1]

	#
	# �X�L�����x��MAX���擾
	#
	def getSkillMaxLev(self):
		return self.mst.getSkillMaxLev(self.getIdStr())
	
	#
	# �X�L���{�����擾
	#
	def getSkillRate(self):
		return self.mst.getSkillRate(self.getIdStr())

	#
	# �X�L�����̂��擾
	#
	def getSkillRyaku(self):
		return self.mst.getSkillRyaku(self.getIdStr())

	#
	# �X�L���R�����g���擾
	#
	def getSkillComment(self):
		return self.mst.getSkillComment(self.getIdStr())










