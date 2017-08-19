#!/usr/bin/python
# -*- coding: sjis -*-

from lib.swMaster import SwMaster
from lib.swRune   import SwRune
from lib.swSkill  import SwSkill

class SwUnit:
	def __init__(self, unit):
		self.__mst = SwMaster.getInstance()
		self.__data = {}
		for k, v in unit.items():   # for/if���ł͕����̃R�����u:�v��Y��Ȃ��悤��
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
			print("runes�����m�̕ϐ�=" + str(type(self.__data['runes'])))
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
	# �I�����擾
	#
	def getAccuracy(self):
		return self.__data["accuracy"]

	#
	# �U���͂��擾
	#
	def getAtk(self):
		return self.__data["atk"]

	#
	# �������擾
	#
	def getAttribute(self):
		return self.__data["attribute"]

	#
	# �����̓��{�����擾
	#
	def getAttributeName(self):
		attribute = self.__data["attribute"]
		return self.__mst.getAttributeName(attribute)

	#
	# �q�ɂɓ����Ă��邩���擾
	#
	def isSouko(self):
		if self.__data["building_id" ] == 9384277:
			return 1
		else:
			return 0

	#
	# �����x�����擾
	#
	def getClass(self):
		return self.__data["class"]

	#
	# �̗͂��擾
	#
	def getCon(self):
		return self.__data["con"]*15

	#
	# �쐬�������擾
	#
	def getCreateTime(self):
		return self.__data["create_time"]

	#
	# �N���_�����擾
	#
	def getCriticalDamage(self):
		return self.__data["critical_damage"]

	#
	# �����X�^�[���x�����擾
	#
	def getCriticalRate(self):
		
		return self.__data["critical_rate"]

	#
	# �h��͂��擾
	#
	def getDef(self):
		return self.__data["def"]

	#
	# �U�����x���擾
	#
	def getSpd(self):
		
		return self.__data["spd"]

	#
	# ��R���擾
	#
	def getResist(self):
		return self.__data["resist"]

	#
	# �������[�����擾
	#
	def getRunes(self):
		return self.__data["runes"]

	#
	# �X�L�����擾
	#
	def getSkills(self):
		return self.__data["skills"]

	#
	# �����X�^�[ID���擾
	#
	def getUnitId(self):
		return self.__data["unit_id"]

	#
	# ���x�����擾
	#
	def getLevel(self):
		return self.__data["unit_level"]

	#
	# �����X�^�[�}�X�^�[ID���擾
	#
	def getUnitMasterId(self):
		return self.__data["unit_master_id"]

	#
	# �o�͑Ώۂ̃����X�^�[�����擾
	#
	def isNotOutputMonster(self):
		return self.__mst.isNotOutputMonster(self.__data["jname"])

	#
	# �����X�^�[�̓��{�ꖼ��ݒ�
	#
	def setJName(self, jname):
		self.__data["jname"] = jname

	#
	# �����X�^�[�̓��{�ꖼ���擾
	#
	def getJName(self):
		return self.__data["jname"]

	#
	# �o�����̂��擾
	def getKakuseiName(self):
		return self.__mst.getKakuseiName(self.__data["unit_master_id"])

	#
	# ���[�_�X�L���R�����g���擾
	#
	def getLSkillComment(self):
		return self.__mst.getLSkillComment(self.getUnitMasterId())
