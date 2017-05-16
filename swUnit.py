#!/usr/bin/python
# -*- coding: sjis -*-

import swMaster
from swRune import SwRune
from swSkill  import SwSkill

class SwUnit:
	def __init__(self, unit):
		self.mst = swMaster.SwMaster.getInstance()
		self.data = {}
		for k, v in unit.items():   # for/if文では文末のコロン「:」を忘れないように
			if k in {
				"accuracy"
				,"atk"
				,"attribute"
				,"building_id"
				,"class"
				,"con"
				,"costume_master_id"
				,"create_time"
				,"critical_damage"
				,"critical_rate"
				,"def"
				,"exp_gain_rate"
				,"exp_gained"
				,"experience"
				,"homunculus"
				,"homunculus_name"
				,"island_id"
				,"pos_x"
				,"pos_y"
				,"resist"
				,"runes"
				,"skills"
				,"source"
				,"spd"
				,"trans_items"
				,"unit_id"
				,"unit_level"
				,"unit_master_id"
				,"wizard_id"
			}:
				self.data[k] = unit[k]
			else:
				print(k)
				sys.exit()
		runes = []
		for rune in self.data['runes']:
			swRune = SwRune(rune)
			runes.append(swRune)
		self.data['runes'] = runes
		skills = []
		for skill in self.data['skills']:
			swSkill = SwSkill(skill)
			skills.append(swSkill)
		self.data['skills'] = skills

	#
	# 倉庫に入っているかを取得
	#
	def isSouko(self):
		if self.data["building_id" ] == 9384277:
			return 1
		else:
			return 0

	#
	# モンスターIDを取得
	#
	def getUnitId(self):
		return self.data["unit_id"]

	#
	# モンスターマスターIDを取得
	#
	def getUnitMasterId(self):
		return self.data["unit_master_id"]

	#
	# モンスターの日本語名を設定
	#
	def setJName(self, jname):
		self.data["jname"] = jname

	#
	# モンスターの日本語名を取得
	#
	def getJName(self):
		return self.data["jname"]

	#
	# モンスターレベルを取得
	#
	def getUnitLevel(self):
		return self.data["unit_level"]

	#
	# 星レベルを取得
	#
	def getClass(self):
		return self.data["class"]

	#
	# 属性を取得
	#
	def getAttribute(self):
		return self.data["attribute"]

	#
	# 属性の日本名を取得
	#
	def getAttributeName(self):
		attribute = self.data["attribute"]
		return self.mst.getAttributeName(attribute)

	#
	# 体力を取得
	#
	def getCon(self):
		return self.data["con"]*15

	#
	# 攻撃力を取得
	#
	def getAtk(self):
		return self.data["atk"]

	#
	# 防御力を取得
	#
	def getDef(self):
		return self.data["def"]

	#
	# 攻撃速度を取得
	#
	def getSpd(self):
		
		return self.data["spd"]

	#
	# モンスターレベルを取得
	#
	def getCriticalRate(self):
		
		return self.data["critical_rate"]

	#
	# クリダメを取得
	#
	def getCriticalDamage(self):
		return self.data["critical_damage"]

	#
	# 抵抗を取得
	#
	def getResist(self):
		return self.data["resist"]

	#
	# 的中を取得
	#
	def getAccuracy(self):
		return self.data["accuracy"]

	#
	# 作成日時を取得
	#
	def getCreateTime(self):
		return self.data["create_time"]

	#
	# レベルを取得
	#
	def getLevel(self):
		return self.data["unit_level"]

	#
	# 所持ルーンを取得
	#
	def getRunes(self):
		return self.data["runes"]

	#
	# スキルを取得
	#
	def getSkills(self):
		return self.data["skills"]







