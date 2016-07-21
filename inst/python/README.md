#methylDNAshapeR 

```{.bash}
 for i in `ls *.py`; \
do \
	name=`echo $i | sed 's:.py$::g'`; \
	echo "$name = system.file (\"python\", \"$i\", package=\"DNAshapeR\")"; \ 
done
```
