python-i18n-demo
=========

下面的例子中实现 `python i18n` 英文和中文 双语显示，因为实现这个功能还是需要几个步骤的，网络上有些例子，但是当时没有找到一个符合心意的，于是写一个备用，尽量好上手。

测试环境

* MacOS 10.13.1
* Python2.7.x

[python gettext doc](https://docs.python.org/2/library/gettext.html)

### gettext 

首先需要一个工具 `gettext`, macos 上已经有了但是没有放到 `/usr/bin` 目录，所以先执行
```
brew link --force gettext
```

打开shell，测试下 `gettext -h`, 看看输出是否正常。

Centos应该是默认安装了这个组件，`gettext -h` 便可以看到，其他系统安装起来应该不是很难。

### 案例

主要是2个小例子

* 纯文本怎样显示中英文
* 带有占位符的句子怎么样显示中英文

创建 demo.py 
```
# coding:utf-8
import gettext 

_ = gettext.gettext


print _('You are a sweet girl!')
print _('My name is {name}').format(name='orangleliu')
```

此时执行测试下
```
$ python demo.py
You are a sweet girl!
My name is orangleliu
```

#### 制作翻译

提取要翻译的句子
```
xgettext -o demo.po demo.py --from-code utf-8
```

打开 `demo.po`, 记得修改字符编码为 `UTF-8`, 翻译下需要翻译的句子
```
# SOME DESCRIPTIVE TITLE.
# Copyright (C) YEAR THE PACKAGE'S COPYRIGHT HOLDER
# This file is distributed under the same license as the PACKAGE package.
# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
#
#, fuzzy
msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\n"
"Report-Msgid-Bugs-To: \n"
"POT-Creation-Date: 2018-03-26 22:53+0800\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
"Language-Team: LANGUAGE <LL@li.org>\n"
"Language: \n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=CHARSET\n"
"Content-Transfer-Encoding: 8bit\n"

#: demo.py:7
msgid "You are a sweet girl!"
msgstr ""

#: demo.py:8
#, python-brace-format
msgid "My name is {name}"
msgstr ""
```

修改之后
```
... #不变的部分
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"

#: demo.py:7
msgid "You are a sweet girl!"
msgstr "您是个甜美的女生!"

#: demo.py:8
#, python-brace-format
msgid "My name is {name}"
msgstr "我的名字是 {name}"
```

接下来创建目录，切换到中文翻译目录，生成mo文件
```
mkdir -p locale/zh_CN/LC_MESSAGES
mv demo.po locale/zh_CN/LC_MESSAGES
cd locale/zh_CN/LC_MESSAGES
msgfmt -o demo.mo demo.po
```

再来修改 `demo.py` 支持双语显示

```
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
```

再来看下执行的结果
```
$ python demo.py

中文
您是个甜美的女生!
我的名字是 orangleliu

English
You are a sweet girl!
My name is orangleliu
```
