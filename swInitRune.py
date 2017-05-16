#!/usr/bin/python
# -*- coding: sjis -*-

import math

class SwInitRune:
	def __init__(self):
		self.hashInitRune = {};
		for line in open('initRune.tsv', 'r') :
			items = line[:-1].split('\t')
			key = int(items[0])
			val = {}
			val['dropdate'] = items[1]
			val['upgrade']  = items[2]
			val['droprank'] = items[3]
			self.hashInitRune[key] = val
	
	def getDropRank(self, rune, lastLogin):
		if rune.getRuneId() not in self.hashInitRune:
			initRune = {}
			initRune['upgrade']  = str(rune.getUpgradeCurr())
			initRune['droprank'] = str(rune.getRank())
			# ファイルに追記
			self.fw = open('initRune.tsv', 'a')
			self.fw.write(str(rune.getRuneId()) + "	")
			self.fw.write(lastLogin + "	")
			self.fw.write(str(rune.getUpgradeCurr()) + "	")
			self.fw.write(str(rune.getRank()))
			self.fw.write("\n")
			self.fw.close()
			print("初期ルーンを追加しました。" + str(rune.getRuneId()) )
		else:
			initRune = self.hashInitRune[rune.getRuneId()]
		if initRune['upgrade'] == "0":
			return initRune['droprank']
		else:
			return initRune['droprank'] + "以下(" + initRune['upgrade'] + ")"