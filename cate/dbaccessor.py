from journal_cate import journal_cate_processor
from pymongo import MongoClient
from logger import mylogger
class mydb:
	def __init__(self):
		self.client = MongoClient(
			'210.30.97.43',
            username='userRW',
			password='thealphaRW',
			authSource='ms-datasets',
            authMechanism='SCRAM-SHA-1'
			)
		self.db = self.client['ms-datasets']
		self.collnames = ['mag_papers_0','mag_papers_1','mag_papers_2','mag_papers_3'
						,'mag_papers_4','mag_papers_5','mag_papers_6','mag_papers_7','mag_papers_8']
	def insert_item(self,data):
		try:
			mylogger.info('start to insert by using isert_item function')
			db = self.db
			coll = db["Computer_Science"]
			coll.insert(data)
			mylogger.info('paper {} get its categories'.format(data['id']))
		except Exception as e:
			print(e)

	def match_paper(self,collname,journal_dict):
		coll=self.db[collname]
		mylogger.crit(' match the papers in {}'.format(collname))
		for jour,cates in journal_dict.items():
			mylogger.crit('matching the {} in the collocation {}'.format(jour,collname))
			cursor = coll.find({'venue':jour}).batch_size(50)
			mylogger.crit('get the matches of {} in the collocation {}'.format(jour,collname))
			itemdic = dict()
			mylogger.crit('begin to insert the matches of {} in the collocation {}'.format(jour,collname))
			for paper in cursor:
				itemdic['venue']=paper['venue']
				itemdic["id"]=paper["id"]
				itemdic["title"]=paper["title"]
				itemdic["subject area"]="Computer Science"
				itemdic["subject categories"]=journal_dict[jour]
				self.insert_item(itemdic)
				itemdic.clear()
			mylogger.crit('finish inserting matches of {} in the collocation {}'.format(jour,collname))



				
				