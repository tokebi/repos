#!/usr/bin/python
# -*- coding: sjis -*-

import math
import sys

import swData
import swInitRune
import swMaster
import swOutputExcel
import swToukei

class MAIN:
	def __init__(self):
		#マスターデータの初期化
		self.mst = swMaster.SwMaster.getInstance()
		self.toukei = swToukei.SwToukei()
		self.initRune = swInitRune.SwInitRune()
		self.outputExcel = swOutputExcel.SwOutputExcel()
		self.unit_master_hash = {}
		self.data = swData.SwData()
		
	def main(self):
		self.last_login = self.data.getLastLogin()
		self.outputUnitList()
		self.outputCraftItemList()
		# Excel出力
		self.outputExcel.save()

	# 
	# モンスター・ルーンデータ処理
	# 
	def outputUnitList(self):
		no = 1
		for unit in self.data.getMonsterList():
			#print(unit.getUnitId())
			# 日本語モンスター名を設定
			jname = self.getJName(unit)
			unit.setJName(jname)
			if self.mst.isNotOutputMonster(unit.getJName()):
				continue
			#モンスターデータの出力
			self.outputMonster(no, unit)
			# 所持ルーン処理
			runes = unit.getRunes()
			for w_slot_no in range(1, 7):
				isFound=False
				for rune in runes:
					if rune.getSlotNo() == w_slot_no:
						rune.setId4Shoji(unit.getUnitId(), unit.getJName())
						self.outputExcel.writeMonsterData([rune.getRuneId()])
						isFound = True
				if isFound == False:
					self.outputExcel.writeMonsterData([1])
			# モンスタータイプ処理
			self.outputMonsterType(unit)
			
			no += 1
			# 統計処理
			self.toukei.addMonster(unit.getClass(), unit.getUnitLevel(), unit.getAttribute())
			# スキル
			skillno = 1
			#      0   1 2  3 4  5 6  7 8  9   10 11 12 13  14 15 16 17  18 19 20 21  22
			arr = ["" ,0,0 ,0,0 ,0,0 ,0,0, "", "","","","", "","","","", "","","","", ""]
			for skill in unit.getSkills():
				skill_id = str(skill.getId())
				skill_lv = str(skill.getLevel())
				#print (skillno)
				arr[(skillno-1)*2+1] = skill_lv
				arr[(skillno-1)*2+2] = self.mst.getSkillMaxLev(skill_id)
				# スキル倍率
				arr[(skillno-1)+10] = self.mst.getSkillRate(skill_id)
				# スキルコメント
				arr[(skillno-1)+18] = self.mst.getSkillComment(skill_id)
				# スキル略称
				arr[(skillno-1)+14] = self.mst.getSkillRyaku(skill_id)
				skillno += 1
			# 覚醒名称
			arr[9] = self.mst.getKakuseiName(unit.getUnitMasterId())
			# リーダスキル
			arr[22] = self.mst.getLSkillComment(unit.getUnitMasterId())
			self.outputExcel.writeMonsterData(arr)
			self.outputExcel.writeMonsterNextRow()
		# 未装備の場合のルーンを作成
		noRune = [""] * 34
		noRune[0] = 1
		noRune[1] = 1
		self.outputExcel.writeRuneData(noRune)
		self.outputExcel.writeRuneNextRow()
		## ルーンを生成
		no = 2
		for rune in self.data.getRuneList():
			self.outputRune(rune, no);
			self.outputExcel.writeRuneNextRow()
			no += 1
		# 統計データ出力
		self.toukei.outputData()

	
	#
	# モンスターデータを出力
	#
	def outputMonster(self, no, unit):
		arr = [
				no
				,unit.getUnitId()
				,unit.getJName()
				,unit.getUnitLevel()
				,unit.getClass()
				,unit.getAttributeName()
				,unit.getCon()
				,unit.getAtk()
				,unit.getDef()
				,unit.getSpd()
				,unit.getCriticalRate()
				,unit.getCriticalDamage()
				,unit.getResist()
				,unit.getAccuracy()
				,unit.getCreateTime()
		]
		self.outputExcel.writeMonsterData(arr)

	#
	# モンスター種類データを出力
	#
	# 1:体力
	# 2:体力%
	# 3:攻撃
	# 4:攻撃%
	# 5:防御
	# 6:防御%
	# 8:速度
	# 9:クリ
	#10:ダメ
	#11:抵抗
	#12:的中
	def outputMonsterType(self, unit):
		# ★数とレベル
		wbCalc = unit.getLevel() * unit.getClass() * 10
		# ルーン
		unit_id = unit.getUnitMasterId()
		type = self.mst.getMonsterTypeName(unit_id)
		for rune in unit.getRunes():
			# ★数と強化数
			wbCalc = wbCalc + rune.getClass() + rune.getUpgradeCurr() * 10
			for eff in [rune.getPriEff()] + [rune.getPrefixEff()] + rune.getSecEff():
				typ = eff[0]
				if len(eff) == 2:
					value = eff[1]
				else:
					value = eff[1]+eff[3]
				if type == "攻撃系":
					if typ in [4,9,10]: # 4:攻撃% 9:クリ 10:ダメ
						wbCalc = wbCalc + value
				if type == "防御系":
					if typ in [6,9,10]:# 6:防御% 9:クリ 10:ダメ
						wbCalc = wbCalc + value
				if type == "サポート系":
					if typ in [8]: # 8:速度 
						wbCalc = wbCalc + value * 6
					if typ in [6,12]: # # 6:防御% #12:的中
						wbCalc = wbCalc + value
				if type == "体力系":    # 2:体力%
					if typ in [2]:
						wbCalc = wbCalc + value
		# 属性
		if   unit.getAttributeName() == "水":
			wbCalc = wbCalc + 1000 * (1.5+1)	# 水＞火　水＝水
		elif unit.getAttributeName() == "火":
			wbCalc = wbCalc + 1000 * (1+0.5)	# 火＝火　火＜水
		elif unit.getAttributeName() == "風":
			wbCalc = wbCalc + 1000 * (0.5+1.5)	# 風＜火　風＞水
		elif unit.getAttributeName() == "光":
			wbCalc = wbCalc + 1000 * (1+1)		# 光＝火　光＝水
		elif unit.getAttributeName() == "闇":
			wbCalc = wbCalc + 1000 * (1+1)		# 闇＝火　闇＝水
		arr = [
			"",
			type,
			wbCalc
		]
		self.outputExcel.writeMonsterData(arr)

	#
	# ルーンテーブルを出力
	#
	def outputRune(self, rune, no):
		arr = []
		arr.append(no)
		arr.append(rune.getRuneId())
		arr.append(rune.getSlotNo())
		arr.append(rune.getUnitMasterId())
		arr.append('★'+ str(rune.getClass()))
		arr.append(rune.getUpgradeCurr())
		arr.append(rune.getRuneSetName())
		# メイン効果
		arr.append(rune.getEffectTypeName("pri"))
		arr.append(rune.getEffectValue("pri"))
		# サブメイン効果
		arr.append(rune.getEffectTypeName("pre"))
		arr.append(rune.getEffectValue("pre"))
		self.setExcelColorYellow(rune.getEffectTypeName("pre"))
		# オプ１〜４効果
		arr.extend(self.getSecEff(rune, 0))
		arr.extend(self.getSecEff(rune, 1))
		arr.extend(self.getSecEff(rune, 2))
		arr.extend(self.getSecEff(rune, 3))
		# 効率
		arr.append(rune.getEfficiency())
		# Excel出力
		arr.append( '★'+ str(rune.getClass()) + "(" + str(rune.getReaDo()) + ")+" + str(rune.getUpgradeCurr()))
		arr.append(int(math.ceil(rune.getReaDo() - int(rune.getUpgradeCurr()))/3))
		#arre = arr[:]
		# Excel用
		row = str(self.outputExcel.getRuneRone()+1)
		arr.append('=IF(J' + row + '="体%" ,K' + row + ',   IF(L' + row + '="体%" ,M' + row + ',   IF(N' + row + '="体%" ,O' + row + ',   IF(P' + row + '="体%" ,Q' + row + ',   IF(R' + row + '="体%" ,S' + row + ',0)))))')	# 体%有無
		arr.append('=IF(J' + row + '="攻%" ,K' + row + ',   IF(L' + row + '="攻%" ,M' + row + ',   IF(N' + row + '="攻%" ,O' + row + ',   IF(P' + row + '="攻%" ,Q' + row + ',   IF(R' + row + '="攻%" ,S' + row + ',0)))))')	# 攻%有無
		arr.append('=IF(J' + row + '="防%" ,K' + row + ',   IF(L' + row + '="防%" ,M' + row + ',   IF(N' + row + '="防%" ,O' + row + ',   IF(P' + row + '="防%" ,Q' + row + ',   IF(R' + row + '="防%" ,S' + row + ',0)))))')	# 防%有無
		arr.append('=IF(J' + row + '="速"  ,K' + row + ',   IF(L' + row + '="速"  ,M' + row + ',   IF(N' + row + '="速"  ,O' + row + ',   IF(P' + row + '="速"  ,Q' + row + ',   IF(R' + row + '="速"  ,S' + row + ',0)))))')	# 速 有無
		arr.append('=IF(J' + row + '="クリ",K' + row + ',   IF(L' + row + '="クリ",M' + row + ',   IF(N' + row + '="クリ",O' + row + ',   IF(P' + row + '="クリ",Q' + row + ',   IF(R' + row + '="クリ",S' + row + ',0)))))')	# クリ有無
		arr.append('=IF(J' + row + '="ダメ",K' + row + ',   IF(L' + row + '="ダメ",M' + row + ',   IF(N' + row + '="ダメ",O' + row + ',   IF(P' + row + '="ダメ",Q' + row + ',   IF(R' + row + '="ダメ",S' + row + ',0)))))')	# ダメ有無
		arr.append('=IF(J' + row + '="抵抗",K' + row + ',   IF(L' + row + '="抵抗",M' + row + ',   IF(N' + row + '="抵抗",O' + row + ',   IF(P' + row + '="抵抗",Q' + row + ',   IF(R' + row + '="抵抗",S' + row + ',0)))))')	# 抵抗有無
		arr.append('=IF(J' + row + '="的中",K' + row + ',   IF(L' + row + '="的中",M' + row + ',   IF(N' + row + '="的中",O' + row + ',   IF(P' + row + '="的中",Q' + row + ',   IF(R' + row + '="的中",S' + row + ',0)))))')	# 的中有無
		# 価格
		arr.append(rune.getSellValue())
		# 売りかどうか
		uri, uricomment = rune.getUriComment()
		
		arr.append(uri)
		arr.append(uricomment)
		arr.append(self.initRune.getDropRank(rune, self.last_login))

		# ルーン統計処理
		self.toukei.addRune(rune.getClass())
		self.outputExcel.writeRuneData(arr)

	#
	# サブオプを取得
	#
	def getSecEff(self,  rune, effno):
		if len(rune.getSecEff()) >= effno+1:
			rune.setReaDo((effno+1) * 3)
			return [
				rune.getEffectTypeName(effno)
				,rune.getEffectValue(effno) +
				 rune.getRenmaEffectValue(effno)
			]
		else:
			return ["",""]

	def setExcelColorYellow(self, type):
		# オプ効果が%系ならばExcelセルを緑色にする
		if type == "体%":
			self.outputExcel.setRuneColorYellow(22)
		elif type == "攻%":
			self.outputExcel.setRuneColorYellow(23)
		elif type == "防%":
			self.outputExcel.setRuneColorYellow(24)
		elif type == "速":
			self.outputExcel.setRuneColorYellow(25)
		elif type == "クリ":
			self.outputExcel.setRuneColorYellow(26)
		elif type == "ダメ":
			self.outputExcel.setRuneColorYellow(27)
		elif type == "抵抗":
			self.outputExcel.setRuneColorYellow(28)
		elif type == "的中":
			self.outputExcel.setRuneColorYellow(29)

	#
	# モンスター名の日本語を取得
	#
	def getJName(self, unit):
		jname = self.mst.getMonsterName(
			unit.getUnitMasterId(), unit.getAttribute)
		if jname in self.unit_master_hash:
			# 既に同じ名前のモンスターがいたら
			self.unit_master_hash[jname] += 1
			jname = jname + "_" + str(self.unit_master_hash[jname])
		else:
			self.unit_master_hash[jname] = 1
		if (jname is None):
			print("日本語名称が見つからない：ID=" + str(unit.getUnitMasterId()))
			sys.exit()
		return jname

	# 
	# 練磨・ジェムの処理
	# 
	def outputCraftItemList(self):
		no = 1
		for craftItem in self.data.getCraftItemList():
			craftTypeId = '{0:06d}'.format(craftItem["craft_type_id"])
			# 元気等
			runeSet = craftTypeId[0:2]
			runeSetName = self.mst.getRuneSetName(int(runeSet))
			# 攻撃等
			effectType = craftTypeId[2:4]
			effectTypeName = self.mst.getEffectTypeName(int(effectType))
			# 魔法等
			rarity = craftTypeId[4:6]
			#02	魔法
			#03	レア
			#04	ヒーロー
			if rarity == "01":
				rarityName = "通常"
			elif rarity == "02":
				rarityName = "+2%〜5%"
			elif rarity == "03":
				rarityName = "+3%〜6%"
			elif rarity == "04":
				rarityName = "+4%〜7%"
			elif rarity == "05":
				rarityName = "レジェント"
			if craftItem["craft_type"] == 1:
				craftType = "ジェム"
			elif craftItem["craft_type"] == 2:
				craftType = "練磨"
			arr = [
				no
				,craftItem["craft_item_id"]
				,craftItem["sell_value"]
				,craftItem["craft_type_id"]
				,craftItem["wizard_id"]
				,craftItem["craft_type"]
				,runeSet
				,effectType
				,rarity
				,runeSetName
				,effectTypeName
				,rarityName
				,craftType
			]
			self.outputExcel.writeCraftItemData(arr)
			no+=1


if __name__ == "__main__":
	a = MAIN()
	a.main()

