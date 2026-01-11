# Data Flow

This document describes how data flows through the system.

1. Legacy patient data is stored in CSV files.
2. The translator script reads each CSV row.
3. Each row is converted into a FHIR Patient resource.
4. FHIR profiles validate mandatory fields.
5. Validated resources are stored in the HAPI FHIR server.

This flow ensures structured, validated, and interoperable healthcare data.
