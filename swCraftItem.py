#!/usr/bin/python
# -*- coding: sjis -*-

import swMaster

class SwCraftItem():
	def __init__(self, craftItem):
		self.mst = swMaster.SwMaster.getInstance()
		id = '{0:06d}'.format(craftItem["craft_type_id"])
		self.setId       = int(id[0:2])
		self.effectType  = int(id[2:4])
		self.rarity      = int(id[4:6])
		self.craftType   = craftItem["craft_type"]
		self.craftItemId = craftItem["craft_item_id"]
		self.sellValue   = craftItem["sell_value"]
		self.craftTypeId = craftItem["craft_type_id"]
		self.wizardId    = craftItem["wizard_id"]
		self.craftType   = craftItem["craft_type"]

	#
	# セット名称を取得
	#
	def getSetName(self):
		return self.mst.getRuneSetName(self.setId)

	#
	# 効果種別を取得
	#
	def getEffectTypeName(self):
		return self.mst.getEffectTypeName(self.effectType)

	#
	# レア度を取得
	#
	def getRarity(self):
		if self.rarity == 1:			# なし
			rarityName = "通常"
		elif self.rarity == 2:			# 魔法
			rarityName = "+2%～5%"
			if self.craftType == 2:		# 練磨
				if self.effectType == 8:# 速度
					rarityName = "+1～2"
		elif self.rarity == 3:			# レア
			rarityName = "+3%～6%"
		elif self.rarity == 4:			# ヒーロー
			rarityName = "+4%～7%"
			if self.craftType == 1:		# ジェム
				if self.effectType == 11: # 抵抗
					rarityName = "+6%～9%"
		elif self.rarity == 5:			# レジェント
			rarityName = "レジェント"
		return rarityName

	#
	# 種類を取得
	#
	def getType(self):
		if self.craftType == 1:
			return "ジェム"
		elif self.craftType == 2:
			return "練磨"


	#
	# craft_item_idを取得
	#
	def getCraftItemId(self):
		return self.craftItemId

	#
	# sell_valueを取得
	#
	def getSellValue(self):
		return self.sellValue

	#
	# craft_type_idを取得
	#
	def getCraftTypeId(self):
		return self.craftTypeId

	#
	# wizard_idを取得
	#
	def getWizardId(self):
		return self.wizardId

	#
	# craft_typeを取得
	#
	def getCraftType(self):
		return self.craftType

