#!/usr/bin/python
# -*- coding: sjis -*-

import xlsxwriter

class SwOutputExcel:
	def __init__(self):
		self.__rowMonster = 4
		self.__rowRunes = 1
		self.__stockMonster = []
		self.__stockRunes = []
		# sw_dra/xlsm�́u�����X�^�[�v�V�[�g
		self.__book = xlsxwriter.Workbook('C:\\Users\\hhara\\OneDrive\\test.xlsx');
		self.__monster = self.__book.add_worksheet('mons')
		self.__runes   = self.__book.add_worksheet('runes')
		self.__initMonsterExcel()
		self.__initRunesExcel()

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
		for var in range(2, 120):
			self.__monster.write(0, var, str(var-1))
		self.__monster.merge_range(1,  0, 3,  0, 'No', format)
		self.__monster.merge_range(1,  1, 3,  1, 'ID', format)
		self.__monster.merge_range(1,  2, 3,  2, '���O', format)
		self.__monster.merge_range(1,  3, 3,  3, '���x��', format)
		self.__monster.merge_range(1,  4, 3,  4, '��', format)
		self.__monster.merge_range(1,  5, 3,  5, '����', format)
		self.__monster.merge_range(1,  6, 3,  6, '�̗�', format)
		self.__monster.merge_range(1,  7, 3,  7, '�U��', format)
		self.__monster.merge_range(1,  8, 3,  8, '�h��', format)
		self.__monster.merge_range(1,  9, 3,  9, '���x', format)
		self.__monster.merge_range(1, 10, 3, 10, '�N����', format)
		self.__monster.merge_range(1, 11, 3, 11, '�N���_��', format)
		self.__monster.merge_range(1, 12, 3, 12, '��R', format)
		self.__monster.merge_range(1, 13, 3, 13, '�I��', format)
		self.__monster.merge_range(1, 14, 3, 14, '�쐬��', format)
		for var in range(0, 6):
			format2 = format1 if (var % 2) == 0 else format
			self.__monster.merge_range(1, 15+16*var   , 1, 15+16*var+15, str(var+1), format2)
			self.__monster.merge_range(2, 15+16*var+0 , 3, 15+16*var+0 ,'��'       , format2)
			self.__monster.merge_range(2, 15+16*var+1 , 3, 15+16*var+1 ,'���x��'   , format2)
			self.__monster.merge_range(2, 15+16*var+2 , 3, 15+16*var+2 ,'���'     , format2)
			self.__monster.merge_range(2, 15+16*var+3 , 2, 15+16*var+4 ,'���C��'   , format2)
			self.__monster.merge_range(2, 15+16*var+5 , 2, 15+16*var+6 ,'�T�u�I�v' , format2)
			self.__monster.merge_range(2, 15+16*var+7 , 2, 15+16*var+8 ,'�T�u�I�v1', format2)
			self.__monster.merge_range(2, 15+16*var+9 , 2, 15+16*var+10,'�T�u�I�v2', format2)
			self.__monster.merge_range(2, 15+16*var+11, 2, 15+16*var+12,'�T�u�I�v3', format2)
			self.__monster.merge_range(2, 15+16*var+13, 2, 15+16*var+14,'�T�u�I�v4', format2)
			self.__monster.merge_range(2, 15+16*var+15, 3, 15+16*var+15,'����'     , format2)
			for var2 in range(0, 6):
				self.__monster.write(3, 15+16*var+3+var2*2 ,'����', format2)
				self.__monster.write(3, 15+16*var+4+var2*2 ,'�l', format2)
		self.__monster.merge_range(1, 111, 3, 111,'���', format)
		self.__monster.merge_range(1, 112, 3, 112,'WB���Ғl', format)
		self.__monster.merge_range(1, 113, 1, 114,'S1', format)
		self.__monster.merge_range(1, 115, 1, 116,'S2', format)
		self.__monster.merge_range(1, 117, 1, 118,'S3', format)
		self.__monster.merge_range(1, 119, 1, 120,'S4', format)
		self.__monster.merge_range(2, 113, 3, 113,'���x��', format)
		self.__monster.merge_range(2, 114, 3, 114,'MAX', format)
		self.__monster.merge_range(2, 115, 3, 115,'���x��', format)
		self.__monster.merge_range(2, 116, 3, 116,'MAX', format)
		self.__monster.merge_range(2, 117, 3, 117,'���x��', format)
		self.__monster.merge_range(2, 118, 3, 118,'MAX', format)
		self.__monster.merge_range(2, 119, 3, 119,'���x��', format)
		self.__monster.merge_range(2, 120, 3, 120,'MAX', format)
		self.__monster.merge_range(1, 121, 3, 121,'�o������', format)

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
		self.__runes.write(0,  19, '���[������', format)
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
		self.__runes.write(0,  33, '�t���O', format)

	def save(self):
		self.__book.close()

	def writeMonsterData(self, arr):
		self.__stockMonster.extend(arr)

	def writeRuneData(self, arr):
		self.__stockRunes.extend(arr)

	def writeMonsterNextRow(self):
		format_per = self.__book.add_format({
			'border': 1,
			'num_format': '0.00%'
			})
		format_date = self.__book.add_format({
			'border': 1,
			'num_format': 'yyyy/m/d h:mm'
			})
		formatHash = {}
		formatHash[14] = format_date
		formatHash[30] = format_per
		formatHash[46] = format_per
		formatHash[62] = format_per
		formatHash[78] = format_per
		formatHash[94] = format_per
		formatHash[110] = format_per
		# ���t�ϊ�
		self.__stockMonster[14] = self.__stockMonster[14].replace('-', '/')
		self.__writeData(self.__monster, self.__stockMonster, self.__rowMonster, formatHash)
		self.__monster,
		self.__rowMonster += 1
		self.__stockMonster = []

	def writeRuneNextRow(self):
		format_per = self.__book.add_format({
			'border': 1,
			'num_format': '0.00%'
			})
		formatHash = {}
		formatHash[19] = format_per
		self.__writeData(self.__runes, self.__stockRunes, self.__rowRunes, formatHash)
		self.__rowRunes += 1
		self.__stockRunes = []

	def __writeData(self, target ,arr, rownum, formatHash):
		format_def = self.__book.add_format({
			'border': 1
			})
		#yyyy/m/d h:mm
		colnum = 0
		for one in arr:
			if colnum in formatHash:
				format = formatHash[colnum]
			else:
				format = format_def
			target.write(rownum,  colnum, one, format)
			colnum += 1
		return colnum
