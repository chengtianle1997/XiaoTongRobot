# -*- coding: utf-8 -*-

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from DetailWidget import DetailWidget
from Ui_KeyBoard import Ui_KeyBoard

str_key = ""
m_nType = 1
m_pPoint = (0, 0)


class KeyBoard(QWidget, Ui_KeyBoard):

	signalShowText = QtCore.pyqtSignal(str)

	def __init__(self, parent=None):
		super(KeyBoard, self).__init__(parent)
		self.setupUi(self)
		self.setWindowFlags(Qt.WindowStaysOnTopHint)
		self.m_pDetailWidget = DetailWidget()
		self.m_pDetailWidget.signalText.connect(self.slot_text)
		self.btn_0.clicked.connect(self.on_btn_f0_clicked)
		self.btn_1.clicked.connect(self.on_btn_f1_clicked)
		self.btn_2.clicked.connect(self.on_btn_f2_clicked)
		self.btn_3.clicked.connect(self.on_btn_f3_clicked)
		self.btn_4.clicked.connect(self.on_btn_f4_clicked)
		self.btn_5.clicked.connect(self.on_btn_f5_clicked)
		self.btn_6.clicked.connect(self.on_btn_f6_clicked)
		self.btn_7.clicked.connect(self.on_btn_f7_clicked)
		self.btn_8.clicked.connect(self.on_btn_f8_clicked)
		self.btn_9.clicked.connect(self.on_btn_f9_clicked)
		#
		self.btn_Sym.clicked.connect(self.on_btn_sym_clicked)
		self.btn_Sma.clicked.connect(self.on_btn_sma_clicked)
		self.btn_Cap.clicked.connect(self.on_btn_cap_clicked)
		self.btn_Num.clicked.connect(self.on_btn_num_clicked)

		self.btn_Space.clicked.connect(self.on_btn_space_clicked)
		self.btn_Point.clicked.connect(self.on_btn_point_clicked)

		self.btn_Hide.clicked.connect(self.on_btn_hide_clicked)
		self.btn_Show.clicked.connect(self.on_btn_show_clicked)

		self.btn_Del.clicked.connect(self.on_btn_del_clicked)
		self.btn_Again.clicked.connect(self.on_btn_again_clicked)
		self.btn_Wrap.clicked.connect(self.on_btn_wrap_clicked)
		self.btn_Sure.clicked.connect(self.on_btn_sure_clicked)

	# 鼠標事件
	def mousePressEvent(self, event):
		global m_pPoint
		m_pPoint = event.globalPos() - self.pos()
		event.accept()

	# 鼠標事件
	def mouseMoveEvent(self, event):
		self.move(event.globalPos() - m_pPoint)
		event.accept()

	# 鼠標事件
	def enterEvent(self, event):
		self.setCursor(Qt.PointingHandCursor)
		event.accept()

	# 鼠標事件
	def leaveEvent(self, event):
		self.setCursor(Qt.ArrowCursor)
		event.accept()

	# 0鍵
	def on_btn_f0_clicked(self):
		global str_key
		global m_nType
		if m_nType == 1:
			str_key += "0"
			self.btn_Show.setText(str_key)
		elif m_nType == 2:
			str_key += " "
			self.btn_Show.setText(str_key)
		elif m_nType == 3:
			str_key += "△"
			self.btn_Show.setText(str_key)

	# 1鍵
	def on_btn_f1_clicked(self):
		global str_key
		if m_nType == 1:
			str_key += "1"
			self.btn_Show.setText(str_key)
		elif m_nType == 2:
			qstr = ',;?;!;'
			strList = qstr.split(';')
			self.m_pDetailWidget.set_small_pad_text(strList)
			m_pPoint = self.btn_1.pos() + self.pos()
			self.m_pDetailWidget.move(m_pPoint.x(), m_pPoint.y() - 35)
		elif m_nType == 3:
			str_key += "@"
			self.btn_Show.setText(str_key)

	#2鍵
	def on_btn_f2_clicked(self):
		global str_key
		if m_nType == 1:
			str_key += "2"
			self.btn_Show.setText(str_key)
		elif m_nType == 2:
			if self.btn_Space.isChecked():
				qstr = 'A;B;C;'
			else:
				qstr = 'a;b;c;'
			qList = qstr.split(';')
			print(qList)
			self.m_pDetailWidget.set_small_pad_text(qList)
			m_pPoint = self.btn_2.pos() + self.pos()
			self.m_pDetailWidget.move(m_pPoint.x(),m_pPoint.y() - 35)
		elif m_nType == 3:
			str_key += "%"
			self.btn_Show.setText(str_key)

	# 3鍵
	def on_btn_f3_clicked(self):
		global str_key
		if m_nType == 1:
			str_key += "3"
			self.btn_Show.setText(str_key)
		elif m_nType == 2:
			if self.btn_Space.isChecked():
				qstr = 'D;E;F;'
			else:
				qstr = 'd;e;f;'
			qList = qstr.split(';')
			self.m_pDetailWidget.set_small_pad_text(qList)
			m_pPoint = self.btn_3.pos() + self.pos()
			self.m_pDetailWidget.move(m_pPoint.x(), m_pPoint.y() - 35)
		elif m_nType == 3:
			str_key += "!"
			self.btn_Show.setText(str_key)

	# 4鍵
	def on_btn_f4_clicked(self):
		global str_key
		if m_nType == 1:
			str_key += "4"
			self.btn_Show.setText(str_key)
		elif m_nType == 2:
			if self.btn_Space.isChecked():
				qstr = 'G;H;I;'
			else:
				qstr = 'g;h;i;'
			qList = qstr.split(';')
			self.m_pDetailWidget.set_small_pad_text(qList)
			m_pPoint = self.btn_4.pos() + self.pos()
			self.m_pDetailWidget.move(m_pPoint.x(), m_pPoint.y() - 35)
		elif m_nType == 3:
			str_key += "+"
			self.btn_Show.setText(str_key)

	# 5鍵
	def on_btn_f5_clicked(self):
		global str_key
		if m_nType == 1:
			str_key += "5"
			self.btn_Show.setText(str_key)
		elif m_nType == 2:
			if self.btn_Space.isChecked():
				qstr = 'J;K;L;'
			else:
				qstr = 'j;k;l;'
			qList = qstr.split(';')
			self.m_pDetailWidget.set_small_pad_text(qList)
			m_pPoint = self.btn_5.pos() + self.pos()
			self.m_pDetailWidget.move(m_pPoint.x(), m_pPoint.y() - 35)
		elif m_nType == 3:
			str_key += "*"
			self.btn_Show.setText(str_key)

	# 6鍵
	def on_btn_f6_clicked(self):
		global str_key
		if m_nType == 1:
			str_key += "6"
			self.btn_Show.setText(str_key)
		elif m_nType == 2:
			if self.btn_Space.isChecked():
				qstr = 'O;M;N;'
			else:
				qstr = 'o;m;n;'
			qList = qstr.split(';')
			self.m_pDetailWidget.set_small_pad_text(qList)
			m_pPoint = self.btn_6.pos() + self.pos()
			self.m_pDetailWidget.move(m_pPoint.x(), m_pPoint.y() - 35)
		elif m_nType == 3:
			str_key += "√"
			self.btn_Show.setText(str_key)

	# 7鍵
	def on_btn_f7_clicked(self):
		global str_key
		if m_nType == 1:
			str_key += "7"
			self.btn_Show.setText(str_key)
		elif m_nType == 2:
			if self.btn_Space.isChecked():
				qstr = 'P;Q;R;S'
			else:
				qstr = 'p;q;r;s'
			qList = qstr.split(';')
			self.m_pDetailWidget.set_small_pad_text(qList)
			m_pPoint = self.btn_7.pos() + self.pos()
			self.m_pDetailWidget.move(m_pPoint.x(), m_pPoint.y() - 35)
		elif m_nType == 3:
			str_key += "-"
			self.btn_Show.setText(str_key)

	# 8鍵
	def on_btn_f8_clicked(self):
		global str_key
		if m_nType == 1:
			str_key += "8"
			self.btn_Show.setText(str_key)
		elif m_nType == 2:
			if self.btn_Space.isChecked():
				qstr = 'T;U;V;'
			else:
				qstr = 't;u;v;'
			qList = qstr.split(';')
			self.m_pDetailWidget.set_small_pad_text(qList)
			m_pPoint = self.btn_8.pos() + self.pos()
			self.m_pDetailWidget.move(m_pPoint.x(), m_pPoint.y() - 35)
		elif m_nType == 3:
			str_key += "/"
			self.btn_Show.setText(str_key)

	# 9鍵
	def on_btn_f9_clicked(self):
		global str_key
		if m_nType == 1:
			str_key += "9"
			self.btn_Show.setText(str_key)
		elif m_nType == 2:
			if self.btn_Space.isChecked():
				qstr = 'W;X;Y;Z'
			else:
				qstr = 'w;x;y;z'
			qList = qstr.split(';')
			self.m_pDetailWidget.set_small_pad_text(qList)
			m_pPoint = self.btn_9.pos() + self.pos()
			self.m_pDetailWidget.move(m_pPoint.x(), m_pPoint.y() - 35)
		elif m_nType == 3:
			str_key += "×"
			self.btn_Show.setText(str_key)

	# 數字模式
	def on_btn_num_clicked(self):
		global m_nType
		m_nType = 1
		self.init_pad_text(1)
		self.btn_Space.setCheckable(False)
		self.btn_Space.setChecked(False)

	# 大寫
	def on_btn_cap_clicked(self):
		global m_nType
		m_nType = 2
		self.btn_Space.setCheckable(True)
		self.btn_Space.setChecked(True)
		self.init_pad_text(2)

	# 小寫
	def on_btn_sma_clicked(self):
		global m_nType
		m_nType = 2
		self.btn_Space.setCheckable(True)
		self.btn_Space.setChecked(False)
		self.init_pad_text(2)

	# 符號
	def on_btn_sym_clicked(self):
		global m_nType
		m_nType = 3
		self.init_pad_text(3)
		self.btn_Space.setCheckable(False)
		self.btn_Space.setChecked(False)

	# 回退
	def on_btn_del_clicked(self):
		global str_key
		str_key = self.btn_Show.text()
		str_key = str_key[0:len(str_key) - 1]
		self.btn_Show.setText(str_key)

	# 清除
	def on_btn_again_clicked(self):
		global str_key
		str_key = ""
		self.btn_Show.setText(str_key)

	# 換行
	def on_btn_wrap_clicked(self):
		global str_key
		str_key += "\n"
		self.btn_Show.setText(str_key)

	# 關閉
	def on_btn_hide_clicked(self):
		self.on_btn_again_clicked()
		self.hide()
		self.m_pDetailWidget.hide()

	# 顯示
	def on_btn_show_clicked(self):
		global str_key
		self.signalShowText.emit(self.btn_Show.text())
		str_key = ""
		self.btn_Show.setText("")

	# 空格
	def on_btn_space_clicked(self):
		global str_key
		if m_nType == 1:
			str_key += " "
			self.btn_Show.setText(str_key)
		elif m_nType == 2:
			if self.btn_Space.isChecked():
				self.on_btn_cap_clicked()
			else:
				self.on_btn_sma_clicked()
		else:
			str_key += " "
			self.btn_Show.setText(str_key)

	#點
	def on_btn_point_clicked(self):
		global str_key
		str_key += "."
		self.btn_Show.setText(str_key)

	# 確定
	def on_btn_sure_clicked(self):
		global str_key
		self.signalShowText.emit(self.btn_Show.text())
		str_key = ""
		self.btn_Show.setText("")

	# 初始化鍵盤
	def init_pad_text(self, m_type):
		if m_type == 1:
			qstr = '1;2;3;4;5;6;7;8;9;└┘;0'
			qList = qstr.split(';')
			self.set_pad_text(qList)
		elif m_type == 2:
			if self.btn_Space.isChecked():
				qstr = ',?!;ABC;DEF;GHI;JKL;OMN;PQRS;TUV;WXYZ;shift;└┘'
				qList = qstr.split(';')
				self.set_pad_text(qList)
			else:
				qstr = ',?!;abc;def;ghi;jkl;omn;pqrs;tuv;wxyz;shift;└┘'
				qList = qstr.split(';')
				self.set_pad_text(qList)
		elif m_type == 3:
			qstr = '@;%;!;+;*;√;-;/;×;└┘;△'
			qList = qstr.split(';')
			self.set_pad_text(qList)

	# 設置鍵盤字符
	def set_pad_text(self, strlist ):
		self.btn_1.setText(strlist[0])
		self.btn_2.setText(strlist[1])
		self.btn_3.setText(strlist[2])

		self.btn_4.setText(strlist[3])
		self.btn_5.setText(strlist[4])
		self.btn_6.setText(strlist[5])

		self.btn_7.setText(strlist[6])
		self.btn_8.setText(strlist[7])
		self.btn_9.setText(strlist[8])
		self.btn_Space.setText(strlist[9])
		self.btn_0.setText(strlist[10])

	# 接收小鍵盤數據
	def slot_text(self, str_text):
		global str_key
		str_key += str_text
		self.btn_Show.setText(str_key)

# if __name__ == "__main__":
# 	import sys
# 	app = QtWidgets.QApplication(sys.argv)
# 	m_pkeyBoard = KeyBoard()
# 	m_pkeyBoard.show()
# 	sys.exit(app.exec_())
