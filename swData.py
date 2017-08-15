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
		# ���[���f�[�^�̎擾
		for rune in self.__data["runes"]:
			self.__runeList.append(SwRune(rune))
		# ���j�b�g�f�[�^�̎擾
		for unit in sorted(self.__data["unit_list"], key=lambda x:(-x['class'],x['attribute'])):
			swUnit = SwUnit(unit)
			self.__unitList.append(swUnit)
			self.__runeList.extend(swUnit.getRunes())
		# �����E�W�F���̎擾
		for craftItem in sorted(self.__data["rune_craft_item_list"], key=lambda x:(x['craft_type_id'],x['craft_type'])):
			self.__craftItemList.append(SwCraftItem(craftItem))
		# �݌ɏ��̎擾
		for inventoryInfo in sorted(self.__data["inventory_info"], key=lambda x:(x['item_master_type'],x['item_master_id'])):
			self.__inventoryList.append(SwInventory(inventoryInfo))

	#
	# JSON�t�@�C���̓ǂݍ���
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
			print(filename + "�����݂��Ȃ�")
			os.exit()
		return json.load(f)

	#
	# �ŏI���O�C�����Ԃ�Ԃ�
	#
	def getLastLogin(self):
		return self.__data["wizard_info"]["wizard_last_login"]

	#
	# �����X�^�[���X�g��Ԃ�
	#
	def getMonsterList(self):
		return self.__unitList

	#
	# �����X�^�[���X�g��Ԃ�
	#
	def getRuneList(self):
		return self.__runeList

	#
	# �����E�W�F���̃��X�g��Ԃ�
	#
	def getCraftItemList(self):
		return self.__craftItemList

	#
	# �݌ɏ���Ԃ�
	#
	def getInventoryList(self):
		return self.__inventoryList