from notion_client import Client
import os

# notion_token = os.getenv("NOTION_TOKEN")
# print(notion_token)

notion = Client(auth=os.environ["NOTION_TOKEN"])
print(notion)




def main():
    print('hello')

if  __name__ == '__main__':
    main()
    