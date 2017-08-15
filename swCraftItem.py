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
	# �Z�b�g���̂��擾
	#
	def getSetName(self):
		return self.__mst.getRuneSetName(self.__setId)

	#
	# ���ʎ�ʂ��擾
	#
	def getEffectTypeName(self):
		return self.__mst.getEffectTypeName(self.__effectType)

	#
	# ���A�x���擾
	#
	def getRarity(self):
		if self.__rarity == 1:			# �Ȃ�
			rarityName = "�ʏ�"
		elif self.__rarity == 2:			# ���@
			rarityName = "+2%�`5%"
			if self.__craftType == 2:		# ����
				if self.__effectType == 8:# ���x
					rarityName = "+1�`2"
		elif self.__rarity == 3:			# ���A
			rarityName = "+3%�`6%"
		elif self.__rarity == 4:			# �q�[���[
			rarityName = "+4%�`7%"
			if self.__craftType == 1:		# �W�F��
				if self.__effectType == 11: # ��R
					rarityName = "+6%�`9%"
		elif self.__rarity == 5:			# ���W�F���g
			rarityName = "���W�F���g"
		return rarityName

	#
	# ��ނ��擾
	#
	def getType(self):
		if self.__craftType == 1:
			return "�W�F��"
		elif self.__craftType == 2:
			return "����"


	#
	# craft_item_id���擾
	#
	def getCraftItemId(self):
		return self.__craftItemId

	#
	# sell_value���擾
	#
	def getSellValue(self):
		return self.__sellValue

	#
	# craft_type_id���擾
	#
	def getCraftTypeId(self):
		return self.__craftTypeId

	#
	# wizard_id���擾
	#
	def getWizardId(self):
		return self.__wizardId

	#
	# craft_type���擾
	#
	def getCraftType(self):
		return self.__craftType

