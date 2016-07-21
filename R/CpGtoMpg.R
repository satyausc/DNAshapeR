#' Reverse complement for a given DNA sequence
#'
#' \code{reverse_complement} Reverse complement of a DNA sequence
#'
#' @usage reverse_complement (sequence)
#'
#' @param sequence A DNA sequence
#' @export
#'
CpGtoMpg <- function(filename, methylated_CpG_pos_file = "", out_filename="") {
    loadPython_CpGtoMpg()
    message = python.call ("CpGtoMpg",
                           filename = filename,
                           pos_fasta =  methylated_CpG_pos_file,
                           out_filename =  out_filename)
    return (message)
}
