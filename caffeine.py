# Import the necessary RDKit modules
from rdkit import Chem
from rdkit.Chem import Descriptors

# Define the SMILES string for caffeine
caffeine_smiles = 'CN1C=NC2=C1C(=O)N(C(=O)N2C)C'

# Create a molecule object from the SMILES string
caffeine_molecule = Chem.MolFromSmiles(caffeine_smiles)

# Calculate the molecular weight of caffeine
molecular_weight = Descriptors.MolWt(caffeine_molecule)

# Get the canonical SMILES representation of caffeine
canonical_smiles = Chem.MolToSmiles(caffeine_molecule)

# Print the results
print(f"Molecular Weight of Caffeine: {molecular_weight:.2f} g/mol")
print(f"Canonical SMILES of Caffeine: {canonical_smiles}")
