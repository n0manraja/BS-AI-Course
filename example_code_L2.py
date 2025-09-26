# Simple Rule-based Expert System Example (inspired by MYCIN)

symptom = input("Enter your symptom: ")

if symptom.lower() in ["fever", "high temperature"]:
    print("Possible infection – consult a doctor.")
elif symptom.lower() in ["headache", "migraine"]:
    print("Possible neurological issue – rest and check-up recommended.")
else:
    print("Symptom not recognized. Please consult a healthcare professional.")
