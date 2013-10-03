
import mimify
mimify.unmimify("thismsg_enc.txt","thismsg_dec.txt",decode_base64=1)

fileh = open('thismsg_dec.txt','r')

msgContent =fileh.read()
msgContent = str.replace(msgContent,'<div','__div__<div')
msgPart = str.split(msgContent,'__div__',4) 

import APsummary
import APtext
import slugTools

summary = APsummary.getSummaryFields(msgPart[3])


# get the four-digit profile ID
profileId = slugTools.getProfile(summary['apcategory'],summary['dateline'])

# get elements for slug: date, trans ref, emailers' initials.
# also get a date formatted for the pubdate field.

staffHandle = slugTools.getStaffHandle(msgPart[0])
pubDate = slugTools.dateString()
slugDate = slugTools.slugDateString()
transNum = slugTools.firstToken(summary['filenametransref'])


# combine the slug elements to appear in the slug field.
# prepend the path and append '.xml' for the physical filename.
theSlug = 'WW' + slugDate + transNum + staffHandle
theFileName = 'workbin/' + theSlug + '.xml'
fileXML = open(theFileName,'w')


# Call the slug tools to separate the name and credit line. 
# Tool changes credit from AP style to ours.

author = slugTools.bylineName(summary['byline'])
staffLine = slugTools.bylineCredit(summary['byline'])
pubText = APtext.getStoryText(msgPart[2],summary['byline'],summary['dateline'])

# Now that full dateline has been used to isolate thestory text, we localize it.
# This really means taking out 'N.J.' for an in-state story.
summary['dateline']=slugTools.localize(summary['dateline'])

# testing to keep fake stories out of today's list
#pubDate = '12/01/11' # <<<<<<< remove when live
 
slugTools.openArticle(fileXML)

slugTools.wrapAndWrite('filename',theSlug,fileXML)
slugTools.wrapAndWrite('profileId',str(profileId),fileXML)
slugTools.wrapAndWrite('Gns','',fileXML)
slugTools.wrapAndWrite('keyword','topnews',fileXML)
slugTools.wrapAndWrite('pubdate',pubDate,fileXML)
slugTools.wrapAndWrite('pagenumber','',fileXML)
slugTools.wrapAndWrite('edition','',fileXML)
slugTools.wrapAndWrite('section','',fileXML)
slugTools.wrapAndWrite('headline',summary['headline'],fileXML)
slugTools.wrapAndWrite('dateline',summary['dateline'],fileXML)
slugTools.wrapAndWrite('byline_name',slugTools.bylineName(summary['byline']),fileXML)
slugTools.wrapAndWrite('byline_credit',slugTools.bylineCredit(summary['byline']),fileXML)

#slugTools.wrapAndWrite('body_text','This is dummy text.',fileXML)

APtext.printStoryText(pubText,fileXML)


slugTools.closeArticle(fileXML)


