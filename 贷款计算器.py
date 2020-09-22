import tkinter as tk  # 使用Tkinter前需要先导入

window = tk.Tk()
window.title('贷款计算器')

#window.geometry('300x200')
ShouFuBox = tk.StringVar()
BenJinBox = tk.StringVar()
NianBox = tk.StringVar()
LiLvBox = tk.StringVar()
NianShouYiBox = tk.StringVar()
WuGuanFeiBox = tk.StringVar()

tk.Label(window,text='首付/万:').grid(row=0,column=0,sticky='w')
tk.Entry(window,show=None,textvariable=ShouFuBox,width=10).grid(row=0,column=1)
tk.Label(window,text='贷款/万:').grid(row=0,column=2,sticky='w')
tk.Entry(window,show=None,textvariable=BenJinBox,width=10).grid(row=0,column=3)
tk.Label(window,text='贷款年限/年:').grid(row=0,column=4,sticky='w')
tk.Entry(window,show=None,textvariable=NianBox,width=10).grid(row=0,column=5)
tk.Label(window,text='贷款年利率/%:').grid(row=1,column=0,sticky='w')
tk.Entry(window,show=None,textvariable=LiLvBox,width=10).grid(row=1,column=1)
tk.Label(window,text='投资年收益率/%:').grid(row=1,column=2,sticky='w')
tk.Entry(window,show=None,textvariable=NianShouYiBox,width=10).grid(row=1,column=3)
tk.Label(window,text='物管费/元/月:').grid(row=1,column=4,sticky='w')
tk.Entry(window,show=None,textvariable=WuGuanFeiBox,width=10).grid(row=1,column=5)

def CalcProcess(): 
	ShouFu = int(ShouFuBox.get())
	BenJin = int(BenJinBox.get())
	Nian = int(NianBox.get())
	LiLv = float(LiLvBox.get())
	NianShouYi = float(NianShouYiBox.get())
	WuGuanFei = float(WuGuanFeiBox.get())

	QiShu   = Nian * 12
	YueLiLv = LiLv / 100 / 12
	YueShouYi = NianShouYi / 100 / 12
	HuanKuan = BenJin * 10000 * YueLiLv * (1+YueLiLv) ** QiShu / ((1+YueLiLv) ** QiShu - 1)

	tk.Label(window,text=str(round(HuanKuan))).grid(row=2,column=3,sticky='w')
	for i in range(Nian):
		tk.Label(window,text=str('第'+str(i+1)+'年房价/万：')).grid(row=3+i,column=0,sticky='w')
		tk.Label(window,text='利息成本/万').grid(row=3+i,column=2,sticky='w')
		tk.Label(window,text='收益损失/万').grid(row=3+i,column=4,sticky='w')

	ShengYuBenJin = BenJin * 10000
	LeiJiLiXi = 0
	LeiJiBenJin = 0
	YueGongShouYi = 0
	for i in range(1,int(QiShu)+1):
		YueLiXi = ShengYuBenJin * YueLiLv
		LeiJiLiXi += YueLiXi
		LeiJiBenJin += HuanKuan - YueLiXi
		ShengYuBenJin -= HuanKuan - YueLiXi
		YueGongShouYi += HuanKuan*i*YueShouYi
		ZongChengBen = ShouFu*10000 + HuanKuan*i + ShouFu*i*YueShouYi*10000 + YueGongShouYi + WuGuanFei*i
		FangJia = ZongChengBen + ShengYuBenJin
		ZhangFu = (FangJia/10000/(ShouFu+BenJin)-1) * 100

		if (i-1)%12 == 0:
			year = int((i-1)/12)
			tk.Label(window,text=str(round(FangJia/10000,1))).grid(row=3+year,column=1,sticky='w')
			tk.Label(window,text=str(round(LeiJiLiXi/10000,1))).grid(row=3+year,column=3,sticky='w')
			tk.Label(window,text=str(round(ShouFu*i*YueShouYi+YueGongShouYi/10000,1))).grid(row=3+year,column=5,sticky='w')

tk.Button(window, text='开始计算', command=CalcProcess).grid(row=2,column=0,sticky='w')
tk.Label(window,text='等额本息/每月:').grid(row=2,column=2,sticky='w')

window.mainloop()