from rdkit.Chem import AllChem as Chem

with open("aminoacids.smi") as f:
    # remove multiple whitespace between smiles and name
    lines = f.readlines()
    lines = [" ".join(line.split()) for line in lines]
    text = "\n".join(lines)

    suppl = Chem.SmilesMolSupplierFromText(text)
    for mol in suppl:
        name = mol.GetProp("_Name")
        print(name, mol)
        mol = Chem.AddHs(mol)
        Chem.EmbedMolecule(mol, randomSeed=0xf00d)
        Chem.MolToMolFile(mol, f"aa_rdkit/mol/{name}.mol")
        Chem.MolToXYZFile(mol, f"aa_rdkit/xyz/{name}.xyz")
        Chem.MolToPDBFile(mol, f"aa_rdkit/pdb/{name}.pdb")
        Chem.SDWriter(f"aa_rdkit/sdf/{name}.sdf").write(mol)

