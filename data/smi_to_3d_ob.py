from openbabel import openbabel as ob

formats = ["mol", "mol2", "pdb", "sdf", "xyz"]

converter = ob.OBConversion()
converter.SetInFormat("smi")

mol = ob.OBMol()
builder = ob.OBBuilder()

not_at_end = converter.ReadFile(mol, "aminoacids.smi")
while not_at_end:
    mol.AddHydrogens()
    builder.Build(mol)
    name = mol.GetTitle()
    for format in formats:
        converter.SetOutFormat(format)
        converter.WriteFile(mol, f"aa_ob/{format}/{name}.{format}")
    mol = ob.OBMol()
    not_at_end = converter.Read(mol)    
