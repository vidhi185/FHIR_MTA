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
Docker was used to deploy the HAPI FHIR server in a containerized environment, mitigating dependency hell caused by differences in underlying system configurations ("metal"). This ensured a consistent and reproducible runtime across student machines. Port mapping bridged the container port to the host machine, enabling local access to the FHIR warehouse.

### Semantic Integrity
Legacy systems frequently store ambiguous "magic strings" such as M/F for gender. To preserve semantic correctness, a ConceptMap was authored to translate legacy codes into FHIR-compliant values using the $translate operation. This guarantees standardized, interoperable representations inside the warehouse.

### Transactional Atomicity
During migration, Patient and Observation resources must be created together to prevent orphaned clinical data. This architecture leverages FHIR Transaction Bundles and UUID-based reference resolution, allowing multiple interdependent resources to be committed atomically in a single operation.


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
