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
		if isinstance(self.data['runes'], list):
			for rune in self.data['runes']:
				swRune = SwRune(rune)
				runes.append(swRune)
		elif isinstance(self.data['runes'], dict):
			for rune in self.data['runes'].values():
				swRune = SwRune(rune)
				runes.append(swRune)
		else:
			print("runesが未知の変数=" + str(type(self.data['runes'])))
		self.data['runes'] = runes
		skills = []
		for skill in self.data['skills']:
			swSkill = SwSkill(skill)
			skills.append(swSkill)
		if len(skills) < 4:
			for dummy in range(1, 4-len(skills)+1):
				skills.append(SwSkill([0,0]))
		self.data['skills'] = skills
		# 値をレベル最大にする
		arr = {
			# unit_id     con  atk def spd c  d  的 抵 
			1426288509 : [ 9555,769,571,101,15,50,15,0], # 火天舞姫
			1840758667 : [ 8730,736,659,102,15,50,15,0], # 水カンフーガール
			1833892363 : [ 9885,637,681,101,15,50,40,0], # 闇デスナイト
			1293724998 : [ 7575,801,505,104,15,50,15,0], # 闇ハーピー
			1715431680 : [10380,790,329,102,15,50,15,0], # 光アマゾン
			1426259960 : [ 7575,845,461,105,15,50,15,0], # 風マジックアーチャー
			 589620128 : [ 9225,845,351,102,15,50,15,0], # 風アマゾン
			 474538221 : [ 9555,900,439,103,15,50,15,0], # 風ピエレット
		}
		for k, v in arr.items():
			if self.data["unit_id"] == k:
				self.data["con"            ] = v[0] / 15
				self.data["atk"            ] = v[1]
				self.data["def"            ] = v[2]
				self.data["spd"            ] = v[3]
				self.data["critical_rate"  ] = v[4]
				self.data["critical_damage"] = v[5]
				self.data["resist"         ] = v[6]
				self.data["accuracy"       ] = v[7]

	#
	# 的中を取得
	#
	def getAccuracy(self):
		return self.data["accuracy"]

	#
	# 攻撃力を取得
	#
	def getAtk(self):
		return self.data["atk"]

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
	# 倉庫に入っているかを取得
	#
	def isSouko(self):
		if self.data["building_id" ] == 9384277:
			return 1
		else:
			return 0

	#
	# 星レベルを取得
	#
	def getClass(self):
		return self.data["class"]

	#
	# 体力を取得
	#
	def getCon(self):
		return self.data["con"]*15

	#
	# 作成日時を取得
	#
	def getCreateTime(self):
		return self.data["create_time"]

	#
	# クリダメを取得
	#
	def getCriticalDamage(self):
		return self.data["critical_damage"]

	#
	# モンスターレベルを取得
	#
	def getCriticalRate(self):
		
		return self.data["critical_rate"]

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
	# 抵抗を取得
	#
	def getResist(self):
		return self.data["resist"]

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

	#
	# モンスターIDを取得
	#
	def getUnitId(self):
		return self.data["unit_id"]

	#
	# レベルを取得
	#
	def getLevel(self):
		return self.data["unit_level"]

	#
	# モンスターマスターIDを取得
	#
	def getUnitMasterId(self):
		return self.data["unit_master_id"]

	#
	# 出力対象のモンスターかを取得
	#
	def isNotOutputMonster(self):
		return self.mst.isNotOutputMonster(self.data["jname"])

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
	# 覚醒名称を取得
	def getKakuseiName(self):
		return self.mst.getKakuseiName(self.data["unit_master_id"])

	#
	# リーダスキルコメントを取得
	#
	def getLSkillComment(self):
		return self.mst.getLSkillComment(self.getUnitMasterId())
