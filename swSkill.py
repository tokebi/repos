#!/usr/bin/python
# -*- coding: sjis -*-

class SwSkill():
	def __init__(self, skills):
		self.data = skills

	#
	# �X�L��ID���擾
	#
	def getId(self):
		return self.data[0]

	#
	# �X�L�����x�����擾
	#
	def getLevel(self):
		return self.data[1]
