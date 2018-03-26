# coding:utf-8
import gettext 

def print_en():
    _ = gettext.gettext
    print '\nEnglish'
    print _('You are a sweet girl!')
    print _('My name is {name}').format(name='orangleliu')

def print_cn():
    t = gettext.translation('demo', 'locale', languages=["zh_CN"])
    _ = t.gettext
    print '\n中文'
    print _('You are a sweet girl!')
    print _('My name is {name}').format(name='orangleliu')

print_cn()
print_en()