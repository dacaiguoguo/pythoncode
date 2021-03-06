# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import json

url = "http://lvioscode.com/dashboard/todos?\
state=&utf8=✓&project_id=&author_id=&type=&action_id=&\
private_token=wVbqcqQyWmH7jvgNsmZf"
cookies = {}
# yes 可以使用cookie 也可以参数里加private_token 来授权
# cookies["_gitlab_session"]="b164db7ed4344f78f46bc3a99d00a8b8"
# cookies["issuable_sort"]="id_desc"
resp = requests.get(url, cookies=cookies)

html_doc = resp.text
soup = BeautifulSoup(html_doc, "html.parser")
# print soup
allTodo = []
for panelDiv in soup.find_all("div"):
    panelClass = panelDiv["class"][0]
    if panelClass == "panel":
        for panelHeadingDiv in panelDiv.find_all("div"):
            panelHeadingClass = panelHeadingDiv["class"][0]
            if panelHeadingClass == "panel-heading":
                oneTodo = {}
                todoItems = []
                for todoItemDiv in panelDiv.find_all("div"):
                    todoItemClass = todoItemDiv["class"][0]
                    if todoItemClass == "todo-item":
                        oneTodo["space"] = (panelHeadingDiv.find_all("a")[0]).text.replace("\n", "").replace(" ", "")
                        oneTodoSub = {}
                        indexOfA = 0
                        for title in todoItemDiv.find_all("a"):
                            if indexOfA ==  0:
                                oneTodoSub["name"] = title.text.replace("\n", "").replace(" ", "")
                            if indexOfA ==  1:
                                oneTodoSub["merge"] = title.text.replace("\n", "").replace(" ", "")
                            if indexOfA ==  2:
                                oneTodoSub["status"] = title.text.replace("\n", "").replace(" ", "")
                                todoItems.append(oneTodoSub)
                            indexOfA = indexOfA + 1
                        oneTodo["items"] = todoItems
        allTodo.append(oneTodo)
jsondump = json.dumps(allTodo)
print jsondump
