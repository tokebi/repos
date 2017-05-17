#!/usr/bin/python
# -*- coding: sjis -*-

import xlsxwriter
import os.path

class SwOutputExcel:
	def __init__(self):
		if os.path.exists("C:\\Users\\hhara\\OneDrive"):
			baseExcel = "C:\\Users\\hhara\\OneDrive\\"
		else:
			baseExcel = "C:\\Users\\tokebi\\OneDrive\\"
		# sw_dra/xlsm�́u�����X�^�[�v�V�[�g
		self.__book = xlsxwriter.Workbook(baseExcel + 'test.xlsx');
		self.__initMonster()
		self.__initRunes()
		self.__initCraftItems()

	#
	# �����X�^�[�p__init__
	#
	def __initMonster(self):
		self.__rowMonster = 2
		self.__stockMonster = []
		self.__monster = self.__book.add_worksheet('mons')
		self.__initMonsterExcel()

	#
	# �����X�^�[Worksheet�̃w�b�_�쐬
	#
	def __initMonsterExcel(self):
		format = self.__book.add_format({
			'bold': 1,
			'border': 1,
			'align': 'center',
			'valign': 'vcenter',
			'fg_color': '#BFBFBF'})
		format1 = self.__book.add_format({
			'bold': 1,
			'border': 1,
			'align': 'center',
			'valign': 'vcenter',
			'fg_color': '#948A54'})
		for var in range(2, 36):
			self.__monster.write(0, var, str(var))
		self.__monster.write(1,  0, 'No', format)
		self.__monster.write(1,  1, 'ID', format)
		self.__monster.write(1,  2, '���O', format)
		self.__monster.write(1,  3, '���x��', format)
		self.__monster.write(1,  4, '��', format)
		self.__monster.write(1,  5, '����', format)
		self.__monster.write(1,  6, '�̗�', format)
		self.__monster.write(1,  7, '�U��', format)
		self.__monster.write(1,  8, '�h��', format)
		self.__monster.write(1,  9, '���x', format)
		self.__monster.write(1, 10, '�N����', format)
		self.__monster.write(1, 11, '�N���_��', format)
		self.__monster.write(1, 12, '��R', format)
		self.__monster.write(1, 13, '�I��', format)
		self.__monster.write(1, 14, '�쐬��', format)
		self.__monster.write(1, 15, '���[��1', format)
		self.__monster.write(1, 16, '���[��2', format)
		self.__monster.write(1, 17, '���[��3', format)
		self.__monster.write(1, 18, '���[��4', format)
		self.__monster.write(1, 19, '���[��5', format)
		self.__monster.write(1, 20, '���[��6', format)
		
		self.__monster.write(1, 21,'���', format)
		self.__monster.write(1, 22,'WB���Ғl', format)
		self.__monster.write(1, 23,'S1���x��', format)
		self.__monster.write(1, 24,'S1MAX', format)
		self.__monster.write(1, 25,'S2���x��', format)
		self.__monster.write(1, 26,'S2MAX', format)
		self.__monster.write(1, 27,'S3���x��', format)
		self.__monster.write(1, 28,'S3MAX', format)
		self.__monster.write(1, 29,'S4���x��', format)
		self.__monster.write(1, 30,'S4MAX', format)
		self.__monster.write(1, 31,'�o������', format)
		self.__monster.write(1, 32,'�X�L���{��1', format)
		self.__monster.write(1, 33,'�X�L���{��2', format)
		self.__monster.write(1, 34,'�X�L���{��3', format)
		self.__monster.write(1, 35,'�X�L���{��4', format)
		self.__monster.write(1, 36,'�X�L���Z�k1', format)
		self.__monster.write(1, 37,'�X�L���Z�k2', format)
		self.__monster.write(1, 38,'�X�L���Z�k3', format)
		self.__monster.write(1, 39,'�X�L���Z�k4', format)
		self.__monster.write(1, 40,'�X�L�����e1', format)
		self.__monster.write(1, 41,'�X�L�����e2', format)
		self.__monster.write(1, 42,'�X�L�����e3', format)
		self.__monster.write(1, 43,'�X�L�����e4', format)
		self.__monster.write(1, 44,'���[�_�X�L��', format)

	#
	# �����X�^�[�f�[�^�̕ۑ�
	#
	def writeMonsterData(self, arr):
		if arr[0] == "":
			del arr[0]
		self.__stockMonster.extend(arr)

	#
	# �����X�^�[�f�[�^�̍s�o��
	#
	def writeMonsterNextRow(self):
		format_per = self.__book.add_format({
			'border': 1,
			'num_format': '0.00%'
		})
		format_date = self.__book.add_format({
			'border': 1,
			'num_format': 'yyyy/m/d h:mm'
		})
		format_shrink = self.__book.add_format({
			'border': 1,
			'shrink': 1,
		})
		formatHash = {}
		formatHash[ 1] = format_shrink
		formatHash[14] = format_date
		# ���t�ϊ�
		self.__stockMonster[14] = self.__stockMonster[14].replace('-', '/')
		self.__writeData(self.__monster, self.__stockMonster, self.__rowMonster, formatHash)
		self.__monster,
		self.__rowMonster += 1
		self.__stockMonster = []

	#
	# ���[���p__init__
	#
	def __initRunes(self):
		self.__rowRunes = 1
		self.__stockRunes = []
		self.__runeFormat = {}
		self.__runeComment = {}
		self.__runes   = self.__book.add_worksheet('runes')
		self.__initRunesExcel()

	#
	# ���[��Worksheet�̃w�b�_�쐬
	#
	def __initRunesExcel(self):
		format = self.__book.add_format({
			'bold': 1,
			'border': 1,
			'text_wrap': 1,
			'align': 'center',
			'valign': 'vcenter',
			'fg_color': '#BFBFBF'})
		self.__runes.write(0,  0, 'No', format)
		self.__runes.write(0,  1, '���[��ID', format)
		self.__runes.write(0,  2, 'SLT', format)
		self.__runes.write(0,  3, '����', format)
		self.__runes.write(0,  4, '��', format)
		self.__runes.write(0,  5, 'LV', format)
		self.__runes.write(0,  6, '���', format)
		self.__runes.merge_range(0,   7, 0,   8, '���C��', format)
		self.__runes.merge_range(0,   9, 0,  10, '�T�u�I�v', format)
		self.__runes.merge_range(0,  11, 0,  12, '�T�u�I�v�P', format)
		self.__runes.merge_range(0,  13, 0,  14, '�T�u�I�v�Q', format)
		self.__runes.merge_range(0,  15, 0,  16, '�T�u�I�v�R', format)
		self.__runes.merge_range(0,  17, 0,  18, '�T�u�I�v�S', format)
		self.__runes.write(0,  19, '���l', format)
		self.__runes.write(0,  20, '', format)
		self.__runes.write(0,  21, '��', format)
		self.__runes.write(0,  22, '��%�L��', format)
		self.__runes.write(0,  23, '�U%�L��', format)
		self.__runes.write(0,  24, '�h%�L��', format)
		self.__runes.write(0,  25, '���@�L��', format)
		self.__runes.write(0,  26, '�N���L��', format)
		self.__runes.write(0,  27, '�_���L��', format)
		self.__runes.write(0,  28, '��R�L��', format)
		self.__runes.write(0,  29, '�I���L��', format)
		self.__runes.write(0,  30, '���i', format)
		self.__runes.write(0,  31, '��', format)
		self.__runes.write(0,  32, '���@���l', format)
		self.__runes.write(0,  33, '�h���b�v�����N', format)
		self.__runes.set_zoom(90)
		self.__runes.set_column('A:A', 5.38)
		self.__runes.set_column('B:B', 11)
		self.__runes.set_column('C:C', 3)
		self.__runes.set_column('D:D', 14.13)
		self.__runes.set_column('E:E', 4.63)
		self.__runes.set_column('F:F', 3.25)
		self.__runes.set_column('G:G', 3.5)
		self.__runes.set_column('H:H', 4.13)
		self.__runes.set_column('I:I', 4.63)
		self.__runes.set_column('J:J', 4.13)
		self.__runes.set_column('K:K', 4.63)
		self.__runes.set_column('L:L', 4.13)
		self.__runes.set_column('M:M', 4.63)
		self.__runes.set_column('N:N', 4.13)
		self.__runes.set_column('O:O', 4.63)
		self.__runes.set_column('P:P', 4.13)
		self.__runes.set_column('Q:Q', 4.63)
		self.__runes.set_column('R:R', 4.13)
		self.__runes.set_column('S:S', 4.63)
		self.__runes.set_column('T:T', 6.5)
		self.__runes.set_column('U:U', 9)
		self.__runes.set_column('V:V', 3.25)
		self.__runes.set_column('W:AD', 4.75)
		self.__runes.set_column('AE:AE', 7.25)
		self.__runes.set_column('AF:AF', 5.13)
		self.__runes.set_column('AG:AG', 4.38)
		self.__runes.set_column('AH:AH', 5.38)

	#
	# ���[���f�[�^�̕ۑ�
	#
	def writeRuneData(self, arr):
		self.__stockRunes.extend(arr)

	#
	# ���[���f�[�^�̍s�o��
	#
	def writeRuneNextRow(self):
		format_def = self.__book.add_format({'border': 1})
		# �p�[�Z���g�\��
		format_per = self.__book.add_format({
			'border': 1,
			'num_format': '0.00%'
		})
		# �k�����đS�̂�\��
		format_shrink = self.__book.add_format({
			'border': 1,
			'shrink': 1,
		})
		# "0"��\�����Ȃ�
		format_nonZero = self.__book.add_format({
			'border': 1,
			'num_format': '#;-#;"";@'
		})
		# �e��̃t�H�[�}�b�g��ݒ�
		formatHash = {}
		formatHash[ 1] = format_shrink	# ���[��ID
		formatHash[19] = format_per		# ���[�����l
		formatHash[22] = format_nonZero	# ��%�L��
		formatHash[23] = format_nonZero	# �U%�L��
		formatHash[24] = format_nonZero	# �h%�L��
		formatHash[25] = format_nonZero	# ���@�L��
		formatHash[26] = format_nonZero	# �N���L��
		formatHash[27] = format_nonZero	# �_���L��
		formatHash[28] = format_nonZero	# ��R�L��
		formatHash[29] = format_nonZero	# �I���L��

		for k, v in self.__runeFormat.items():
			formatHash[k] = v
		self.__writeData(self.__runes, self.__stockRunes, self.__rowRunes, formatHash)
		for k, v in self.__runeComment.items():
			self.__runes.write_comment(self.__rowRunes, k, v)
		self.__rowRunes += 1
		self.__stockRunes = []
		self.__runeFormat = {}
		self.__runeComment = {}

	#
	# ���[���f�[�^�̏����o���s���擾
	#
	def getRuneRone(self):
		return self.__rowRunes


	#
	# �Z���̔w�i�F��ݒ�
	#
	def setRuneColorYellow(self, col, color):
		format = self.__book.add_format({'border': 1})
		if col in self.__runeFormat:
			format = self.__runeFormat[col]
		format.set_bg_color(color)
		self.__runeFormat[col] = format

	#
	# �Z���̃R�����g��ݒ�
	#
	def setRuneComment(self, col, comment):
		self.__runeComment[col] = comment

	#
	# ���[���p__init__
	#
	def __initCraftItems(self):
		self.__rowCraftItems = 1
		self.__craftItems   = self.__book.add_worksheet('craftItems')
		self.__initCraftItemsExcel()

	#
	# �����E�W�F��Worksheet�̃w�b�_�쐬
	#
	def __initCraftItemsExcel(self):
		format = self.__book.add_format({
			'bold': 1,
			'border': 1,
			'text_wrap': 1,
			'align': 'center',
			'valign': 'vcenter',
			'fg_color': '#BFBFBF'})
		self.__craftItems.write(0,  0, 'No', format)
		self.__craftItems.write(0,  1, '���[��ID', format)
		self.__craftItems.write(0,  2, 'sell_value', format)
		self.__craftItems.write(0,  3, 'craft_type_id', format)
		self.__craftItems.write(0,  4, 'craft_type', format)
		self.__craftItems.write(0,  5, 'runeSetName', format)
		self.__craftItems.write(0,  6, 'effectTypeName', format)
		self.__craftItems.write(0,  7, 'rarityName', format)
		self.__craftItems.write(0,  8, '���', format)

	#
	# �����E�W�F��Worksheet�֏o��
	#
	def writeCraftItemData(self, arr):
		formatHash = {}
		self.__writeData(self.__craftItems, arr, self.__rowCraftItems, formatHash)
		self.__rowCraftItems += 1




	#
	# Excel���[�N�u�b�N�̕ۑ�
	#
	def save(self):
		self.__book.close()

	#
	# Worksheet�Ƀf�[�^�o��
	#
	def __writeData(self, target ,arr, rownum, formatHash):
		format_def = self.__book.add_format({
			'border': 1,
			})
		colnum = 0
		for one in arr:
			if colnum in formatHash:
				format = formatHash[colnum]
			else:
				format = format_def
			target.write(rownum,  colnum, one, format)
			colnum += 1
		return colnum
