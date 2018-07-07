from journal_cate import journal_cate_processor
from pymongo import MongoClient
from logger import mylogger
import threading
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

	def update_paper_main(self,collname,journal_dict):
		threads=[]
		for jour,cates in journal_dict.items():
			threads.append(threading.Thread(target=self.update_paper,args=(collname,jour,cates)))
		for t in threads:
			t.start()
		for t in threads:
			t.join()

	def update_paper(self,collname,jour,cates):
		coll=self.db[collname]
		mylogger.crit('matching the {} in the collocation {}'.format(jour,collname))
		coll.update_many({'venue':jour},{"$set":{"subject area":"Computer Science","subject category":cates}})
		mylogger.crit('finish updating matches of {} in the collocation {}'.format(jour,collname))
	



				
				