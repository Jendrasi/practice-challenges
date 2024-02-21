def toBool(value: str):
    if value.lower() in ["y", "yes", "1", "true"]:
        return True;
    return False;

patientName = input("What is the patient's full name?")
patientAge = int(input("What is the patient's age?"))
patientIsNew = toBool(input("Is this a new patient?"))
print("Patient Name:", patientName)
print("Patient Age:", patientAge)
print("New Patient?:", patientIsNew)