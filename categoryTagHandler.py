from os.path import dirname,abspath,join
from os import listdir,remove,rename
workDir=dirname(abspath(__file__))

def readCategoryDict(categoryDictFile):
    dirContents=listdir(join(workDir))
    if categoryDictFile not in dirContents:
        file=open(join(workDir,categoryDictFile),'x')
        file.close()
    categoryDict=dict()
    with open(join(workDir,categoryDictFile),'r') as file:
        for row in file:
            tag,category=row.split(':')
            categoryDict[tag]=category.replace('\n','')
    return categoryDict

def appendTag(categoryDict,appendList=None):
    if appendList is None:
        while True:
            print('Input format is tag:category, then enter, write ->X to stop')
            inp=input()
            if inp=='->X':
                break
            inpList=inp.split(':')
            if len(inpList)==2:
                if inpList[0] in categoryDict.keys():
                    print('This tag already exists as '+inpList[0]+':'+categoryDict[inpList[0]])
                    print('Re-enter the association to keep')
                    inp=input()
                    if inp=='->X':
                        break
                    inpList=inp.split(':')
                
                categoryDict[inpList[0]]=inpList[1]
    else:
        existingTags=[]
        for tag,category in appendList:
            if tag in categoryDict.keys():
                existingTags.append(tag)
            else:
                categoryDict[tag]=category
        return existingTags

def saveCategoryDict(categoryDict,categoryDictFile):
    with open(join(workDir,categoryDictFile+'_temp'),'w') as file: #create a temporary file to write to first instead of overwriting existing file in case something goes wrong in the process
        for tag in categoryDict.keys():
            file.write(tag+':'+categoryDict[tag]+'\n')
    dirContents=listdir(workDir)
    if categoryDictFile in dirContents: #removing existing file and then renaming temporary file
        remove(join(workDir,categoryDictFile))
    rename(join(workDir,categoryDictFile+'_temp'),join(workDir,categoryDictFile))

# testDict=readCategoryDict('test')
# appendTag(testDict)
# # saveCategoryDict(testDict,'test')
# print(testDict)