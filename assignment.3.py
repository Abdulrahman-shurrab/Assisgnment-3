import csv

class Physician: #class for Physician.
    _slots=["id","name","_specialty"] #slots for Physician.
    def init(self,id1,name,specialty): #constructor for Physician.
        self.__id=id1
        self.__name=name
        self.__specialty=specialty
        def set_id(self,id1): #accessors and mutators for all fields.
            self.__id=id1
            def get_id(self):
                return self.__id
                def set_name(self,name):
                    self.__name=name
                    def get_name(self):
                        return self.__name
                        def set_specialty(self,specialty):
                            self.__specialty=specialty
                            def get_specialty(self):
                                return self.__specialty
                                def str(self): #str for Physician.
                                    return f'Physician with id {self._id} name is {self.name} and he is specialist in {self._specialty}'
def repr(self): #repr for Physician.
    return f'Physician(id={self._id},name={self.name},specialty={self._specialty})'
    class Patient: #class for Patient.
        _slots=["emr_id","name","gender","_phone_number"] #slots for Patient.
        def init(self,emr_id,name,gender,number): #constructor for patient.
            self.__emr_id=emr_id
            self.__name=name
            self.__gender=gender
            self.__phone_number=number
            def set_emr_id(self,emr_id): #accessors and mutators for all fields.
                self.__emr_id=emr_id
                def get_emr_id(self):
                    return self.__emr_id
                    def set_name(self,name):
                        self.__name=name
                        def get_name(self):
                            return self.__name
                        def set_gender(self,gender):
                            self.__gender=gender
                            def get_gender(self):
                                return self.__gender
                                def set_phone_number(self,number):
                                    self.__phone_number=number
                                    def get_phone_number(self):
                                        return self.__phone_number
                                        def str(self):
                                            return f'Patient with id {self._emr_id} name is {self.name} whose gender is {self.gender} and phone is {self._phone_number}'
def repr(self):
    return f'Patient(id={self._emr_id},name={self.name},gender={self.gender},phone_number={self._phone_number}'

class Encounter: #class for Encounter.
    def init(self,physician,patient,date,disease,medication): #constructor for Encounter.
        self.physician=physician
        self.patient=patient
        self.date=date
        self.disease=disease
        self.medication=medication
def repr(self):
    return f'Encounter(Physician={self.physician},Patient={self.patient},Date={self.date},Disease={self.disease},Medication={self.medication}'
  
one_objs=[] #list to store the objects of Physician.
with open('1.csv','r') as f:
    for row in f:
        par= row.strip().split(",")
        one_objs.append(Physician(par[0],par[1],par[2])) #for every row in 1.csv create an object for Physician and append it to one_objs list.
  
two_objs=[] #list to store the objects of Patient.
with open('2.csv','r') as f:
    for row in f:
        par= row.strip().split(",")
        two_objs.append((par[0],par[1],par[2],par[3])) #for every row in 1.csv create an object for Physician and append it to one_objs list.
  
thrid_objs=[] #list to store the objects for Encounter.
thrid_objs.append(Encounter(1,3,'17-5-2021','AB','M1')) #creating 5 objects for Encounter.
thrid_objs.append(Encounter(1,1,'29-6-2021','ABC','M2'))
thrid_objs.append(Encounter(4,3,'8-9-2021','ABD','M3'))
thrid_objs.append(Encounter(8,2,'1-2-2021','ABE','M4'))
thrid_objs.append(Encounter(9,2,'7-8-2021','AE','M5'))

for i in one_objs: #printing the objects of all classes.
    print(str(i))
for i in two_objs:
    print(str(i))
for i in thrid_objs:print(repr(i))
with open('encounter.csv', 'w') as f: #writing the encounters into a file.
# create the csv writer.
  writer = csv.writer(f)
  for item in thrid_objs:
      writer.writerow([item.patient,item.physician,item.date,item.disease,item.medication])