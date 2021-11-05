from stackshare_class.stackshare import StackShare

new = StackShare()
new.get_page(language="javascript")
companies = new.get_companies()
print(companies)

