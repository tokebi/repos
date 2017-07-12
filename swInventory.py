#!/usr/bin/python
# -*- coding: sjis -*-

import swMaster

class SwInventory():
	def __init__(self, craftItem):
		#�}�X�^�[�f�[�^�̏�����
		self.mst = swMaster.SwMaster.getInstance()
		self.masterType = craftItem["item_master_type"]
		self.quantity   = craftItem["item_quantity"]
		self.masterId   = craftItem["item_master_id"]
		self.JName      = self.__getJName()

	def __getJName(self):
		#item_master_type	item_quantity	item_master_id
		if   self.masterType ==  9 and self.masterId ==  1:		return "���m�̏��ҏ�"
		elif self.masterType ==  9 and self.masterId ==  2:		return "�s�v�c�ȏ��ҏ�"
		elif self.masterType ==  9 and self.masterId ==  3:		return "�`���̏��ҏ������ƈł̏��ҏ������̏��ҏ�"
		elif self.masterType ==  9 and self.masterId ==  4:		return "���̏��ҏ�"
		elif self.masterType ==  9 and self.masterId ==  5:		return "�΂̏��ҏ�"
		elif self.masterType ==  9 and self.masterId ==  6:		return "�`���̏��ҏ������ƈł̏��ҏ������̏��ҏ�"
		elif self.masterType ==  9 and self.masterId ==  7:		return "�`���̏��ҏ������ƈł̏��ҏ������̏��ҏ�"
		elif self.masterType ==  9 and self.masterId ==  8:		return "���ꏢ�Ґ�"
		elif self.masterType ==  9 and self.masterId ==  9:		return "�u�`���̏��ҏ��v�̌���"
		elif self.masterType ==  9 and self.masterId == 10:		return "�u���ƈł̏��ҏ��v�̌���"
		elif self.masterType == 11 and self.masterId == 11001:	return "���̐����i�����j"
		elif self.masterType == 11 and self.masterId == 11002:	return "���̐����i�����j"
		elif self.masterType == 11 and self.masterId == 11003:	return "���̐����i�����j"
		elif self.masterType == 11 and self.masterId == 11004:	return "���̐����i�����j"
		elif self.masterType == 11 and self.masterId == 11005:	return "�ł̐����i�����j"
		elif self.masterType == 11 and self.masterId == 11006:	return "���͂̐����i�����j"
		elif self.masterType == 11 and self.masterId == 12001:	return "���̐����i�����j"
		elif self.masterType == 11 and self.masterId == 12002:	return "���̐����i�����j"
		elif self.masterType == 11 and self.masterId == 12003:	return "���̐����i�����j"
		elif self.masterType == 11 and self.masterId == 12004:	return "���̐����i�����j"
		elif self.masterType == 11 and self.masterId == 12005:	return "�ł̐����i�����j"
		elif self.masterType == 11 and self.masterId == 12006:	return "���͂̐����i�����j"
		elif self.masterType == 11 and self.masterId == 13001:	return "���̐����i�㋉�j"
		elif self.masterType == 11 and self.masterId == 13002:	return "���̐����i�㋉�j"
		elif self.masterType == 11 and self.masterId == 13003:	return "���̐����i�㋉�j"
		elif self.masterType == 11 and self.masterId == 13004:	return "���̐����i�㋉�j"
		elif self.masterType == 11 and self.masterId == 13005:	return "�ł̐����i�㋉�j"
		elif self.masterType == 11 and self.masterId == 13006:	return "���͂̐����i�㋉�j"
		elif self.masterType == 12:
			# �����X�^�[���ҏ��̌���
			return self.mst.getMonsterName(self.masterId)+"���ҏ��̌���"
		elif self.masterType == 19 and self.masterId == 19200:	return "�u�C�t���[�g�v�̏��ҏ��̌���"
		elif self.masterType == 20 and self.masterId == 1:		return "���\���҂̌���"
		elif self.masterType == 29 and self.masterId == 1001:	return "���łȌÖ�"
		elif self.masterType == 29 and self.masterId == 1002:	return "���x�Ȕ�"
		elif self.masterType == 29 and self.masterId == 1003:	return "�d���Ȑ΍�"
		elif self.masterType == 29 and self.masterId == 1004:	return "�|�̍z��"
		elif self.masterType == 29 and self.masterId == 1005:	return "�P���~�X����"
		elif self.masterType == 29 and self.masterId == 1006:	return "�������z"
		elif self.masterType == 29 and self.masterId == 2001:	return "���[���̌���"
		elif self.masterType == 29 and self.masterId == 3001:	return "���@�̕�"
		elif self.masterType == 29 and self.masterId == 4001:	return "���a�̖��"
		elif self.masterType == 29 and self.masterId == 4002:	return "���z�̖��"
		elif self.masterType == 29 and self.masterId == 4003:	return "���ׂ̖��"
		elif self.masterType == 29 and self.masterId == 5001:	return "����t�������̌���"
		elif self.masterType == 29 and self.masterId == 5002:	return "�R���オ��΂̌���"
		elif self.masterType == 29 and self.masterId == 5003:	return "�����r��镗�̌���"
		elif self.masterType == 29 and self.masterId == 5004:	return "ῂ����P�����̌���"
		elif self.masterType == 29 and self.masterId == 5005:	return "�����̍��̈ł̌���"
		elif self.masterType == 29 and self.masterId == 6001:	return "�Ïk���ꂽ���͂̌���"
		elif self.masterType == 29 and self.masterId == 7001:	return "�����Ȗ��͂̌���"
		elif self.masterType == 37 and self.masterId == 1:		return "������"
		else:													return "�s���ȍ݌�"

	#
	# �݌Ɏ�ނ��擾
	#
	def getMasterType(self):
		return self.masterType

	#
	# �݌ɐ����擾
	#
	def getQuantity(self):
		return self.quantity

	#
	# �݌�ID���擾
	#
	def getMasterId(self):
		return self.masterId

	#
	# �݌ɓ��{�ꖼ���擾
	#
	def getJName(self):
		return self.JName
