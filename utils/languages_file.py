
#languages is a list of dictionaries that contain information about the languages that are being used in the project
#The dictionaries contain the following
#name: the name of the language
#language_code: the ISO code for the language
#name_column: the name of the column in the csv file that contains the name of the character
#char_column: the name of the column in the csv file that contains the character
#braille_column: the name of the column in the csv file that contains the braille code for the character
#replace: a list of strings that are to be removed from the name of the character
#language_information: a string that contains information about the language for Lib Louis
#contributors: a string that contains information about the people who have contributed to the project
languages=[
    {"name":"Akkadian","language_code":"akk","name_column":"Name","char_column":"Character(decimal)","braille_column":"Braille","replace":["CUNEIFORM SIGN"],"language_information":"""
#for more information on the Akkadian language, please go to:
#https://oracc.museum.upenn.edu/dcclt/signlists/signlists/
#The standard for Akkadian has been set by the academic community represented by ORACC. The braille code for Akkadian follows the standard set by ORACC. The braille code for Akkadian is represented in braille as the name for the sign in Akkadian. Thus, if the Akkadian sign is a "Lum," then the braille code for this sign would be lum.
""","contributors":"""
# Authors and Contributors to Braille Code:
# Maintained by Matityahu Yeshurun and Paul Geoghegan
"""},
    

{"name":"Amharic","language_code":"amh","name_column":"Name","char_column":"Char","braille_column":"Braille","replace":["CUNEIFORM SIGN"],"language_information":"""
#for more information on braille in the Amharic language, please read this paper.
#https://www.researchgate.net/publication/303773888_RECOGNITION_OF_AMHARIC_BRAILLE
#The standard for Amharic has been set by the community mentioned above. 
""","contributors":"""
# Maintained by Matityahu Yeshurun and Paul Geoghegan
"""},
        {"name":"Criticle-Apparatus-NT","language_code":"Criticle-Apparatus-NT","name_column":"Name","char_column":"Char","braille_column":"Braille","replace":["CUNEIFORM SIGN"],"language_information":"""
#for more information on the Criticle Apparatus , please check out this link:
#https://biblequestions.info/2020/10/24/what-do-the-sigla-in-a-new-testament-apparatus-mean-ubs-edition/
#The standard for the Criticle Apparatus has been set by the community mentioned above. 
""","contributors":"""
# Maintained by Matityahu Yeshurun and Paul Geoghegan
"""},
        {"name":"Greek","language_code":"grc-koine","name_column":"Name","char_column":"Character","braille_column":"Braille","replace":["CUNEIFORM SIGN"],"language_information":"""
#for more information on the Koine Greek language, please go to:
#https://www.koinegreek.com/
#The standard for Koine Greek has been set by the academic community . The braille code for Koine Greek follows the standard set.
""","contributors":"""
# Maintained by Matityahu Yeshurun and Paul Geoghegan
"""},
        {"name":"Hebrew","language_code":"heb","name_column":"Name","char_column":"Character","braille_column":"Braille","replace":["point","punctuation","mark","letter","accent","*"],"language_information":"""
# This table represents Classical or Biblical Hebrew. This table is different from a modern Hebrew table because this table provides support for the points, vowels, cantillation marks, and for the criticle apparatus for the BHS.This table only departs from the above mentioned standards, when an innovative braille code is required to represent symbols in the Criticle apparatus and cantillation marks, that have never had braille assigned to them before. Modern Hebrew tables do not provide this support. for more information on how the standard for  Biblical Hebrew was developed, please see to the following links::
#https://en.wikipedia.org/wiki/Hebrew_Braille#:~:text=The%20International%20Hebrew%20Braille%20Code
#also see: 
#https://huc.edu/library_blog/learning-about-hebrew-braille/#:~:text=The%20Code%20created%20by%20Brevis,books%20written%20in%20Hebrew%20Braille.
""","contributors":"""
# Maintained by Matityahu Yeshurun and Paul Geoghegan
"""},
{"name":"Syriac","language_code":"syc","name_column":"Name","char_column":"Character","braille_column":"Braille","replace":[],"language_information":"""
#This table provides support for ʾEsṭrangēlā, Maḏnḥāyā and Serṭā Syriac also known as  Old, Eastern and Western Syriac. 
#For more information, please see: 
#https://en.wikipedia.org/wiki/Syriac_language
""","contributors":"""
#This braille code was developed by: Sarah LaRose,Ray McAllester, and Matthew Yeater .
#Maintained by Paul Geoghegan and Matityhau Yeshurun
"""},
{"name":"Sumero-Akkadian","language_code":"akk-sumero","name_column":"Borger Translitteration","char_column":"Character","braille_column":"Braille","replace":["CUNEIFORM SIGN"],"language_information":"""
#for more information on the Akkadian language, please go to:
#https://oracc.museum.upenn.edu/dcclt/signlists/signlists/
#The standard for Akkadian has been set by the academic community represented by ORACC. The braille code for Akkadian follows the standard set by ORACC. The braille code for Akkadian is represented in braille as the name for the sign in Akkadian. Thus, if the Akkadian sign is a "Lum," then the braille code for this sign would be lum.
""","contributors":"""
# Maintained by Matityahu Yeshurun and Paul Geoghegan
"""},    \
        {"name":"Cuneiform-Transliteration","language_code":"Cuneiform-transliteration","name_column":"Name","char_column":"Character","braille_column":"Braille","replace":[],"language_information":"""
#This transliteration table provides support for the transliteration of all Cuneiform languages. For more information on the Transliteration table, please go to:
#http://oracc.ub.uni-muenchen.de/doc/help/languages/ugaritic/index.html
#The standard for Transliteration has been set by the academic community represented by ORACC. The braille code for transliteration follows the standard set by ORACC. The braille code for transliteration is represented in braille as the name for the sign in the transliteration table. Thus, if the sign is a "a," then the braille code for this sign would be a.
""","contributors":"""
# Maintained by Matityahu Yeshurun and Paul Geoghegan
"""},
        {"name":"Ugaritic","language_code":"uga","name_column":"Name","char_column":"Character(decimal)","braille_column":"Braille","replace":["UGARITIC LETTER","UGARITIC "],"language_information":"""
#for more information on the Ugaritic language, please go to:
#https://oracc.museum.upenn.edu/aemw/ugarit/corpus
#The standard for Ugaritic has been set by the academic community represented by ORACC. The braille code for Ugaritic follows the standard set by ORACC. The braille code for Ugaritic is represented in braille as the name for the sign in Ugaritic. Thus, if the Ugaritic sign is a "Alepha," then the braille code for this sign would be a.
""","contributors":"""
# Maintained by Matityahu Yeshurun and Paul Geoghegan
"""}
    ]
