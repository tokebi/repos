#!/usr/bin/python
# -*- coding: sjis -*-

class SwSkill():
	def __init__(self, skills):
		self.data = skills

	#
	# スキルIDを取得
	#
	def getId(self):
		return self.data[0]

	#
	# スキルレベルを取得
	#
	def getLevel(self):
		return self.data[1]
