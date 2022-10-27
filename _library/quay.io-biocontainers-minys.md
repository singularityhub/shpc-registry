---
layout: container
name:  "quay.io/biocontainers/minys"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/minys/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/minys/container.yaml"
updated_at: "2022-10-27 00:31:29.338454"
latest: "1.1--h9f5acd7_4"
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
versions:
 - "1.1--h9f5acd7_4"
description: "shpc-registry automated BioContainers addition for minys"
config: {"url": "https://biocontainers.pro/tools/minys", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for minys", "latest": {"1.1--h9f5acd7_4": "sha256:62ef23cefa617cb10ed631d5633d166f2766159a620d00e778bb674b3e79d67b"}, "tags": {"1.1--h9f5acd7_4": "sha256:62ef23cefa617cb10ed631d5633d166f2766159a620d00e778bb674b3e79d67b"}, "docker": "quay.io/biocontainers/minys", "aliases": {"MinYS.py": "/usr/local/bin/MinYS.py", "MindTheGap": "/usr/local/bin/MindTheGap", "average_nucleotide_identity.py": "/usr/local/bin/average_nucleotide_identity.py", "dbgh5": "/usr/local/bin/dbgh5", "dbginfo": "/usr/local/bin/dbginfo", "delta_filter_wrapper.py": "/usr/local/bin/delta_filter_wrapper.py", "enumerate_paths.py": "/usr/local/bin/enumerate_paths.py", "filter_components.py": "/usr/local/bin/filter_components.py", "gatb-h5dump": "/usr/local/bin/gatb-h5dump", "genbank_get_genomes_by_taxon.py": "/usr/local/bin/genbank_get_genomes_by_taxon.py", "graph_simplification.py": "/usr/local/bin/graph_simplification.py", "merci": "/usr/local/bin/merci", "minia": "/usr/local/bin/minia"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/minys.
shpc-registry automated BioContainers addition for minys
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/minys
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/minys:1.1--h9f5acd7_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/minys/1.1--h9f5acd7_4
$ module help quay.io/biocontainers/minys/1.1--h9f5acd7_4
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