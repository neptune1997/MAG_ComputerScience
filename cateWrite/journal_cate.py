import xlrd
class journal_cate_processor:
	def __init__(self,filepath):
		self.filepath=filepath
		self.wb = xlrd.open_workbook(filepath,'r')
		self.table = self.wb.sheets()[0]
	def process(self):
		nrows = self.table.nrows
		ncols = self.table.ncols
		journal_dic = {};
		for i in range(1,nrows):
			journal = self.table.cell(i,2).value
			cates = []
			for j in self.table.cell(i,16).value.split("; "):
				cates.append(j.split(" (Q1)")[0])
			journal_dic[journal]=cates
		return journal_dic

if __name__=='__main__':
	file = open(".\journals.txt",'w')
	pj = journal_cate_processor(".\computerScienceJR.xlsx")
	diction = pj.process()
	for journal in diction:
		file.write(journal+"\n")

