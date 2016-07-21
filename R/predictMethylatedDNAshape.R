predictMethylatedDNAshape <- function (filename) {
    loadPythonModules()
    query_table = system.file ("python",
                               "QueryTable.methyl-DNAshape_with_M_and_g.dat",
                               package = "DNAshapeR")
    v = python.call ("prediction", filename, 30, ",", query_table)
    return (v)
}