# Notification of class change NIT GC

## Abstract
This software is for notifying class change of NIT,GC. Only supporting Linux System.
Not available for Windows.

## How to use
First, you need to install xpdf on your linux system. In ubuntu,

```
$ sudo apt-get install xpdf xpdf-japanese
```
An error may occur when you install. Don't worry. Manual install is available. To obtain more detail, visit xpdf official web site.

<br>

Next, clone this project and run main.py

```
$ python main.py
```
Then, the class change list was displayed.


## Option

Filter with gakunen and gakka.

```
$ python main.py --filter [1E|2E|2C etc...]
```


To avoid to download pdf, Use chache.
```
$ python main.py --chache true
```


<!--
```
$ python main.py --date 2/2
```

```
$ python main.py --gakka [M|E|C|D|A|Y|S|K]
```

```
$ python main.py --gakunen [1|2|3|4|5]
```
-->



## Other
To use this, at your own lisk.





