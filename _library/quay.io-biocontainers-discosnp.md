---
layout: container
name:  "quay.io/biocontainers/discosnp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/discosnp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/discosnp/container.yaml"
updated_at: "2023-08-20 03:04:29.076528"
latest: "2.6.2--h43eeafb_3"
container_url: "https://biocontainers.pro/tools/discosnp"
aliases:
 - "SRC_counter"
 - "SRC_linker_ram"
 - "dbgh5"
 - "dsk"
 - "dsk2ascii"
 - "extract_reads_from_bv"
 - "generate_bv"
 - "kissnp2"
 - "kissreads2"
 - "quick_hierarchical_clustering"
 - "read_file_names"
 - "run_discoSnp++.sh"
 - "run_discoSnp++_ML.sh"
 - "run_discoSnpRad.sh"
 - "short_read_connector.sh"
 - "qualfa2fq.pl"
 - "xa2multi.pl"
 - "bwa"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
 - "h5cc"
versions:
 - "2.6.2--h5b5514e_1"
 - "2.6.2--h43eeafb_3"
description: "shpc-registry automated BioContainers addition for discosnp"
config: {"url": "https://biocontainers.pro/tools/discosnp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for discosnp", "latest": {"2.6.2--h43eeafb_3": "sha256:9b27ccf463c966eae32d2e7bfb809934113ad4e054c4659083a0a6912d09b346"}, "tags": {"2.6.2--h5b5514e_1": "sha256:625b8bc040cb5fe5acc7738ae8af97e71e2beed24ebef730e2e636427db202a0", "2.6.2--h43eeafb_3": "sha256:9b27ccf463c966eae32d2e7bfb809934113ad4e054c4659083a0a6912d09b346"}, "docker": "quay.io/biocontainers/discosnp", "aliases": {"SRC_counter": "/usr/local/bin/SRC_counter", "SRC_linker_ram": "/usr/local/bin/SRC_linker_ram", "dbgh5": "/usr/local/bin/dbgh5", "dsk": "/usr/local/bin/dsk", "dsk2ascii": "/usr/local/bin/dsk2ascii", "extract_reads_from_bv": "/usr/local/bin/extract_reads_from_bv", "generate_bv": "/usr/local/bin/generate_bv", "kissnp2": "/usr/local/bin/kissnp2", "kissreads2": "/usr/local/bin/kissreads2", "quick_hierarchical_clustering": "/usr/local/bin/quick_hierarchical_clustering", "read_file_names": "/usr/local/bin/read_file_names", "run_discoSnp++.sh": "/usr/local/bin/run_discoSnp++.sh", "run_discoSnp++_ML.sh": "/usr/local/bin/run_discoSnp++_ML.sh", "run_discoSnpRad.sh": "/usr/local/bin/run_discoSnpRad.sh", "short_read_connector.sh": "/usr/local/bin/short_read_connector.sh", "qualfa2fq.pl": "/usr/local/bin/qualfa2fq.pl", "xa2multi.pl": "/usr/local/bin/xa2multi.pl", "bwa": "/usr/local/bin/bwa", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "h5cc": "/usr/local/bin/h5cc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/discosnp.
shpc-registry automated BioContainers addition for discosnp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/discosnp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/discosnp:2.6.2--h43eeafb_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/discosnp/2.6.2--h43eeafb_3
$ module help quay.io/biocontainers/discosnp/2.6.2--h43eeafb_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### discosnp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### discosnp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### discosnp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### discosnp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### discosnp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### discosnp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SRC_counter

```bash
$ singularity exec <container> /usr/local/bin/SRC_counter
$ podman run --it --rm --entrypoint /usr/local/bin/SRC_counter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SRC_counter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SRC_linker_ram

```bash
$ singularity exec <container> /usr/local/bin/SRC_linker_ram
$ podman run --it --rm --entrypoint /usr/local/bin/SRC_linker_ram   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SRC_linker_ram   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbgh5

```bash
$ singularity exec <container> /usr/local/bin/dbgh5
$ podman run --it --rm --entrypoint /usr/local/bin/dbgh5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbgh5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dsk

```bash
$ singularity exec <container> /usr/local/bin/dsk
$ podman run --it --rm --entrypoint /usr/local/bin/dsk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dsk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dsk2ascii

```bash
$ singularity exec <container> /usr/local/bin/dsk2ascii
$ podman run --it --rm --entrypoint /usr/local/bin/dsk2ascii   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dsk2ascii   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_reads_from_bv

```bash
$ singularity exec <container> /usr/local/bin/extract_reads_from_bv
$ podman run --it --rm --entrypoint /usr/local/bin/extract_reads_from_bv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_reads_from_bv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_bv

```bash
$ singularity exec <container> /usr/local/bin/generate_bv
$ podman run --it --rm --entrypoint /usr/local/bin/generate_bv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_bv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kissnp2

```bash
$ singularity exec <container> /usr/local/bin/kissnp2
$ podman run --it --rm --entrypoint /usr/local/bin/kissnp2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kissnp2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kissreads2

```bash
$ singularity exec <container> /usr/local/bin/kissreads2
$ podman run --it --rm --entrypoint /usr/local/bin/kissreads2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kissreads2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quick_hierarchical_clustering

```bash
$ singularity exec <container> /usr/local/bin/quick_hierarchical_clustering
$ podman run --it --rm --entrypoint /usr/local/bin/quick_hierarchical_clustering   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quick_hierarchical_clustering   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### read_file_names

```bash
$ singularity exec <container> /usr/local/bin/read_file_names
$ podman run --it --rm --entrypoint /usr/local/bin/read_file_names   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/read_file_names   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_discoSnp++.sh

```bash
$ singularity exec <container> /usr/local/bin/run_discoSnp++.sh
$ podman run --it --rm --entrypoint /usr/local/bin/run_discoSnp++.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_discoSnp++.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_discoSnp++_ML.sh

```bash
$ singularity exec <container> /usr/local/bin/run_discoSnp++_ML.sh
$ podman run --it --rm --entrypoint /usr/local/bin/run_discoSnp++_ML.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_discoSnp++_ML.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_discoSnpRad.sh

```bash
$ singularity exec <container> /usr/local/bin/run_discoSnpRad.sh
$ podman run --it --rm --entrypoint /usr/local/bin/run_discoSnpRad.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_discoSnpRad.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### short_read_connector.sh

```bash
$ singularity exec <container> /usr/local/bin/short_read_connector.sh
$ podman run --it --rm --entrypoint /usr/local/bin/short_read_connector.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/short_read_connector.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qualfa2fq.pl

```bash
$ singularity exec <container> /usr/local/bin/qualfa2fq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/qualfa2fq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qualfa2fq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xa2multi.pl

```bash
$ singularity exec <container> /usr/local/bin/xa2multi.pl
$ podman run --it --rm --entrypoint /usr/local/bin/xa2multi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xa2multi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa

```bash
$ singularity exec <container> /usr/local/bin/bwa
$ podman run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5cc

```bash
$ singularity exec <container> /usr/local/bin/h5cc
$ podman run --it --rm --entrypoint /usr/local/bin/h5cc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5cc   -v ${PWD} -w ${PWD} <container> -c " $@"
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