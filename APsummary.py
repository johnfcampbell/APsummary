def getSummaryFields(summaryString):
    #
    # input string includes an HTML table.
    # excess text before the table is stripped off.
    #
    # return a hash:
    #   key value is the first column of the table
    #   value associated with the key is from the second column.

    import re
        
    summaryLine = summaryString.split('<tr>')   # each table row is a line
    #print summaryLine[3]
    spaghetti=summaryLine.pop(0)                # don't want text above first table row
    #print summaryLine[3]
    summaryHash = {}                            # establish table as a dictionary
    
    #print "\nsum keys: ";    
    
    for sumEntry in summaryLine:                # put the whole line in both sumKey and sumEntry...
        sumKey = sumEntry                       # ...we'll strip off excess using replace.
        sumKey=sumKey.lower()                          # simplify by making case consistent.
        sumValue = sumEntry
        
        sumKey = re.sub(r'(?ms)</td>.*',r'',sumKey)
        sumKey = re.sub(r'(?ms)\:|\(|\)|\'|\s*',r'',sumKey)     
        sumKey = re.sub(r'(?ms)<td>',r'',sumKey)     

        sumValue = re.sub(r'(?ms).*?<td>',r'',sumValue)
        sumValue = re.sub(r'(?ms)<td>.*',r'',sumValue)
        sumValue = re.sub(r'(?ms)(.*?)<.*',r'\1',sumValue)
        sumValue = re.sub(r'(?ms)(.*?)\n.*',r'\1',sumValue) 
        
        #print sumKey, sumValue
        summaryHash[sumKey]=sumValue
        
    return summaryHash


