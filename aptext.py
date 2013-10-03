def getStoryText(textPart, byline, dateline):
    print 'getStoryText  called'
    import re
    
    pubText = textPart
    dashChars=dashRegex(textPart)

    pubText = re.sub(r'\050AP\051 *.',r'_AAB_',pubText)
    pubText = re.sub(r'_AAB_..',r'_AABP_',pubText)
    pubText = re.sub(r'<p>.*_AABP_',r'<p>',pubText)
    pubText = re.sub(r'<p>.*_AAB_',r'<p>',pubText)    
    pubText = re.sub(r'(?ms)</div>.*',r'',pubText)
    pubText = re.sub(r'(?ms)<p>',r'_L_body_text_R_',pubText)
    pubText = re.sub(r'(?ms)</p>',r'_L_/body_text_R_',pubText)
    pubText = re.sub(r'(?ms)<.{1,20}>',r'',pubText)
    pubText = re.sub(r'(?msi)<A HREF\075\042.*?\042>',r'',pubText)    
    pubText = re.sub(r'(?ms)_L_',r'<',pubText)
    pubText = re.sub(r'(?ms)_R_',r'>',pubText)
    #pubText = re.sub(r'(?ms).\304.',r'--',pubText)    
    #pubText = re.sub(r'(?ms)..\356.',r'--',pubText)
    pubText = re.sub(dashChars,r'--',pubText)
      
    pubText = re.sub(r'(?ms)</body_text>',r'</body_text>\n',pubText)    
    
    return pubText     

def printStoryText(theText,fileHandle):
    print >> fileHandle, theText 

def dashRegex(textPart):
    import re
    dashText = re.sub(r'(?ms).*?\050AP\051\040(.*?)\040.*',r'\1',textPart)
    if dashText == textPart:
        return re.compile('--')
        # return ''
    
    dashRegex = re.compile(dashText)
    return dashRegex
