#!/usr/bin/python
# -*- coding: sjis -*-

from lib.swMaster import SwMaster

class SwSkill():
	def __init__(self, skills):
		self.__mst = SwMaster.getInstance()
		self.__data = skills

	#
	# �X�L��ID���擾
	#
	def getId(self):
		return self.__data[0]

	#
	# �X�L��ID���擾
	#
	def getIdStr(self):
		return str(self.__data[0])
		
	#
	# �X�L�����x�����擾
	#
	def getLevel(self):
		return self.__data[1]

	#
	# �X�L�����x��MAX���擾
	#
	def getSkillMaxLev(self):
		return self.__mst.getSkillMaxLev(self.getIdStr())
	
	#
	# �X�L���{�����擾
	#
	def getSkillRate(self):
		return self.__mst.getSkillRate(self.getIdStr())

	#
	# �X�L�����̂��擾
	#
	def getSkillRyaku(self):
		return self.__mst.getSkillRyaku(self.getIdStr())

	#
	# �X�L���R�����g���擾
	#
	def getSkillComment(self):
		return self.__mst.getSkillComment(self.getIdStr())

