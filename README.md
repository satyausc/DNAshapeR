# methyl-DNAshapeR

This packages is an extension of DNAshapeR to profile the fully methylated DNA sequences. User can now use the letter "**M**" for 5-methylcytosine and the letter "**g**" for guanine followed by 5-methylcytosine to charecterize methylated site(s). 

## Using DNAshapeR for methylated sequences

This development version consider two cases for a given sequence. First, it predicts the shape features for unmethylated sequence and second, it methylates specified/all CpG positions and predicts shape features. The prediction also return the difference between shape features (methylated - unmethylated).
### Installation guide 
Please follow the instructions below to install this package in R environment 
```{r}
library (devtools)
devtools::install_github("satyausc/DNAshapeR") 
```
### Demo
#### Case I: Methylating all CpG sites in the sequence
```{r}
library("DNAshapeR")
Pred = getShape ("tmp.fa")
plotShape(Pred$meth.MGW)
plotShape(Pred$unmeth.MGW)
plotShape(Pred$Delta.MGW)
```
#### Case II: Methylating specific CpG sites in the sequence
```{r}
library("DNAshapeR")
Pred = getShape ("tmp.fa", methylated_CpG_pos_file ="pos.fa")
plotShape(Pred$meth.MGW)
plotShape(Pred$unmeth.MGW)
plotShape(Pred$Delta.MGW)
```

