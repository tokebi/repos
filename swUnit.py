#!/usr/bin/python
# -*- coding: sjis -*-

import swMaster
from swRune import SwRune
from swSkill  import SwSkill

class SwUnit:
	def __init__(self, unit):
		self.mst = swMaster.SwMaster.getInstance()
		self.data = {}
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
			print("runes�����m�̕ϐ�=" + str(type(self.data['runes'])))
		self.data['runes'] = runes
		skills = []
		for skill in self.data['skills']:
			swSkill = SwSkill(skill)
			skills.append(swSkill)
		if len(skills) < 4:
			for dummy in range(1, 4-len(skills)+1):
				skills.append(SwSkill([0,0]))
		self.data['skills'] = skills

	#
	# �I�����擾
	#
	def getAccuracy(self):
		return self.data["accuracy"]

	#
	# �U���͂��擾
	#
	def getAtk(self):
		return self.data["atk"]

	#
	# �������擾
	#
	def getAttribute(self):
		return self.data["attribute"]

	#
	# �����̓��{�����擾
	#
	def getAttributeName(self):
		attribute = self.data["attribute"]
		return self.mst.getAttributeName(attribute)

	#
	# �q�ɂɓ����Ă��邩���擾
	#
	def isSouko(self):
		if self.data["building_id" ] == 9384277:
			return 1
		else:
			return 0

	#
	# �����x�����擾
	#
	def getClass(self):
		return self.data["class"]

	#
	# �̗͂��擾
	#
	def getCon(self):
		return self.data["con"]*15

	#
	# �쐬�������擾
	#
	def getCreateTime(self):
		return self.data["create_time"]

	#
	# �N���_�����擾
	#
	def getCriticalDamage(self):
		return self.data["critical_damage"]

	#
	# �����X�^�[���x�����擾
	#
	def getCriticalRate(self):
		
		return self.data["critical_rate"]

	#
	# �h��͂��擾
	#
	def getDef(self):
		return self.data["def"]

	#
	# �U�����x���擾
	#
	def getSpd(self):
		
		return self.data["spd"]

	#
	# ��R���擾
	#
	def getResist(self):
		return self.data["resist"]

	#
	# �������[�����擾
	#
	def getRunes(self):
		return self.data["runes"]

	#
	# �X�L�����擾
	#
	def getSkills(self):
		return self.data["skills"]

	#
	# �����X�^�[ID���擾
	#
	def getUnitId(self):
		return self.data["unit_id"]

	#
	# ���x�����擾
	#
	def getLevel(self):
		return self.data["unit_level"]

	#
	# �����X�^�[�}�X�^�[ID���擾
	#
	def getUnitMasterId(self):
		return self.data["unit_master_id"]

	#
	# �o�͑Ώۂ̃����X�^�[�����擾
	#
	def isNotOutputMonster(self):
		return self.mst.isNotOutputMonster(self.data["jname"])

	#
	# �����X�^�[�̓��{�ꖼ��ݒ�
	#
	def setJName(self, jname):
		self.data["jname"] = jname

	#
	# �����X�^�[�̓��{�ꖼ���擾
	#
	def getJName(self):
		return self.data["jname"]

	#
	# �o�����̂��擾
	def getKakuseiName(self):
		return self.mst.getKakuseiName(self.data["unit_master_id"])

	#
	# ���[�_�X�L���R�����g���擾
	#
	def getLSkillComment(self):
		return self.mst.getLSkillComment(self.getUnitMasterId())