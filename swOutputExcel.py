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
		for var in range(2, 36):
			self.__monster.write(0, var, str(var))
		arr = [
			['No'          , 0,  1, self.headerFormat],
			['ID'          , 0,  1, self.headerFormat],
			['名前'        , 0,  1, self.headerFormat],
			['レベル'      , 0,  1, self.headerFormat],
			['★'          , 0,  1, self.headerFormat],
			['属性'        , 0,  1, self.headerFormat],
			['体力'        , 0,  1, self.headerFormat],
			['攻撃'        , 0,  1, self.headerFormat],
			['防御'        , 0,  1, self.headerFormat],
			['速度'        , 0,  1, self.headerFormat],
			['クリ率'      , 0,  1, self.headerFormat],
			['クリダメ'    , 0,  1, self.headerFormat],
			['抵抗'        , 0,  1, self.headerFormat],
			['的中'        , 0,  1, self.headerFormat],
			['作成日'      , 0,  1, self.headerFormat],
			['ルーン1'     , 0,  1, self.headerFormat],
			['ルーン2'     , 0,  1, self.headerFormat],
			['ルーン3'     , 0,  1, self.headerFormat],
			['ルーン4'     , 0,  1, self.headerFormat],
			['ルーン5'     , 0,  1, self.headerFormat],
			['ルーン6'     , 0,  1, self.headerFormat],
			['種類'        , 0,  1, self.headerFormat],
			['WB期待値'    , 0,  1, self.headerFormat],
			['S1レベル'    , 0,  1, self.headerFormat],
			['S1MAX'       , 0,  1, self.headerFormat],
			['S2レベル'    , 0,  1, self.headerFormat],
			['S2MAX'       , 0,  1, self.headerFormat],
			['S3レベル'    , 0,  1, self.headerFormat],
			['S3MAX'       , 0,  1, self.headerFormat],
			['S4レベル'    , 0,  1, self.headerFormat],
			['S4MAX'       , 0,  1, self.headerFormat],
			['覚醒名称'    , 0,  1, self.headerFormat],
			['スキル倍率1' , 0,  1, self.headerFormat],
			['スキル倍率2' , 0,  1, self.headerFormat],
			['スキル倍率3' , 0,  1, self.headerFormat],
			['スキル倍率4' , 0,  1, self.headerFormat],
			['スキル短縮1' , 0,  1, self.headerFormat],
			['スキル短縮2' , 0,  1, self.headerFormat],
			['スキル短縮3' , 0,  1, self.headerFormat],
			['スキル短縮4' , 0,  1, self.headerFormat],
			['スキル内容1' , 0,  1, self.headerFormat],
			['スキル内容2' , 0,  1, self.headerFormat],
			['スキル内容3' , 0,  1, self.headerFormat],
			['スキル内容4' , 0,  1, self.headerFormat],
			['リーダスキル', 0,  1, self.headerFormat],
		]
		self.__writeHeader(self.__monster, arr)

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
		formatHash = {}
		formatHash[ 1] = self.shrinkFormat
		formatHash[14] = self.dateFormat
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
		arr = [
			['No'            ,  5.38,  1, self.headerFormat2],
			['ルーンID'      , 11   ,  1, self.headerFormat2],
			['SLT'           ,  3   ,  1, self.headerFormat2],
			['所持'          , 14.13,  1, self.headerFormat2],
			['星'            ,  4.63,  1, self.headerFormat2],
			['LV'            ,  3.25,  1, self.headerFormat2],
			['種類'          ,  3.5 ,  1, self.headerFormat2],
			['メイン'        ,  4.13,  2, self.headerFormat2],
			[''              ,  4.63, -1, self.headerFormat2],
			['サブオプ'      ,  4.13,  2, self.headerFormat2],
			[''              ,  4.63, -1, self.headerFormat2],
			['サブオプ１'    ,  4.13,  2, self.headerFormat2],
			[''              ,  4.63, -1, self.headerFormat2],
			['サブオプ２'    ,  4.13,  2, self.headerFormat2],
			[''              ,  4.63, -1, self.headerFormat2],
			['サブオプ３'    ,  4.13,  2, self.headerFormat2],
			[''              ,  4.63, -1, self.headerFormat2],
			['サブオプ４'    ,  4.13,  2, self.headerFormat2],
			[''              ,  4.63, -1, self.headerFormat2],
			['価値'          ,  6.5 ,  1, self.headerFormat2],
			['星'            ,  9   ,  1, self.headerFormat2],
			[''              ,  3.25,  1, self.headerFormat2],
			['体%有無'       ,  4.75,  1, self.headerFormat2],
			['攻%有無'       ,  4.75,  1, self.headerFormat2],
			['防%有無'       ,  4.75,  1, self.headerFormat2],
			['速　有無'      ,  4.75,  1, self.headerFormat2],
			['クリ有無'      ,  4.75,  1, self.headerFormat2],
			['ダメ有無'      ,  4.75,  1, self.headerFormat2],
			['抵抗有無'      ,  4.75,  1, self.headerFormat2],
			['的中有無'      ,  4.75,  1, self.headerFormat2],
			['価格'          ,  7.25,  1, self.headerFormat2],
			['売'            ,  5.13,  1, self.headerFormat2],
			['売　備考'      ,  4.38,  1, self.headerFormat2],
			['ドロップランク',  5.38,  1, self.headerFormat2],
		]
		self.__writeHeader(self.__runes, arr)
		self.__runes.set_zoom(90)

	#
	# ルーンデータの保存
	#
	def writeRuneData(self, arr):
		self.__stockRunes.extend(arr)

	#
	# ルーンデータの行出力
	#
	def writeRuneNextRow(self):
		# 各列のフォーマットを設定
		formatHash = {}
		formatHash[ 1] = self.shrinkFormat	# ルーンID
		formatHash[19] = self.perFormat		# ルーン価値
		formatHash[22] = self.nonZeroFormat	# 体%有無
		formatHash[23] = self.nonZeroFormat	# 攻%有無
		formatHash[24] = self.nonZeroFormat	# 防%有無
		formatHash[25] = self.nonZeroFormat	# 速　有無
		formatHash[26] = self.nonZeroFormat	# クリ有無
		formatHash[27] = self.nonZeroFormat	# ダメ有無
		formatHash[28] = self.nonZeroFormat	# 抵抗有無
		formatHash[29] = self.nonZeroFormat	# 的中有無

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
		arr = [
			['No'            , 0,  1, self.headerFormat2],
			['ルーンID'      , 0,  1, self.headerFormat2],
			['sell_value'    , 0,  1, self.headerFormat2],
			['craft_type_id' , 0,  1, self.headerFormat2],
			['craft_type'    , 0,  1, self.headerFormat2],
			['runeSetName'   , 0,  1, self.headerFormat2],
			['effectTypeName', 0,  1, self.headerFormat2],
			['rarityName'    , 0,  1, self.headerFormat2],
			['種類'          , 0,  1, self.headerFormat2],
		]
		self.__writeHeader(self.__craftItems, arr)

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
	# worksheetにヘッダ出力
	#
	def __writeHeader(self, target, arr):
		for i in range(0, len(arr)):
			value, width, colspan, format = arr[i]
			if colspan > 1:
				target.merge_range(0, i, 0, i+colspan-1, value, format)
			elif colspan == -1:
				#なにもしない
				pass
			else:
				target.write(0,  i, value, format)
			if width > 0:
				target.set_column(i, i, width)
	#
	# Worksheetにデータ出力
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
