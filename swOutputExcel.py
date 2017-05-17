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
		# sw_dra/xlsmの「モンスター」シート
		self.__book = xlsxwriter.Workbook(baseExcel + 'test.xlsx');
		self.__initMonster()
		self.__initRunes()
		self.__initCraftItems()

	#
	# モンスター用__init__
	#
	def __initMonster(self):
		self.__rowMonster = 2
		self.__stockMonster = []
		self.__monster = self.__book.add_worksheet('mons')
		self.__initMonsterExcel()

	#
	# モンスターWorksheetのヘッダ作成
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
		self.__monster.write(1,  2, '名前', format)
		self.__monster.write(1,  3, 'レベル', format)
		self.__monster.write(1,  4, '★', format)
		self.__monster.write(1,  5, '属性', format)
		self.__monster.write(1,  6, '体力', format)
		self.__monster.write(1,  7, '攻撃', format)
		self.__monster.write(1,  8, '防御', format)
		self.__monster.write(1,  9, '速度', format)
		self.__monster.write(1, 10, 'クリ率', format)
		self.__monster.write(1, 11, 'クリダメ', format)
		self.__monster.write(1, 12, '抵抗', format)
		self.__monster.write(1, 13, '的中', format)
		self.__monster.write(1, 14, '作成日', format)
		self.__monster.write(1, 15, 'ルーン1', format)
		self.__monster.write(1, 16, 'ルーン2', format)
		self.__monster.write(1, 17, 'ルーン3', format)
		self.__monster.write(1, 18, 'ルーン4', format)
		self.__monster.write(1, 19, 'ルーン5', format)
		self.__monster.write(1, 20, 'ルーン6', format)
		
		self.__monster.write(1, 21,'種類', format)
		self.__monster.write(1, 22,'WB期待値', format)
		self.__monster.write(1, 23,'S1レベル', format)
		self.__monster.write(1, 24,'S1MAX', format)
		self.__monster.write(1, 25,'S2レベル', format)
		self.__monster.write(1, 26,'S2MAX', format)
		self.__monster.write(1, 27,'S3レベル', format)
		self.__monster.write(1, 28,'S3MAX', format)
		self.__monster.write(1, 29,'S4レベル', format)
		self.__monster.write(1, 30,'S4MAX', format)
		self.__monster.write(1, 31,'覚醒名称', format)
		self.__monster.write(1, 32,'スキル倍率1', format)
		self.__monster.write(1, 33,'スキル倍率2', format)
		self.__monster.write(1, 34,'スキル倍率3', format)
		self.__monster.write(1, 35,'スキル倍率4', format)
		self.__monster.write(1, 36,'スキル短縮1', format)
		self.__monster.write(1, 37,'スキル短縮2', format)
		self.__monster.write(1, 38,'スキル短縮3', format)
		self.__monster.write(1, 39,'スキル短縮4', format)
		self.__monster.write(1, 40,'スキル内容1', format)
		self.__monster.write(1, 41,'スキル内容2', format)
		self.__monster.write(1, 42,'スキル内容3', format)
		self.__monster.write(1, 43,'スキル内容4', format)
		self.__monster.write(1, 44,'リーダスキル', format)

	#
	# モンスターデータの保存
	#
	def writeMonsterData(self, arr):
		if arr[0] == "":
			del arr[0]
		self.__stockMonster.extend(arr)

	#
	# モンスターデータの行出力
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
		# 日付変換
		self.__stockMonster[14] = self.__stockMonster[14].replace('-', '/')
		self.__writeData(self.__monster, self.__stockMonster, self.__rowMonster, formatHash)
		self.__monster,
		self.__rowMonster += 1
		self.__stockMonster = []

	#
	# ルーン用__init__
	#
	def __initRunes(self):
		self.__rowRunes = 1
		self.__stockRunes = []
		self.__runeFormat = {}
		self.__runeComment = {}
		self.__runes   = self.__book.add_worksheet('runes')
		self.__initRunesExcel()

	#
	# ルーンWorksheetのヘッダ作成
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
		self.__runes.write(0,  1, 'ルーンID', format)
		self.__runes.write(0,  2, 'SLT', format)
		self.__runes.write(0,  3, '所持', format)
		self.__runes.write(0,  4, '星', format)
		self.__runes.write(0,  5, 'LV', format)
		self.__runes.write(0,  6, '種類', format)
		self.__runes.merge_range(0,   7, 0,   8, 'メイン', format)
		self.__runes.merge_range(0,   9, 0,  10, 'サブオプ', format)
		self.__runes.merge_range(0,  11, 0,  12, 'サブオプ１', format)
		self.__runes.merge_range(0,  13, 0,  14, 'サブオプ２', format)
		self.__runes.merge_range(0,  15, 0,  16, 'サブオプ３', format)
		self.__runes.merge_range(0,  17, 0,  18, 'サブオプ４', format)
		self.__runes.write(0,  19, '価値', format)
		self.__runes.write(0,  20, '', format)
		self.__runes.write(0,  21, '星', format)
		self.__runes.write(0,  22, '体%有無', format)
		self.__runes.write(0,  23, '攻%有無', format)
		self.__runes.write(0,  24, '防%有無', format)
		self.__runes.write(0,  25, '速　有無', format)
		self.__runes.write(0,  26, 'クリ有無', format)
		self.__runes.write(0,  27, 'ダメ有無', format)
		self.__runes.write(0,  28, '抵抗有無', format)
		self.__runes.write(0,  29, '的中有無', format)
		self.__runes.write(0,  30, '価格', format)
		self.__runes.write(0,  31, '売', format)
		self.__runes.write(0,  32, '売　備考', format)
		self.__runes.write(0,  33, 'ドロップランク', format)
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
	# ルーンデータの保存
	#
	def writeRuneData(self, arr):
		self.__stockRunes.extend(arr)

	#
	# ルーンデータの行出力
	#
	def writeRuneNextRow(self):
		format_def = self.__book.add_format({'border': 1})
		# パーセント表示
		format_per = self.__book.add_format({
			'border': 1,
			'num_format': '0.00%'
		})
		# 縮小して全体を表示
		format_shrink = self.__book.add_format({
			'border': 1,
			'shrink': 1,
		})
		# "0"を表示しない
		format_nonZero = self.__book.add_format({
			'border': 1,
			'num_format': '#;-#;"";@'
		})
		# 各列のフォーマットを設定
		formatHash = {}
		formatHash[ 1] = format_shrink	# ルーンID
		formatHash[19] = format_per		# ルーン価値
		formatHash[22] = format_nonZero	# 体%有無
		formatHash[23] = format_nonZero	# 攻%有無
		formatHash[24] = format_nonZero	# 防%有無
		formatHash[25] = format_nonZero	# 速　有無
		formatHash[26] = format_nonZero	# クリ有無
		formatHash[27] = format_nonZero	# ダメ有無
		formatHash[28] = format_nonZero	# 抵抗有無
		formatHash[29] = format_nonZero	# 的中有無

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
	# ルーンデータの書き出し行を取得
	#
	def getRuneRone(self):
		return self.__rowRunes


	#
	# セルの背景色を設定
	#
	def setRuneColorYellow(self, col, color):
		format = self.__book.add_format({'border': 1})
		if col in self.__runeFormat:
			format = self.__runeFormat[col]
		format.set_bg_color(color)
		self.__runeFormat[col] = format

	#
	# セルのコメントを設定
	#
	def setRuneComment(self, col, comment):
		self.__runeComment[col] = comment

	#
	# ルーン用__init__
	#
	def __initCraftItems(self):
		self.__rowCraftItems = 1
		self.__craftItems   = self.__book.add_worksheet('craftItems')
		self.__initCraftItemsExcel()

	#
	# 練磨・ジェムWorksheetのヘッダ作成
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
		self.__craftItems.write(0,  1, 'ルーンID', format)
		self.__craftItems.write(0,  2, 'sell_value', format)
		self.__craftItems.write(0,  3, 'craft_type_id', format)
		self.__craftItems.write(0,  4, 'craft_type', format)
		self.__craftItems.write(0,  5, 'runeSetName', format)
		self.__craftItems.write(0,  6, 'effectTypeName', format)
		self.__craftItems.write(0,  7, 'rarityName', format)
		self.__craftItems.write(0,  8, '種類', format)

	#
	# 練磨・ジェムWorksheetへ出力
	#
	def writeCraftItemData(self, arr):
		formatHash = {}
		self.__writeData(self.__craftItems, arr, self.__rowCraftItems, formatHash)
		self.__rowCraftItems += 1




	#
	# Excelワークブックの保存
	#
	def save(self):
		self.__book.close()

	#
	# Worksheetにデータ出力
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
