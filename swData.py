#!/usr/bin/python
# -*- coding: sjis -*-

import codecs
import json
import os.path
import sys

from swRune import SwRune
from swUnit import SwUnit
from swCraftItem import SwCraftItem
from swInventory import SwInventory

class SwData:
	def __init__(self, dataID):
		self.__data = self.ReadJson(dataID + "-swarfarm.json")
		self.__runeList = []
		self.__unitList = []
		self.__craftItemList = []
		self.__inventoryList = []
		# ルーンデータの取得
		for rune in self.__data["runes"]:
			self.__runeList.append(SwRune(rune))
		# ユニットデータの取得
		for unit in sorted(self.__data["unit_list"], key=lambda x:(-x['class'],x['attribute'])):
			swUnit = SwUnit(unit)
			self.__unitList.append(swUnit)
			self.__runeList.extend(swUnit.getRunes())
		# 練磨・ジェムの取得
		for craftItem in sorted(self.__data["rune_craft_item_list"], key=lambda x:(x['craft_type_id'],x['craft_type'])):
			self.__craftItemList.append(SwCraftItem(craftItem))
		# 在庫情報の取得
		for inventoryInfo in sorted(self.__data["inventory_info"], key=lambda x:(x['item_master_type'],x['item_master_id'])):
			self.__inventoryList.append(SwInventory(inventoryInfo))

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
			print(filename + "が存在しない")
			os.exit()
		return json.load(f)

	#
	# 最終ログイン時間を返す
	#
	def getLastLogin(self):
		return self.__data["wizard_info"]["wizard_last_login"]

	#
	# モンスターリストを返す
	#
	def getMonsterList(self):
		return self.__unitList

	#
	# モンスターリストを返す
	#
	def getRuneList(self):
		return self.__runeList

	#
	# 練磨・ジェムのリストを返す
	#
	def getCraftItemList(self):
		return self.__craftItemList

	#
	# 在庫情報を返す
	#
	def getInventoryList(self):
		return self.__inventoryList