from dbaccessor import mydb
from journal_cate import journal_cate_processor
from logger import Logger
import threading
def main():
	print("the program starts!")
	print("begin to process the category data!")
	journal_dic_generator = journal_cate_processor(".\computerScienceJR.xlsx")
	journal_dic = journal_dic_generator.process()
	print("the journal category dictionary has been successfully built.")
	db =mydb()#create a mongo db accessor
	collnames = db.collnames#get all the collacation names of database ms-datasets
	threads =[]
	for collname in collnames:
		threads.append(threading.Thread(target=db.match_paper,args=(collname,journal_dic,)))
	for t in threads:
		t.start()
	for t in threads:
		t.join()
	print("Congratulations!!! All the papers of Computer Science find their categories.")

	
if __name__ == '__main__':
	main()