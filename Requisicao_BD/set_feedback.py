from dotenv import load_dotenv
from Log import Log

if (__name__ == "__main__"):
	load_dotenv(dotenv_path='login.env')
	log = Log()

	query = input("Query: ")
	if not query:
		log.set_feedback()
	else:
		log.set_feedback(query=query)

	log.con.close()
