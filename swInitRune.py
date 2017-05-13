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
		if rune['rune_id'] not in self.hashInitRune:
			initRune = {}
			initRune['upgrade']  = str(rune["upgrade_curr"])
			initRune['droprank'] = str(len(rune["sec_eff"]))
			# ファイルに追記
			self.fw = open('initRune.tsv', 'a')
			self.fw.write(str(rune["rune_id"]) + "	")
			self.fw.write(lastLogin + "	")
			self.fw.write(str(rune["upgrade_curr"]) + "	")
			self.fw.write(str(len(rune["sec_eff"])))
			self.fw.write("\n")
			self.fw.close()
			print("初期ルーンを追加しました。" + str(rune["rune_id"]) )
		else:
			initRune = self.hashInitRune[rune['rune_id']]
		if initRune['upgrade'] == "0":
			return initRune['droprank']
		else:
			return initRune['droprank'] + "以下(" + initRune['upgrade'] + ")"