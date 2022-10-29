---
layout: container
name:  "quay.io/biocontainers/rnaquast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rnaquast/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/rnaquast/container.yaml"
updated_at: "2022-10-29 05:48:21.436112"
latest: "2.2.1--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/rnaquast"
aliases:
 - "PF00225_full.blocks.txt"
 - "PF00225_seed.blocks.txt"
 - "add_name_to_gff3.pl"
 - "aln2wig"
 - "augustify.py"
 - "busco"
 - "executeTestCGP.py"
 - "extractAnno.py"
 - "generate_plot.py"
 - "get_loci_from_gb.pl"
 - "gmap_cat"
 - "indexdb_cat"
 - "metaeuk"
 - "pp_simScore"
 - "pslSort"
 - "rnaQUAST.py"
 - "run-sepp.sh"
 - "run_abundance.py"
 - "run_sepp.py"
 - "run_tipp.py"
 - "run_tipp_tool.py"
 - "run_upp.py"
 - "seppJsonMerger.jar"
 - "split_sequences.py"
 - "2to3-3.9"
 - "STAR"
 - "STARlong"
 - "SplicedAlignment.pm"
 - "_aaindexextract"
 - "_abiview"
 - "_acdc"
 - "_acdpretty"
 - "_acdtable"
 - "_acdtrace"
versions:
 - "2.2.1--h9ee0642_0"
description: "shpc-registry automated BioContainers addition for rnaquast"
config: {"url": "https://biocontainers.pro/tools/rnaquast", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rnaquast", "latest": {"2.2.1--h9ee0642_0": "sha256:6b3678537b50cc63c9c1cf6088eb9f64cf833b51836e743f1733fb98d234f989"}, "tags": {"2.2.1--h9ee0642_0": "sha256:6b3678537b50cc63c9c1cf6088eb9f64cf833b51836e743f1733fb98d234f989"}, "docker": "quay.io/biocontainers/rnaquast", "aliases": {"PF00225_full.blocks.txt": "/usr/local/bin/PF00225_full.blocks.txt", "PF00225_seed.blocks.txt": "/usr/local/bin/PF00225_seed.blocks.txt", "add_name_to_gff3.pl": "/usr/local/bin/add_name_to_gff3.pl", "aln2wig": "/usr/local/bin/aln2wig", "augustify.py": "/usr/local/bin/augustify.py", "busco": "/usr/local/bin/busco", "executeTestCGP.py": "/usr/local/bin/executeTestCGP.py", "extractAnno.py": "/usr/local/bin/extractAnno.py", "generate_plot.py": "/usr/local/bin/generate_plot.py", "get_loci_from_gb.pl": "/usr/local/bin/get_loci_from_gb.pl", "gmap_cat": "/usr/local/bin/gmap_cat", "indexdb_cat": "/usr/local/bin/indexdb_cat", "metaeuk": "/usr/local/bin/metaeuk", "pp_simScore": "/usr/local/bin/pp_simScore", "pslSort": "/usr/local/bin/pslSort", "rnaQUAST.py": "/usr/local/bin/rnaQUAST.py", "run-sepp.sh": "/usr/local/bin/run-sepp.sh", "run_abundance.py": "/usr/local/bin/run_abundance.py", "run_sepp.py": "/usr/local/bin/run_sepp.py", "run_tipp.py": "/usr/local/bin/run_tipp.py", "run_tipp_tool.py": "/usr/local/bin/run_tipp_tool.py", "run_upp.py": "/usr/local/bin/run_upp.py", "seppJsonMerger.jar": "/usr/local/bin/seppJsonMerger.jar", "split_sequences.py": "/usr/local/bin/split_sequences.py", "2to3-3.9": "/usr/local/bin/2to3-3.9", "STAR": "/usr/local/bin/STAR", "STARlong": "/usr/local/bin/STARlong", "SplicedAlignment.pm": "/usr/local/bin/SplicedAlignment.pm", "_aaindexextract": "/usr/local/bin/_aaindexextract", "_abiview": "/usr/local/bin/_abiview", "_acdc": "/usr/local/bin/_acdc", "_acdpretty": "/usr/local/bin/_acdpretty", "_acdtable": "/usr/local/bin/_acdtable", "_acdtrace": "/usr/local/bin/_acdtrace"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rnaquast.
shpc-registry automated BioContainers addition for rnaquast
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rnaquast
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rnaquast:2.2.1--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rnaquast/2.2.1--h9ee0642_0
$ module help quay.io/biocontainers/rnaquast/2.2.1--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rnaquast-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rnaquast-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rnaquast-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rnaquast-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rnaquast-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rnaquast-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### busco

```bash
$ singularity exec <container> /usr/local/bin/busco
$ podman run --it --rm --entrypoint /usr/local/bin/busco   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/busco   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### generate_plot.py

```bash
$ singularity exec <container> /usr/local/bin/generate_plot.py
$ podman run --it --rm --entrypoint /usr/local/bin/generate_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_loci_from_gb.pl

```bash
$ singularity exec <container> /usr/local/bin/get_loci_from_gb.pl
$ podman run --it --rm --entrypoint /usr/local/bin/get_loci_from_gb.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_loci_from_gb.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap_cat

```bash
$ singularity exec <container> /usr/local/bin/gmap_cat
$ podman run --it --rm --entrypoint /usr/local/bin/gmap_cat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap_cat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### indexdb_cat

```bash
$ singularity exec <container> /usr/local/bin/indexdb_cat
$ podman run --it --rm --entrypoint /usr/local/bin/indexdb_cat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/indexdb_cat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaeuk

```bash
$ singularity exec <container> /usr/local/bin/metaeuk
$ podman run --it --rm --entrypoint /usr/local/bin/metaeuk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaeuk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pp_simScore

```bash
$ singularity exec <container> /usr/local/bin/pp_simScore
$ podman run --it --rm --entrypoint /usr/local/bin/pp_simScore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pp_simScore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pslSort

```bash
$ singularity exec <container> /usr/local/bin/pslSort
$ podman run --it --rm --entrypoint /usr/local/bin/pslSort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pslSort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnaQUAST.py

```bash
$ singularity exec <container> /usr/local/bin/rnaQUAST.py
$ podman run --it --rm --entrypoint /usr/local/bin/rnaQUAST.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnaQUAST.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-sepp.sh

```bash
$ singularity exec <container> /usr/local/bin/run-sepp.sh
$ podman run --it --rm --entrypoint /usr/local/bin/run-sepp.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-sepp.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_abundance.py

```bash
$ singularity exec <container> /usr/local/bin/run_abundance.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_abundance.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_abundance.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_sepp.py

```bash
$ singularity exec <container> /usr/local/bin/run_sepp.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_sepp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_sepp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_tipp.py

```bash
$ singularity exec <container> /usr/local/bin/run_tipp.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_tipp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_tipp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_tipp_tool.py

```bash
$ singularity exec <container> /usr/local/bin/run_tipp_tool.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_tipp_tool.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_tipp_tool.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_upp.py

```bash
$ singularity exec <container> /usr/local/bin/run_upp.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_upp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_upp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seppJsonMerger.jar

```bash
$ singularity exec <container> /usr/local/bin/seppJsonMerger.jar
$ podman run --it --rm --entrypoint /usr/local/bin/seppJsonMerger.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seppJsonMerger.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split_sequences.py

```bash
$ singularity exec <container> /usr/local/bin/split_sequences.py
$ podman run --it --rm --entrypoint /usr/local/bin/split_sequences.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split_sequences.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STAR

```bash
$ singularity exec <container> /usr/local/bin/STAR
$ podman run --it --rm --entrypoint /usr/local/bin/STAR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STARlong

```bash
$ singularity exec <container> /usr/local/bin/STARlong
$ podman run --it --rm --entrypoint /usr/local/bin/STARlong   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STARlong   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SplicedAlignment.pm

```bash
$ singularity exec <container> /usr/local/bin/SplicedAlignment.pm
$ podman run --it --rm --entrypoint /usr/local/bin/SplicedAlignment.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SplicedAlignment.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _aaindexextract

```bash
$ singularity exec <container> /usr/local/bin/_aaindexextract
$ podman run --it --rm --entrypoint /usr/local/bin/_aaindexextract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_aaindexextract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _abiview

```bash
$ singularity exec <container> /usr/local/bin/_abiview
$ podman run --it --rm --entrypoint /usr/local/bin/_abiview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_abiview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _acdc

```bash
$ singularity exec <container> /usr/local/bin/_acdc
$ podman run --it --rm --entrypoint /usr/local/bin/_acdc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_acdc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _acdpretty

```bash
$ singularity exec <container> /usr/local/bin/_acdpretty
$ podman run --it --rm --entrypoint /usr/local/bin/_acdpretty   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_acdpretty   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _acdtable

```bash
$ singularity exec <container> /usr/local/bin/_acdtable
$ podman run --it --rm --entrypoint /usr/local/bin/_acdtable   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_acdtable   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _acdtrace

```bash
$ singularity exec <container> /usr/local/bin/_acdtrace
$ podman run --it --rm --entrypoint /usr/local/bin/_acdtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_acdtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
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