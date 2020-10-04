from googletrans import Translator

translator = Translator(service_urls=['translate.google.com' ])

print("Started...")

# function to read strings from en.js file to convert to other language
def Translation(filename, toConvertintoLang, fromConvertLang):
    data=[]
    with open(filename,'r') as reader:
        for line in reader.readlines():                      # reading lines
            if (line.find(":") != -1):                        #  lines containing strings
                if (line.find(",")):                            # removing commas from lines
                    line = line.replace(",", "")
                    line = line.split(':')                      # splitting on the basis of semi-colon
                    keyName=line[0].strip()                     # keyname 
                    stringValue = line[1].strip().replace("\"","")    # value
                    translations = translator.translate(stringValue,toConvertintoLang,src=fromConvertLang)
                    print(translations.text)
                    print("\n\n")
                    data.append({keyName: translations.text})     # appending to data array
    return data         # returning the data array



# For writing the translated strings into the ur.js file 

def WritingTranslationToOtherFile(filename):
    with open(filename,'w+') as file:        # creates file
        file.write("export default {\n")
        for data in result:
            key=list(data.keys())
            value=list(data.values())
            file.write(str(key[0]+" : \""+ value[0]+"\",\n"))   # writing lines
        file.write("}")
    return "Completed... check "+filename+" file."




result = Translation("en.js", "ur","en")                     
print(WritingTranslationToOtherFile("ur.js"))
                