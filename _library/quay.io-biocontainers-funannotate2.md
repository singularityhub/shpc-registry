---
layout: container
name:  "quay.io/biocontainers/funannotate2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/funannotate2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/funannotate2/container.yaml"
updated_at: "2026-05-10 06:14:53.134285"
latest: "26.2.12--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/funannotate2"
aliases:
 - "MitoHighConfidenceFilter"
 - "annorefine"
 - "buscolite"
 - "buscolite-plot"
 - "fathom"
 - "findRepetitiveProtSeqs.py"
 - "forge"
 - "funannotate2"
 - "gapmm2"
 - "gff3_to_zff.pl"
 - "gfftk"
 - "hmm-assembler.pl"
 - "json_repair"
 - "rename_species.pl"
 - "snap"
 - "stringtie2fa.py"
 - "table2asn"
 - "zff2gff3.pl"
 - "PF00225_full.blocks.txt"
 - "PF00225_seed.blocks.txt"
 - "add_name_to_gff3.pl"
 - "aln2wig"
 - "augustify.py"
 - "executeTestCGP.py"
 - "extractAnno.py"
 - "get_loci_from_gb.pl"
 - "miniprot"
 - "pp_simScore"
 - "bamToWig.py"
 - "compare_masking.pl"
 - "fix_in_frame_stop_codon_genes.py"
 - "fix_joingenes_gtf.pl"
 - "merge_masking.pl"
 - "EukHighConfidenceFilter"
 - "aa2nonred.pl"
 - "cdbfasta"
 - "cdbyank"
 - "compileSpliceCands"
 - "computeFlankingRegion.pl"
 - "covels-SE"
 - "coves-SE"
 - "eufindtRNA"
 - "eval_multi_gtf.pl"
versions:
 - "26.2.12--pyhdfd78af_0"
description: "singularity registry hpc automated addition for funannotate2"
config: {"url": "https://biocontainers.pro/tools/funannotate2", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for funannotate2", "latest": {"26.2.12--pyhdfd78af_0": "sha256:3194d71046b568482b619269b63c1e333757834dc117c9a5583efdbc1d65a39b"}, "tags": {"26.2.12--pyhdfd78af_0": "sha256:3194d71046b568482b619269b63c1e333757834dc117c9a5583efdbc1d65a39b"}, "docker": "quay.io/biocontainers/funannotate2", "aliases": {"MitoHighConfidenceFilter": "/usr/local/bin/MitoHighConfidenceFilter", "annorefine": "/usr/local/bin/annorefine", "buscolite": "/usr/local/bin/buscolite", "buscolite-plot": "/usr/local/bin/buscolite-plot", "fathom": "/usr/local/bin/fathom", "findRepetitiveProtSeqs.py": "/usr/local/bin/findRepetitiveProtSeqs.py", "forge": "/usr/local/bin/forge", "funannotate2": "/usr/local/bin/funannotate2", "gapmm2": "/usr/local/bin/gapmm2", "gff3_to_zff.pl": "/usr/local/bin/gff3_to_zff.pl", "gfftk": "/usr/local/bin/gfftk", "hmm-assembler.pl": "/usr/local/bin/hmm-assembler.pl", "json_repair": "/usr/local/bin/json_repair", "rename_species.pl": "/usr/local/bin/rename_species.pl", "snap": "/usr/local/bin/snap", "stringtie2fa.py": "/usr/local/bin/stringtie2fa.py", "table2asn": "/usr/local/bin/table2asn", "zff2gff3.pl": "/usr/local/bin/zff2gff3.pl", "PF00225_full.blocks.txt": "/usr/local/bin/PF00225_full.blocks.txt", "PF00225_seed.blocks.txt": "/usr/local/bin/PF00225_seed.blocks.txt", "add_name_to_gff3.pl": "/usr/local/bin/add_name_to_gff3.pl", "aln2wig": "/usr/local/bin/aln2wig", "augustify.py": "/usr/local/bin/augustify.py", "executeTestCGP.py": "/usr/local/bin/executeTestCGP.py", "extractAnno.py": "/usr/local/bin/extractAnno.py", "get_loci_from_gb.pl": "/usr/local/bin/get_loci_from_gb.pl", "miniprot": "/usr/local/bin/miniprot", "pp_simScore": "/usr/local/bin/pp_simScore", "bamToWig.py": "/usr/local/bin/bamToWig.py", "compare_masking.pl": "/usr/local/bin/compare_masking.pl", "fix_in_frame_stop_codon_genes.py": "/usr/local/bin/fix_in_frame_stop_codon_genes.py", "fix_joingenes_gtf.pl": "/usr/local/bin/fix_joingenes_gtf.pl", "merge_masking.pl": "/usr/local/bin/merge_masking.pl", "EukHighConfidenceFilter": "/usr/local/bin/EukHighConfidenceFilter", "aa2nonred.pl": "/usr/local/bin/aa2nonred.pl", "cdbfasta": "/usr/local/bin/cdbfasta", "cdbyank": "/usr/local/bin/cdbyank", "compileSpliceCands": "/usr/local/bin/compileSpliceCands", "computeFlankingRegion.pl": "/usr/local/bin/computeFlankingRegion.pl", "covels-SE": "/usr/local/bin/covels-SE", "coves-SE": "/usr/local/bin/coves-SE", "eufindtRNA": "/usr/local/bin/eufindtRNA", "eval_multi_gtf.pl": "/usr/local/bin/eval_multi_gtf.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/funannotate2.
singularity registry hpc automated addition for funannotate2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/funannotate2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/funannotate2:26.2.12--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/funannotate2/26.2.12--pyhdfd78af_0
$ module help quay.io/biocontainers/funannotate2/26.2.12--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### funannotate2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### funannotate2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### funannotate2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### funannotate2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### funannotate2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### funannotate2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MitoHighConfidenceFilter

```bash
$ singularity exec <container> /usr/local/bin/MitoHighConfidenceFilter
$ podman run --it --rm --entrypoint /usr/local/bin/MitoHighConfidenceFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MitoHighConfidenceFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annorefine

```bash
$ singularity exec <container> /usr/local/bin/annorefine
$ podman run --it --rm --entrypoint /usr/local/bin/annorefine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annorefine   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### buscolite

```bash
$ singularity exec <container> /usr/local/bin/buscolite
$ podman run --it --rm --entrypoint /usr/local/bin/buscolite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/buscolite   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### buscolite-plot

```bash
$ singularity exec <container> /usr/local/bin/buscolite-plot
$ podman run --it --rm --entrypoint /usr/local/bin/buscolite-plot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/buscolite-plot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fathom

```bash
$ singularity exec <container> /usr/local/bin/fathom
$ podman run --it --rm --entrypoint /usr/local/bin/fathom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fathom   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### findRepetitiveProtSeqs.py

```bash
$ singularity exec <container> /usr/local/bin/findRepetitiveProtSeqs.py
$ podman run --it --rm --entrypoint /usr/local/bin/findRepetitiveProtSeqs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/findRepetitiveProtSeqs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### forge

```bash
$ singularity exec <container> /usr/local/bin/forge
$ podman run --it --rm --entrypoint /usr/local/bin/forge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/forge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### funannotate2

```bash
$ singularity exec <container> /usr/local/bin/funannotate2
$ podman run --it --rm --entrypoint /usr/local/bin/funannotate2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/funannotate2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gapmm2

```bash
$ singularity exec <container> /usr/local/bin/gapmm2
$ podman run --it --rm --entrypoint /usr/local/bin/gapmm2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gapmm2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff3_to_zff.pl

```bash
$ singularity exec <container> /usr/local/bin/gff3_to_zff.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gff3_to_zff.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff3_to_zff.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfftk

```bash
$ singularity exec <container> /usr/local/bin/gfftk
$ podman run --it --rm --entrypoint /usr/local/bin/gfftk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfftk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmm-assembler.pl

```bash
$ singularity exec <container> /usr/local/bin/hmm-assembler.pl
$ podman run --it --rm --entrypoint /usr/local/bin/hmm-assembler.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmm-assembler.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### json_repair

```bash
$ singularity exec <container> /usr/local/bin/json_repair
$ podman run --it --rm --entrypoint /usr/local/bin/json_repair   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/json_repair   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rename_species.pl

```bash
$ singularity exec <container> /usr/local/bin/rename_species.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rename_species.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rename_species.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snap

```bash
$ singularity exec <container> /usr/local/bin/snap
$ podman run --it --rm --entrypoint /usr/local/bin/snap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stringtie2fa.py

```bash
$ singularity exec <container> /usr/local/bin/stringtie2fa.py
$ podman run --it --rm --entrypoint /usr/local/bin/stringtie2fa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stringtie2fa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### table2asn

```bash
$ singularity exec <container> /usr/local/bin/table2asn
$ podman run --it --rm --entrypoint /usr/local/bin/table2asn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/table2asn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zff2gff3.pl

```bash
$ singularity exec <container> /usr/local/bin/zff2gff3.pl
$ podman run --it --rm --entrypoint /usr/local/bin/zff2gff3.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zff2gff3.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PF00225_full.blocks.txt

```bash
$ singularity exec <container> /usr/local/bin/PF00225_full.blocks.txt
$ podman run --it --rm --entrypoint /usr/local/bin/PF00225_full.blocks.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PF00225_full.blocks.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PF00225_seed.blocks.txt

```bash
$ singularity exec <container> /usr/local/bin/PF00225_seed.blocks.txt
$ podman run --it --rm --entrypoint /usr/local/bin/PF00225_seed.blocks.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PF00225_seed.blocks.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### add_name_to_gff3.pl

```bash
$ singularity exec <container> /usr/local/bin/add_name_to_gff3.pl
$ podman run --it --rm --entrypoint /usr/local/bin/add_name_to_gff3.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/add_name_to_gff3.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aln2wig

```bash
$ singularity exec <container> /usr/local/bin/aln2wig
$ podman run --it --rm --entrypoint /usr/local/bin/aln2wig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aln2wig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### augustify.py

```bash
$ singularity exec <container> /usr/local/bin/augustify.py
$ podman run --it --rm --entrypoint /usr/local/bin/augustify.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/augustify.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### executeTestCGP.py

```bash
$ singularity exec <container> /usr/local/bin/executeTestCGP.py
$ podman run --it --rm --entrypoint /usr/local/bin/executeTestCGP.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/executeTestCGP.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extractAnno.py

```bash
$ singularity exec <container> /usr/local/bin/extractAnno.py
$ podman run --it --rm --entrypoint /usr/local/bin/extractAnno.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extractAnno.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_loci_from_gb.pl

```bash
$ singularity exec <container> /usr/local/bin/get_loci_from_gb.pl
$ podman run --it --rm --entrypoint /usr/local/bin/get_loci_from_gb.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_loci_from_gb.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### miniprot

```bash
$ singularity exec <container> /usr/local/bin/miniprot
$ podman run --it --rm --entrypoint /usr/local/bin/miniprot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miniprot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pp_simScore

```bash
$ singularity exec <container> /usr/local/bin/pp_simScore
$ podman run --it --rm --entrypoint /usr/local/bin/pp_simScore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pp_simScore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToWig.py

```bash
$ singularity exec <container> /usr/local/bin/bamToWig.py
$ podman run --it --rm --entrypoint /usr/local/bin/bamToWig.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToWig.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compare_masking.pl

```bash
$ singularity exec <container> /usr/local/bin/compare_masking.pl
$ podman run --it --rm --entrypoint /usr/local/bin/compare_masking.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compare_masking.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fix_in_frame_stop_codon_genes.py

```bash
$ singularity exec <container> /usr/local/bin/fix_in_frame_stop_codon_genes.py
$ podman run --it --rm --entrypoint /usr/local/bin/fix_in_frame_stop_codon_genes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fix_in_frame_stop_codon_genes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fix_joingenes_gtf.pl

```bash
$ singularity exec <container> /usr/local/bin/fix_joingenes_gtf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fix_joingenes_gtf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fix_joingenes_gtf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_masking.pl

```bash
$ singularity exec <container> /usr/local/bin/merge_masking.pl
$ podman run --it --rm --entrypoint /usr/local/bin/merge_masking.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_masking.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### EukHighConfidenceFilter

```bash
$ singularity exec <container> /usr/local/bin/EukHighConfidenceFilter
$ podman run --it --rm --entrypoint /usr/local/bin/EukHighConfidenceFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EukHighConfidenceFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aa2nonred.pl

```bash
$ singularity exec <container> /usr/local/bin/aa2nonred.pl
$ podman run --it --rm --entrypoint /usr/local/bin/aa2nonred.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aa2nonred.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cdbfasta

```bash
$ singularity exec <container> /usr/local/bin/cdbfasta
$ podman run --it --rm --entrypoint /usr/local/bin/cdbfasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cdbfasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cdbyank

```bash
$ singularity exec <container> /usr/local/bin/cdbyank
$ podman run --it --rm --entrypoint /usr/local/bin/cdbyank   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cdbyank   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compileSpliceCands

```bash
$ singularity exec <container> /usr/local/bin/compileSpliceCands
$ podman run --it --rm --entrypoint /usr/local/bin/compileSpliceCands   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compileSpliceCands   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### computeFlankingRegion.pl

```bash
$ singularity exec <container> /usr/local/bin/computeFlankingRegion.pl
$ podman run --it --rm --entrypoint /usr/local/bin/computeFlankingRegion.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/computeFlankingRegion.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### covels-SE

```bash
$ singularity exec <container> /usr/local/bin/covels-SE
$ podman run --it --rm --entrypoint /usr/local/bin/covels-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/covels-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coves-SE

```bash
$ singularity exec <container> /usr/local/bin/coves-SE
$ podman run --it --rm --entrypoint /usr/local/bin/coves-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coves-SE   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eufindtRNA

```bash
$ singularity exec <container> /usr/local/bin/eufindtRNA
$ podman run --it --rm --entrypoint /usr/local/bin/eufindtRNA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eufindtRNA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eval_multi_gtf.pl

```bash
$ singularity exec <container> /usr/local/bin/eval_multi_gtf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/eval_multi_gtf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eval_multi_gtf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)