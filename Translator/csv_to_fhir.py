"""
This script demonstrates the logical translation of legacy CSV data into FHIR resources.
In a production-grade migration, Patient and Observation resources would be grouped
inside a FHIR Transaction Bundle using UUID-based references to ensure atomic execution
and avoid orphaned clinical data.
"""
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
