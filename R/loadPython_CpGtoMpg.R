loadPython_CpGtoMpg <- function (){
    CpGtoMpg <- system.file("python",
                            "CpGtoMpg.py",
                            package = "DNAshapeR")
    read_pos <- system.file("python",
                            "read_pos.py",
                            package = "DNAshapeR")
    read_data <- system.file("python",
                            "read_data.py",
                            package = "DNAshapeR")
    convert_unmeth_to_meth_fasta <- system.file("python",
                                                "convert_unmeth_to_meth_fasta.py",
                                                package = "DNAshapeR")
    autoconvert <- system.file("python",
                               "autoconvert.py",
                               package = "DNAshapeR")
    rev_with_M_and_g = system.file ("python", "rev_with_M_and_g.py", package="DNAshapeR")
    check = system.file ("python", "check.py", package="DNAshapeR")
    python.load(autoconvert)
    python.load(rev_with_M_and_g)
    python.load(check)
    python.load(read_pos)
    python.load(read_data)
    python.load(CpGtoMpg)
    
    
}