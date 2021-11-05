from stackshare_class.stackshare import StackShare
from dotenv import load_dotenv


if (__name__ == "__main__"):
	load_dotenv(dotenv_path='login.env')

	scrap = StackShare()

	scrap.get_stacks_by_companies()
	