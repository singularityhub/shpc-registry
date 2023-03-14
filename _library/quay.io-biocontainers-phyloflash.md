---
layout: container
name:  "quay.io/biocontainers/phyloflash"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phyloflash/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/phyloflash/container.yaml"
updated_at: "2023-03-14 02:53:42.141781"
latest: "3.4.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/phyloflash"
aliases:
 - "ENA_phyloFlash.pl"
 - "emirge.py"
 - "emirge_amplicon.py"
 - "emirge_makedb.py"
 - "emirge_rename_fasta.py"
 - "phyloFlash.pl"
 - "phyloFlash_barplot.R"
 - "phyloFlash_compare.pl"
 - "phyloFlash_fastgFishing.pl"
 - "phyloFlash_heatmap.R"
 - "phyloFlash_makedb.pl"
 - "phyloFlash_plotscript_svg.pl"
 - "kmutate.sh"
 - "runhmm.sh"
 - "kmerposition.sh"
 - "reformatpb.sh"
 - "summarizecoverage.sh"
 - "alltoall.sh"
 - "analyzesketchresults.sh"
 - "comparessu.sh"
 - "filtersilva.sh"
 - "sketchblacklist2.sh"
versions:
 - "3.4.1--hdfd78af_0"
 - "3.4--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for phyloflash"
config: {"url": "https://biocontainers.pro/tools/phyloflash", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for phyloflash", "latest": {"3.4.1--hdfd78af_0": "sha256:d110b0bb01fc725502adad58e6cb36a679890bf745c3d0c02526a126e848294c"}, "tags": {"3.4.1--hdfd78af_0": "sha256:d110b0bb01fc725502adad58e6cb36a679890bf745c3d0c02526a126e848294c", "3.4--hdfd78af_1": "sha256:5f9f2fb78806dd87e14f236f15e98683493c8e378ab5f3884a5d863a2fc7bffe"}, "docker": "quay.io/biocontainers/phyloflash", "aliases": {"ENA_phyloFlash.pl": "/usr/local/bin/ENA_phyloFlash.pl", "emirge.py": "/usr/local/bin/emirge.py", "emirge_amplicon.py": "/usr/local/bin/emirge_amplicon.py", "emirge_makedb.py": "/usr/local/bin/emirge_makedb.py", "emirge_rename_fasta.py": "/usr/local/bin/emirge_rename_fasta.py", "phyloFlash.pl": "/usr/local/bin/phyloFlash.pl", "phyloFlash_barplot.R": "/usr/local/bin/phyloFlash_barplot.R", "phyloFlash_compare.pl": "/usr/local/bin/phyloFlash_compare.pl", "phyloFlash_fastgFishing.pl": "/usr/local/bin/phyloFlash_fastgFishing.pl", "phyloFlash_heatmap.R": "/usr/local/bin/phyloFlash_heatmap.R", "phyloFlash_makedb.pl": "/usr/local/bin/phyloFlash_makedb.pl", "phyloFlash_plotscript_svg.pl": "/usr/local/bin/phyloFlash_plotscript_svg.pl", "kmutate.sh": "/usr/local/bin/kmutate.sh", "runhmm.sh": "/usr/local/bin/runhmm.sh", "kmerposition.sh": "/usr/local/bin/kmerposition.sh", "reformatpb.sh": "/usr/local/bin/reformatpb.sh", "summarizecoverage.sh": "/usr/local/bin/summarizecoverage.sh", "alltoall.sh": "/usr/local/bin/alltoall.sh", "analyzesketchresults.sh": "/usr/local/bin/analyzesketchresults.sh", "comparessu.sh": "/usr/local/bin/comparessu.sh", "filtersilva.sh": "/usr/local/bin/filtersilva.sh", "sketchblacklist2.sh": "/usr/local/bin/sketchblacklist2.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/phyloflash.
shpc-registry automated BioContainers addition for phyloflash
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/phyloflash
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/phyloflash:3.4.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/phyloflash/3.4.1--hdfd78af_0
$ module help quay.io/biocontainers/phyloflash/3.4.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### phyloflash-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### phyloflash-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### phyloflash-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### phyloflash-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### phyloflash-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### phyloflash-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ENA_phyloFlash.pl

```bash
$ singularity exec <container> /usr/local/bin/ENA_phyloFlash.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ENA_phyloFlash.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ENA_phyloFlash.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### emirge.py

```bash
$ singularity exec <container> /usr/local/bin/emirge.py
$ podman run --it --rm --entrypoint /usr/local/bin/emirge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/emirge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### emirge_amplicon.py

```bash
$ singularity exec <container> /usr/local/bin/emirge_amplicon.py
$ podman run --it --rm --entrypoint /usr/local/bin/emirge_amplicon.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/emirge_amplicon.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### emirge_makedb.py

```bash
$ singularity exec <container> /usr/local/bin/emirge_makedb.py
$ podman run --it --rm --entrypoint /usr/local/bin/emirge_makedb.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/emirge_makedb.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### emirge_rename_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/emirge_rename_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/emirge_rename_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/emirge_rename_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phyloFlash.pl

```bash
$ singularity exec <container> /usr/local/bin/phyloFlash.pl
$ podman run --it --rm --entrypoint /usr/local/bin/phyloFlash.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phyloFlash.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phyloFlash_barplot.R

```bash
$ singularity exec <container> /usr/local/bin/phyloFlash_barplot.R
$ podman run --it --rm --entrypoint /usr/local/bin/phyloFlash_barplot.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phyloFlash_barplot.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phyloFlash_compare.pl

```bash
$ singularity exec <container> /usr/local/bin/phyloFlash_compare.pl
$ podman run --it --rm --entrypoint /usr/local/bin/phyloFlash_compare.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phyloFlash_compare.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phyloFlash_fastgFishing.pl

```bash
$ singularity exec <container> /usr/local/bin/phyloFlash_fastgFishing.pl
$ podman run --it --rm --entrypoint /usr/local/bin/phyloFlash_fastgFishing.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phyloFlash_fastgFishing.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phyloFlash_heatmap.R

```bash
$ singularity exec <container> /usr/local/bin/phyloFlash_heatmap.R
$ podman run --it --rm --entrypoint /usr/local/bin/phyloFlash_heatmap.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phyloFlash_heatmap.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phyloFlash_makedb.pl

```bash
$ singularity exec <container> /usr/local/bin/phyloFlash_makedb.pl
$ podman run --it --rm --entrypoint /usr/local/bin/phyloFlash_makedb.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phyloFlash_makedb.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phyloFlash_plotscript_svg.pl

```bash
$ singularity exec <container> /usr/local/bin/phyloFlash_plotscript_svg.pl
$ podman run --it --rm --entrypoint /usr/local/bin/phyloFlash_plotscript_svg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phyloFlash_plotscript_svg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmutate.sh

```bash
$ singularity exec <container> /usr/local/bin/kmutate.sh
$ podman run --it --rm --entrypoint /usr/local/bin/kmutate.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmutate.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runhmm.sh

```bash
$ singularity exec <container> /usr/local/bin/runhmm.sh
$ podman run --it --rm --entrypoint /usr/local/bin/runhmm.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runhmm.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmerposition.sh

```bash
$ singularity exec <container> /usr/local/bin/kmerposition.sh
$ podman run --it --rm --entrypoint /usr/local/bin/kmerposition.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmerposition.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reformatpb.sh

```bash
$ singularity exec <container> /usr/local/bin/reformatpb.sh
$ podman run --it --rm --entrypoint /usr/local/bin/reformatpb.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reformatpb.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### summarizecoverage.sh

```bash
$ singularity exec <container> /usr/local/bin/summarizecoverage.sh
$ podman run --it --rm --entrypoint /usr/local/bin/summarizecoverage.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/summarizecoverage.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alltoall.sh

```bash
$ singularity exec <container> /usr/local/bin/alltoall.sh
$ podman run --it --rm --entrypoint /usr/local/bin/alltoall.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alltoall.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyzesketchresults.sh

```bash
$ singularity exec <container> /usr/local/bin/analyzesketchresults.sh
$ podman run --it --rm --entrypoint /usr/local/bin/analyzesketchresults.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyzesketchresults.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### comparessu.sh

```bash
$ singularity exec <container> /usr/local/bin/comparessu.sh
$ podman run --it --rm --entrypoint /usr/local/bin/comparessu.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/comparessu.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filtersilva.sh

```bash
$ singularity exec <container> /usr/local/bin/filtersilva.sh
$ podman run --it --rm --entrypoint /usr/local/bin/filtersilva.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filtersilva.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sketchblacklist2.sh

```bash
$ singularity exec <container> /usr/local/bin/sketchblacklist2.sh
$ podman run --it --rm --entrypoint /usr/local/bin/sketchblacklist2.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sketchblacklist2.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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