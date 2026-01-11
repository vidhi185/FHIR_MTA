# FHIR MTA Project – IIHMR Bangalore

## Overview
This project demonstrates an end-to-end healthcare data interoperability pipeline using FHIR standards. The objective is to show how legacy healthcare data can be translated, validated, and stored in a modern FHIR-based system.

The project is structured to reflect real-world healthcare IT architecture, focusing on infrastructure, semantic control, and data translation.

---

## Repository Structure

- **Infrastructure/**  
  Docker-based deployment of the HAPI FHIR server.

- **Rulebook/**  
  FHIR Shorthand (FSH) profiles defining mandatory clinical fields.

- **Translator/**  
  Python-based scripts to convert legacy CSV data into FHIR resources.

- **Documentation/**  
  Architecture, data flow, source-to-target mapping, and conclusions.

---

## Architect’s Narrative

### The Container Advantage
Docker is used to deploy the HAPI FHIR server in a consistent and reproducible environment. This eliminates dependency conflicts and allows rapid setup of a validated FHIR data store.

### Semantic Integrity
FHIR profiles created using FHIR Shorthand act as a rulebook to enforce mandatory clinical fields. This prevents incomplete or unsafe data from entering the system and replaces ambiguous legacy representations.

### Transactional Atomicity
Legacy data translation is designed with the concept of atomic operations in mind. By grouping related resources into transactions (conceptually), the system avoids orphaned or inconsistent healthcare data.

---

## Documentation
Detailed documentation is available in the `Documentation/` folder, including:
- Source to Target Mapping
- System Architecture
- Data Flow
- Project Conclusion

---

## Learning Outcome
This project helped transition my thinking from basic data modelling to designing interoperable healthcare systems using industry-aligned standards and architectural principles.
