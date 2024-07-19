---
layout: container
name:  "quay.io/biocontainers/minys"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/minys/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/minys/container.yaml"
updated_at: "2024-07-19 03:17:59.663084"
latest: "1.1--h4ac6f70_5"
container_url: "https://biocontainers.pro/tools/minys"
aliases:
 - "MinYS.py"
 - "MindTheGap"
 - "average_nucleotide_identity.py"
 - "dbgh5"
 - "dbginfo"
 - "delta_filter_wrapper.py"
 - "enumerate_paths.py"
 - "filter_components.py"
 - "gatb-h5dump"
 - "genbank_get_genomes_by_taxon.py"
 - "graph_simplification.py"
 - "merci"
 - "minia"
 - "bl2seq"
 - "blastall"
 - "blastclust"
 - "blastpgp"
 - "copymat"
 - "fastacmd"
 - "formatdb"
 - "formatrpsdb"
 - "impala"
 - "makemat"
versions:
 - "1.1--h9f5acd7_4"
 - "1.1--h4ac6f70_5"
description: "shpc-registry automated BioContainers addition for minys"
config: {"url": "https://biocontainers.pro/tools/minys", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for minys", "latest": {"1.1--h4ac6f70_5": "sha256:5bfe5cf2e3780683c95eeec83fb3e6bcd71a4b57c681049639cec6d652c21f27"}, "tags": {"1.1--h9f5acd7_4": "sha256:62ef23cefa617cb10ed631d5633d166f2766159a620d00e778bb674b3e79d67b", "1.1--h4ac6f70_5": "sha256:5bfe5cf2e3780683c95eeec83fb3e6bcd71a4b57c681049639cec6d652c21f27"}, "docker": "quay.io/biocontainers/minys", "aliases": {"MinYS.py": "/usr/local/bin/MinYS.py", "MindTheGap": "/usr/local/bin/MindTheGap", "average_nucleotide_identity.py": "/usr/local/bin/average_nucleotide_identity.py", "dbgh5": "/usr/local/bin/dbgh5", "dbginfo": "/usr/local/bin/dbginfo", "delta_filter_wrapper.py": "/usr/local/bin/delta_filter_wrapper.py", "enumerate_paths.py": "/usr/local/bin/enumerate_paths.py", "filter_components.py": "/usr/local/bin/filter_components.py", "gatb-h5dump": "/usr/local/bin/gatb-h5dump", "genbank_get_genomes_by_taxon.py": "/usr/local/bin/genbank_get_genomes_by_taxon.py", "graph_simplification.py": "/usr/local/bin/graph_simplification.py", "merci": "/usr/local/bin/merci", "minia": "/usr/local/bin/minia", "bl2seq": "/usr/local/bin/bl2seq", "blastall": "/usr/local/bin/blastall", "blastclust": "/usr/local/bin/blastclust", "blastpgp": "/usr/local/bin/blastpgp", "copymat": "/usr/local/bin/copymat", "fastacmd": "/usr/local/bin/fastacmd", "formatdb": "/usr/local/bin/formatdb", "formatrpsdb": "/usr/local/bin/formatrpsdb", "impala": "/usr/local/bin/impala", "makemat": "/usr/local/bin/makemat"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/minys.
shpc-registry automated BioContainers addition for minys
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/minys
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/minys:1.1--h4ac6f70_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/minys/1.1--h4ac6f70_5
$ module help quay.io/biocontainers/minys/1.1--h4ac6f70_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### minys-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### minys-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### minys-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### minys-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### minys-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### minys-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MinYS.py

```bash
$ singularity exec <container> /usr/local/bin/MinYS.py
$ podman run --it --rm --entrypoint /usr/local/bin/MinYS.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MinYS.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MindTheGap

```bash
$ singularity exec <container> /usr/local/bin/MindTheGap
$ podman run --it --rm --entrypoint /usr/local/bin/MindTheGap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MindTheGap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### average_nucleotide_identity.py

```bash
$ singularity exec <container> /usr/local/bin/average_nucleotide_identity.py
$ podman run --it --rm --entrypoint /usr/local/bin/average_nucleotide_identity.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/average_nucleotide_identity.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbgh5

```bash
$ singularity exec <container> /usr/local/bin/dbgh5
$ podman run --it --rm --entrypoint /usr/local/bin/dbgh5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbgh5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbginfo

```bash
$ singularity exec <container> /usr/local/bin/dbginfo
$ podman run --it --rm --entrypoint /usr/local/bin/dbginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### delta_filter_wrapper.py

```bash
$ singularity exec <container> /usr/local/bin/delta_filter_wrapper.py
$ podman run --it --rm --entrypoint /usr/local/bin/delta_filter_wrapper.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delta_filter_wrapper.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### enumerate_paths.py

```bash
$ singularity exec <container> /usr/local/bin/enumerate_paths.py
$ podman run --it --rm --entrypoint /usr/local/bin/enumerate_paths.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/enumerate_paths.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_components.py

```bash
$ singularity exec <container> /usr/local/bin/filter_components.py
$ podman run --it --rm --entrypoint /usr/local/bin/filter_components.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_components.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gatb-h5dump

```bash
$ singularity exec <container> /usr/local/bin/gatb-h5dump
$ podman run --it --rm --entrypoint /usr/local/bin/gatb-h5dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gatb-h5dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genbank_get_genomes_by_taxon.py

```bash
$ singularity exec <container> /usr/local/bin/genbank_get_genomes_by_taxon.py
$ podman run --it --rm --entrypoint /usr/local/bin/genbank_get_genomes_by_taxon.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genbank_get_genomes_by_taxon.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### graph_simplification.py

```bash
$ singularity exec <container> /usr/local/bin/graph_simplification.py
$ podman run --it --rm --entrypoint /usr/local/bin/graph_simplification.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/graph_simplification.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merci

```bash
$ singularity exec <container> /usr/local/bin/merci
$ podman run --it --rm --entrypoint /usr/local/bin/merci   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merci   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minia

```bash
$ singularity exec <container> /usr/local/bin/minia
$ podman run --it --rm --entrypoint /usr/local/bin/minia   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minia   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bl2seq

```bash
$ singularity exec <container> /usr/local/bin/bl2seq
$ podman run --it --rm --entrypoint /usr/local/bin/bl2seq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bl2seq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastall

```bash
$ singularity exec <container> /usr/local/bin/blastall
$ podman run --it --rm --entrypoint /usr/local/bin/blastall   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastall   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastclust

```bash
$ singularity exec <container> /usr/local/bin/blastclust
$ podman run --it --rm --entrypoint /usr/local/bin/blastclust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastclust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastpgp

```bash
$ singularity exec <container> /usr/local/bin/blastpgp
$ podman run --it --rm --entrypoint /usr/local/bin/blastpgp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastpgp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### copymat

```bash
$ singularity exec <container> /usr/local/bin/copymat
$ podman run --it --rm --entrypoint /usr/local/bin/copymat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/copymat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastacmd

```bash
$ singularity exec <container> /usr/local/bin/fastacmd
$ podman run --it --rm --entrypoint /usr/local/bin/fastacmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastacmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### formatdb

```bash
$ singularity exec <container> /usr/local/bin/formatdb
$ podman run --it --rm --entrypoint /usr/local/bin/formatdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/formatdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### formatrpsdb

```bash
$ singularity exec <container> /usr/local/bin/formatrpsdb
$ podman run --it --rm --entrypoint /usr/local/bin/formatrpsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/formatrpsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### impala

```bash
$ singularity exec <container> /usr/local/bin/impala
$ podman run --it --rm --entrypoint /usr/local/bin/impala   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/impala   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makemat

```bash
$ singularity exec <container> /usr/local/bin/makemat
$ podman run --it --rm --entrypoint /usr/local/bin/makemat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makemat   -v ${PWD} -w ${PWD} <container> -c " $@"
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