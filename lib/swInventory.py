#!/usr/bin/python
# -*- coding: sjis -*-

from lib.swMaster import SwMaster

class SwInventory():
	def __init__(self, craftItem):
		#�}�X�^�[�f�[�^�̏�����
		self.__mst = SwMaster.getInstance()
		self.__masterType = craftItem["item_master_type"]
		self.__quantity   = craftItem["item_quantity"]
		self.__masterId   = craftItem["item_master_id"]

	def __getJName(self):
		#item_master_type	item_quantity	item_master_id
		if   self.__masterType ==  9 and self.__masterId ==  1:		return "���m�̏��ҏ�"
		elif self.__masterType ==  9 and self.__masterId ==  2:		return "�s�v�c�ȏ��ҏ�"
		elif self.__masterType ==  9 and self.__masterId ==  3:		return "���ƈł̏��ҏ�"
		elif self.__masterType ==  9 and self.__masterId ==  4:		return "���̏��ҏ�"
		elif self.__masterType ==  9 and self.__masterId ==  5:		return "�΂̏��ҏ�"
		elif self.__masterType ==  9 and self.__masterId ==  6:		return "���̏��ҏ�"
		elif self.__masterType ==  9 and self.__masterId ==  7:		return "�`���̏��ҏ�"
		elif self.__masterType ==  9 and self.__masterId ==  8:		return "���ꏢ�Ґ�"
		elif self.__masterType ==  9 and self.__masterId ==  9:		return "�u�`���̏��ҏ��v�̌���"
		elif self.__masterType ==  9 and self.__masterId == 10:		return "�u���ƈł̏��ҏ��v�̌���"
		elif self.__masterType == 11 and self.__masterId == 11001:	return "���̐����i�����j"
		elif self.__masterType == 11 and self.__masterId == 11002:	return "���̐����i�����j"
		elif self.__masterType == 11 and self.__masterId == 11003:	return "���̐����i�����j"
		elif self.__masterType == 11 and self.__masterId == 11004:	return "���̐����i�����j"
		elif self.__masterType == 11 and self.__masterId == 11005:	return "�ł̐����i�����j"
		elif self.__masterType == 11 and self.__masterId == 11006:	return "���͂̐����i�����j"
		elif self.__masterType == 11 and self.__masterId == 12001:	return "���̐����i�����j"
		elif self.__masterType == 11 and self.__masterId == 12002:	return "���̐����i�����j"
		elif self.__masterType == 11 and self.__masterId == 12003:	return "���̐����i�����j"
		elif self.__masterType == 11 and self.__masterId == 12004:	return "���̐����i�����j"
		elif self.__masterType == 11 and self.__masterId == 12005:	return "�ł̐����i�����j"
		elif self.__masterType == 11 and self.__masterId == 12006:	return "���͂̐����i�����j"
		elif self.__masterType == 11 and self.__masterId == 13001:	return "���̐����i�㋉�j"
		elif self.__masterType == 11 and self.__masterId == 13002:	return "���̐����i�㋉�j"
		elif self.__masterType == 11 and self.__masterId == 13003:	return "���̐����i�㋉�j"
		elif self.__masterType == 11 and self.__masterId == 13004:	return "���̐����i�㋉�j"
		elif self.__masterType == 11 and self.__masterId == 13005:	return "�ł̐����i�㋉�j"
		elif self.__masterType == 11 and self.__masterId == 13006:	return "���͂̐����i�㋉�j"
		elif self.__masterType == 12:
			# �����X�^�[���ҏ��̌���
			return self.__mst.getMonsterName(self.__masterId)+"���ҏ��̌���"
		elif self.__masterType == 19 and self.__masterId == 19200:	return "�u�C�t���[�g�v�̏��ҏ��̌���"
		elif self.__masterType == 20 and self.__masterId == 1:		return "���\���҂̌���"
		elif self.__masterType == 29 and self.__masterId == 1001:	return "���łȌÖ�"
		elif self.__masterType == 29 and self.__masterId == 1002:	return "���x�Ȕ�"
		elif self.__masterType == 29 and self.__masterId == 1003:	return "�d���Ȑ΍�"
		elif self.__masterType == 29 and self.__masterId == 1004:	return "�|�̍z��"
		elif self.__masterType == 29 and self.__masterId == 1005:	return "�P���~�X����"
		elif self.__masterType == 29 and self.__masterId == 1006:	return "�������z"
		elif self.__masterType == 29 and self.__masterId == 2001:	return "���[���̌���"
		elif self.__masterType == 29 and self.__masterId == 3001:	return "���@�̕�"
		elif self.__masterType == 29 and self.__masterId == 4001:	return "���a�̖��"
		elif self.__masterType == 29 and self.__masterId == 4002:	return "���z�̖��"
		elif self.__masterType == 29 and self.__masterId == 4003:	return "���ׂ̖��"
		elif self.__masterType == 29 and self.__masterId == 5001:	return "����t�������̌���"
		elif self.__masterType == 29 and self.__masterId == 5002:	return "�R���オ��΂̌���"
		elif self.__masterType == 29 and self.__masterId == 5003:	return "�����r��镗�̌���"
		elif self.__masterType == 29 and self.__masterId == 5004:	return "ῂ����P�����̌���"
		elif self.__masterType == 29 and self.__masterId == 5005:	return "�����̍��̈ł̌���"
		elif self.__masterType == 29 and self.__masterId == 6001:	return "�Ïk���ꂽ���͂̌���"
		elif self.__masterType == 29 and self.__masterId == 7001:	return "�����Ȗ��͂̌���"
		elif self.__masterType == 37 and self.__masterId == 1:		return "������"
		else:													return "�s���ȍ݌�"

	#
	# �݌Ɏ�ނ��擾
	#
	def getMasterType(self):
		return self.__masterType

	#
	# �݌ɐ����擾
	#
	def getQuantity(self):
		return self.__quantity

	#
	# �݌�ID���擾
	#
	def getMasterId(self):
		return self.__masterId

	#
	# �݌ɓ��{�ꖼ���擾
	#
	def getJName(self):
		return self.__getJName()
