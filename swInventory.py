#!/usr/bin/python
# -*- coding: sjis -*-

import swMaster

class SwInventory():
	def __init__(self, craftItem):
		#マスターデータの初期化
		self.mst = swMaster.SwMaster.getInstance()
		self.masterType = craftItem["item_master_type"]
		self.quantity   = craftItem["item_quantity"]
		self.masterId   = craftItem["item_master_id"]
		self.JName      = self.__getJName()

	def __getJName(self):
		#item_master_type	item_quantity	item_master_id
		if   self.masterType ==  9 and self.masterId ==  1:		return "未知の召還書"
		elif self.masterType ==  9 and self.masterId ==  2:		return "不思議な召還書"
		elif self.masterType ==  9 and self.masterId ==  3:		return "伝説の召還書か光と闇の召還書か風の召還書"
		elif self.masterType ==  9 and self.masterId ==  4:		return "水の召還書"
		elif self.masterType ==  9 and self.masterId ==  5:		return "火の召還書"
		elif self.masterType ==  9 and self.masterId ==  6:		return "伝説の召還書か光と闇の召還書か風の召還書"
		elif self.masterType ==  9 and self.masterId ==  7:		return "伝説の召還書か光と闇の召還書か風の召還書"
		elif self.masterType ==  9 and self.masterId ==  8:		return "特殊召還石"
		elif self.masterType ==  9 and self.masterId ==  9:		return "「伝説の召還書」の欠片"
		elif self.masterType ==  9 and self.masterId == 10:		return "「光と闇の召還書」の欠片"
		elif self.masterType == 11 and self.masterId == 11001:	return "水の聖水（下級）"
		elif self.masterType == 11 and self.masterId == 11002:	return "炎の聖水（下級）"
		elif self.masterType == 11 and self.masterId == 11003:	return "風の聖水（下級）"
		elif self.masterType == 11 and self.masterId == 11004:	return "光の聖水（下級）"
		elif self.masterType == 11 and self.masterId == 11005:	return "闇の聖水（下級）"
		elif self.masterType == 11 and self.masterId == 11006:	return "魔力の聖水（下級）"
		elif self.masterType == 11 and self.masterId == 12001:	return "水の聖水（中級）"
		elif self.masterType == 11 and self.masterId == 12002:	return "炎の聖水（中級）"
		elif self.masterType == 11 and self.masterId == 12003:	return "風の聖水（中級）"
		elif self.masterType == 11 and self.masterId == 12004:	return "光の聖水（中級）"
		elif self.masterType == 11 and self.masterId == 12005:	return "闇の聖水（中級）"
		elif self.masterType == 11 and self.masterId == 12006:	return "魔力の聖水（中級）"
		elif self.masterType == 11 and self.masterId == 13001:	return "水の聖水（上級）"
		elif self.masterType == 11 and self.masterId == 13002:	return "炎の聖水（上級）"
		elif self.masterType == 11 and self.masterId == 13003:	return "風の聖水（上級）"
		elif self.masterType == 11 and self.masterId == 13004:	return "光の聖水（上級）"
		elif self.masterType == 11 and self.masterId == 13005:	return "闇の聖水（上級）"
		elif self.masterType == 11 and self.masterId == 13006:	return "魔力の聖水（上級）"
		elif self.masterType == 12:
			# モンスター召還書の欠片
			return self.mst.getMonsterName(self.masterId)+"召還書の欠片"
		elif self.masterType == 19 and self.masterId == 19200:	return "「イフリート」の召還書の欠片"
		elif self.masterType == 20 and self.masterId == 1:		return "万能召還の欠片"
		elif self.masterType == 29 and self.masterId == 1001:	return "堅固な古木"
		elif self.masterType == 29 and self.masterId == 1002:	return "強靭な皮"
		elif self.masterType == 29 and self.masterId == 1003:	return "重厚な石材"
		elif self.masterType == 29 and self.masterId == 1004:	return "鋼の鉱石"
		elif self.masterType == 29 and self.masterId == 1005:	return "輝くミスリル"
		elif self.masterType == 29 and self.masterId == 1006:	return "分厚い布"
		elif self.masterType == 29 and self.masterId == 2001:	return "ルーンの欠片"
		elif self.masterType == 29 and self.masterId == 3001:	return "魔法の粉"
		elif self.masterType == 29 and self.masterId == 4001:	return "調和の紋章"
		elif self.masterType == 29 and self.masterId == 4002:	return "超越の紋章"
		elif self.masterType == 29 and self.masterId == 4003:	return "混沌の紋章"
		elif self.masterType == 29 and self.masterId == 5001:	return "凍り付いた水の結晶"
		elif self.masterType == 29 and self.masterId == 5002:	return "燃え上がる火の結晶"
		elif self.masterType == 29 and self.masterId == 5003:	return "吹き荒れる風の結晶"
		elif self.masterType == 29 and self.masterId == 5004:	return "眩しく輝く光の結晶"
		elif self.masterType == 29 and self.masterId == 5005:	return "漆黒の黒の闇の結晶"
		elif self.masterType == 29 and self.masterId == 6001:	return "凝縮された魔力の結晶"
		elif self.masterType == 29 and self.masterId == 7001:	return "純粋な魔力の結晶"
		elif self.masterType == 37 and self.masterId == 1:		return "練成石"
		else:													return "不明な在庫"

	#
	# 在庫種類を取得
	#
	def getMasterType(self):
		return self.masterType

	#
	# 在庫数を取得
	#
	def getQuantity(self):
		return self.quantity

	#
	# 在庫IDを取得
	#
	def getMasterId(self):
		return self.masterId

	#
	# 在庫日本語名を取得
	#
	def getJName(self):
		return self.JName
