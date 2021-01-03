from spellchecker import SpellChecker
def removespecchar(test):
    """Function to Clean Up Strings.

    Specifically gets rid of quotes,tabs,new lines, and evens out the spaces."""
    import re
    if type(test) == str:
        test=re.sub('\t',' ',test)
        test=re.sub('\"',' ',test)
        test=re.sub('\n',' ',test)
        test=re.sub('\r',' ',test)
        test=re.sub(' +',' ',test)
    return(test)
def spellCheck(text):
    spell = SpellChecker()
    splitText=text.split()
    string1=""
    tempstring1=""
    tempstring2=""
    boolean=False
    for word1 in splitText:
        words=spell.candidates(word1)
        for word in words:
            if(word1!=word):
                tempstring1+=word1+" "
                boolean=True
            if(boolean):
                break
    tempstring2=tempstring1.split()
    for temp in tempstring2:
        string1+="\n"+"("+temp+"):"
        words=spell.candidates(temp)
        for word in words:
            string1+=word+" "
    return (string1)
def correctSpell(text):
    spell = SpellChecker()
    string2=""
    splitText=text.split()
    for word in splitText:
        newText = spell.correction(word)
        if(newText!=word):
            string2+="("+word+"):"+newText+"\n"
    return (string2)

