#!/usr/bin/python
# -*- coding: sjis -*-

import swMaster

class SwRune():
	def __init__(self, rune):
		self.mst = swMaster.SwMaster.getInstance()
		self.data = {}
		for k, v in rune.items():   # for/if���ł͕����̃R�����u:�v��Y��Ȃ��悤��
			if k in {
				"base_value"
				,"class"
				,"extra"
				,"occupied_id"
				,"occupied_type"
				,"prefix_eff"
				,"pri_eff"
				,"rank"
				,"rune_id"
				,"sec_eff"
				,"sell_value"
				,"set_id"
				,"slot_no"
				,"upgrade_curr"
				,"upgrade_limit"
				,"wizard_id"
			}:
				self.data[k] = rune[k]
			else:
				print(k)
				sys.exit()
		self.data["unit_id"] = ""
		self.data["unit_master_id"] = ""
		self.data["reaDo"] = 0

	#
	# ����Ԃ�
	#
	def getClass(self):
		return self.data["class"]

	#
	# �T�u�I�v��Ԃ�
	#
	def getPrefixEff(self):
		return self.data["prefix_eff"]

	#
	# ���C���I�v��Ԃ�
	#
	def getPriEff(self):
		return self.data["pri_eff"]

	#
	# ID���擾
	#
	def getRuneId(self):
		return self.data['rune_id']

	#
	# ��������Ԃ�
	#
	def getSecEff(self):
		return self.data["sec_eff"]

	#
	# ���l��Ԃ�
	#
	def getSellValue(self):
		return self.data["sell_value"]

	#
	# ���[���̃Z�b�g���̂�Ԃ�
	#
	def getRuneSetName(self):
		return self.mst.getRuneSetName(self.data['set_id'])

	#
	# �����X���b�g���擾
	#
	def getSlotNo(self):
		return self.data['slot_no']

	#
	# ��������Ԃ�
	#
	def getUpgradeCurr(self):
		return self.data["upgrade_curr"]

	#
	# �������Ă���}�X�^�[ID��Ԃ�
	#
	def getUnitMasterId(self):
		return self.data["unit_master_id"]

	#
	# �������Ă���ID��ݒ�
	#
	def setId4Shoji(self, unitId, MasterId):
		self.data["unit_id"] = unitId
		self.data["unit_master_id"] = MasterId

	#
	# ���[���̌��ʖ��̂�Ԃ�
	#
	def getEffectTypeName(self, key):
		if key == "pri":
			return self.mst.getEffectTypeName(self.data["pri_eff"][0])
		elif key == "pre":
			return self.mst.getEffectTypeName(self.data["prefix_eff"][0])
		elif key in {0, 1, 2, 3}:
			return self.mst.getEffectTypeName(self.data["sec_eff"][key][0])
		else:
			print("not EffectTypeName key = " + str(key))

	#
	# ���[���̌��ʒl��Ԃ�
	#
	def getEffectValue(self, key):
		if key == "pri":
			return self.data["pri_eff"][1]
		elif key == "pre":
			if self.data["prefix_eff"][0] == 0 and self.data["prefix_eff"][1] == 0:
				return ""
			else:
				return self.data["prefix_eff"][1]
		elif key in {0, 1, 2, 3}:
			return self.data["sec_eff"][key][1]
		else:
			print("not getEffectValue key = " + str(key))

	#
	# ���[���̗����l��Ԃ�
	#
	def getRenmaEffectValue(self, key):
		if key in {0, 1, 2, 3}:
			return self.data["sec_eff"][key][3]
		else:
			print("not getEffectValue key = " + str(key))

	#
	# ���A�x��Ԃ�
	#
	def getReaDo(self):
		return self.data["reaDo"]

	#
	# ���A�x��ݒ�
	#
	def setReaDo(self, val):
		self.data["reaDo"] = val

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
	def getEfficiency(self):
		sum = 0
		for eff in [self.data['prefix_eff']] + self.data['sec_eff']:
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
		sum += 1 if self.data['class'] == 6 else 0.85
		return sum / 2.8

	def getUriComment(self):
		uri = ""
		uricomment = ""
		if self.data["reaDo"] == 6: # ���A
			if self.data["sec_eff"][0][0] in [1,3,5]: # 1:�́A3:�U�A5:�h
				uri = "��"
				uricomment = "1�Ԏ���"
			if self.data["sec_eff"][1][0] in [1,3,5]:
				uri = "��"
				uricomment = "2�Ԏ���"
			if self.data["slot_no"] in [2,4,6]:
				uri = ""
				uricomment = ""
			if uri == "":
				if self.data["sec_eff"][0][0] == 8 or self.data["sec_eff"][1][0] == 8:# ���x
					if self.data["class"] == 5 and \
						((self.data["sec_eff"][0][0] == 8 and self.data["sec_eff"][0][1] == 3) or \
						 (self.data["sec_eff"][1][0] == 8 and self.data["sec_eff"][1][1] == 3)):# ���x:3
						uri = "��"
						uricomment = "���x3"
					else:
						uri = ""
						uricomment = ""
				elif self.data["slot_no"] in [2,4,6]: # �X���b�g��2,4,6
					uri = ""
					uricomment = ""
				elif self.data["sec_eff"][0][0] in [9, 10] and self.data["sec_eff"][1][0] in [9, 10]: # 9:�N���A10:�_��
					uri = ""
					uricomment = ""
				else:
					uri = "��3"
					uricomment = "���x�Ȃ��A�N���Ȃ��A�_���Ȃ�"
		if self.data["reaDo"] == 9: # �q�[���[
			if self.data["sec_eff"][0][0] in [1,3,5]:
				uri = "��4"
				uricomment = "1�Ԏ���"
			if self.data["sec_eff"][1][0] in [1,3,5]:
				uri = "��5"
				uricomment = "2�Ԏ���"
			if self.data["sec_eff"][2][0] in [1,3,5]:
				uri = "��6"
				uricomment = "3�Ԏ���"
			if self.data["slot_no"] in [2,4,6]:
				uri = ""
				uricomment = ""
			if uri != "":
				if self.data["sec_eff"][0][0] == 8:
					uri = ""
					uricomment = ""
				if self.data["sec_eff"][1][0] == 8:
					uri = ""
					uricomment = ""
				if self.data["sec_eff"][2][0] == 8:
					uri = ""
					uricomment = ""
		return [uri,uricomment]

	def getRank(self):
		return len(self.data["sec_eff"])


