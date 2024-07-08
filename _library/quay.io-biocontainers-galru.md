---
layout: container
name:  "quay.io/biocontainers/galru"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/galru/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/galru/container.yaml"
updated_at: "2024-07-08 02:40:43.808757"
latest: "1.0.0--py_0"
container_url: "https://biocontainers.pro/tools/galru"
aliases:
 - "galru"
 - "galru_create_database"
 - "galru_create_species"
 - "galru_shrink_database"
 - "mlst"
 - "ncbi-genome-download"
 - "ngd"
 - "any2fasta"
 - "fastaq"
 - "minced"
 - "FET.pl"
 - "cd-hit-clstr_2_blm8.pl"
 - "clstr_list.pl"
 - "clstr_list_sort.pl"
 - "cd-hit"
 - "cd-hit-2d"
 - "cd-hit-2d-para.pl"
versions:
 - "1.0.0--py_0"
description: "shpc-registry automated BioContainers addition for galru"
config: {"url": "https://biocontainers.pro/tools/galru", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for galru", "latest": {"1.0.0--py_0": "sha256:9c225f7c554e24791d53ad26bf2054f433f8190910c011f04181efc0db1a7129"}, "tags": {"1.0.0--py_0": "sha256:9c225f7c554e24791d53ad26bf2054f433f8190910c011f04181efc0db1a7129"}, "docker": "quay.io/biocontainers/galru", "aliases": {"galru": "/usr/local/bin/galru", "galru_create_database": "/usr/local/bin/galru_create_database", "galru_create_species": "/usr/local/bin/galru_create_species", "galru_shrink_database": "/usr/local/bin/galru_shrink_database", "mlst": "/usr/local/bin/mlst", "ncbi-genome-download": "/usr/local/bin/ncbi-genome-download", "ngd": "/usr/local/bin/ngd", "any2fasta": "/usr/local/bin/any2fasta", "fastaq": "/usr/local/bin/fastaq", "minced": "/usr/local/bin/minced", "FET.pl": "/usr/local/bin/FET.pl", "cd-hit-clstr_2_blm8.pl": "/usr/local/bin/cd-hit-clstr_2_blm8.pl", "clstr_list.pl": "/usr/local/bin/clstr_list.pl", "clstr_list_sort.pl": "/usr/local/bin/clstr_list_sort.pl", "cd-hit": "/usr/local/bin/cd-hit", "cd-hit-2d": "/usr/local/bin/cd-hit-2d", "cd-hit-2d-para.pl": "/usr/local/bin/cd-hit-2d-para.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/galru.
shpc-registry automated BioContainers addition for galru
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/galru
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/galru:1.0.0--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/galru/1.0.0--py_0
$ module help quay.io/biocontainers/galru/1.0.0--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### galru-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### galru-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### galru-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### galru-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### galru-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### galru-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### galru

```bash
$ singularity exec <container> /usr/local/bin/galru
$ podman run --it --rm --entrypoint /usr/local/bin/galru   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/galru   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### galru_create_database

```bash
$ singularity exec <container> /usr/local/bin/galru_create_database
$ podman run --it --rm --entrypoint /usr/local/bin/galru_create_database   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/galru_create_database   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### galru_create_species

```bash
$ singularity exec <container> /usr/local/bin/galru_create_species
$ podman run --it --rm --entrypoint /usr/local/bin/galru_create_species   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/galru_create_species   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### galru_shrink_database

```bash
$ singularity exec <container> /usr/local/bin/galru_shrink_database
$ podman run --it --rm --entrypoint /usr/local/bin/galru_shrink_database   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/galru_shrink_database   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mlst

```bash
$ singularity exec <container> /usr/local/bin/mlst
$ podman run --it --rm --entrypoint /usr/local/bin/mlst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mlst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncbi-genome-download

```bash
$ singularity exec <container> /usr/local/bin/ncbi-genome-download
$ podman run --it --rm --entrypoint /usr/local/bin/ncbi-genome-download   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncbi-genome-download   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngd

```bash
$ singularity exec <container> /usr/local/bin/ngd
$ podman run --it --rm --entrypoint /usr/local/bin/ngd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### any2fasta

```bash
$ singularity exec <container> /usr/local/bin/any2fasta
$ podman run --it --rm --entrypoint /usr/local/bin/any2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/any2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaq

```bash
$ singularity exec <container> /usr/local/bin/fastaq
$ podman run --it --rm --entrypoint /usr/local/bin/fastaq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minced

```bash
$ singularity exec <container> /usr/local/bin/minced
$ podman run --it --rm --entrypoint /usr/local/bin/minced   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minced   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FET.pl

```bash
$ singularity exec <container> /usr/local/bin/FET.pl
$ podman run --it --rm --entrypoint /usr/local/bin/FET.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FET.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-clstr_2_blm8.pl

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-clstr_2_blm8.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-clstr_2_blm8.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-clstr_2_blm8.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clstr_list.pl

```bash
$ singularity exec <container> /usr/local/bin/clstr_list.pl
$ podman run --it --rm --entrypoint /usr/local/bin/clstr_list.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clstr_list.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clstr_list_sort.pl

```bash
$ singularity exec <container> /usr/local/bin/clstr_list_sort.pl
$ podman run --it --rm --entrypoint /usr/local/bin/clstr_list_sort.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clstr_list_sort.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit

```bash
$ singularity exec <container> /usr/local/bin/cd-hit
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-2d

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-2d
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-2d   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-2d   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-2d-para.pl

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-2d-para.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-2d-para.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-2d-para.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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