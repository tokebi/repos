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
		#�}�X�^�[�f�[�^�̏�����
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
		# Excel�o��
		self.outputExcel.save()

	# 
	# �����X�^�[�E���[���f�[�^����
	# 
	def outputUnitList(self):
		no = 1
		for unit in self.data.getMonsterList():
			#print(unit.getUnitId())
			# ���{�ꃂ���X�^�[����ݒ�
			jname = self.getJName(unit)
			unit.setJName(jname)
			if self.mst.isNotOutputMonster(unit.getJName()):
				continue
			#�����X�^�[�f�[�^�̏o��
			self.outputMonster(no, unit)
			# �������[������
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
			# �����X�^�[�^�C�v����
			self.outputMonsterType(unit)
			
			no += 1
			# ���v����
			self.toukei.addMonster(unit.getClass(), unit.getUnitLevel(), unit.getAttribute())
			# �X�L��
			skillno = 1
			#      0   1 2  3 4  5 6  7 8  9   10 11 12 13  14 15 16 17  18 19 20 21  22
			arr = ["" ,0,0 ,0,0 ,0,0 ,0,0, "", "","","","", "","","","", "","","","", ""]
			for skill in unit.getSkills():
				skill_id = str(skill.getId())
				skill_lv = str(skill.getLevel())
				#print (skillno)
				arr[(skillno-1)*2+1] = skill_lv
				arr[(skillno-1)*2+2] = self.mst.getSkillMaxLev(skill_id)
				# �X�L���{��
				arr[(skillno-1)+10] = self.mst.getSkillRate(skill_id)
				# �X�L���R�����g
				arr[(skillno-1)+18] = self.mst.getSkillComment(skill_id)
				# �X�L������
				arr[(skillno-1)+14] = self.mst.getSkillRyaku(skill_id)
				skillno += 1
			# �o������
			arr[9] = self.mst.getKakuseiName(unit.getUnitMasterId())
			# ���[�_�X�L��
			arr[22] = self.mst.getLSkillComment(unit.getUnitMasterId())
			self.outputExcel.writeMonsterData(arr)
			self.outputExcel.writeMonsterNextRow()
		# �������̏ꍇ�̃��[�����쐬
		noRune = [""] * 34
		noRune[0] = 1
		noRune[1] = 1
		self.outputExcel.writeRuneData(noRune)
		self.outputExcel.writeRuneNextRow()
		## ���[���𐶐�
		no = 2
		for rune in self.data.getRuneList():
			self.outputRune(rune, no);
			self.outputExcel.writeRuneNextRow()
			no += 1
		# ���v�f�[�^�o��
		self.toukei.outputData()

	
	#
	# �����X�^�[�f�[�^���o��
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
	def outputMonsterType(self, unit):
		# �����ƃ��x��
		wbCalc = unit.getLevel() * unit.getClass() * 10
		# ���[��
		unit_id = unit.getUnitMasterId()
		type = self.mst.getMonsterTypeName(unit_id)
		for rune in unit.getRunes():
			# �����Ƌ�����
			wbCalc = wbCalc + rune.getClass() + rune.getUpgradeCurr() * 10
			for eff in [rune.getPriEff()] + [rune.getPrefixEff()] + rune.getSecEff():
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
		if   unit.getAttributeName() == "��":
			wbCalc = wbCalc + 1000 * (1.5+1)	# �����΁@������
		elif unit.getAttributeName() == "��":
			wbCalc = wbCalc + 1000 * (1+0.5)	# �΁��΁@�΁���
		elif unit.getAttributeName() == "��":
			wbCalc = wbCalc + 1000 * (0.5+1.5)	# �����΁@������
		elif unit.getAttributeName() == "��":
			wbCalc = wbCalc + 1000 * (1+1)		# �����΁@������
		elif unit.getAttributeName() == "��":
			wbCalc = wbCalc + 1000 * (1+1)		# �Ł��΁@�Ł���
		arr = [
			"",
			type,
			wbCalc
		]
		self.outputExcel.writeMonsterData(arr)

	#
	# ���[���e�[�u�����o��
	#
	def outputRune(self, rune, no):
		arr = []
		arr.append(no)
		arr.append(rune.getRuneId())
		arr.append(rune.getSlotNo())
		arr.append(rune.getUnitMasterId())
		arr.append('��'+ str(rune.getClass()))
		arr.append(rune.getUpgradeCurr())
		arr.append(rune.getRuneSetName())
		# ���C������
		arr.append(rune.getEffectTypeName("pri"))
		arr.append(rune.getEffectValue("pri"))
		# �T�u���C������
		arr.append(rune.getEffectTypeName("pre"))
		arr.append(rune.getEffectValue("pre"))
		self.setExcelColorYellow(rune.getEffectTypeName("pre"))
		# �I�v�P�`�S����
		arr.extend(self.getSecEff(rune, 0))
		arr.extend(self.getSecEff(rune, 1))
		arr.extend(self.getSecEff(rune, 2))
		arr.extend(self.getSecEff(rune, 3))
		# ����
		arr.append(rune.getEfficiency())
		# Excel�o��
		arr.append( '��'+ str(rune.getClass()) + "(" + str(rune.getReaDo()) + ")+" + str(rune.getUpgradeCurr()))
		arr.append(int(math.ceil(rune.getReaDo() - int(rune.getUpgradeCurr()))/3))
		#arre = arr[:]
		# Excel�p
		row = str(self.outputExcel.getRuneRone()+1)
		arr.append('=IF(J' + row + '="��%" ,K' + row + ',   IF(L' + row + '="��%" ,M' + row + ',   IF(N' + row + '="��%" ,O' + row + ',   IF(P' + row + '="��%" ,Q' + row + ',   IF(R' + row + '="��%" ,S' + row + ',0)))))')	# ��%�L��
		arr.append('=IF(J' + row + '="�U%" ,K' + row + ',   IF(L' + row + '="�U%" ,M' + row + ',   IF(N' + row + '="�U%" ,O' + row + ',   IF(P' + row + '="�U%" ,Q' + row + ',   IF(R' + row + '="�U%" ,S' + row + ',0)))))')	# �U%�L��
		arr.append('=IF(J' + row + '="�h%" ,K' + row + ',   IF(L' + row + '="�h%" ,M' + row + ',   IF(N' + row + '="�h%" ,O' + row + ',   IF(P' + row + '="�h%" ,Q' + row + ',   IF(R' + row + '="�h%" ,S' + row + ',0)))))')	# �h%�L��
		arr.append('=IF(J' + row + '="��"  ,K' + row + ',   IF(L' + row + '="��"  ,M' + row + ',   IF(N' + row + '="��"  ,O' + row + ',   IF(P' + row + '="��"  ,Q' + row + ',   IF(R' + row + '="��"  ,S' + row + ',0)))))')	# �� �L��
		arr.append('=IF(J' + row + '="�N��",K' + row + ',   IF(L' + row + '="�N��",M' + row + ',   IF(N' + row + '="�N��",O' + row + ',   IF(P' + row + '="�N��",Q' + row + ',   IF(R' + row + '="�N��",S' + row + ',0)))))')	# �N���L��
		arr.append('=IF(J' + row + '="�_��",K' + row + ',   IF(L' + row + '="�_��",M' + row + ',   IF(N' + row + '="�_��",O' + row + ',   IF(P' + row + '="�_��",Q' + row + ',   IF(R' + row + '="�_��",S' + row + ',0)))))')	# �_���L��
		arr.append('=IF(J' + row + '="��R",K' + row + ',   IF(L' + row + '="��R",M' + row + ',   IF(N' + row + '="��R",O' + row + ',   IF(P' + row + '="��R",Q' + row + ',   IF(R' + row + '="��R",S' + row + ',0)))))')	# ��R�L��
		arr.append('=IF(J' + row + '="�I��",K' + row + ',   IF(L' + row + '="�I��",M' + row + ',   IF(N' + row + '="�I��",O' + row + ',   IF(P' + row + '="�I��",Q' + row + ',   IF(R' + row + '="�I��",S' + row + ',0)))))')	# �I���L��
		# ���i
		arr.append(rune.getSellValue())
		# ���肩�ǂ���
		uri, uricomment = rune.getUriComment()
		
		arr.append(uri)
		arr.append(uricomment)
		arr.append(self.initRune.getDropRank(rune, self.last_login))

		# ���[�����v����
		self.toukei.addRune(rune.getClass())
		self.outputExcel.writeRuneData(arr)

	#
	# �T�u�I�v���擾
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
		# �I�v���ʂ�%�n�Ȃ��Excel�Z����ΐF�ɂ���
		if type == "��%":
			self.outputExcel.setRuneColorYellow(22)
		elif type == "�U%":
			self.outputExcel.setRuneColorYellow(23)
		elif type == "�h%":
			self.outputExcel.setRuneColorYellow(24)
		elif type == "��":
			self.outputExcel.setRuneColorYellow(25)
		elif type == "�N��":
			self.outputExcel.setRuneColorYellow(26)
		elif type == "�_��":
			self.outputExcel.setRuneColorYellow(27)
		elif type == "��R":
			self.outputExcel.setRuneColorYellow(28)
		elif type == "�I��":
			self.outputExcel.setRuneColorYellow(29)

	#
	# �����X�^�[���̓��{����擾
	#
	def getJName(self, unit):
		jname = self.mst.getMonsterName(
			unit.getUnitMasterId(), unit.getAttribute)
		if jname in self.unit_master_hash:
			# ���ɓ������O�̃����X�^�[��������
			self.unit_master_hash[jname] += 1
			jname = jname + "_" + str(self.unit_master_hash[jname])
		else:
			self.unit_master_hash[jname] = 1
		if (jname is None):
			print("���{�ꖼ�̂�������Ȃ��FID=" + str(unit.getUnitMasterId()))
			sys.exit()
		return jname

	# 
	# �����E�W�F���̏���
	# 
	def outputCraftItemList(self):
		no = 1
		for craftItem in self.data.getCraftItemList():
			craftTypeId = '{0:06d}'.format(craftItem["craft_type_id"])
			# ���C��
			runeSet = craftTypeId[0:2]
			runeSetName = self.mst.getRuneSetName(int(runeSet))
			# �U����
			effectType = craftTypeId[2:4]
			effectTypeName = self.mst.getEffectTypeName(int(effectType))
			# ���@��
			rarity = craftTypeId[4:6]
			#02	���@
			#03	���A
			#04	�q�[���[
			if rarity == "01":
				rarityName = "�ʏ�"
			elif rarity == "02":
				rarityName = "+2%�`5%"
			elif rarity == "03":
				rarityName = "+3%�`6%"
			elif rarity == "04":
				rarityName = "+4%�`7%"
			elif rarity == "05":
				rarityName = "���W�F���g"
			if craftItem["craft_type"] == 1:
				craftType = "�W�F��"
			elif craftItem["craft_type"] == 2:
				craftType = "����"
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

