import re

dataset = [['Acetic', 'CH3CO2H', '1.75*10**5'], ['Arsenic', 'H3AsO4', '5.5*10**3'], ['Benzoic', 'C6H5CO2H', '6.25*10**5'], ['Boric', 'H3BO3', '5.4*10**10'], ['Bromoacetic', 'CH2BrCO2H', '1.3*10**3'], ['Carbonic', 'H2CO3', '4.5*10**7'], ['Chloroacetic', 'CH2ClCO2H', '1.3*10**3'], ['Chlorous', 'HClO2', '1.1*10**2'], ['Chromic', 'H2CrO4', '1.8*10**1'], ['Citric', 'C6H8O7', '7.4*10**4'], ['Cyanic', 'HCNO', '3.5*10**4'], ['Dichloroacetic', 'CHCl2CO2H', '4.5*10**2'], ['Fluoroacetic', 'CH2FCO2H', '2.6*10**3'], ['Formic', 'CH2O2', '1.8*10**4'], ['Hydrazoic', 'HN3', '2.5*10**5'], ['Hydrocyanic', 'HCN', '6.2*10**10'], ['Hydrofluoric', 'HF', '6.3*10**4'], ['Hydrogen selenide', 'H2Se', '1.3*10**4'], ['Hydrogen sulfide', 'H2S', '8.9*10**8'], ['Hydrogen telluride', 'H2Te', '2.5*10**3'], ['Hypobromous', 'HBrO', '2.8*10**9'], ['Hypochlorous', 'HClO', '4.0*10**8'], ['Hypoiodous', 'HIO', '3.2*10**11'], ['Iodic', 'HIO3', '1.7*10**1'], ['Iodoacetic', 'CH2ICO2H', '6.6*10**4'], ['Nitrous', 'HNO2', '5.6*10**4']]

def f():#if 1==1:

    dataset = [['Acetic', 'CH3CO2H', '1.75*10**5'], ['Arsenic', 'H3AsO4', '5.5*10**3'], ['Benzoic', 'C6H5CO2H', '6.25*10**5'], ['Boric', 'H3BO3', '5.4*10**10'], ['Bromoacetic', 'CH2BrCO2H', '1.3*10**3'], ['Carbonic', 'H2CO3', '4.5*10**7']]
    chemical = input(">")
    chemical = chemical.replace(" ", "").replace("acid", "").replace("Acid", "")

    dataset_names = {}
    for i in range(0,len(dataset)):
        dataset_names[str(dataset[i][0]).lower()] = i
    if chemical.lower() in dataset_names:
        return(dataset[dataset_names[chemical.lower()]][2])

    dataset_formulas = {}
    chemical_formula = []
    for i in re.findall(r'([A-Z][a-z]*)(\d*)',chemical):
        if i[1] == "":	chemical_formula.append([i[0], i[1].replace("", "1")])
        else:	chemical_formula.append([i[0], i[1]])
    for i in range(0,len(dataset)):
        dataset_formula = []
        dataset_chemical = re.findall(r'([A-Z][a-z]*)(\d*)', str(dataset[i][1]))
        for ii in dataset_chemical:
        	if ii[1] == "":  dataset_formula.append([ii[0], ii[1].replace("", "1")])
        	else:   dataset_formula.append([ii[0], ii[1]])
        dataset_formula_s = "" # String made so HOH is the same as H2O
        chemical_formula_s = ""
        for ii in dataset_formula:
            dataset_formula_s = dataset_formula_s + str(ii[0])*int(ii[1])
        for ii in chemical_formula:
            chemical_formula_s = chemical_formula_s + str(ii[0])*int(ii[1])
        if sorted(dataset_formula_s) == sorted(chemical_formula_s):
                return(dataset[i][2])
    return(False)
print(f())