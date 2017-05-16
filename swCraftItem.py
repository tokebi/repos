#!/usr/bin/python
# -*- coding: sjis -*-

import swMaster

class SwCraftItem():
	def __init__(self, craftItem):
		self.mst = swMaster.SwMaster.getInstance()
		self.data = craftItem
		self.id = '{0:06d}'.format(self.data["craft_type_id"])

	#
	# セット名称を取得
	#
	def getSetName(self):
		return self.mst.getRuneSetName(int(self.id[0:2]))

	#
	# 効果種別を取得
	#
	def getEffectTypeName(self):
		return self.mst.getEffectTypeName(int(self.id[2:4]))

	#
	# レア度を取得
	#
	def getRarity(self):
		rarity = self.id[4:6]
		if rarity == "01":
			rarityName = "通常"
		elif rarity == "02":
			rarityName = "+2%～5%"
		elif rarity == "03":
			rarityName = "+3%～6%"
		elif rarity == "04":
			rarityName = "+4%～7%"
		elif rarity == "05":
			rarityName = "レジェント"
		return rarityName

	#
	# 種類を取得
	#
	def getType(self):
		if self.data["craft_type"] == 1:
			return "ジェム"
		elif self.data["craft_type"] == 2:
			return "練磨"


	#
	# craft_item_idを取得
	#
	def getCraftItemId(self):
		return self.data["craft_item_id"]

	#
	# sell_valueを取得
	#
	def getSellValue(self):
		return self.data["sell_value"]

	#
	# craft_type_idを取得
	#
	def getCraftTypeId(self):
		return self.data["craft_type_id"]

	#
	# wizard_idを取得
	#
	def getWizardId(self):
		return self.data["wizard_id"]

	#
	# craft_typeを取得
	#
	def getCraftType(self):
		return self.data["craft_type"]

