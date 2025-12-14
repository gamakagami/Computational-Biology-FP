import streamlit as st

st.subheader("Data Preparation")
st.markdown("1. Read file and drop rows that have missing values from used attributes:")
st.markdown("""
    ```python
    import pandas as pd

    df = pd.read_csv("/acetylcholinesterase_data.csv", sep=";")
    removed_missing_values = df.dropna(subset=["Smiles", "Standard Type", "Standard Value", "Standard Units", "Molecular Weight", "AlogP"])
""")

st.markdown("2. Filter the dataset to have the IC50 standard type:")
st.markdown("""
    ```python
    IC50_type = removed_missing_values[removed_missing_values["Standard Type"] == "IC50"]
""")

st.markdown("3. Filter the dataset to have nM standard units:")
st.markdown("""
    ```python
    nM_units = IC50_type[IC50_type["Standard Units"] == "nM"]
""")

st.markdown("4. Calculate IC50 in (m) from (nM), and convert it to pIC50 (m). Additionally, invalid pIC50 values that became infinite during the log transformation are removed:")
st.markdown("""
    ```python
    nM_units["IC50_m"] = nM_units["Standard Value"] * 1e-9
    nM_units["pIC50_m"] = -np.log10(nM_units["IC50_m"])
    nM_units = nM_units[nM_units["pIC50_m"] != np.inf]
""")

st.markdown("5. Initializes a MoleculeDescriptorCalculator with the intended descriptors produces as the parameter. Each smile's mol is calculated, which is then converted into a list of numerical descriptors:")
st.markdown("""
    ```python
    from rdkit import Chem
    from rdkit.ML.Descriptors.MoleculeDescriptors import MolecularDescriptorCalculator

    def smiles_column_converter(smiles):
        chosen_descriptors = ['BalabanJ', 'BertzCT', 'Chi0', 'Chi0n', 'Chi0v', 'Chi1', 'Chi1n', 'Chi1v', 'Chi2n', 'Chi2v', 'Chi3n', 'Chi3v', 'Chi4n', 'Chi4v', 'EState_VSA1', 'EState_VSA10', 'EState_VSA11', 'EState_VSA2', 'EState_VSA3', 'EState_VSA4', 'EState_VSA5', 'EState_VSA6', 'EState_VSA7', 'EState_VSA8', 'EState_VSA9', 'ExactMolWt', 'FpDensityMorgan1', 'FpDensityMorgan2', 'FpDensityMorgan3', 'FractionCSP3', 'HallKierAlpha', 'HeavyAtomCount', 'HeavyAtomMolWt', 'Ipc', 'Kappa1', 'Kappa2', 'Kappa3', 'LabuteASA', 'MaxAbsEStateIndex', 'MaxAbsPartialCharge', 'MaxEStateIndex', 'MaxPartialCharge', 'MinAbsEStateIndex', 'MinAbsPartialCharge', 'MinEStateIndex', 'MinPartialCharge', 'MolLogP', 'MolMR', 'MolWt', 'NHOHCount', 'NOCount', 'NumAliphaticCarbocycles', 'NumAliphaticHeterocycles', 'NumAliphaticRings', 'NumAromaticCarbocycles', 'NumAromaticHeterocycles', 'NumAromaticRings', 'NumHAcceptors', 'NumHDonors', 'NumHeteroatoms', 'NumRadicalElectrons', 'NumRotatableBonds', 'NumSaturatedCarbocycles', 'NumSaturatedHeterocycles', 'NumSaturatedRings', 'NumValenceElectrons', 'PEOE_VSA1', 'PEOE_VSA10', 'PEOE_VSA11', 'PEOE_VSA12', 'PEOE_VSA13', 'PEOE_VSA14', 'PEOE_VSA2', 'PEOE_VSA3', 'PEOE_VSA4', 'PEOE_VSA5', 'PEOE_VSA6', 'PEOE_VSA7', 'PEOE_VSA8', 'PEOE_VSA9', 'RingCount', 'SMR_VSA1', 'SMR_VSA10', 'SMR_VSA2', 'SMR_VSA3', 'SMR_VSA4', 'SMR_VSA5', 'SMR_VSA6', 'SMR_VSA7', 'SMR_VSA8', 'SMR_VSA9', 'SlogP_VSA1', 'SlogP_VSA10', 'SlogP_VSA11', 'SlogP_VSA12', 'SlogP_VSA2', 'SlogP_VSA3', 'SlogP_VSA4', 'SlogP_VSA5', 'SlogP_VSA6', 'SlogP_VSA7', 'SlogP_VSA8', 'SlogP_VSA9', 'TPSA', 'VSA_EState1', 'VSA_EState10', 'VSA_EState2', 'VSA_EState3', 'VSA_EState4', 'VSA_EState5', 'VSA_EState6', 'VSA_EState7', 'VSA_EState8', 'VSA_EState9', 'fr_Al_COO', 'fr_Al_OH', 'fr_Al_OH_noTert', 'fr_ArN', 'fr_Ar_COO', 'fr_Ar_N', 'fr_Ar_NH', 'fr_Ar_OH', 'fr_COO', 'fr_COO2', 'fr_C_O', 'fr_C_O_noCOO', 'fr_C_S', 'fr_HOCCN', 'fr_Imine', 'fr_NH0', 'fr_NH1', 'fr_NH2', 'fr_N_O', 'fr_Ndealkylation1', 'fr_Ndealkylation2', 'fr_Nhpyrrole', 'fr_SH', 'fr_aldehyde', 'fr_alkyl_carbamate', 'fr_alkyl_halide', 'fr_allylic_oxid', 'fr_amide', 'fr_amidine', 'fr_aniline', 'fr_aryl_methyl', 'fr_azide', 'fr_azo', 'fr_barbitur', 'fr_benzene', 'fr_benzodiazepine', 'fr_bicyclic', 'fr_diazo', 'fr_dihydropyridine', 'fr_epoxide', 'fr_ester', 'fr_ether', 'fr_furan', 'fr_guanido', 'fr_halogen', 'fr_hdrzine', 'fr_hdrzone', 'fr_imidazole', 'fr_imide', 'fr_isocyan', 'fr_isothiocyan', 'fr_ketone', 'fr_ketone_Topliss', 'fr_lactam', 'fr_lactone', 'fr_methoxy', 'fr_morpholine', 'fr_nitrile', 'fr_nitro', 'fr_nitro_arom', 'fr_nitro_arom_nonortho', 'fr_nitroso', 'fr_oxazole', 'fr_oxime', 'fr_para_hydroxylation', 'fr_phenol', 'fr_phenol_noOrthoHbond', 'fr_phos_acid', 'fr_phos_ester', 'fr_piperdine', 'fr_piperzine', 'fr_priamide', 'fr_prisulfonamd', 'fr_pyridine', 'fr_quatN', 'fr_sulfide', 'fr_sulfonamd', 'fr_sulfone', 'fr_term_acetylene', 'fr_tetrazole', 'fr_thiazole', 'fr_thiocyan', 'fr_thiophene', 'fr_unbrch_alkane', 'fr_urea', 'qed']
        calculator = MolecularDescriptorCalculator(chosen_descriptors)
        mol = Chem.MolFromSmiles(smiles)

        list_of_descriptor_vals = list(calculator.CalcDescriptors(mol))
        return list_of_descriptor_vals

    nM_units["Converted Smiles"] = nM_units["Smiles"].apply(smiles_column_converter)
""")

st.markdown("6. Converts the array from a string data type into an array data type:")
st.markdown("""
    ```python
    import ast
            
    smiles_arr_df["Converted Smiles"] = smiles_arr_df["Converted Smiles"].apply(ast.literal_eval)
""")

st.markdown("7. For each smiles descriptors array, it converts each value into its own independent column/attribute. Each attribute is then renamed to converted_smile_*, where * represents the index:")
st.markdown("""
    ```python
    smiles_into_attributes = smiles_arr_df['Converted Smiles'].apply(pd.Series).add_prefix('converted_smile_')
""")

st.markdown("8. Combine th descriptors df with the original dataframe:")
st.markdown("""
    ```python
    combined_data = pd.concat([smiles_arr_df, smiles_into_attributes], axis=1)
""")

st.markdown("9. Remove non numerical unused attributes to produce a df ready for machine learning:")
st.markdown("""
    ```python
    machine_learning_df = combined_data.drop(columns=["Molecule ChEMBL ID", "Molecule Name", "Molecule Max Phase", "#RO5 Violations", 
                                                    "Compound Key", "Smiles", "Standard Type", "Standard Relation", "Standard Value", "Standard Units", 
                                                    "pChEMBL Value", "Data Validity Comment", "Comment", "Uo Units", "Ligand Efficiency BEI", "Ligand Efficiency LE",
                                                    "Ligand Efficiency LLE", "Ligand Efficiency SEI", "Potential Duplicate", "Assay ChEMBL ID", "Assay Description",
                                                    "Assay Type", "BAO Format ID", "BAO Label", "Assay Organism", "Assay Tissue ChEMBL ID", "Assay Tissue Name",	
                                                    "Assay Cell Type", "Assay Subcellular Fraction", "Assay Parameters", "Assay Variant Accession", 
                                                    "Assay Variant Mutation", "Target ChEMBL ID", "Target Name", "Target Organism", "Target Type", "Document ChEMBL ID",
                                                    "Source ID", "Source Description", "Document Journal", "Document Year", "Cell ChEMBL ID", "Properties", "Action Type",
                                                    "Standard Text Value", "Value", "IC50_m", "Converted Smiles"])
""")