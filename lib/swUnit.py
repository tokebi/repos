#!/usr/bin/python
# -*- coding: sjis -*-

from lib.swMaster import SwMaster
from lib.swRune   import SwRune
from lib.swSkill  import SwSkill

class SwUnit:
	def __init__(self, unit):
		self.__mst = SwMaster.getInstance()
		self.__data = {}
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
				self.__data[k] = unit[k]
			else:
				print(k)
				sys.exit()
		self.__data["con"            ] = self.__mst.getMonsterCon(self.__data["unit_master_id"]) / 15
		self.__data["atk"            ] = self.__mst.getMonsterAtk(self.__data["unit_master_id"])
		self.__data["def"            ] = self.__mst.getMonsterDef(self.__data["unit_master_id"])
		self.__data["spd"            ] = self.__mst.getMonsterSpd(self.__data["unit_master_id"])
		self.__data["critical_rate"  ] = self.__mst.getMonsterCri(self.__data["unit_master_id"])
		self.__data["critical_damage"] = self.__mst.getMonsterDame(self.__data["unit_master_id"])
		self.__data["resist"         ] = self.__mst.getMonsterResist(self.__data["unit_master_id"])
		self.__data["accuracy"       ] = self.__mst.getMonsterAccuracy(self.__data["unit_master_id"])
		
		runes = []
		if isinstance(self.__data['runes'], list):
			for rune in self.__data['runes']:
				swRune = SwRune(rune)
				runes.append(swRune)
		elif isinstance(self.__data['runes'], dict):
			for rune in self.__data['runes'].values():
				swRune = SwRune(rune)
				runes.append(swRune)
		else:
			print("runesが未知の変数=" + str(type(self.__data['runes'])))
		self.__data['runes'] = runes
		skills = []
		for skill in self.__data['skills']:
			swSkill = SwSkill(skill)
			skills.append(swSkill)
		if len(skills) < 4:
			for dummy in range(1, 4-len(skills)+1):
				skills.append(SwSkill([0,0]))
		self.__data['skills'] = skills

	#
	# 的中を取得
	#
	def getAccuracy(self):
		return self.__data["accuracy"]

	#
	# 攻撃力を取得
	#
	def getAtk(self):
		return self.__data["atk"]

	#
	# 属性を取得
	#
	def getAttribute(self):
		return self.__data["attribute"]

	#
	# 属性の日本名を取得
	#
	def getAttributeName(self):
		attribute = self.__data["attribute"]
		return self.__mst.getAttributeName(attribute)

	#
	# 倉庫に入っているかを取得
	#
	def isSouko(self):
		if self.__data["building_id" ] == 9384277:
			return 1
		else:
			return 0

	#
	# 星レベルを取得
	#
	def getClass(self):
		return self.__data["class"]

	#
	# 体力を取得
	#
	def getCon(self):
		return self.__data["con"]*15

	#
	# 作成日時を取得
	#
	def getCreateTime(self):
		return self.__data["create_time"]

	#
	# クリダメを取得
	#
	def getCriticalDamage(self):
		return self.__data["critical_damage"]

	#
	# モンスターレベルを取得
	#
	def getCriticalRate(self):
		
		return self.__data["critical_rate"]

	#
	# 防御力を取得
	#
	def getDef(self):
		return self.__data["def"]

	#
	# 攻撃速度を取得
	#
	def getSpd(self):
		
		return self.__data["spd"]

	#
	# 抵抗を取得
	#
	def getResist(self):
		return self.__data["resist"]

	#
	# 所持ルーンを取得
	#
	def getRunes(self):
		return self.__data["runes"]

	#
	# スキルを取得
	#
	def getSkills(self):
		return self.__data["skills"]

	#
	# モンスターIDを取得
	#
	def getUnitId(self):
		return self.__data["unit_id"]

	#
	# レベルを取得
	#
	def getLevel(self):
		return self.__data["unit_level"]

	#
	# モンスターマスターIDを取得
	#
	def getUnitMasterId(self):
		return self.__data["unit_master_id"]

	#
	# 出力対象のモンスターかを取得
	#
	def isNotOutputMonster(self):
		return self.__mst.isNotOutputMonster(self.__data["jname"])

	#
	# モンスターの日本語名を設定
	#
	def setJName(self, jname):
		self.__data["jname"] = jname

	#
	# モンスターの日本語名を取得
	#
	def getJName(self):
		return self.__data["jname"]

	#
	# 覚醒名称を取得
	def getKakuseiName(self):
		return self.__mst.getKakuseiName(self.__data["unit_master_id"])

	#
	# リーダスキルコメントを取得
	#
	def getLSkillComment(self):
		return self.__mst.getLSkillComment(self.getUnitMasterId())
