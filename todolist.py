#-*- coding: UTF-8 -*- 
import sys
import requests
from bs4 import BeautifulSoup
import json

url="http://lvioscode.com/dashboard/todos?state=&utf8=✓&project_id=&author_id=&type=&action_id="
cookies={}
cookies["_gitlab_session"]="b164db7ed4344f78f46bc3a99d00a8b8"
cookies["issuable_sort"]="id_desc"
resp = requests.get(url,cookies=cookies)

html_doc = resp.text
soup = BeautifulSoup(html_doc,"html.parser")
# print soup
allTodo = []
for panelDiv in soup.find_all("div"):
  panelClass = panelDiv["class"][0]
  if panelClass == "panel":
    for panelHeadingDiv in panelDiv.find_all("div"):
      panelHeadingClass = panelHeadingDiv["class"][0]
      if panelHeadingClass == "panel-heading":
        oneTodoList = []
        for todoItemDiv in panelDiv.find_all("div"):
          todoItemClass = todoItemDiv["class"][0]
          oneTodo = {}
          if todoItemClass == "todo-item":
            oneTodo["space"] = (panelHeadingDiv.find_all("a")[0]).text.replace("\n", "").replace(" ", "")
            indexOfA = 0
            for title in todoItemDiv.find_all("a"):
              if indexOfA ==  0:
                oneTodo["name"] = title.text.replace("\n", "").replace(" ", "")
              if indexOfA ==  1:
                oneTodo["merge"] = title.text.replace("\n", "").replace(" ", "")
              if indexOfA ==  2:
                oneTodo["status"] = title.text.replace("\n", "").replace(" ", "")
                oneTodoList.append(oneTodo)
                oneTodo = {}
              indexOfA = indexOfA + 1
    allTodo.append(oneTodoList)        
jsondump = json.dumps(allTodo)
print jsondump
