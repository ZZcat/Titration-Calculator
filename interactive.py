import math, pickle, sys, re

def choose_a_solutionBase():#Chooses a basic solution
    solution=input('\nWhat is your basic solution of the weak bases provided?').lower()
    if solution == 'ammonia' or 'nh3':
        Kb=1.8*(10**-5)
    elif solution =='aniline' or 'c6h5nh2':
        Kb=4.3*(10**-10)
    elif solution ==' dimethylene' or '(ch3)2nh':
        Kb=5.4*(10**-4)
    elif solution == 'ethylamine' or 'c2h5nh2':
        Kb=6.4*(10**-4)
    elif solution == 'hydrazine' or 'h2nnh2':
        Kb=1.3*(10**-6)
    elif solution == 'hydroxylmine' or 'honh2':
        Kb=1.18*(10**-8)
    elif solution == 'methylamine' or 'ch3nh2':
        Kb=4.4*(10**-4)
    elif solution == 'pyrridine' or 'c5h5n':
        Kb=1.7*(10**-9)
    elif solution == 'trimethylamine' or '(ch3)3n':
        Kb=6.4*(10**-5)
    return Kb                                            #choose_a_solutionBase() and choose_a_titrantBase() are practically the same but are needed for separate uses

def choose_a_titrantBase(Ka_1):#Chooses a basic titrant
    weakBases=['ammonia','aniline','dimethylene','ethylamine','hydrazine','hydroxylmine','methylamine','pyrridine','trimethylamine']
    titrant=input('\nWhat is your titrant?').lower()
    if titrant not in weakBases:
        Kb=((1.0*(10**-14))/Ka_1)
    elif titrant=='ammonia' or 'nh3':
        Kb=(1.8*(10**-5))
    elif titrant == 'aniline' or 'c6h5nh2':
        Kb=4.3*(10**-10)
    elif titrant == 'dimethylene' or '(ch3)2nh':
        Kb=5.4*(10**-4)
    elif titrant == 'ethylamine' or 'c2h5nh2':
        Kb=6.4*(10**-4)
    elif titrant == 'hydrazine' or 'h2nnh2':
        Kb=1.3*(10**-6)
    elif titrant == 'hydroxylmine' or 'honh2':
        Kb=1.18*(10**-8)
    elif titrant == 'methylamine' or 'ch3nh2':
        Kb=4.4*(10**-4)
    elif titrant == 'pyrridine' or 'c5h5n':
        Kb=1.7*(10**-9)
    elif titrant == 'trimethylamine' or '(ch3)3n':
        Kb=6.4*(10**-5)
    return Kb

def find_pH_before_titrationAcid(Ka_1,x_1):#Finds pH of the acid before titration starts
    x_2 = (Ka_1*x_1)
    x = math.sqrt(x_2)
    pH = -math.log10(x)
    return pH

def find_pH_before_titrationBase(Kb_1,x_1):#Finds pH of the base before titration starts
    x_2 = Kb_1*x_1
    x = math.sqrt(x2)
    pOH = -math.log10(x)
    pH = 14-pOH
    return pH

def find_vol_at_equivalence_ptBase(x_1,y_1,z_1):#Finds volume of base required to titrate an acid to the equivalence point
    molAequiv = ((y_1*x_1)/1000)
    volBequiv = (molAequiv*(1000/z_1))
    print('\nThe volume of base required to titrate the acid to the equivalence point is',volBequiv)
    total_volume = volBequiv+y_1
    print('\nThe total volume is',total_volume)
    return total_volume

def find_vol_at_equivalence_ptAcid(x_1,y_1,z_1):#Finds volume of acid required to titrate a base to the equivalence point
    molBequiv = ((y_1*x_1)/1000)
    volAequiv = (molBequiv*(1000/molarityAcid))
    print('\nThe volume of the acid required to titrate the base to the equivalence point is',volAequiv)
    total_volume = volAequiv+y_1
    print('\nThe total volume is',total_volume,'mL or',(total_volume/1000),'L')
    return total_volume
    
def find_pH_before_equivalence_ptAcid(x_1,Ka_1,y_1):#Finds the pH before the equivalence point and after the titration has begun if the titrant is an acid
    volB_before_equivalence=input('What is the volume of base used?')
    molB_before_equivalence=((volB_before_titration*molarity)/1000)
    molA_before_equivalence=((x_1*y_2)/1000)
    molarityA=molA_before_equivalence/((volB_before_equivalence+y)/1000)
    molarityB=molB_before_equivalence/((volB_before_equivalence+y)/1000)
    pH=-math.log(Ka)+log(molarityB/molarityA)
    return molarityA,molarityB,pH

def find_pH_before_equivalence_ptBase(x_1,Ka_1,y_1,):#Finds the pH before the equivalence point and after the titration has begun if the titrant is an Base
    volA_before_equivalence=float(input('What is the volume of acid '))
    molA_before_equivalence = ((volA_before_titration*molarity)/1000)
    molB_before_equivalence = ((x_1*y_1)/1000)
    molarityA = molA_before_equivalence/((volB_before_equivalence+y)/1000)
    molarityB = molB_before_equivalence/((volB_before_equivalence+y)/1000)
    pH = -math.log(Ka)+log(molarityB/molarityA)
    return molarityA,molarityB,pH

def find_pH_after_equivalence_ptAcid(a_1,b_1,x_1):#Finds the pH after the equivalence point and before the titration has ended if the titrant is a base
    volB_after_equivalence = input('What is the volume of the base used?')
    molB_after_equivalence = ((volB_after_equivalence*z)/1000)
    molBase = x_1
    molarityBase = (x_1/((volB_after_equivalence+y)/1000))
    pOH = -math.log10(molarityBase)
    pH = 14-pOH
    return pH
def chemicalSearch(chemical, dataset):
    chemical = chemical.replace(" ", "").replace("acid", "").replace("Acid", "")

    dataset_names = {}
    for i in range(0,len(dataset)):
        dataset_names[str(dataset[i][0]).lower()] = i
    if chemical.lower() in dataset_names:
        print("[IDENTIFIED] " + dataset[dataset_names[chemical.lower()]][0] + "(" + dataset[dataset_names[chemical.lower()]][1] + ")") # Occures twice in funcion
        return(dataset[dataset_names[chemical.lower()]][2])

    dataset_formulas = {}
    chemical_formula = []
    for i in re.findall(r'([A-Z][a-z]*)(\d*)',chemical):
        if i[1] == "":  chemical_formula.append([i[0], i[1].replace("", "1")])
        else:   chemical_formula.append([i[0], i[1]])
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
                print("[IDENTIFIED] " + dataset[dataset_names[chemical.lower()]][0] + "(" + dataset[dataset_names[chemical.lower()]][1] + ")") # Occures twice in funcion
                return(dataset[i][2])
    return(False)


   ########
   # Main #
   ########

if sys.version_info[0] == 3: # Check to see if user is using python3
    running = True
else:
    running = False
    print("You must use python3 to run this program.\nCurrent version information:"+str(sys.version))

if running:
    # Import data from csv files
    acidConstants = []
    for i in open("acidDissociationConstants.csv", "r").read().split("\n"):
        acidConstants.append(i.split(","))
    baseConstants = []
    for i in open("baseDissociationConstants.csv", "r").read().split("\n"):
        baseConstants.append(i.split(","))

    print('\nThis code is meant to go through the steps of doing a titration one at a time, at each point, a volume or a pH is calculated. It assumes the tempature of all solutions is 25 C.')
    print("\nSupported acids: " + str(list(zip(*acidConstants))[0]).replace("'", "").replace("[", "").replace("]", "").replace("(","").replace(")", "")) 
    print("\nSupported Bases: " + str(list(zip(*baseConstants))[0]).replace("'", "").replace("[", "").replace("]", "").replace("(","").replace(")", "")) 
    list_acid_base=[]
           
    choice = ""

    while not choice == '0':
        print('''
            0. Exit
            1. Determine Acid/Base
            2. Find the pH of the solution before titrant is added
            3. Find volume and pH at equivalence point
            4. Find pH before equivalence point
            5. Find pH after equivalence point
            6. Show Graph
            ''')
    
        choice = input('Enter your choice')
    
        print("")
    
        if choice=='0':
        
            print('Exiting ...')#If choice = 0, user is logged out
        
        elif choice=='1':#Determines whether the solution is an acid or base
            solution1='c'

            while solution1 not in ['a','b']:
                solution1=input("Please tell what the solution is acid or base-a or b?")
            
            list_acid_base.append(solution1)

            if list_acid_base[0]=='a':#Determines the initial values of the concentration and volume of the acid and titrant base
                # Get acid and find Ka1
                results = False
                while not results:
                    acidicSolution = input('\nWhat is your acidic solution?')
                    results = chemicalSearch(acidicSolution, acidConstants)
                    if not results:
                        print("Unable to identify chemical, try again.")
                Ka_1 = results
                x_1,y_1,z_1 = float(input('\nWhat is the concentration of the acid in mol/L or M?')), float(input('\nWhat is the volume of the acid in mL?')), float(input('\nWhat is the concentration of the titrant base in M?'))
                Kb_1=choose_a_titrantBase(Ka_1)
           
            elif list_acid_base[0]=='b':#Determines the initial values of the concentration and volume of the base and titrant acid
                Kb_1=choose_a_solutionBase()
                x_1,y_1,z_1 = float(input('\nWhat is the concentration of the Base in mol/L or M?')), float(input('\nWhat is the volume of the base in mL?')), float(input('\nWhat is the molarity of the titrant acid in M?'))
                results = False
                while not results:
                    acidicSolution = input('\nWhat is your titrant acid?')
                    results = chemicalSearch(acidicSolution, acidConstants)
                    if not results:
                        print("Unable to identify chemical, try again.")
                Ka_1 = results
        elif choice=='2':#Finds pH before the titration has begun

            if list_acid_base[0]=='a':
                pH=find_pH_before_titrationAcid(Ka_1,x_1)
                print(pH)

            elif list_acid_base[0]=='b':
                pH=find_pH_before_titrationBase(Kb_1,x_1)
                print(pH)
                  
        elif choice=='3':#Equivalence Point Calculations

            if list_acid_base[0]=='a':
                find_vol_at_equivalence_ptBase(x_1,y_1,z_1)
           
            elif list_acid_base[0]=='b':
                find_vol_at_equivalence_ptAcid(x_1,y_1,z_1)
           
        elif choice=='4':#Calculates the pH before the equivalence point and after the titration has started

            if list_acid_base[0]=='a':
                pH1=find_pH_before_equivalence_ptAcid(x_1,Ka_1,y_1)
                print(pH1)

            elif list_acid_base[0]=='b':
                pH1=find_pH_before_equivalence_ptBase(x_1,Kb_1,y_1)
                print(pH1)

        #elif choice=='5':#Calculates the pH after the equivalence point 
        
            
            
