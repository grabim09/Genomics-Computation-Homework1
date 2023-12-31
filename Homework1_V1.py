#!/usr/bin/env python
# coding: utf-8

# # 07311940000046_Agra Bima Yuda_Genomics Computation_Homework 1

# ## This python program will solve all problem given by Homework 1 of Genomics Computation Subject

# ### 1. Preparation

# #### 1.1. Importing Necessary Library

# In[1]:


#All Necessary Library
import streamlit as st
import numpy as np
import pandas as pd
import random as rand


# #### 1.2. Creating Genetic Code Data from Publicly Available Source

# In[2]:


Genetic_Code = {
    0: {
        "Amino Acid": "Isoleucine",
        "Single_Letter": "I",
        "3-Letter Code": "Iso",
        "Codon": ['ATT', 'ATC', 'ATA']
    },
    1: {
        "Amino Acid": "Leucine",
        "Single_Letter": "L",
        "3-Letter Code": "Leu",
        "Codon": ['CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG']
    },
    2: {
        "Amino Acid": "Valine",
        "Single_Letter": "V",
        "3-Letter Code": "Val",
        "Codon": ['GTT', 'GTC', 'GTA', 'GTG']
    },
    3: {
        "Amino Acid": "Phenylalanine",
        "Single_Letter": "F",
        "3-Letter Code": "Phe",
        "Codon": ['TTT', 'TTC']
    },
    4: {
        "Amino Acid": "Methionine",
        "Single_Letter": "M",
        "3-Letter Code": "Met (Start)",
        "Codon": ['ATG']
    },
    5: {
        "Amino Acid": "Cysteine",
        "Single_Letter": "C",
        "3-Letter Code": "Cys",
        "Codon": ['TGT', 'TGC']
    },
    6: {
        "Amino Acid": "Alanine",
        "Single_Letter": "A",
        "3-Letter Code": "Ala",
        "Codon": ['GCT', 'GCC', 'GCA', 'GCG']
    },
    7: {
        "Amino Acid": "Glycine",
        "Single_Letter": "G",
        "3-Letter Code": "Gly",
        "Codon": ['GGT', 'GGC', 'GGA', 'GGG']
    },
    8: {
        "Amino Acid": "Proline",
        "Single_Letter": "P",
        "3-Letter Code": "Pro",
        "Codon": ['CCT', 'CCC', 'CCA', 'CCG']
    },
    9: {
        "Amino Acid": "Threonine",
        "Single_Letter": "T",
        "3-Letter Code": "Thr",
        "Codon": ['ACT', 'ACC', 'ACA', 'ACG']
    },
    10: {
        "Amino Acid": "Serine",
        "Single_Letter": "S",
        "3-Letter Code": "Ser",
        "Codon": ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC']
    },
    11: {
        "Amino Acid": "Tyrosine",
        "Single_Letter": "Y",
        "3-Letter Code": "Tyr",
        "Codon": ['TAT', 'TAC']
    },
    12: {
        "Amino Acid": "Tryptophan",
        "Single_Letter": "V",
        "3-Letter Code": "Trp",
        "Codon": ['TGG']
    },
    13: {
        "Amino Acid": "Glutamine",
        "Single_Letter": "Q",
        "3-Letter Code": "Glu",
        "Codon": ['CAA', 'CAG']
    },
    14: {
        "Amino Acid": "Asparagine",
        "Single_Letter": "N",
        "3-Letter Code": "Asn",
        "Codon": ['AAT', 'AAC']
    },
    15: {
        "Amino Acid": "Histidine",
        "Single_Letter": "H",
        "3-Letter Code": "His",
        "Codon": ['CAT', 'CAC']
    },
    16: {
        "Amino Acid": "Glutamic Acid",
        "Single_Letter": "E",
        "3-Letter Code": "Glu",
        "Codon": ['GAA', 'GAG']
    },
    17: {
        "Amino Acid": "Aspartic Acid",
        "Single_Letter": "D",
        "3-Letter Code": "Asp",
        "Codon": ['GAT', 'GAC']
    },
    18: {
        "Amino Acid": "Lysine",
        "Single_Letter": "K",
        "3-Letter Code": "Lys",
        "Codon": ['AAA', 'AAG']
    },
    19: {
        "Amino Acid": "Arginine",
        "Single_Letter": "R",
        "3-Letter Code": "Arg",
        "Codon": ['CGT', 'CGC', 'CGA', 'AGA', 'AGG']
    },
    20: {
        "Amino Acid": "Stop Codon",
        "Single_Letter": "Stop",
        "3-Letter Code": "Termination",
        "Codon": ['TAA', 'TAG', 'TGA']
    }
}


# In[13]:


GC = pd.DataFrame(Genetic_Code).T


# ### Solution

# #### Problem 1. Using concept of set and related commands in Programming Language, write a program to list the nitrogen base of DNA and RNA

# ##### 1.1. Defining All Nucleic Acid

# In[4]:


Nucleic_Acid = {"DNA","RNA"}


# ###### 1.2. Defining All Nitrogen Base

# In[5]:


Nitrogen_Base = {
    "Purines": {
        "Adenine",
        "Guanine"
    },
    "Pyrimidines": {
        "Cytosine",
        "Thymine",
        "Uracile"
    }
}


# ##### 1.3. Defining Nitrogen Base of Each Nucleic Acid

# In[6]:


Nucleic_Acid_Nitrogen_Base = {
    "DNA":{
        "Purines": Nitrogen_Base["Purines"],
        "Pyrimidines": Nitrogen_Base["Pyrimidines"] - {'Uracile'},
        "Nitrogen Base Name": Nitrogen_Base["Purines"] | (Nitrogen_Base["Pyrimidines"] - {'Uracile'}),
        "Nitrogen Base Code": set()
    },
    "RNA":{
        "Purines": Nitrogen_Base["Purines"],
        "Pyrimidines": Nitrogen_Base["Pyrimidines"] - {'Thymine'},
        "Nitrogen Base Name": Nitrogen_Base["Purines"] | (Nitrogen_Base["Pyrimidines"] - {'Thymine'}),
        "Nitrogen Base Code": set()
    }
}
for code in Nucleic_Acid_Nitrogen_Base["DNA"]["Nitrogen Base Name"]:
    Nucleic_Acid_Nitrogen_Base["DNA"]["Nitrogen Base Code"].add(code[0])
for code in Nucleic_Acid_Nitrogen_Base["RNA"]["Nitrogen Base Name"]:
    Nucleic_Acid_Nitrogen_Base["RNA"]["Nitrogen Base Code"].add(code[0])


# ##### 1.4. Function to Return Nitrogen Base Details of Chosen Nucleic Acid in Streamlit

# In[7]:


def nitrogen_base(molecule):
    mol = Nucleic_Acid_Nitrogen_Base.get(molecule)
#     print('Molecule Type: ' + molecule)
#     print('Purines: ' + ', '.join(sorted(mol.get("Purines"))))
#     print('Pyrimidines: ' + ', '.join(sorted(mol.get("Pyrimidines"))))
#     print('Nitrogen Base Name: ' + ', '.join(sorted(mol.get("Nitrogen Base Name"))))
#     print('Nitrogen Base Code: ' + ', '.join(sorted(mol.get("Nitrogen Base Code"))))
    st.write('Molecule Type: ' + molecule)
    st.write('Purines: ' + ', '.join(sorted(mol.get("Purines"))))
    st.write('Pyrimidines: ' + ', '.join(sorted(mol.get("Pyrimidines"))))
    st.write('Nitrogen Base Name: ' + ', '.join(sorted(mol.get("Nitrogen Base Name"))))
    st.write('Nitrogen Base Code: ' + ', '.join(sorted(mol.get("Nitrogen Base Code"))))


# ##### 1.4.a Alterncative Function to Return Nitrogen Base Details of Chosen Nucleic Acid in Streamlit

# In[8]:


def nitrogen_base2(molecule):
    Purines = Nitrogen_Base["Purines"]
    Pur = Purines
    Pyrimidines = Nitrogen_Base["Pyrimidines"]
    if molecule == 'DNA':
        Pyr = Pyrimidines - {'Uracile'}
    elif molecule == 'RNA':
        Pyr = Pyrimidines - {'Thymine'}
    NBF = Pur | Pyr
    NBC = set()
    for code in NBF:
        NBC.add(code[0])
#     print('Molecule Type: ' + molecule)
#     print('Purines: ' + str(Pur))
#     print('Pyrimidines: ' + str(Pyr))
#     print('Nitrogen Base Name: ' + str(NBF))
#     print('Nitrogen Base Code: ' + str(NBC))
    st.write('Molecule Type: ' + molecule)
    st.write('Purines: ' + str(Pur))
    st.write('Pyrimidines: ' + str(Pyr))
    st.write('Nitrogen Base Name: ' + str(NBF))
    st.write('Nitrogen Base Code: ' + str(NBC))


# #### Problem 2. Write a program that lists all the DNA and RNA sequences that encode a given protein sequences

# ##### 2.1. Function to Generate Random Protein Sequence

# In[9]:


def generate_random_sequence(acid,length):
    code = list(Nucleic_Acid_Nitrogen_Base[acid]["Nitrogen Base Code"])
    random_sequence = ''.join(rand.choice(code) for i in range(length))
    return random_sequence


# ##### 2.2. Function to Split Random Protein Sequence into Codons

# In[10]:


def split_into_codon(random_sequence):
    split_codon = [random_sequence[i:i+3] for i in range(0,len(random_sequence),3)]
    return split_codon


# ##### 2.3. Function to Map Codons into Corresponding Amino Acid

# In[11]:


def map_codon(split_codon):
    for codon in split_codon:
        temp = codon.replace("U","T")
        for idx, ele in enumerate(GC.loc[:,'Codon']):
            if temp in ele:
                st.write(f"Codon {codon}: {GC.loc[idx]['Amino Acid']} ({GC.loc[idx]['Single_Letter']})")


# #### Main Function

# In[12]:


def main():
    st.title("07311940000046_Agra Bima Yuda_Genomics Computation_Homework 1")
    st.divider()
    acid = st.radio(
        "Select one nucleic acid below:",
        sorted(Nucleic_Acid),
        captions = ["Deoxyribonucleic Acid","Ribonucleic Acid"])
    st.divider()
    st.header("Problem 1. Using concept of set and related commands in Programming Language, write a program to list the nitrogen base of DNA and RNA")
    st.subheader("Nitrogen base of selected Nucleic Acid")
    nitrogen_base(acid)
    st.divider()
    st.header("Problem 2. Write a program that lists all the DNA and RNA sequences that encode a given protein sequences")
    sequences_length = st.number_input("Enter the number of sequences: ", min_value=3, step=3)
    st.write(sequences_length)
    st.subheader("Generated Random Sequence")
    random_sequence = generate_random_sequence(acid,sequences_length)
    st.write(random_sequence)
    st.subheader("Splitting Sequence into Codons")
    split_codon = split_into_codon(random_sequence)
    st.write(split_codon)
    st.subheader("Defining Amino Acid form Codons")
    map_codon(split_codon)
    
if __name__ == "__main__":
    main()

