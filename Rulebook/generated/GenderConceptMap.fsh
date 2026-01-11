Instance: GenderConceptMap
InstanceOf: ConceptMap
Description: "Maps legacy gender codes to FHIR administrative gender"

* sourceUri = "http://example.org/legacy-gender"
* targetUri = "http://hl7.org/fhir/administrative-gender"

* group[0].element[0].code = #M
* group[0].element[0].target[0].code = #male

* group[0].element[1].code = #F
* group[0].element[1].target[0].code = #female
