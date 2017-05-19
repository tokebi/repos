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
	# �Z�b�g���̂��擾
	#
	def getSetName(self):
		return self.mst.getRuneSetName(self.setId)

	#
	# ���ʎ�ʂ��擾
	#
	def getEffectTypeName(self):
		return self.mst.getEffectTypeName(self.effectType)

	#
	# ���A�x���擾
	#
	def getRarity(self):
		if self.rarity == 1:			# �Ȃ�
			rarityName = "�ʏ�"
		elif self.rarity == 2:			# ���@
			rarityName = "+2%�`5%"
			if self.craftType == 2:		# ����
				if self.effectType == 8:# ���x
					rarityName = "+1�`2"
		elif self.rarity == 3:			# ���A
			rarityName = "+3%�`6%"
		elif self.rarity == 4:			# �q�[���[
			rarityName = "+4%�`7%"
			if self.craftType == 1:		# �W�F��
				if self.effectType == 11: # ��R
					rarityName = "+6%�`9%"
		elif self.rarity == 5:			# ���W�F���g
			rarityName = "���W�F���g"
		return rarityName

	#
	# ��ނ��擾
	#
	def getType(self):
		if self.craftType == 1:
			return "�W�F��"
		elif self.craftType == 2:
			return "����"


	#
	# craft_item_id���擾
	#
	def getCraftItemId(self):
		return self.craftItemId

	#
	# sell_value���擾
	#
	def getSellValue(self):
		return self.sellValue

	#
	# craft_type_id���擾
	#
	def getCraftTypeId(self):
		return self.craftTypeId

	#
	# wizard_id���擾
	#
	def getWizardId(self):
		return self.wizardId

	#
	# craft_type���擾
	#
	def getCraftType(self):
		return self.craftType

