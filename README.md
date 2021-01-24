# prep_GLIPH2

## create input TCR file from mixcr output

expecting mixcr output from bulk RNAseq. CDR3A will be ignored.
{sample_name}.clonotypes.TRB.txt is the expected file name.

```
python prep_GLIPH2_mixcr.py dir_mixcr
```

## create HLA input from arcasHLA output

before the execution, collect `*.genotype.json` in a directory.

```
#!/bin/bash
set -x

mkdir -p arcasHLA 
cut -f 1 gdc_manifest.2020-01-18.txt | tail -n +2 | while read line
do
echo $line
cp ${line}/VIRTUS_1.2.1_kz0.3/arcasHLA/humanAligned.full.csv arcasHLA/${line}.csv
cp ${line}/VIRTUS_1.2.1_kz0.3/arcasHLA/humanAligned.genotype.json arcasHLA/${line}.genotype.json
done
```

then,

```
python prep_GLIPH2_arcasHLA.py test
```

## run GLIPH2

See http://50.255.35.37:8080/tools and download refs. 

```
cd test
irtools.centos -c GLIPH2.params.txt
```
