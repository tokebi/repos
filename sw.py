#!/usr/bin/python
# -*- coding: sjis -*-

import codecs
import json
import math
import os.path
import swMaster
import swToukei
import swOutputExcel

class MAIN:
	def __init__(self):
		self.fm = open("monster.tsv", "w")
		self.fr = open("runes.tsv", "w")
		self.fs = open("skill.tsv", "w")
		#�}�X�^�[�f�[�^�̏�����
		self.mst = swMaster.SwMaster()
		self.toukei = swToukei.SwToukei()
		self.outputExcel = swOutputExcel.SwOutputExcel()
		self.unit_master_hash = {}

	def main(self):
		data = self.ReadJson("819205-swarfarm.json")
		no = 1

		for unit_list in sorted(data["unit_list"], key=lambda x:(-x['class'],x['attribute'])):
			# ���{�ꃂ���X�^�[����ݒ�
			self.setJname(unit_list)
			if (unit_list["unit_master_id_c"] is None):
				print(unit_list["unit_master_id"])
			if self.mst.isNotOutputMonster(unit_list["unit_master_id_c"]):
				continue
			# �q�ɂ��ۂ�
			sort_souko = 0
			if unit_list["building_id" ] == 9384277:
				sort_souko = 1
			#�����X�^�[�f�[�^�̏o��
			self.outputMonster(self.fm, no, unit_list)
			# �������[������
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
					self.outputExcel.writeMonsterData([""] * (16 + 1))
			# �����X�^�[�^�C�v����
			self.outputMonsterType(self.fm, unit_list, runes)
			
			no += 1
			# ���v����
			self.toukei.addMonster(unit_list["class"], unit_list["unit_level"], unit_list["attribute"])
			# �X�L��
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
			# �o������
			arr.append(self.mst.getKakuseiName(unit_list["unit_master_id"]))
			self.outputData(self.fm, arr)
			self.outputExcel.writeMonsterData(arr)
			self.fm.write("\n")
			self.outputExcel.writeMonsterNextRow()
		#���[���𐶐�
		no = 1
		#sorted(data["unit_list"], key=lambda x:(-x['class'],x['attribute'])):
		for rune in data["runes"]:
			self.outputRune(self.fr, rune, no);
			#self.fr.write(str(no) + "	" + runeTag + "\n")
			self.fr.write("\n")
			self.outputExcel.writeRuneNextRow()
			no += 1
		# ���v�f�[�^�o��
		self.toukei.outputData()
		# Excel�o��
		self.outputExcel.save()
	#
	# �����X�^�[�f�[�^���o��
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
		self.outputExcel.writeMonsterData(arr)

	#
	# �����X�^�[��ރf�[�^���o��
	#
	# 1:�̗�
	# 2:�̗�%
	# 3:�U��
	# 4:�U��%
	# 5:�h��
	# 6:�h��%
	# 8:���x
	# 9:�N��
	#10:�_��
	#11:��R
	#12:�I��
	def outputMonsterType(self, fm, unit_list, runes):
		# �����ƃ��x��
		wbCalc = unit_list["unit_level"] * unit_list["class"] * 10
		# ���[��
		unit_id = unit_list["unit_master_id"]
		type = self.mst.getMonsterTypeName(unit_id)
		for rune in runes:
			# �����Ƌ�����
			wbCalc = wbCalc + rune["class"] + rune["upgrade_curr"] * 10
			for eff in [rune["pri_eff"]] + [rune['prefix_eff']] + rune['sec_eff']:
				typ = eff[0]
				if len(eff) == 2:
					value = eff[1]
				else:
					value = eff[1]+eff[3]
				if type == "�U���n":
					if typ in [4,9,10]: # 4:�U��% 9:�N�� 10:�_��
						wbCalc = wbCalc + value
				if type == "�h��n":
					if typ in [6,9,10]:# 6:�h��% 9:�N�� 10:�_��
						wbCalc = wbCalc + value
				if type == "�T�|�[�g�n":
					if typ in [8]: # 8:���x 
						wbCalc = wbCalc + value * 6
					if typ in [6,12]: # # 6:�h��% #12:�I��
						wbCalc = wbCalc + value
				if type == "�̗͌n":    # 2:�̗�%
					if typ in [2]:
						wbCalc = wbCalc + value
		# ����
		if   unit_list["attribute"] == 1: # ��
			wbCalc = wbCalc + 1000 * (1.5+1)	# �����΁@������
		elif unit_list["attribute"] == 2: # ��
			wbCalc = wbCalc + 1000 * (1+0.5)	# �΁��΁@�΁���
		elif unit_list["attribute"] == 3: # ��
			wbCalc = wbCalc + 1000 * (0.5+1.5)	# �����΁@������
		elif unit_list["attribute"] == 4: # ��
			wbCalc = wbCalc + 1000 * (1+1)		# �����΁@������
		elif unit_list["attribute"] == 5: # ��
			wbCalc = wbCalc + 1000 * (1+1)		# �Ł��΁@�Ł���
		arr = [
			"",
			type,
			wbCalc
		]
		self.outputData(fm, arr)
		self.outputExcel.writeMonsterData(arr)

	#
	# �f�[�^���t�@�C���ɏo��
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
	# ���[���e�[�u�����o��
	#
	def outputRune(self, fr, rune, isRune):
		arr = []
		if isRune > 0:	# ���[���o�͂Ȃ�
			arr.append(isRune)
			arr.append(rune["rune_id"])
			arr.append(rune["slot_no"])
			if "unit_master_id" in rune:
				arr.append(rune["unit_master_id"])
			else:
				arr.append("")
		else:
			arr.append("")
		#kouritu = self.rune_efficiency(rune)
		arr.append('��'+ str(rune["class"]))
		arr.append(rune["upgrade_curr"])
		arr.append(self.mst.getRuneSetName(rune["set_id"]))
		# ���C������
		arr.append(self.mst.getEffectTypeName(rune["pri_eff"][0]))
		arr.append(rune["pri_eff"][1])
		# �I�v����
		arr.append(self.mst.getEffectTypeName(rune["prefix_eff"][0]))
		if rune["prefix_eff"][0] == 0 and rune["prefix_eff"][1] == 0:
			arr.append("")
		else:
			arr.append(rune["prefix_eff"][1])
		# �I�v�P�`�S����
		rune["reado"] = 0
		arr.extend(self.getSecEff(rune, 0))
		arr.extend(self.getSecEff(rune, 1))
		arr.extend(self.getSecEff(rune, 2))
		arr.extend(self.getSecEff(rune, 3))
		# ����
		arr.append(self.rune_efficiency(rune))
		arre = []
		# Excel�o��
		if isRune == 0:
			self.outputExcel.writeMonsterData(arr)
		if isRune > 0: # ���[���o�͂̂ݑΏ�
			arr.append( '��'+ str(rune["class"]) + "(" + str(rune["reado"]) + ")+" + str(rune["upgrade_curr"]))
			arr.append(int(math.ceil(rune["reado"] - int(rune["upgrade_curr"]))/3))
			arre = arr[:]
			# tsv�p
			arr.append(self.getUmuValue(rune, 2))	# ��%�L��
			arr.append(self.getUmuValue(rune, 4))	# �U%�L��
			arr.append(self.getUmuValue(rune, 6))	# �h%�L��
			arr.append(self.getUmuValue(rune, 8))	# �� �L��
			arr.append(self.getUmuValue(rune, 9))	# �N���L��
			arr.append(self.getUmuValue(rune, 10))	# �_���L��
			arr.append(self.getUmuValue(rune, 11))	# ��R�L��
			arr.append(self.getUmuValue(rune, 12))	# �I���L��
			# Excel�p
			row = str(self.outputExcel.getRuneRone()+1)
			arre.append('=IF(J' + row + '="��%" ,K' + row + ',   IF(L' + row + '="��%" ,M' + row + ',   IF(N' + row + '="��%" ,O' + row + ',   IF(P' + row + '="��%" ,Q' + row + ',   IF(R' + row + '="��%" ,S' + row + ',"")))))')	# ��%�L��
			arre.append('=IF(J' + row + '="�U%" ,K' + row + ',   IF(L' + row + '="�U%" ,M' + row + ',   IF(N' + row + '="�U%" ,O' + row + ',   IF(P' + row + '="�U%" ,Q' + row + ',   IF(R' + row + '="�U%" ,S' + row + ',"")))))')	# �U%�L��
			arre.append('=IF(J' + row + '="�h%" ,K' + row + ',   IF(L' + row + '="�h%" ,M' + row + ',   IF(N' + row + '="�h%" ,O' + row + ',   IF(P' + row + '="�h%" ,Q' + row + ',   IF(R' + row + '="�h%" ,S' + row + ',"")))))')	# �h%�L��
			arre.append('=IF(J' + row + '="��"  ,K' + row + ',   IF(L' + row + '="��"  ,M' + row + ',   IF(N' + row + '="��"  ,O' + row + ',   IF(P' + row + '="��"  ,Q' + row + ',   IF(R' + row + '="��"  ,S' + row + ',"")))))')	# �� �L��
			arre.append('=IF(J' + row + '="�N��",K' + row + ',   IF(L' + row + '="�N��",M' + row + ',   IF(N' + row + '="�N��",O' + row + ',   IF(P' + row + '="�N��",Q' + row + ',   IF(R' + row + '="�N��",S' + row + ',"")))))')	# �N���L��
			arre.append('=IF(J' + row + '="�_��",K' + row + ',   IF(L' + row + '="�_��",M' + row + ',   IF(N' + row + '="�_��",O' + row + ',   IF(P' + row + '="�_��",Q' + row + ',   IF(R' + row + '="�_��",S' + row + ',"")))))')	# �_���L��
			arre.append('=IF(J' + row + '="��R",K' + row + ',   IF(L' + row + '="��R",M' + row + ',   IF(N' + row + '="��R",O' + row + ',   IF(P' + row + '="��R",Q' + row + ',   IF(R' + row + '="��R",S' + row + ',"")))))')	# ��R�L��
			arre.append('=IF(J' + row + '="�I��",K' + row + ',   IF(L' + row + '="�I��",M' + row + ',   IF(N' + row + '="�I��",O' + row + ',   IF(P' + row + '="�I��",Q' + row + ',   IF(R' + row + '="�I��",S' + row + ',"")))))')	# �I���L��
			# ���i
			arr.append(rune["sell_value"])
			arre.append(rune["sell_value"])
			# ���肩�ǂ���
			uri = ""
			uricomment = ""
			if rune["reado"] == 6: # ���A
				if rune["sec_eff"][0][0] in [1,3,5]: # 1:�́A3:�U�A5:�h
					uri = "��"
					uricomment = "1�Ԏ���"
				if rune["sec_eff"][1][0] in [1,3,5]:
					uri = "��"
					uricomment = "2�Ԏ���"
				if rune["slot_no"] in [2,4,6]:
					uri = ""
					uricomment = ""
				if uri == "":
					if rune["sec_eff"][0][0] == 8 or rune["sec_eff"][1][0] == 8:# ���x
						if rune["class"] == 5 and \
							((rune["sec_eff"][0][0] == 8 and rune["sec_eff"][0][1] == 3) or \
							 (rune["sec_eff"][1][0] == 8 and rune["sec_eff"][1][1] == 3)):# ���x:3
							uri = "��"
							uricomment = "���x3"
						else:
							uri = ""
							uricomment = ""
					elif rune["slot_no"] in [2,4,6]: # �X���b�g��2,4,6
						uri = ""
						uricomment = ""
					elif rune["sec_eff"][0][0] in [9, 10] and rune["sec_eff"][1][0] in [9, 10]: # 9:�N���A10:�_��
						uri = ""
						uricomment = ""
					else:
						uri = "��3"
						uricomment = "���x�Ȃ��A�N���Ȃ��A�_���Ȃ�"
			if rune["reado"] == 9: # �q�[���[
				if rune["sec_eff"][0][0] in [1,3,5]:
					uri = "��4"
					uricomment = "1�Ԏ���"
				if rune["sec_eff"][1][0] in [1,3,5]:
					uri = "��5"
					uricomment = "2�Ԏ���"
				if rune["sec_eff"][2][0] in [1,3,5]:
					uri = "��6"
					uricomment = "3�Ԏ���"
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
			arre.append(uri)
			arre.append(uricomment)
		# ���[�����v����
		self.toukei.addRune(rune["class"])
		self.outputData(fr, arr)
		self.outputExcel.writeRuneData(arre)

	#
	# �T�u�I�v���擾
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
	# ���l�L�����擾
	#
	def getUmuValue(self, rune, type):
		i = 0
		for eff in [rune['prefix_eff']] + rune['sec_eff']:
			if type == eff[0]:
				if i == 0: # prefix_eff�Ȃ�Z���̐F�����F�ɂ���
					self.setExcelColorYellow(type)
				if len(eff) == 2:
					return eff[1]
				else:
					return eff[1]+eff[3]
			i += 1
		return ""

	def setExcelColorYellow(self, type):
		# �I�v���ʂ�%�n�Ȃ��Excel�Z�������F�ɂ���
		if type == 2:
			self.outputExcel.setRuneColorYellow(22)
		elif type == 4:
			self.outputExcel.setRuneColorYellow(23)
		elif type == 6:
			self.outputExcel.setRuneColorYellow(24)
		elif type == 8:
			self.outputExcel.setRuneColorYellow(25)
		elif type == 9:
			self.outputExcel.setRuneColorYellow(26)
		elif type == 10:
			self.outputExcel.setRuneColorYellow(27)
		elif type == 11:
			self.outputExcel.setRuneColorYellow(28)
		elif type == 12:
			self.outputExcel.setRuneColorYellow(29)

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
	# JSON�t�@�C���̓ǂݍ���
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
			print("819205-swarfarm.json�����݂��Ȃ�")
			os.exit()
		return json.load(f)

	#
	# �����X�^�[���̓��{����擾
	#
	def setJname(self, unit_list):
		jname = self.mst.getMonsterName(unit_list["unit_master_id"], unit_list["attribute"])
		if jname in self.unit_master_hash:
			# ���ɓ������O�̃����X�^�[��������
			self.unit_master_hash[jname] += 1
			jname = jname + "_" + str(self.unit_master_hash[jname])
		else:
			self.unit_master_hash[jname] = 1
		unit_list["unit_master_id_c"] = jname

if __name__ == "__main__":
	a = MAIN()
	a.main()

