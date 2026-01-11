import csv
import uuid

def create_patient_resource(row):
    patient = {
        "resourceType": "Patient",
        "id": str(uuid.uuid4()),
        "gender": row["gender"],
        "birthDate": row["birth_date"]
    }
    return patient

with open("patients.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        patient_resource = create_patient_resource(row)
        print(patient_resource)
