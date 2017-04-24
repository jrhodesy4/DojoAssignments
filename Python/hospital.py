class Patient(object):
    def __init__(self, number, name, allergies, bed):
        self.id = number
        self.name = name
        self.allergies = allergies
        self.bed = bed

patient1 = Patient(1, 'Tim', 'nuts', 0)
patient2 = Patient(2, 'Bob', 'seeds', 0)
patient3 = Patient(3, 'Charles', 'grass', 0)
patient4 = Patient(4, 'Fred', 'flowers', 0)

class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity

    def Admit(self, patient):
        if len(self.patients) < self.capacity:
            self.patients.append(patient)
            patient.bed = self.patients.index(patient)+1
            print 'Id:', patient.id, 'Name:', patient.name, 'Allergies:', patient.allergies, 'Bed Number', patient.bed, 'Status:', 'Admitted'
        else:
            print 'Id:', patient.id, 'Name:', patient.name, 'Allergies:', patient.allergies, 'Status:', 'Hospital is full...'
        return self

    def Discharge(self, patient):
        self.patients.remove(self.patients[1])
        patient.bed = 'none'
        print 'Id:', patient.id, 'Name:', patient.name, 'Allergies:', patient.allergies, 'Bed Number', patient.bed,'Status:', 'Discharged'
        return self

hos = Hospital('SunnySide Hospital', 2)

print hos.Admit(patient1).Admit(patient2).Admit(patient3).Discharge(patient2)
