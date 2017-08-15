#!/usr/bin/python
# -*- coding: sjis -*-

import xlsxwriter
import os.path

class SwOutputExcel:
	def __init__(self, dataID):
		if os.path.exists("C:\\Users\\hhara\\OneDrive"):
			baseExcel = "C:\\Users\\hhara\\OneDrive\\"
		else:
			baseExcel = "C:\\Users\\tokebi\\OneDrive\\"
		# sw_dra/xlsm�́u�����X�^�[�v�V�[�g
		self.__book = xlsxwriter.Workbook(baseExcel + 'test' + dataID + '.xlsx');
		self.format = self.__book.add_format({
			'border': 1,
			})
		self.headerFormat = self.__book.add_format({
			'bold': 1,
			'border': 1,
			'align': 'center',
			'valign': 'vcenter',
			'fg_color': '#BFBFBF'})
		self.headerFormat2 = self.__book.add_format({
			'bold': 1,
			'border': 1,
			'text_wrap': 1,
			'align': 'center',
			'valign': 'vcenter',
			'fg_color': '#BFBFBF'})
		self.perFormat = self.__book.add_format({
			'border': 1,
			'num_format': '0.00%'
		})
		self.shrinkFormat = self.__book.add_format({
			'border': 1,
			'shrink': 1,
		})
		self.nonZeroFormat = self.__book.add_format({
			'border': 1,
			'num_format': '#;-#;"";@'
		})
		self.dateFormat = self.__book.add_format({
			'border': 1,
			'num_format': 'yyyy/m/d h:mm'
		})
		self.__initMonster()
		self.__initRunes()
		self.__initCraftItems()
		self.__initInventoryItems()

	#
	# �����X�^�[�p__init__
	#
	def __initMonster(self):
		self.__rowMonster = 1
		self.__stockMonster = []
		self.__monster = self.__book.add_worksheet('mons')
		self.__initMonsterExcel()

	#
	# �����X�^�[Worksheet�̃w�b�_�쐬
	#
	def __initMonsterExcel(self):
		arr = [
			['No'          , 0,  0, self.headerFormat],
			['ID'          , 0,  0, self.headerFormat],
			['���O'        , 0,  0, self.headerFormat],
			['���x��'      , 0,  0, self.headerFormat],
			['��'          , 0,  0, self.headerFormat],
			['����'        , 0,  0, self.headerFormat],
			['�̗�'        , 0,  0, self.headerFormat],
			['�U��'        , 0,  0, self.headerFormat],
			['�h��'        , 0,  0, self.headerFormat],
			['���x'        , 0,  0, self.headerFormat],
			['�N����'      , 0,  0, self.headerFormat],
			['�N���_��'    , 0,  0, self.headerFormat],
			['��R'        , 0,  0, self.headerFormat],
			['�I��'        , 0,  0, self.headerFormat],
			['�쐬��'      , 0,  0, self.headerFormat],
			['���[��1'     , 0,  0, self.headerFormat],
			['���[��2'     , 0,  0, self.headerFormat],
			['���[��3'     , 0,  0, self.headerFormat],
			['���[��4'     , 0,  0, self.headerFormat],
			['���[��5'     , 0,  0, self.headerFormat],
			['���[��6'     , 0,  0, self.headerFormat],
			['���'        , 0,  0, self.headerFormat],
			['WB���Ғl'    , 0,  0, self.headerFormat],
			['S1���x��'    , 0,  0, self.headerFormat],
			['S1MAX'       , 0,  0, self.headerFormat],
			['S2���x��'    , 0,  0, self.headerFormat],
			['S2MAX'       , 0,  0, self.headerFormat],
			['S3���x��'    , 0,  0, self.headerFormat],
			['S3MAX'       , 0,  0, self.headerFormat],
			['S4���x��'    , 0,  0, self.headerFormat],
			['S4MAX'       , 0,  0, self.headerFormat],
			['�o������'    , 0,  0, self.headerFormat],
			['�X�L���{��1' , 0,  0, self.headerFormat],
			['�X�L���{��2' , 0,  0, self.headerFormat],
			['�X�L���{��3' , 0,  0, self.headerFormat],
			['�X�L���{��4' , 0,  0, self.headerFormat],
			['�X�L���Z�k1' , 0,  0, self.headerFormat],
			['�X�L���Z�k2' , 0,  0, self.headerFormat],
			['�X�L���Z�k3' , 0,  0, self.headerFormat],
			['�X�L���Z�k4' , 0,  0, self.headerFormat],
			['�X�L�����e1' , 0,  0, self.headerFormat],
			['�X�L�����e2' , 0,  0, self.headerFormat],
			['�X�L�����e3' , 0,  0, self.headerFormat],
			['�X�L�����e4' , 0,  0, self.headerFormat],
			['���[�_�X�L��', 0,  0, self.headerFormat],
		]
		self.__writeHeader(self.__monster, arr, self.__rowMonster-1)

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
		formatHash = {}
		formatHash[ 1] = self.shrinkFormat
		formatHash[14] = self.dateFormat
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
		arr = [
			['No'            ,  5.38,  1, self.headerFormat2],
			['���[��ID'      , 11   ,  1, self.headerFormat2],
			['SLT'           ,  3   ,  1, self.headerFormat2],
			['����'          , 14.13,  1, self.headerFormat2],
			['��'            ,  4.63,  1, self.headerFormat2],
			['LV'            ,  3.25,  1, self.headerFormat2],
			['���'          ,  3.5 ,  1, self.headerFormat2],
			['���C��'        ,  4.13,  2, self.headerFormat2],
			[''              ,  4.63, -1, self.headerFormat2],
			['�T�u�I�v'      ,  4.13,  2, self.headerFormat2],
			[''              ,  4.63, -1, self.headerFormat2],
			['�T�u�I�v�P'    ,  4.13,  2, self.headerFormat2],
			[''              ,  4.63, -1, self.headerFormat2],
			['�T�u�I�v�Q'    ,  4.13,  2, self.headerFormat2],
			[''              ,  4.63, -1, self.headerFormat2],
			['�T�u�I�v�R'    ,  4.13,  2, self.headerFormat2],
			[''              ,  4.63, -1, self.headerFormat2],
			['�T�u�I�v�S'    ,  4.13,  2, self.headerFormat2],
			[''              ,  4.63, -1, self.headerFormat2],
			['���l'          ,  6.5 ,  1, self.headerFormat2],
			['��'            ,  9   ,  1, self.headerFormat2],
			[''              ,  3.25,  1, self.headerFormat2],
			['��%�L��'       ,  4.75,  1, self.headerFormat2],
			['�U%�L��'       ,  4.75,  1, self.headerFormat2],
			['�h%�L��'       ,  4.75,  1, self.headerFormat2],
			['���@�L��'      ,  4.75,  1, self.headerFormat2],
			['�N���L��'      ,  4.75,  1, self.headerFormat2],
			['�_���L��'      ,  4.75,  1, self.headerFormat2],
			['��R�L��'      ,  4.75,  1, self.headerFormat2],
			['�I���L��'      ,  4.75,  1, self.headerFormat2],
			['���i'          ,  7.25,  1, self.headerFormat2],
			['��'            ,  5.13,  1, self.headerFormat2],
			['���@���l'      ,  4.38,  1, self.headerFormat2],
			['�h���b�v�����N',  9   ,  1, self.headerFormat2],
			['�h���b�v�m�F��', 10   ,  1, self.headerFormat2],
		]
		self.__writeHeader(self.__runes, arr, self.__rowRunes-1)
		self.__runes.set_zoom(90)

	#
	# ���[���f�[�^�̕ۑ�
	#
	def writeRuneData(self, arr):
		self.__stockRunes.extend(arr)

	#
	# ���[���f�[�^�̍s�o��
	#
	def writeRuneNextRow(self):
		# �e��̃t�H�[�}�b�g��ݒ�
		formatHash = {}
		formatHash[ 1] = self.shrinkFormat	# ���[��ID
		formatHash[19] = self.perFormat		# ���[�����l
		formatHash[22] = self.nonZeroFormat	# ��%�L��
		formatHash[23] = self.nonZeroFormat	# �U%�L��
		formatHash[24] = self.nonZeroFormat	# �h%�L��
		formatHash[25] = self.nonZeroFormat	# ���@�L��
		formatHash[26] = self.nonZeroFormat	# �N���L��
		formatHash[27] = self.nonZeroFormat	# �_���L��
		formatHash[28] = self.nonZeroFormat	# ��R�L��
		formatHash[29] = self.nonZeroFormat	# �I���L��
		formatHash[34] = self.dateFormat	# �h���b�v�m�F��
		# ���t�����̂ݎ擾
		self.__stockRunes[34] = self.__stockRunes[34].replace('-', '/').split(" ", 1)[0]
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
		arr = [
			['No'            , 0,  1, self.headerFormat2],
			['���[��ID'      , 0,  1, self.headerFormat2],
			['sell_value'    , 0,  1, self.headerFormat2],
			['craft_type_id' , 0,  1, self.headerFormat2],
			['craft_type'    , 0,  1, self.headerFormat2],
			['runeSetName'   , 0,  1, self.headerFormat2],
			['effectTypeName', 0,  1, self.headerFormat2],
			['rarityName'    , 0,  1, self.headerFormat2],
			['���'          , 0,  1, self.headerFormat2],
		]
		self.__writeHeader(self.__craftItems, arr, self.__rowCraftItems-1)

	#
	# �����E�W�F��Worksheet�֏o��
	#
	def writeCraftItemData(self, arr):
		formatHash = {}
		self.__writeData(self.__craftItems, arr, self.__rowCraftItems, formatHash)
		self.__rowCraftItems += 1


	#
	# �݌ɏ��p__init__
	#
	def __initInventoryItems(self):
		self.__rowInventoryItems = 1
		self.__inventoryItems   = self.__book.add_worksheet('inventoryItem')
		self.__initInventoryExcel()

	#
	# �݌ɏ��Worksheet�̃w�b�_�쐬
	#
	def __initInventoryExcel(self):
		arr = [
			['No' , 0,  1, self.headerFormat2],
			['�݌Ɏ��' ,  0,  1, self.headerFormat2],
			['�݌�ID'   ,  0,  1, self.headerFormat2],
			['�݌ɖ�'   , 40,  1, self.headerFormat2],
			['�݌ɐ�'   ,  0,  1, self.headerFormat2],
		]
		self.__writeHeader(self.__inventoryItems, arr, self.__rowInventoryItems-1)

	#
	# �݌ɏ��Worksheet�֏o��
	#
	def writeInventoryData(self, arr):
		formatHash = {}
		self.__writeData(self.__inventoryItems, arr, self.__rowInventoryItems, formatHash)
		self.__rowInventoryItems += 1


	#
	# Excel���[�N�u�b�N�̕ۑ�
	#
	def save(self):
		for var in range(0, 36):
			self.__monster.write(self.__rowMonster, var, str(var))
		self.__book.close()

	#
	# worksheet�Ƀw�b�_�o��
	#
	def __writeHeader(self, target, arr, row):
		for i in range(0, len(arr)):
			value, width, colspan, format = arr[i]
			if colspan > 1:
				target.merge_range(row, i, row, i+colspan-1, value, format)
			elif colspan == -1:
				#�Ȃɂ����Ȃ�
				pass
			else:
				target.write(row,  i, value, format)
			if width > 0:
				target.set_column(i, i, width)
	#
	# Worksheet�Ƀf�[�^�o��
	#
	def __writeData(self, target ,arr, rownum, formatHash):
		colnum = 0
		for one in arr:
			if colnum in formatHash:
				format = formatHash[colnum]
			else:
				format = self.format
			target.write(rownum,  colnum, one, format)
			colnum += 1
		return colnum
