#!/usr/bin/python
# -*- coding: sjis -*-

import codecs
import json
import os.path
import sys

from swRune import SwRune
from swUnit import SwUnit
from swCraftItem import SwCraftItem

class SwData:
	def __init__(self):
		self.data = self.ReadJson("819205-swarfarm.json")
		self.runeList = []
		self.unitList = []
		self.craftItemList = []
		# ルーンデータの取得
		for rune in self.data["runes"]:
			self.runeList.append(SwRune(rune))
		# ユニットデータの取得
		for unit in sorted(self.data["unit_list"], key=lambda x:(-x['class'],x['attribute'])):
			swUnit = SwUnit(unit)
			self.unitList.append(swUnit)
			self.runeList.extend(swUnit.getRunes())
		# 練磨・ジェムの取得
		for craftItem in sorted(self.data["rune_craft_item_list"], key=lambda x:(x['craft_type_id'],x['craft_type'])):
			swCraftItem = SwCraftItem(craftItem)
			self.craftItemList.append(swCraftItem)

	#
	# JSONファイルの読み込み
	#
	def ReadJson(self, filename):
		targetDirs = {"C:\\Users\\hhara\\OneDrive\\SWProxy-windows"
			     ,"C:\\Users\\tokebi\\OneDrive\\SWProxy-windows"}
		f = None
		for targetDir in targetDirs:
			targetFile = targetDir + "\\" + filename
			if os.path.exists(targetFile):
				f = codecs.open(targetFile, "r", "utf-8")
		if f is None:
			print("819205-swarfarm.jsonが存在しない")
			os.exit()
		return json.load(f)

	#
	# 最終ログイン時間を返す
	#
	def getLastLogin(self):
		return self.data["wizard_info"]["wizard_last_login"]

	#
	# モンスターリストを返す
	#
	def getMonsterList(self):
		return self.unitList

	#
	# モンスターリストを返す
	#
	def getRuneList(self):
		return self.runeList

	#
	# 練磨・ジェムのリストを返す
	#
	def getCraftItemList(self):
		return self.craftItemList
