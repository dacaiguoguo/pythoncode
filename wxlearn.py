#!usr/bin/env python
# -*- coding: utf-8 -*-
# hanhan load
import wx 
from base64 import encodestring
import json
import hashlib   
import re


def load(event):
    m2 = hashlib.md5()   
    m2.update(contents.GetValue().encode('utf-8'))   
    contents.SetValue(m2.hexdigest())
def base64fun(event):
    base64string = encodestring(contents.GetValue().encode('utf-8'))
    print base64string
    contents.SetValue(base64string)
def jsonfom(event):
    contentstext = contents.GetValue()
    dic = json.loads(contentstext)
    jsonfomdstring = json.dumps(dic, indent=4, ensure_ascii=False)   
    contents.SetValue(jsonfomdstring)

def jsonre(event):
    contentstext = contents.GetValue()
    strinfo = re.compile(r'"')
    jsonfomdstring = strinfo.sub(r'\"',contentstext) 
    contents.SetValue(jsonfomdstring)

if __name__ == '__main__':
    app = wx.App()
    win = wx.Frame(None, title = 'show', size = (410,335))
    bkg = wx.Panel(win)
    loadButton = wx.Button(bkg, label = 'md5')
    loadButton.Bind(wx.EVT_BUTTON, load)
    base64Button = wx.Button(bkg, label = 'base64')
    base64Button.Bind(wx.EVT_BUTTON, base64fun)
    jsonButton = wx.Button(bkg, label = 'json格式化')
    jsonButton.Bind(wx.EVT_BUTTON, jsonfom)
    jsonReButton = wx.Button(bkg, label = 'json转义')
    jsonReButton.Bind(wx.EVT_BUTTON, jsonre)
    contents = wx.TextCtrl(bkg, style = wx.TE_WORDWRAP| wx.HSCROLL, validator=wx.DefaultValidator)
    hbox = wx.BoxSizer()
    hbox.Add(loadButton, proportion = 1, flag = wx.LEFT, border = 5)
    hbox.Add(base64Button, proportion = 1, flag = wx.LEFT, border = 5)
    hbox.Add(jsonButton, proportion = 1, flag = wx.LEFT, border = 5)
    vbox= wx.BoxSizer(wx.VERTICAL)
    vbox.Add(hbox, proportion = 0, flag = wx.EXPAND| wx.ALL, border = 5)
    vbox.Add(contents, proportion = 1, flag = wx.EXPAND| wx.LEFT| wx.BOTTOM|wx.RIGHT, border = 5)
    bkg.SetSizer(vbox)
    win.Show()
    app.MainLoop()

    