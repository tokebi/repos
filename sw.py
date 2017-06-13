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
			if unit.isNotOutputMonster():
				continue
			#�����X�^�[�f�[�^�̏o��
			arr = [
				no
				,unit.getUnitId()
				,unit.getJName()
				,unit.getLevel()
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
			no += 1
			# �������[������
			runes = unit.getRunes()
			for w_slot_no in range(1, 7):
				isFound=False
				for rune in runes:
					if rune.getSlotNo() == w_slot_no:
						rune.setId4Shoji(unit.getUnitId(), unit.getJName())
						arr.append(rune.getRuneId())
						isFound = True
				if isFound == False:
					arr.append(1)
			# �����X�^�[�^�C�v�EWB���Ғl�̏���
			arr.extend(self.outputMonsterType(unit))
			
			# ���v����
			self.toukei.addMonster(unit.getClass(), unit.getLevel(), unit.getAttribute())
			# �X�L�����x���E�X�L��MAX���x��
			for skill in unit.getSkills():
				arr.append(skill.getLevel())
				arr.append(skill.getSkillMaxLev())
			# �o������
			arr.append(unit.getKakuseiName())
			# �X�L���{��
			for skill in unit.getSkills():
				arr.append(skill.getSkillRate())
			# �X�L������
			for skill in unit.getSkills():
				arr.append(skill.getSkillRyaku())
			# �X�L���R�����g
			for skill in unit.getSkills():
				arr.append(skill.getSkillComment())
			# ���[�_�X�L��
			arr.append(unit.getLSkillComment())
			self.outputExcel.writeMonsterData(arr)
			self.outputExcel.writeMonsterNextRow()
		# �������̏ꍇ�̃��[�����쐬
		noRune = [""] * 35
		noRune[0] = 1
		noRune[1] = 1
		self.outputExcel.writeRuneData(noRune)
		self.outputExcel.writeRuneNextRow()
		# ���[���𐶐�
		no = 2
		for rune in self.data.getRuneList():
			self.outputRune(rune, no);
			self.outputExcel.writeRuneNextRow()
			no += 1
		# ���v�f�[�^�o��
		self.toukei.outputData()

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
		return [type, wbCalc]

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
		self.setExcelColor(rune.getEffectTypeName("pre"), 'green')
		# �I�v�P�`�S����
		self.getSecEff(arr, rune, 0)
		self.getSecEff(arr, rune, 1)
		self.getSecEff(arr, rune, 2)
		self.getSecEff(arr, rune, 3)
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
		arr.append(self.initRune.getDropDate(rune))

		# ���[�����v����
		self.toukei.addRune(rune.getClass())
		self.outputExcel.writeRuneData(arr)

	#
	# �T�u�I�v���擾
	#
	def getSecEff(self, arr, rune, effno):
		if len(rune.getSecEff()) >= effno+1:
			rune.setReaDo((effno+1) * 3)
			arr.append(rune.getEffectTypeName(effno))
			arr.append(rune.getEffectValue(effno) + 
				rune.getRenmaEffectValue(effno))
			if rune.getRenmaEffectValue(effno) > 0:
				self.outputExcel.setRuneComment(
					len(arr)-1,
					str(rune.getEffectValue(effno)) + "+" +
					str(rune.getRenmaEffectValue(effno)))
		else:
			arr.extend(["",""])

	def setExcelColor(self, type, color):
		# �I�v���ʂ�%�n�Ȃ��Excel�Z����ΐF�ɂ���
		if type == "��%":
			self.outputExcel.setRuneColorYellow(22, color)
		elif type == "�U%":
			self.outputExcel.setRuneColorYellow(23, color)
		elif type == "�h%":
			self.outputExcel.setRuneColorYellow(24, color)
		elif type == "��":
			self.outputExcel.setRuneColorYellow(25, color)
		elif type == "�N��":
			self.outputExcel.setRuneColorYellow(26, color)
		elif type == "�_��":
			self.outputExcel.setRuneColorYellow(27, color)
		elif type == "��R":
			self.outputExcel.setRuneColorYellow(28, color)
		elif type == "�I��":
			self.outputExcel.setRuneColorYellow(29, color)

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
			arr = [
				no
				,craftItem.getCraftItemId()
				,craftItem.getSellValue()
				,craftItem.getCraftTypeId()
				,craftItem.getCraftType()
				# ���C��
				,craftItem.getSetName()
				# �U����
				,craftItem.getEffectTypeName()
				# ���@��
				,craftItem.getRarity()
				# ���
				,craftItem.getType()
			]
			self.outputExcel.writeCraftItemData(arr)
			no+=1

if __name__ == "__main__":
	a = MAIN()
	a.main()

