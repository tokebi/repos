#!/usr/bin/python
# -*- coding: sjis -*-

import swMaster

class SwCraftItem():
	def __init__(self, craftItem):
		self.__mst = swMaster.SwMaster.getInstance()
		id = '{0:06d}'.format(craftItem["craft_type_id"])
		self.__setId       = int(id[0:2])
		self.__effectType  = int(id[2:4])
		self.__rarity      = int(id[4:6])
		self.__craftType   = craftItem["craft_type"]
		self.__craftItemId = craftItem["craft_item_id"]
		self.__sellValue   = craftItem["sell_value"]
		self.__craftTypeId = craftItem["craft_type_id"]
		self.__wizardId    = craftItem["wizard_id"]
		self.__craftType   = craftItem["craft_type"]

	#
	# セット名称を取得
	#
	def getSetName(self):
		return self.__mst.getRuneSetName(self.__setId)

	#
	# 効果種別を取得
	#
	def getEffectTypeName(self):
		return self.__mst.getEffectTypeName(self.__effectType)

	#
	# レア度を取得
	#
	def getRarity(self):
		if self.__rarity == 1:			# なし
			rarityName = "通常"
		elif self.__rarity == 2:			# 魔法
			rarityName = "+2%～5%"
			if self.__craftType == 2:		# 練磨
				if self.__effectType == 8:# 速度
					rarityName = "+1～2"
		elif self.__rarity == 3:			# レア
			rarityName = "+3%～6%"
		elif self.__rarity == 4:			# ヒーロー
			rarityName = "+4%～7%"
			if self.__craftType == 1:		# ジェム
				if self.__effectType == 11: # 抵抗
					rarityName = "+6%～9%"
		elif self.__rarity == 5:			# レジェント
			rarityName = "レジェント"
		return rarityName

	#
	# 種類を取得
	#
	def getType(self):
		if self.__craftType == 1:
			return "ジェム"
		elif self.__craftType == 2:
			return "練磨"


	#
	# craft_item_idを取得
	#
	def getCraftItemId(self):
		return self.__craftItemId

	#
	# sell_valueを取得
	#
	def getSellValue(self):
		return self.__sellValue

	#
	# craft_type_idを取得
	#
	def getCraftTypeId(self):
		return self.__craftTypeId

	#
	# wizard_idを取得
	#
	def getWizardId(self):
		return self.__wizardId

	#
	# craft_typeを取得
	#
	def getCraftType(self):
		return self.__craftType

