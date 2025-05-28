---
layout: container
name:  "quay.io/biocontainers/hapcut2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hapcut2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hapcut2/container.yaml"
updated_at: "2025-05-28 03:26:24.138662"
latest: "1.3.4--h577a1d6_1"
container_url: "https://biocontainers.pro/tools/hapcut2"
aliases:
 - "HAPCUT2"
 - "LinkFragments.py"
 - "calculate_haplotype_statistics.py"
 - "extractHAIRS"
 - "hapcut2"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "1.3.3--hb0d9459_3"
 - "1.3.3--hc88714e_4"
 - "1.3.3--h6141fd1_5"
 - "1.3.4--he4a0461_0"
 - "1.3.4--h577a1d6_1"
description: "shpc-registry automated BioContainers addition for hapcut2"
config: {"url": "https://biocontainers.pro/tools/hapcut2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hapcut2", "latest": {"1.3.4--h577a1d6_1": "sha256:77f1e880224163270af693076a7ed525dac03c27e700eec210c3699cbad43897"}, "tags": {"1.3.3--hb0d9459_3": "sha256:40f48104f97e5a17d14c9deece97b7ce5f006e09a1bd78c6d058d23ed7e08d7c", "1.3.3--hc88714e_4": "sha256:ce67ba04c780abb3a02c294480a815919022fddebd98ec7a7af8b7835b497880", "1.3.3--h6141fd1_5": "sha256:4d7caef6482b10e82d5648eaeb5d3f1a4f7bca313e47b5cd09d02f1f191fa74e", "1.3.4--he4a0461_0": "sha256:499fc79e1dfdb84b2620ce036651d2ba92c321755d595fdb39022b7517463a89", "1.3.4--h577a1d6_1": "sha256:77f1e880224163270af693076a7ed525dac03c27e700eec210c3699cbad43897"}, "docker": "quay.io/biocontainers/hapcut2", "aliases": {"HAPCUT2": "/usr/local/bin/HAPCUT2", "LinkFragments.py": "/usr/local/bin/LinkFragments.py", "calculate_haplotype_statistics.py": "/usr/local/bin/calculate_haplotype_statistics.py", "extractHAIRS": "/usr/local/bin/extractHAIRS", "hapcut2": "/usr/local/bin/hapcut2", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hapcut2.
shpc-registry automated BioContainers addition for hapcut2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hapcut2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hapcut2:1.3.4--h577a1d6_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hapcut2/1.3.4--h577a1d6_1
$ module help quay.io/biocontainers/hapcut2/1.3.4--h577a1d6_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hapcut2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hapcut2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hapcut2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hapcut2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hapcut2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hapcut2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### HAPCUT2

```bash
$ singularity exec <container> /usr/local/bin/HAPCUT2
$ podman run --it --rm --entrypoint /usr/local/bin/HAPCUT2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HAPCUT2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LinkFragments.py

```bash
$ singularity exec <container> /usr/local/bin/LinkFragments.py
$ podman run --it --rm --entrypoint /usr/local/bin/LinkFragments.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LinkFragments.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### calculate_haplotype_statistics.py

```bash
$ singularity exec <container> /usr/local/bin/calculate_haplotype_statistics.py
$ podman run --it --rm --entrypoint /usr/local/bin/calculate_haplotype_statistics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/calculate_haplotype_statistics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extractHAIRS

```bash
$ singularity exec <container> /usr/local/bin/extractHAIRS
$ podman run --it --rm --entrypoint /usr/local/bin/extractHAIRS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extractHAIRS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hapcut2

```bash
$ singularity exec <container> /usr/local/bin/hapcut2
$ podman run --it --rm --entrypoint /usr/local/bin/hapcut2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hapcut2   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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