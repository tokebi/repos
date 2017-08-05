#!/usr/bin/python
# -*- coding: sjis -*-

import datetime

class SwToukei:
	def __init__(self, dataID):
		self.__rune6 = 0
		self.__rune5 = 0
		self.__monster6 = 7*[0]
		self.__monster5 = 7*[0]
		self.__dataID = dataID

	#
	# モンスター統計の処理
	#
	def addMonster(self, classNum, level, attribute):
		if classNum == 6:
			self.__monster6[0] += 1
			self.__monster6[attribute] += 1
		elif classNum == 5 and level == 35:
			self.__monster5[0] += 1
			self.__monster5[attribute] += 1

	#
	# ルーン統計の処理
	#
	def addRune(self, classNum):
		if classNum == 6:
			self.__rune6 += 1
		elif classNum == 5:
			self.__rune5 += 1

	#
	# 統計データ取得
	#
	def outputData(self):
		f = open("tokei" + self.__dataID + ".tsv", "a")
		f.write(datetime.date.today().strftime("%Y/%m/%d") + "\t")
		f.write(str(self.__monster6[0]) + "\t")
		f.write(str(self.__monster6[1]) + "\t")
		f.write(str(self.__monster6[2]) + "\t")
		f.write(str(self.__monster6[3]) + "\t")
		f.write(str(self.__monster6[4]) + "\t")
		f.write(str(self.__monster6[5]) + "\t")
		f.write(str(self.__monster5[0]) + "\t")
		f.write(str(self.__monster5[1]) + "\t")
		f.write(str(self.__monster5[2]) + "\t")
		f.write(str(self.__monster5[3]) + "\t")
		f.write(str(self.__monster5[4]) + "\t")
		f.write(str(self.__monster5[5]) + "\t")
		f.write(str(self.__rune6) + "\t")
		f.write(str(self.__rune5) + "\n")
		f.close()
