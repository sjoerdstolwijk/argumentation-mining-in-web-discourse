import os
import pandas as pd

from cassis import load_typesystem, TypeSystem, load_cas_from_xmi, Cas


def process_xmi_files(data_path: str, type_system_file: str) -> pd.DataFrame:
    
    type_system_file: str = os.path.join(data_path, type_system_file)
    
    with open(type_system_file, 'rb') as f:
        type_system: TypeSystem = load_typesystem(f)
    
    # List all XMI files
    xmi_files = [f for f in os.listdir(data_path) if f.endswith('.xmi')]
    
    data = []
    for xmi_file_name in xmi_files:
        file_number = int(xmi_file_name.split('.')[0])
        xmi_file_path = os.path.join(data_path, xmi_file_name)
        with open(xmi_file_path, 'rb') as f:
            cas: Cas = load_cas_from_xmi(f, type_system)
    
        # Define the types of elements to extract
        element_types = [
            'de.tudarmstadt.ukp.dkpro.argumentation.types.Claim',
            'de.tudarmstadt.ukp.dkpro.argumentation.types.Premise',
            'de.tudarmstadt.ukp.dkpro.argumentation.types.Rebuttal',
            'de.tudarmstadt.ukp.dkpro.argumentation.types.Refutation',
            'de.tudarmstadt.ukp.dkpro.argumentation.types.Backing'
        ]
        
        # Extract elements of each type
        for element_type in element_types:
            for element in cas.select(element_type):
                element_data = {
                    'file': file_number,
                    'type': element_type,
                    'text': element.get_covered_text()
                }
                data.append(element_data)
    
    df = pd.DataFrame(data)
    df = df.pivot_table(index = 'file', columns = 'type', values = 'text', aggfunc = list)

    return df