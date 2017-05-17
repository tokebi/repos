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
		# ���[���f�[�^�̎擾
		for rune in self.data["runes"]:
			self.runeList.append(SwRune(rune))
		# ���j�b�g�f�[�^�̎擾
		for unit in sorted(self.data["unit_list"], key=lambda x:(-x['class'],x['attribute'])):
			swUnit = SwUnit(unit)
			self.unitList.append(swUnit)
			self.runeList.extend(swUnit.getRunes())
		# �����E�W�F���̎擾
		for craftItem in sorted(self.data["rune_craft_item_list"], key=lambda x:(x['craft_type_id'],x['craft_type'])):
			swCraftItem = SwCraftItem(craftItem)
			self.craftItemList.append(swCraftItem)

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
			print("819205-swarfarm.json�����݂��Ȃ�")
			os.exit()
		return json.load(f)

	#
	# �ŏI���O�C�����Ԃ�Ԃ�
	#
	def getLastLogin(self):
		return self.data["wizard_info"]["wizard_last_login"]

	#
	# �����X�^�[���X�g��Ԃ�
	#
	def getMonsterList(self):
		return self.unitList

	#
	# �����X�^�[���X�g��Ԃ�
	#
	def getRuneList(self):
		return self.runeList

	#
	# �����E�W�F���̃��X�g��Ԃ�
	#
	def getCraftItemList(self):
		return self.craftItemList
