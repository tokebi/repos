#!/usr/bin/python
# -*- coding: sjis -*-

from lib.swMaster import SwMaster

class SwInventory():
	def __init__(self, craftItem):
		#マスターデータの初期化
		self.__mst = SwMaster.getInstance()
		self.__masterType = craftItem["item_master_type"]
		self.__quantity   = craftItem["item_quantity"]
		self.__masterId   = craftItem["item_master_id"]

	def __getJName(self):
		#item_master_type	item_quantity	item_master_id
		if   self.__masterType ==  9 and self.__masterId ==  1:		return "未知の召還書"
		elif self.__masterType ==  9 and self.__masterId ==  2:		return "不思議な召還書"
		elif self.__masterType ==  9 and self.__masterId ==  3:		return "光と闇の召還書"
		elif self.__masterType ==  9 and self.__masterId ==  4:		return "水の召還書"
		elif self.__masterType ==  9 and self.__masterId ==  5:		return "火の召還書"
		elif self.__masterType ==  9 and self.__masterId ==  6:		return "風の召還書"
		elif self.__masterType ==  9 and self.__masterId ==  7:		return "伝説の召還書"
		elif self.__masterType ==  9 and self.__masterId ==  8:		return "特殊召還石"
		elif self.__masterType ==  9 and self.__masterId ==  9:		return "「伝説の召還書」の欠片"
		elif self.__masterType ==  9 and self.__masterId == 10:		return "「光と闇の召還書」の欠片"
		elif self.__masterType == 11 and self.__masterId == 11001:	return "水の聖水（下級）"
		elif self.__masterType == 11 and self.__masterId == 11002:	return "炎の聖水（下級）"
		elif self.__masterType == 11 and self.__masterId == 11003:	return "風の聖水（下級）"
		elif self.__masterType == 11 and self.__masterId == 11004:	return "光の聖水（下級）"
		elif self.__masterType == 11 and self.__masterId == 11005:	return "闇の聖水（下級）"
		elif self.__masterType == 11 and self.__masterId == 11006:	return "魔力の聖水（下級）"
		elif self.__masterType == 11 and self.__masterId == 12001:	return "水の聖水（中級）"
		elif self.__masterType == 11 and self.__masterId == 12002:	return "炎の聖水（中級）"
		elif self.__masterType == 11 and self.__masterId == 12003:	return "風の聖水（中級）"
		elif self.__masterType == 11 and self.__masterId == 12004:	return "光の聖水（中級）"
		elif self.__masterType == 11 and self.__masterId == 12005:	return "闇の聖水（中級）"
		elif self.__masterType == 11 and self.__masterId == 12006:	return "魔力の聖水（中級）"
		elif self.__masterType == 11 and self.__masterId == 13001:	return "水の聖水（上級）"
		elif self.__masterType == 11 and self.__masterId == 13002:	return "炎の聖水（上級）"
		elif self.__masterType == 11 and self.__masterId == 13003:	return "風の聖水（上級）"
		elif self.__masterType == 11 and self.__masterId == 13004:	return "光の聖水（上級）"
		elif self.__masterType == 11 and self.__masterId == 13005:	return "闇の聖水（上級）"
		elif self.__masterType == 11 and self.__masterId == 13006:	return "魔力の聖水（上級）"
		elif self.__masterType == 12:
			# モンスター召還書の欠片
			return self.__mst.getMonsterName(self.__masterId)+"召還書の欠片"
		elif self.__masterType == 19 and self.__masterId == 19200:	return "「イフリート」の召還書の欠片"
		elif self.__masterType == 20 and self.__masterId == 1:		return "万能召還の欠片"
		elif self.__masterType == 29 and self.__masterId == 1001:	return "堅固な古木"
		elif self.__masterType == 29 and self.__masterId == 1002:	return "強靭な皮"
		elif self.__masterType == 29 and self.__masterId == 1003:	return "重厚な石材"
		elif self.__masterType == 29 and self.__masterId == 1004:	return "鋼の鉱石"
		elif self.__masterType == 29 and self.__masterId == 1005:	return "輝くミスリル"
		elif self.__masterType == 29 and self.__masterId == 1006:	return "分厚い布"
		elif self.__masterType == 29 and self.__masterId == 2001:	return "ルーンの欠片"
		elif self.__masterType == 29 and self.__masterId == 3001:	return "魔法の粉"
		elif self.__masterType == 29 and self.__masterId == 4001:	return "調和の紋章"
		elif self.__masterType == 29 and self.__masterId == 4002:	return "超越の紋章"
		elif self.__masterType == 29 and self.__masterId == 4003:	return "混沌の紋章"
		elif self.__masterType == 29 and self.__masterId == 5001:	return "凍り付いた水の結晶"
		elif self.__masterType == 29 and self.__masterId == 5002:	return "燃え上がる火の結晶"
		elif self.__masterType == 29 and self.__masterId == 5003:	return "吹き荒れる風の結晶"
		elif self.__masterType == 29 and self.__masterId == 5004:	return "眩しく輝く光の結晶"
		elif self.__masterType == 29 and self.__masterId == 5005:	return "漆黒の黒の闇の結晶"
		elif self.__masterType == 29 and self.__masterId == 6001:	return "凝縮された魔力の結晶"
		elif self.__masterType == 29 and self.__masterId == 7001:	return "純粋な魔力の結晶"
		elif self.__masterType == 37 and self.__masterId == 1:		return "練成石"
		else:													return "不明な在庫"

	#
	# 在庫種類を取得
	#
	def getMasterType(self):
		return self.__masterType

	#
	# 在庫数を取得
	#
	def getQuantity(self):
		return self.__quantity

	#
	# 在庫IDを取得
	#
	def getMasterId(self):
		return self.__masterId

	#
	# 在庫日本語名を取得
	#
	def getJName(self):
		return self.__getJName()
