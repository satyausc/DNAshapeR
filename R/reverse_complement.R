#' Reverse complement for a given DNA sequence
#'
#' \code{reverse_complement} Reverse complement of a DNA sequence
#'
#' @usage reverse_complement (sequence)
#'
#' @param sequence A DNA sequence
#' @export
#'
reverse_complement <- function(sequence) {
    loadPythonModules()
    rev_strand = python.call ("revcompl", sequence)
    return (rev_strand)
}
