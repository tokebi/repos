#!/usr/bin/python
# -*- coding: sjis -*-

import swMaster

class SwCraftItem():
	def __init__(self, craftItem):
		self.mst = swMaster.SwMaster.getInstance()
		self.data = craftItem
		self.id = '{0:06d}'.format(self.data["craft_type_id"])

	#
	# �Z�b�g���̂��擾
	#
	def getSetName(self):
		return self.mst.getRuneSetName(int(self.id[0:2]))

	#
	# ���ʎ�ʂ��擾
	#
	def getEffectTypeName(self):
		return self.mst.getEffectTypeName(int(self.id[2:4]))

	#
	# ���A�x���擾
	#
	def getRarity(self):
		rarity = self.id[4:6]
		if rarity == "01":
			rarityName = "�ʏ�"
		elif rarity == "02":
			rarityName = "+2%�`5%"
		elif rarity == "03":
			rarityName = "+3%�`6%"
		elif rarity == "04":
			rarityName = "+4%�`7%"
		elif rarity == "05":
			rarityName = "���W�F���g"
		return rarityName

	#
	# ��ނ��擾
	#
	def getType(self):
		if self.data["craft_type"] == 1:
			return "�W�F��"
		elif self.data["craft_type"] == 2:
			return "����"


	#
	# craft_item_id���擾
	#
	def getCraftItemId(self):
		return self.data["craft_item_id"]

	#
	# sell_value���擾
	#
	def getSellValue(self):
		return self.data["sell_value"]

	#
	# craft_type_id���擾
	#
	def getCraftTypeId(self):
		return self.data["craft_type_id"]

	#
	# wizard_id���擾
	#
	def getWizardId(self):
		return self.data["wizard_id"]

	#
	# craft_type���擾
	#
	def getCraftType(self):
		return self.data["craft_type"]

