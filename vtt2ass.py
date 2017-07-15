#! D:\python36\python3
# -*- coding: utf-8 -*- 


import sys,os
import codecs
import xml.etree.ElementTree as ET
from copy import copy as copy

ao = """[Script Info]
Title: 
ScriptType: v4.00+
WrapStyle: 0
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.601
PlayResX: 1280
PlayResY: 720
Aegisub Video Aspect Ratio: 0
Script Updated By: sa

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,黑体,38,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,3,0,2,10,10,10,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.00,0:00:00.00,Default,,0,0,0,,
"""



def writetxt(txt, content, mod="w"):
    opentxt = codecs.open(txt, mod, encoding="utf8")
    try:
        opentxt.write(content)
    except:
        print("哎呀 寫以下文件出錯了\n"+txt)
    finally:
        opentxt.close()


def timestamp2timestr(Timestamp):
    t0 = int(Timestamp)
    tms = t0 % 1000
    ts = t0 // 1000
    tm = ts // 60
    ts = ts % 60
    th = tm // 60
    tm = tm % 60
    tms = str(tms // 10).zfill(2)
    ts = str(ts).zfill(2)
    tm = str(tm).zfill(2)
    th = str(th).zfill(2)
    timestr = "%s:%s:%s.%s" % (th,tm,ts,tms)
    return timestr


def makeass(vtt):
    t = ET.ElementTree(file=vtt)
    root = t.getroot()
    ac = []
    acl = ["Dialogue: ", "0", "starttime", "endtime", "Default", "", "0", "0", "0", "", "text",]


    for line in root[0]:
        lt = line.attrib["t"]
        ld = line.attrib["d"]
        ls = line.text
        endtime = str(int(lt) + int(ld))
        starttime = timestamp2timestr(lt)
        endtime = timestamp2timestr(endtime)

        aclt = copy(acl)
        aclt[2] = starttime
        aclt[3] = endtime
        aclt[-1] = ls
        aclts = aclt[0] + ",".join(aclt[1:])
        ac.append(aclts)

    ass = ao + "\n".join(ac) + "\n"

    return ass


vttfile = r'D:\TEMP\T1.vtt'

def pause():
    print(u"要繼續就按回車哦")
    input("")


def check_input():
    if len(sys.argv)>1:
        l = sys.argv[1:]
        lp = []
        for i in l:
            if os.path.isfile(i):
                lp.append(i)
    else:
        return 0
    return lp

if __name__ == '__main__':
    l = check_input()
    #l = [vttfile]
    if l:
#        print(u"現在將會開始處理下面這些文件:\n")
#        for i in l:
#            print(i)
#            print("\n")
#        pause()
#       print("========================================")
        for i in l :
            ass = makeass(i)
            fn = os.path.splitext(i)[0] + ".ass"
            writetxt(fn,ass)

#    pause()









































