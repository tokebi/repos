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
		self.__jsonDir = "C:\\Users\hhara\\OneDrive\\SWProxy-windows"
		self.__hashRune = {}
		self.__lstRune  = []
		self.__fw = open('initRune.tsv', 'w')
		self.__fl = open('initRune.log', 'w')

	def main(self):
		for file in self.fild_all_files(self.__jsonDir):
			data = self.ReadJson(file)
			self.runeSokyu(data)
		for key in sorted(self.__hashRune):
			rune = self.__hashRune[key]
			#print(str(rune["rune_id"]) + "	" + rune["wizard_last_login"] + "	" + str(len(rune["sec_eff"])))
			self.__fw.write(str(rune["rune_id"]) + "	")
			self.__fw.write(rune["wizard_last_login"] + "	")
			self.__fw.write(str(rune["upgrade_curr"]) + "	")
			self.__fw.write(str(len(rune["sec_eff"])))
			self.__fw.write("\n")
		for rune in sorted(self.__lstRune, key=lambda h: h["rune_id"]):
			self.__fl.write(str(rune["rune_id"]) + "	")
			self.__fl.write(rune["wizard_last_login"] + "	")
			self.__fl.write(str(rune["upgrade_curr"]) + "	")
			self.__fl.write(str(len(rune["sec_eff"])))
			self.__fl.write("\n")
		self.__fw.close()
		self.__fl.close()

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
			if rune_id in self.__hashRune:
				if self.__hashRune[rune_id]["wizard_last_login"] > wizard_last_login:
					self.__hashRune[rune_id] = rune
			else:
				self.__hashRune[rune_id] = rune
			self.__lstRune.append(rune)


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

