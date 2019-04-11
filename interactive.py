#Titration Calculator
print('\nThis code is meant to go through the steps of doing a titration one at a time, at each point, a volume or a pH is calculated')

print('\nThe weak bases are, Ammonia, Aniline, Dimethylene, Ethylamine, Hydrazine, Hydroxylmine, Methylamine, Pyrridine, Trimethylamine')

print('''\nThe weak acids are Acetic Acid, Arsenic Acid, Arsenous Acid, Ascorbic Acid, Benzoic Acid, Boric Acid, Butanoic Acid, Carbonic Acid, Chloroacetic Acid, Chlorous Acid, Citric Acid, Cyanic Acid, Formic, Hydrazoic Acid, Hydrocyanic Acid, Hydrofluoric Acid, Hydrogen Chromate Ion Acid, Hydrogen peroxide
Hydrogen selenate ion Acid, Hydrosulfuric Acid, Hypobromous Acid, Hypoiodous Acid, Iodic Acid, Lactic Acid, Malonic Acid, Nitrous Acid, Oxalic Acid, Paraperiodic Acid, Phenol, Phosphoric Acid, Propionic Acid, Pyrophosphoric Acid, Selenous Acid, Sulfurous Acid, Tartaric Acid''')

import math

import pickle

'''def acid_or_base(question):#Determines whether the solution being titrated is an acid or a base
    response=None
    while response not in ('a','b'):
        resonse=input(question)
    return response'''

def molarity_mL_Acid():#Determines the initial concentrations and volumes of the Acidic solution and the base titrant
    x=float(input('\nWhat is the concentration of the acid in mol/L or M?'))
    y=float(input('\nWhat is the volume of the acid in mL?'))
    z=float(input('\nWhat is the concentration of the titrant base in M?'))
    return x,y,z

def molarity_mL_Base():#Determines the initial concentrations and volumes of the Basic solution and the acid titrant
    x=float(input('\nWhat is the concentration of the Base in mol/L or M?'))
    y=float(input('\nWhat is the volume of the base in mL?'))
    z=float(input('\nWhat is the molarity of the titrant acid in M?'))
    return x,y,z

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

def choose_a_solutionAcid():#Chooses an acidic solution
    solution=input('\nWhat is your acidc solution?').lower()    
    if solution == 'acetic acid' or 'ch3cooh' or 'hc2h3o2':
        Ka=(1.8*(10**-5))
    elif solution == 'Arsenic Acid' or 'H3AsO4':
        Ka=5.6*(10**-3)
    elif solution == 'Arsenous Acid' or 'H3AsO3':
        Ka=5.1*(10**-10)
    elif solution == 'Ascorbic Acid' or 'H2C6H6O6':
        Ka=8*(10**-5)
    elif solution == 'Benzoic Acid' or 'C6H7COOH' or 'HC7H5O2':
        Ka=1.5*(10**-5)
    elif solution == 'Carbonic Acid' or 'H2CO3':
        Ka=4.3*(10**-7)
    elif solution == 'Chloracetic Acid' or 'CH2ClCOOH' or 'HC2H2O2Cl':
        Ka=1.4*(10-3)
    elif solution == 'Chlorous Acid' or 'HClO2':
        Ka=1.1*(10**-2)
    elif solution == 'Citric Acid' or 'HOOCC(OH)(CH2COOH)2' or 'H3C6H5O7':
        Ka=7.4*(10**-4)
    elif solution == 'Cyanic Acid' or 'HCNO':
        Ka=3.5*(10**-4)
    elif solution == 'Formic Acid' or 'HCOOH' or 'HCHO2':
        Ka=1.8*(10**-4)
    elif solution == 'Hydroazoic Acid' or 'HN3':
        Ka=1.9*(10**-5)
    elif solution == 'Hydrocyanic Acid' or 'HCN':
        Ka=4.9*(10**-10)
    elif solution == 'Hydrofluoric Acid' or 'HF':
        Ka=6.8*(10**-4)
    elif solution == 'Hydrogen Chromate Ion' or 'HCrO4-':
        Ka=3.0*(10**-7)
    elif solution == 'Hydrogen Peroxide' or 'H2O2':
        Ka=2.4*(10**-12)
    elif titrant == 'Hydrogen Selenate Ion' or 'HSeO4-':
        Ka=2.2*(10**-2)
    elif solution == 'Hydrosulfuric Acid' or 'H2S':
        Ka=9.5*(10**-8)
    elif solution == 'Hypobromous Acid' or 'HBrO':
        Ka=2.5*(10**-9)
    elif solution == 'Hypochlorous Acid' or 'HClO':
        Ka=3.0*(10**-8)
    elif solution == 'Hypoiodous Acid' or 'HIO':
        Ka=2.3*(10**-11)
    elif solution == 'Iodic Acid' or 'HIO3':
        Ka=1.7*(10**-1)
    elif solution == 'Lactic Acid' or 'CH3CH(OH)COOH' or 'HC3H5O3':
        Ka==1.4*(10**-4)
    elif solution == 'Malonic Acid' or 'CH2(COOH)2' or 'H2C3H2O4':
        Ka=1.5*(10**-3)
    elif solution == 'Nitrous Acid' or 'HNO2':
        Ka=4.5*(10**-4)
    elif solution == 'Oxalic Acid' or '(COOH)2' or 'H2C2O4':
        Ka=5.9*(10**-2)
    elif solution == 'Paraperiodic Acid' or 'H5IO6':
        Ka=2.8*(10**-2)
    elif solution == 'Phenol' or 'C6H5OH' or 'HC6H5O':
        Ka=1.3*(10**-13)
    elif solution == 'Phosphoric Acid' or 'H3PO4':
        Ka=7.5*(10**-3)
    elif solution == 'Propionic Acid' or 'C2H5COOH' or 'HC3H5O2':
        Ka=1.3*(10**-5)
    elif solution == 'Pyrophosphoric Acid' or 'H4P2O7':
        Ka=3.0*(10**-2)
    elif solution == 'Selenous Acid' or 'H2SeO3':
        Ka=2.3*(10**-3)
    elif solution == 'Sulfurous Acid' or 'H2SO3':
        Ka=1.7*(10**-2)
    elif solution == 'Tartaric Acid' or 'HOOC(CHOH)2COOH' or 'H2C4H4O6':
        Ka=1.0*(10**-3)
    return Ka                                               #choose_a_solutionAcid() is slightly different than choose_a_titrantAcid() but are needed to determine different things

def choose_a_titrantAcid(Kb_1):#Chooses an acidic titrant
    titrant=input('\nWhat is your acidic titrant?').lower()
    #weakAcids=['Acetic Acid','Arsenic Acid','Arsenous Acid','
    #if titrant not in weakAcids:
     #   Ka=((1*(10**-14))/Kb_1)
    if titrant == 'Acetic Acid' or 'CH3COOH' or 'HC2H3O2':
        Ka=1.8*(10**-5)
    elif titrant == 'Arsenic Acid' or 'H3AsO4':
        Ka=5.6*(10**-3)
    elif titrant == 'Arsenous Acid' or 'H3AsO3':
        Ka=5.1*(10**-10)
    elif titrant == 'Ascorbic Acid' or 'H2C6H6O6':
        Ka=8*(10**-5)
    elif titrant == 'Benzoic Acid' or 'C6H7COOH' or 'HC7H5O2':
        Ka=1.5*(10**-5)
    elif titrant == 'Carbonic Acid' or 'H2CO3':
        Ka=4.3*(10**-7)
    elif titrant == 'Chloracetic Acid' or 'CH2ClCOOH' or 'HC2H2O2Cl':
        Ka=1.4*(10-3)
    elif titrant == 'Chlorous Acid' or 'HClO2':
        Ka=1.1*(10**-2)
    elif titrant == 'Citric Acid' or 'HOOCC(OH)(CH2COOH)2' or 'H3C6H5O7':
        Ka=7.4*(10**-4)
    elif titrant == 'Cyanic Acid' or 'HCNO':
        Ka=3.5*(10**-4)
    elif titrant == 'Formic Acid' or 'HCOOH' or 'HCHO2':
        Ka=1.8*(10**-4)
    elif titrant == 'Hydroazoic Acid' or 'HN3':
        Ka=1.9*(10**-5)
    elif titrant == 'Hydrocyanic Acid' or 'HCN':
        Ka=4.9*(10**-10)
    elif titrant == 'Hydrofluoric Acid' or 'HF':
        Ka=6.8*(10**-4)
    elif titrant == 'Hydrogen Chromate Ion' or 'HCrO4-':
        Ka=3.0*(10**-7)
    elif titrant == 'Hydrogen Peroxide' or 'H2O2':
        Ka=2.4*(10**-12)
    elif titrant == 'Hydrogen Selenate Ion' or 'HSeO4-':
        Ka=2.2*(10**-2)
    elif titrant == 'Hydrosulfuric Acid' or 'H2S':
        Ka=9.5*(10**-8)
    elif titrant == 'Hypobromous Acid' or 'HBrO':
        Ka=2.5*(10**-9)
    elif titrant == 'Hypochlorous Acid' or 'HClO':
        Ka=3.0*(10**-8)
    elif titrant == 'Hypoiodous Acid' or 'HIO':
        Ka=2.3*(10**-11)
    elif titrant == 'Iodic Acid' or 'HIO3':
        Ka=1.7*(10**-1)
    elif titrant == 'Lactic Acid' or 'CH3CH(OH)COOH' or 'HC3H5O3':
        Ka==1.4*(10**-4)
    elif titrant == 'Malonic Acid' or 'CH2(COOH)2' or 'H2C3H2O4':
        Ka=1.5*(10**-3)
    elif titrant == 'Nitrous Acid' or 'HNO2':
        Ka=4.5*(10**-4)
    elif titrant == 'Oxalic Acid' or '(COOH)2' or 'H2C2O4':
        Ka=5.9*(10**-2)
    elif titrant == 'Paraperiodic Acid' or 'H5IO6':
        Ka=2.8*(10**-2)
    elif titrant == 'Phenol' or 'C6H5OH' or 'HC6H5O':
        Ka=1.3*(10**-13)
    elif titrant == 'Phosphoric Acid' or 'H3PO4':
        Ka=7.5*(10**-3)
    elif titrant == 'Propionic Acid' or 'C2H5COOH' or 'HC3H5O2':
        Ka=1.3*(10**-5)
    elif titrant == 'Pyrophosphoric Acid' or 'H4P2O7':
        Ka=3.0*(10**-2)
    elif titrant == 'Selenous Acid' or 'H2SeO3':
        Ka=2.3*(10**-3)
    elif titrant == 'Sulfurous Acid' or 'H2SO3':
        Ka=1.7*(10**-2)
    elif titrant == 'Tartaric Acid' or 'HOOC(CHOH)2COOH' or 'H2C4H4O6':
        Ka=1.0*(10**-3)
    return Ka

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
#def find_pH_after_equivalence_ptBase():#Finds the pH after the equivalence point and beforethe titration has ended if the titrant is an acide
    

#Main()
list_acid_base=[]
           
choice=None

while choice!='0':
    
    print('''
        0. Exit
        1. Determine Acid/Base
        2. Find the pH of the solution before titrant is added
        3. Find volume and pH at equivalence point
        4. Find pH before equivalence point
        5. Find pH after equivalence point
        6. Show Graph
        ''')
    
    choice=input('Enter your choice')
    
    print()
    
    if choice=='0':
        
        print('Goodbye')#If choice = 0, user is logged out
        
    
    elif choice=='1':#Determines whether the solution is an acid or base
        solution1='c'

        while solution1 not in ['a','b']:

            solution1=input("Please tell what the solution is acid or base-a or b?")
            
        list_acid_base.append(solution1)

        if list_acid_base[0]=='a':#Determines the initial values of the concentration and volume of the acid and titrant base

            Ka_1=choose_a_solutionAcid()

            x_1,y_1,z_1=molarity_mL_Acid()

            Kb_1=choose_a_titrantBase(Ka_1)
           
        elif list_acid_base[0]=='b':#Determines the initial values of the concentration and volume of the base and titrant acid

            Kb_1=choose_a_solutionBase()

            x_1,y_1,z_1molarity_mL_Base()

            Ka_1=choose_a_titrantAcid(Kb_1)

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
        
            
            
