from json import dump
'''
Enumerate function: built-in enumerate function create a counter for each
ielement of an iterable and return a enumerate object. Enumerate function za return
kore ta <class 'enumerate'> theke ase.

enumerate(iterable, start=1) ==> enumerateObj return kore
list(enumerateObj) ==> [(counter, iterableItem),(counter, iterableItem)] / [tuple,tuple]
dict([tuple,tuple]) ==> {counter:'iterableItem', counter2:'iterableItem, ....}
'''
students=['MSA','PVS','MHD','ALD']
enumerate_obj=enumerate(students,start=1)
enumObjList=list(enumerate_obj)
# print(enumObjList) # [(1, 'MSA'), (2, 'PVS'), (3, 'MHD'), (4, 'ALD')]

# manually conver a enumerate obj into a dictionary
studentsObj={}
for singleTuple in enumObjList:
     studentsObj[singleTuple[0]]=singleTuple[1]
# print(studentsObj) # {1: 'MSA', 2: 'PVS', 3: 'MHD', 4: 'ALD'}

# convert into dict by dict function
subjects=['Python','Java','JavaScript']
enumObj=enumerate(subjects, start=1)
enumListTuple=list(enumObj)
# print(enumListTuple) # [(1, 'Python'), (2, 'Java'), (3, 'JavaScript')]
enumerateDict=dict(enumListTuple)
# print(enumerateDict) # {1: 'Python', 2: 'Java', 3: 'JavaScript'}

# enumerate dict convert into json
data=enumerateDict.copy()
fileObj=open('data.json','w')
dump(data,fileObj)
# json module er dump(dataObj, fileHandler) function kuno kichu return kore na.
