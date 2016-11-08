#!/usr/bin/python
# -*- coding: sjis -*-

class SwEffectType:
	#
	# 効果名のハッシュを返す
	#
	def getMap(self):
		return {
			0:  "",
			1:  "体",
			2:  "体%",
			3:  "攻",
			4:  "攻%",
			5:  "防",
			6:  "防%",
			8:  "速",
			9:  "クリ",
			10: "ダメ",
			11: "抵抗",
			12: "的中"
		}