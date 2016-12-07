#!/usr/bin/python
# -*- coding: sjis -*-

import codecs
import json
import math
import os.path
import swMaster

class MAIN:
	def __init__(self):
		self.fm = open("monster.tsv", "w")
		self.fr = open("runes.tsv", "w")
		self.fs = open("skill.tsv", "w")
		self.ft = open("tokei.tsv", "w")
		#マスターデータの初期化
		self.mst = swMaster.SwMaster()
		self.unit_master_hash = {}
		self.toukei = {}
		self.toukei["★6ルーン総数"] = 0
		self.toukei["★5ルーン総数"] = 0
		self.toukei["★6モンス総数"] = 0
		self.toukei["★5モンス総数"] = 0
		
		self.toukei["★6水モンス総数"] = 0
		self.toukei["★6火モンス総数"] = 0
		self.toukei["★6風モンス総数"] = 0
		self.toukei["★6光モンス総数"] = 0
		self.toukei["★6闇モンス総数"] = 0
		
		self.toukei["★5水モンス総数"] = 0
		self.toukei["★5火モンス総数"] = 0
		self.toukei["★5風モンス総数"] = 0
		self.toukei["★5光モンス総数"] = 0
		self.toukei["★5闇モンス総数"] = 0

	def main(self):
		data = self.ReadJson("819205-swarfarm.json")
		no = 1

		for unit_list in sorted(data["unit_list"], key=lambda x:(-x['class'],x['attribute'])):
			# 日本語モンスター名を設定
			self.setJname(unit_list)
			if self.mst.isNotOutputMonster(unit_list["unit_master_id_c"]):
				continue
			# 倉庫か否か
			sort_souko = 0
			if unit_list["building_id" ] == 9384277:
				sort_souko = 1
			#モンスターデータの出力
			self.outputMonster(self.fm, no, unit_list)
			# 所持ルーン処理
			runes = unit_list["runes"]
			for w_slot_no in range(1, 7):
				isFound=False
				for rune in runes:
					if rune["slot_no"] == w_slot_no:
						rune["unit_id"] = unit_list["unit_id"]
						rune["unit_master_id"] = unit_list["unit_master_id_c"]
						data["runes"].append(rune)
						self.outputRune(self.fm, rune, 0)
						isFound=True
				if isFound == False:
					self.outputData(self.fm, [""] * (16 + 1))
			# モンスタータイプ処理
			self.outputMonsterType(self.fm, unit_list, runes)
			
			no += 1
			if unit_list["class"] == 6:
				self.toukei["★6モンス総数"] += 1
				if unit_list["attribute"] == 1: # 水
					self.toukei["★6水モンス総数"] += 1
				if unit_list["attribute"] == 2: # 火
					self.toukei["★6火モンス総数"] += 1
				if unit_list["attribute"] == 3: # 風
					self.toukei["★6風モンス総数"] += 1
				if unit_list["attribute"] == 4: # 光
					self.toukei["★6光モンス総数"] += 1
				if unit_list["attribute"] == 5: # 闇
					self.toukei["★6闇モンス総数"] += 1
			elif unit_list["class"] == 5 and unit_list["unit_level"] == 35:
				self.toukei["★5モンス総数"] += 1
				if unit_list["attribute"] == 1: # 水
					self.toukei["★5水モンス総数"] += 1
				if unit_list["attribute"] == 2: # 火
					self.toukei["★5火モンス総数"] += 1
				if unit_list["attribute"] == 3: # 風
					self.toukei["★5風モンス総数"] += 1
				if unit_list["attribute"] == 4: # 光
					self.toukei["★5光モンス総数"] += 1
				if unit_list["attribute"] == 5: # 闇
					self.toukei["★5闇モンス総数"] += 1
			# スキル
			skillno = 1
			arr = ["" ,0,0 ,0,0 ,0,0 ,0,0]
			for skill in unit_list["skills"]:
				skill_id = str(skill[0])
				skill_lv = str(skill[1])
				self.fs.write(unit_list["unit_master_id_c"] + "_" + str(skillno)+ "\t")
				self.fs.write(skill_id + "\t")
				self.fs.write(skill_lv + "\t")
				self.fs.write("\n")
				#print (skillno)
				arr[(skillno-1)*2+1] = skill_lv
				arr[(skillno-1)*2+2] = self.mst.getSkillMaxLev(skill_id)
				skillno += 1
			# 覚醒名称
			arr.append(self.mst.getKakuseiName(unit_list["unit_master_id"]))
			self.outputData(self.fm, arr)
			self.fm.write("\n")
		#ルーンを生成
		no = 1
		#sorted(data["unit_list"], key=lambda x:(-x['class'],x['attribute'])):
		for rune in data["runes"]:
			self.outputRune(self.fr, rune, no);
			#self.fr.write(str(no) + "	" + runeTag + "\n")
			self.fr.write("\n")
			no += 1
		arr = [
			self.toukei["★6モンス総数"]
			,self.toukei["★6水モンス総数"]
			,self.toukei["★6火モンス総数"]
			,self.toukei["★6風モンス総数"]
			,self.toukei["★6光モンス総数"]
			,self.toukei["★6闇モンス総数"]
			,self.toukei["★5モンス総数"]
			,self.toukei["★5水モンス総数"]
			,self.toukei["★5火モンス総数"]
			,self.toukei["★5風モンス総数"]
			,self.toukei["★5光モンス総数"]
			,self.toukei["★5闇モンス総数"]
			,self.toukei["★6ルーン総数"]
			,self.toukei["★5ルーン総数"]
		]
		self.outputData(self.ft, arr)


	#
	# モンスターデータを出力
	#
	def outputMonster(self, fm, no, unit_list):
		arr = [
				no
				,unit_list["unit_id"]
				,unit_list["unit_master_id_c"]
				,unit_list["unit_level"]
				,unit_list["class"]
				,self.mst.getAttributeName(unit_list["attribute"])
				,unit_list["con"]*15
				,unit_list["atk"]
				,unit_list["def"]
				,unit_list["spd"]
				,unit_list["critical_rate"]
				,unit_list["critical_damage"]
				,unit_list["resist"]
				,unit_list["accuracy"]
				,unit_list["create_time"]
		]
		self.outputData(fm, arr)

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
	def outputMonsterType(self, fm, unit_list, runes):
		# ★数とレベル
		wbCalc = unit_list["unit_level"] * unit_list["class"] * 10
		# ルーン
		unit_id = unit_list["unit_master_id"]
		type = self.mst.getMonsterTypeName(unit_id)
		for rune in runes:
			# ★数と強化数
			wbCalc = wbCalc + rune["class"] + rune["upgrade_curr"] * 10
			for eff in [rune["pri_eff"]] + [rune['prefix_eff']] + rune['sec_eff']:
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
		if   unit_list["attribute"] == 1: # 水
			wbCalc = wbCalc + 1000 * (1.5+1)	# 水＞火　水＝水
		elif unit_list["attribute"] == 2: # 火
			wbCalc = wbCalc + 1000 * (1+0.5)	# 火＝火　火＜水
		elif unit_list["attribute"] == 3: # 風
			wbCalc = wbCalc + 1000 * (0.5+1.5)	# 風＜火　風＞水
		elif unit_list["attribute"] == 4: # 光
			wbCalc = wbCalc + 1000 * (1+1)		# 光＝火　光＝水
		elif unit_list["attribute"] == 5: # 闇
			wbCalc = wbCalc + 1000 * (1+1)		# 闇＝火　闇＝水
		arr = [
			"",
			type,
			wbCalc
		]
		self.outputData(fm, arr)

	#
	# データをファイルに出力
	#
	def outputData(self, fm, arr):
		isFirst = True
		for one in arr:
			if isFirst:
				isFirst = False
			else:
				fm.write("\t")
			if isinstance(one, (int, float)):
				fm.write(str(one))
			else:
				fm.write(one)

	#
	# ルーンテーブルを出力
	#
	def outputRune(self, fr, rune, no):
		arr = []
		if no > 0:	# ルーン出力なら
			arr.append(no)
			arr.append(rune["rune_id"])
			arr.append(rune["slot_no"])
			if "unit_master_id" in rune:
				arr.append(rune["unit_master_id"])
			else:
				arr.append("")
		else:
			arr.append("")
		#kouritu = self.rune_efficiency(rune)
		arr.append('★'+ str(rune["class"]))
		arr.append(rune["upgrade_curr"])
		arr.append(self.mst.getRuneSetName(rune["set_id"]))
		# メイン効果
		arr.append(self.mst.getEffectTypeName(rune["pri_eff"][0]))
		arr.append(rune["pri_eff"][1])
		# オプ効果
		arr.append(self.mst.getEffectTypeName(rune["prefix_eff"][0]))
		arr.append(rune["prefix_eff"][1])
		# オプ１～４効果
		rune["reado"] = 0
		arr.extend(self.getSecEff(rune, 0))
		arr.extend(self.getSecEff(rune, 1))
		arr.extend(self.getSecEff(rune, 2))
		arr.extend(self.getSecEff(rune, 3))
		# 効率
		arr.append(self.rune_efficiency(rune))
		if no > 0:
			arr.append( '★'+ str(rune["class"]) + "(" + str(rune["reado"]) + ")+" + str(rune["upgrade_curr"]))
			arr.append(int(math.ceil(rune["reado"] - int(rune["upgrade_curr"]))/3))
			arr.append(self.getUmuValue(rune, 2))	# 体%有無
			arr.append(self.getUmuValue(rune, 4))	# 攻%有無
			arr.append(self.getUmuValue(rune, 6))	# 防%有無
			arr.append(self.getUmuValue(rune, 8))	# 速 有無
			arr.append(self.getUmuValue(rune, 9))	# クリ有無
			arr.append(self.getUmuValue(rune, 10))	# ダメ有無
			arr.append(self.getUmuValue(rune, 11))	# 抵抗有無
			arr.append(self.getUmuValue(rune, 12))	# 的中有無
			# 価格
			arr.append(rune["sell_value"])
			# 売りかどうか
			uri = ""
			uricomment = ""
			if rune["reado"] == 6: # レア
				if rune["sec_eff"][0][0] in [1,3,5]: # 1:体、3:攻、5:防
					uri = "売"
					uricomment = "1番実数"
				if rune["sec_eff"][1][0] in [1,3,5]:
					uri = "売"
					uricomment = "2番実数"
				if rune["slot_no"] in [2,4,6]:
					uri = ""
					uricomment = ""
				if uri == "":
					if rune["sec_eff"][0][0] == 8 or rune["sec_eff"][1][0] == 8:# 速度
						if rune["class"] == 5 and \
							((rune["sec_eff"][0][0] == 8 and rune["sec_eff"][0][1] == 3) or \
							 (rune["sec_eff"][1][0] == 8 and rune["sec_eff"][1][1] == 3)):# 速度:3
							uri = "売"
							uricomment = "速度3"
						else:
							uri = ""
							uricomment = ""
					elif rune["slot_no"] in [2,4,6]: # スロットが2,4,6
						uri = ""
						uricomment = ""
					elif rune["sec_eff"][0][0] in [9, 10] and rune["sec_eff"][1][0] in [9, 10]: # 9:クリ、10:ダメ
						uri = ""
						uricomment = ""
					else:
						uri = "売3"
						uricomment = "速度なし、クリなし、ダメなし"
			if rune["reado"] == 9: # ヒーロー
				if rune["sec_eff"][0][0] in [1,3,5]:
					uri = "売4"
					uricomment = "1番実数"
				if rune["sec_eff"][1][0] in [1,3,5]:
					uri = "売5"
					uricomment = "2番実数"
				if rune["sec_eff"][2][0] in [1,3,5]:
					uri = "売6"
					uricomment = "3番実数"
				if rune["slot_no"] in [2,4,6]:
					uri = ""
					uricomment = ""
				if uri != "":
					if rune["sec_eff"][0][0] == 8:
						uri = ""
						uricomment = ""
					if rune["sec_eff"][1][0] == 8:
						uri = ""
						uricomment = ""
					if rune["sec_eff"][2][0] == 8:
						uri = ""
						uricomment = ""
			arr.append(uri)
			arr.append(uricomment)
		if rune["class"] == 6:
			self.toukei["★6ルーン総数"] += 1
		elif rune["class"] == 5:
			self.toukei["★5ルーン総数"] += 1
		self.outputData(fr, arr)

	#
	# サブオプを取得
	#
	def getSecEff(self,  rune, effno):
		if len(rune["sec_eff"]) >= effno+1:
			rune["reado"] = (effno+1) * 3
			return [self.mst.getEffectTypeName(rune["sec_eff"][effno][0])
				,rune["sec_eff"][effno][1]+rune["sec_eff"][effno][3]
				]
		else:
			return ["",""]
	#
	# 数値有無を取得
	#
	def getUmuValue(self, rune, type):
		for eff in [rune['prefix_eff']] + rune['sec_eff']:
			if type == eff[0]:
				if len(eff) == 2:
					return eff[1]
				else:
					return eff[1]+eff[3]
		return ""

	#  0: ("",""),
	#  1: ("HP flat", "HP +%s"),
	#  2: ("HP%", "HP %s%%"),
	#  3: ("ATK flat", "ATK +%s"),
	#  4: ("ATK%", "ATK %s%%"),
	#  5: ("DEF flat", "DEF +%s"),
	#  6: ("DEF%", "DEF %s%%"),
	#  7: "UNKNOWN",  # ?
	#  8: ("SPD", "SPD +%s"),
	#  9: ("CRate", "CRI Rate %s%%"),
	# 10: ("CDmg", "CRI Dmg %s%%"),
	# 11: ("RES", "Resistance %s%%"),
	# 12: ("ACC", "Accuracy %s%%")
	def rune_efficiency(self, rune):
		sum = 0
		for eff in [rune['prefix_eff']] + rune['sec_eff']:
			typ = eff[0]
			if len(eff) == 2:
				value = eff[1]
			else:
				value = eff[1]+eff[3]
			max = 0
			if typ in [2, 4, 6, 11, 12]:
				max = 40.0
			elif typ == 8 or typ == 9:
				max = 30.0
			elif typ == 10:
				max = 35.0
			if max > 0:
				sum += (value / max)
		sum += 1 if rune['class'] == 6 else 0.85
		return sum / 2.8

	#
	# JSONファイルの読み込み
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
			print("819205-swarfarm.jsonが存在しない")
			os.exit()
		return json.load(f)

	#
	# モンスター名の日本語を取得
	#
	def setJname(self, unit_list):
		jname = self.mst.getMonsterName(unit_list["unit_master_id"], unit_list["attribute"])
		if jname in self.unit_master_hash:
			# 既に同じ名前のモンスターがいたら
			self.unit_master_hash[jname] += 1
			jname = jname + "_" + str(self.unit_master_hash[jname])
		else:
			self.unit_master_hash[jname] = 1
		unit_list["unit_master_id_c"] = jname

if __name__ == "__main__":
	a = MAIN()
	a.main()

