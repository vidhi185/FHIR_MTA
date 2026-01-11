# Source to Target Mapping (STM)

This document describes how legacy CSV data fields are mapped to FHIR resources.

## Patient Mapping

| Source (CSV Column) | Target (FHIR Field) |
|--------------------|---------------------|
| patient_id         | Patient.id          |
| gender             | Patient.gender      |
| birth_date         | Patient.birthDate   |

This mapping ensures that legacy tabular data is converted into structured and semantically valid FHIR resources.
