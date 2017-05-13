#!/usr/bin/python
# -*- coding: sjis -*-

import codecs
import json
import math
import os.path
import swMaster
import swToukei
import swOutputExcel
import sys
import os

class MAIN:
	def __init__(self):
		self.jsonDir = "C:\\Users\hhara\\OneDrive\\SWProxy-windows"
		self.hashRune = {}
		self.lstRune  = []
		self.fw = open('initRune.tsv', 'w')
		self.fl = open('initRune.log', 'w')

	def main(self):
		for file in self.fild_all_files(self.jsonDir):
			data = self.ReadJson(file)
			self.runeSokyu(data)
		for key in sorted(self.hashRune):
			rune = self.hashRune[key]
			#print(str(rune["rune_id"]) + "	" + rune["wizard_last_login"] + "	" + str(len(rune["sec_eff"])))
			self.fw.write(str(rune["rune_id"]) + "	")
			self.fw.write(rune["wizard_last_login"] + "	")
			self.fw.write(str(rune["upgrade_curr"]) + "	")
			self.fw.write(str(len(rune["sec_eff"])))
			self.fw.write("\n")
		for rune in sorted(self.lstRune, key=lambda h: h["rune_id"]):
			self.fl.write(str(rune["rune_id"]) + "	")
			self.fl.write(rune["wizard_last_login"] + "	")
			self.fl.write(str(rune["upgrade_curr"]) + "	")
			self.fl.write(str(len(rune["sec_eff"])))
			self.fl.write("\n")
		self.fw.close()
		self.fl.close()

	def runeSokyu(self, data):
		wizard_last_login = data["wizard_info"]["wizard_last_login"]
		runes = data["runes"]
		
		for rune in runes:
			self.output(rune, wizard_last_login)
		for unit_list in data["unit_list"]:
			for rune in unit_list["runes"]:
				self.output(rune, wizard_last_login)
		
	def output(self, rune, wizard_last_login):
		rune_id      = rune["rune_id"]
		upgrade_curr = rune["upgrade_curr"]
		sec_eff      = rune["sec_eff"]
		rune["wizard_last_login"] = wizard_last_login
		if upgrade_curr >= 0:
			if rune_id in self.hashRune:
				if self.hashRune[rune_id]["wizard_last_login"] > wizard_last_login:
					self.hashRune[rune_id] = rune
			else:
				self.hashRune[rune_id] = rune
			self.lstRune.append(rune)


	#
	# JSONファイルの読み込み
	#
	def ReadJson(self, filename):
		f = codecs.open(filename, "r", "utf-8")
		if f is None:
			print("819205-swarfarm.jsonが存在しない")
			os.exit()
		return json.load(f)

	def fild_all_files(self, directory):
		for root, dirs, files in os.walk(directory):
			#yield root
			for file in files:
				if file == "819205-swarfarm.json":
					yield os.path.join(root, file)

if __name__ == "__main__":
	a = MAIN()
	a.main()

