def getProfile(category,dateline):
    # print 'getProfile called'
    import re
    
    category = re.sub(r'\n|\r','',category)
    
    profileNum = 1001
    profileRaw= 1001
    filec = open('wireweb.cfg','r')
    
    cfgContent = filec.read()
    
    if cfgContent :

         if re.search('DEFAULT_PROFILE',cfgContent) :
             profileRaw=re.sub(r'(?ms).*?DEFAULT_PROFILE=(\d\d\d\d).*',r'\1',cfgContent)
             cfgContent = filec.read()
    
    profileTable = { 'f' : 1003, 'a' : 1012, 'w' : 1012, 'e' : 1041, 'i':1012, 'l' : 1004, 'n' : 1012, 'p' :1012, 's' : 1002 }

    if category in profileTable:
        #print 'got category'
        profileRaw = profileTable[category]
        
    if re.search(', N.J.',dateline):
        if profileRaw == 1012:
            profileRaw = 1007
                          
    return profileRaw

def getStaffHandle(mailHeader):
    import re
    import string
    
    mailHeader = re.sub(r'(?ms)Return.path..<(.*?)>.*',r'\1',mailHeader)
    mailHeader = re.sub(r'joc',r'jc',mailHeader)
    mailHeader = re.sub(r'(..).*',r'\1',mailHeader)
    
    return string.upper(mailHeader)

def dateString():
    import time
    theString = time.strftime("%m/%d/%y")
    #print "theString "
    #print theString
    return theString    
    
def slugDateString():
    import time
    theString = time.strftime("%m%d")
    #print "theString"
    #print theString
    return theString

def tomorrowString():
    import datetime
    #import timedelta
    tomTime = datetime.datetime.now()
    #print "now = " +  tomTime.strftime("%m%d")
    tomTime = tomTime + datetime.timedelta(hours=12)
    theString = tomTime.strftime("%m/%d/%y")
    return theString

def slugTomorrowString():
    import datetime
    #import timedelta
    tomTime = datetime.datetime.now()
    #print "now = " +  tomTime.strftime("%m%d")
    tomTime = tomTime + datetime.timedelta(hours=12)
    theString = tomTime.strftime("%m%d")
    return theString
    
def firstToken(transRefLine):
    import re
    import string
    
    transRefLine = string.upper(transRefLine)
    transRefLine = re.sub(r'(?ms)([A-Z][0-9]{4,4}).*',r'\1',transRefLine)
    return string.upper(transRefLine)

def localize(dateline):
    import re
    import string
    print "1.localize "
    print dateline
    dateline = re.sub(r'(?ms)(.*), N.J.',r'\1',dateline)
    print "2.localize"
    print dateline
    return dateline


# AP byline is all in  one field. 
# We break it up into name and staffline.
# Also, add the word BY.

def bylineName(bylineFull):
    import re
    print "1.bylineFull"
    print bylineFull
    bylineWork = re.sub(r'(.*?)AP .* Writer',r'\1',bylineFull)
    bylineWork = re.sub(r'(.*?)Associated.*',r'\1',bylineWork)
    bylineWork = re.sub(r'(.*)\,',r'\1',bylineWork)
    print "2.bylinework"
    print bylineWork
    bylineWork = re.sub(r'(^.?)',r'By \1',bylineWork)
    bylineWork = re.sub(r'By $',r'',bylineWork)    
    #bylineWork = 'By ' + bylineWork
    print "3.bylinework"
    print bylineWork
    return bylineWork

def bylineCredit(bylineFull):
    import re
    bylineWork = re.sub(r'.*AP .*Writer',r'Associated Press',bylineFull)
    bylineWork = re.sub(r'.*Associated.*',r'Associated Press',bylineWork)
    bylineWork = re.sub(r'.*USA.*?',r'USA TODAY',bylineWork)
    return bylineWork
      
# these routines write out the xml.
# openarticle and closearticle put out the boilerplate beginning andending.
# wrapAndWrite takes a tag name and wraps the content in opening and closing tags,
# writing the results to the XML file.

def openArticle(fileHandle):

    print >> fileHandle, '<?xml version="1.0"?>'
    print >> fileHandle, '<article>'
    return

def closeArticle(fileHandle):
    print >> fileHandle, '</article>'
    fileHandle.close()
    return
    
def wrapAndWrite( tag, content, fileHandle):
    import re

    content = re.sub(r'(?ms)\n|\r',r'',content)
    theLine = '<' + tag + '>' + ""
    if content:
        theLine = theLine + content + ""
    theLine = theLine + '</' + tag + '>'
    
    #print theLine
    print >> fileHandle, theLine 
