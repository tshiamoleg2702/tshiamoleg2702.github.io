# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 20:01:07 2026

@author: tshiamo
"""
#FOL rules translated to python
knowledge_base= {"flu": ["fever","cough","sore_throat"], 
                 "common_cold": ["sneezing", "runny_nose","mild_fever"],
                 "malaria": ["fever","chills", "sweating","headache"],
                 "covid19": ["fever","cough", "shortness_of_breath", "loss_of_taste"],
                 "strep_throat": ["sore_throat", "swollen_lymph_nodes","fever"]}
#Advice base
advice_base = {"flu": ["Rest","Drink lots of fluids to stay hydrated","Take medications ibuprofen"],
               "common_cold": ["Rest", "Drink lots of fluids to stay hydrated", "Take medications such as ibuprofen"],
               "malaria": ["Seek medical help urgently","Drink lost of fluids to stay hydrated", "Take prescribed medications such as Chloroquine"],
               "covid19": ["Quarantine immediatley to avoid spreading","Seek medical help if symptoms become severe", "Take antiviral medications like Paxlovid"],
               "strep_throat": ["Seek medical help urgently", "Take prescribed antibiotics","Drink lots of fluids to stay hydrated"] }

#Chatbot function
def diagnosis(symptoms):
    #For flu
    if("fever" in symptoms and "cough" in symptoms and "sore_throat" in symptoms):
        return "flu"
    
    #For common cold 
    elif("sneezing" in symptoms and "runny_nose" in symptoms and "mild_fever" in symptoms):
        return "common_cold"
    #For malaria
    elif("fever" in symptoms and "chills" in symptoms and "sweating" in symptoms):
        return "malaria"
    #for covid19
    elif("fever" in symptoms and "cough" in symptoms and "shortness_of_breath" in symptoms and "loss_of_taste" in symptoms and "headache"):
        return "covid19"
    elif("sore_throat" in symptoms and "swollen_lymph_nodes" in symptoms and "fever" in symptoms):
        return "strep_throat"
    else: return None
    
#input
print("Welcome to the HealthBot!")
print("Please enter your symptoms(comma-separated):")
input = input()
symptoms = input

#calling diagnosis function
disease = diagnosis(symptoms)

#ouput
if disease:
    print("-", disease)
    print("Advice:")
    for advice in advice_base[disease]:
        print(advice)

   
