from rdkit import Chem
from rdkit.Chem import Draw

# Defina a SMILES que você deseja visualizar
smiles = 'CC(=O)OC1=CC=CC=C1C(=Oh)O'

# Crie um objeto de molécula a partir da SMILES
mol = Chem.MolFromSmiles(smiles)

# Desenhe a molécula
img = Draw.MolToImage(mol)

# Exiba a imagem
img.show()