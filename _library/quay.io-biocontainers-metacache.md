---
layout: container
name:  "quay.io/biocontainers/metacache"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metacache/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metacache/container.yaml"
updated_at: "2025-10-26 03:14:17.876935"
latest: "2.5.1--h077b44d_0"
container_url: "https://biocontainers.pro/tools/metacache"
aliases:
 - "download-ncbi-genomes"
 - "download-ncbi-taxmaps"
 - "download-ncbi-taxonomy"
 - "metacache"
 - "metacache-build-refseq"
 - "metacache-db-info"
 - "metacache-partition-genomes"
 - "summarize-results"
 - "gawk-5.1.0"
 - "awk"
 - "gawk"
 - "idn2"
 - "wget"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
versions:
 - "2.2.3--hd03093a_1"
 - "2.3.0--hd03093a_0"
 - "2.3.1--hd03093a_0"
 - "2.3.1--hdcf5f25_2"
 - "2.4.2--hdcf5f25_0"
 - "2.3.2--hdcf5f25_0"
 - "2.4.2--hdcf5f25_1"
 - "2.4.3--hdcf5f25_1"
 - "2.4.3--h077b44d_2"
 - "2.5.0--h077b44d_0"
 - "2.5.1--h077b44d_0"
description: "shpc-registry automated BioContainers addition for metacache"
config: {"url": "https://biocontainers.pro/tools/metacache", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metacache", "latest": {"2.5.1--h077b44d_0": "sha256:634a2d24b2e7ff7325be4745e2ec86a1409229b35e1e34f6a85f5c83fbdf82f7"}, "tags": {"2.2.3--hd03093a_1": "sha256:85c927d789db3e9da7d0435892d528d1c8e44d1e6e5446d4bb68c40f163739ba", "2.3.0--hd03093a_0": "sha256:52cde7d1d66fb56f98231cfd5d1e6bebabdda0136e974da80e9ca1e07e4a24b2", "2.3.1--hd03093a_0": "sha256:896d1f572bd3e70f6e480f47b61f9db18084dcbbf47ccbdfee01abea6e6f676d", "2.3.1--hdcf5f25_2": "sha256:85868a624ce8924e5c2f4c842ef4e8ded508a08dd028d29f3df7c562799b66cf", "2.4.2--hdcf5f25_0": "sha256:d3ffe0825c196d3c462148fbaab1185a8b91119d6d5d295a8b8fb2a50ae44bea", "2.3.2--hdcf5f25_0": "sha256:7246beb62a79d2b849d041fcefb5f46280844baa26d302a0002a4300c2d74439", "2.4.2--hdcf5f25_1": "sha256:b72244e761027b2f7bcfc10c1142761f30a13ab30ec981fc8368245d5e13bc34", "2.4.3--hdcf5f25_1": "sha256:3cdb9168fbf88a80b1811ea3851035890227058bfdddc2986c57620c1ea6f502", "2.4.3--h077b44d_2": "sha256:8dd33bab13d03f3620830deea70ad9e797e5e38992af409cbd909b11902f77c6", "2.5.0--h077b44d_0": "sha256:5619ea0dd9e5b576731435a9fb5bef28f9f4361f7263b3dd39afde83ccf3b45d", "2.5.1--h077b44d_0": "sha256:634a2d24b2e7ff7325be4745e2ec86a1409229b35e1e34f6a85f5c83fbdf82f7"}, "docker": "quay.io/biocontainers/metacache", "aliases": {"download-ncbi-genomes": "/usr/local/bin/download-ncbi-genomes", "download-ncbi-taxmaps": "/usr/local/bin/download-ncbi-taxmaps", "download-ncbi-taxonomy": "/usr/local/bin/download-ncbi-taxonomy", "metacache": "/usr/local/bin/metacache", "metacache-build-refseq": "/usr/local/bin/metacache-build-refseq", "metacache-db-info": "/usr/local/bin/metacache-db-info", "metacache-partition-genomes": "/usr/local/bin/metacache-partition-genomes", "summarize-results": "/usr/local/bin/summarize-results", "gawk-5.1.0": "/usr/local/bin/gawk-5.1.0", "awk": "/usr/local/bin/awk", "gawk": "/usr/local/bin/gawk", "idn2": "/usr/local/bin/idn2", "wget": "/usr/local/bin/wget", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metacache.
shpc-registry automated BioContainers addition for metacache
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metacache
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metacache:2.5.1--h077b44d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metacache/2.5.1--h077b44d_0
$ module help quay.io/biocontainers/metacache/2.5.1--h077b44d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metacache-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metacache-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metacache-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metacache-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metacache-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metacache-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### download-ncbi-genomes

```bash
$ singularity exec <container> /usr/local/bin/download-ncbi-genomes
$ podman run --it --rm --entrypoint /usr/local/bin/download-ncbi-genomes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download-ncbi-genomes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download-ncbi-taxmaps

```bash
$ singularity exec <container> /usr/local/bin/download-ncbi-taxmaps
$ podman run --it --rm --entrypoint /usr/local/bin/download-ncbi-taxmaps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download-ncbi-taxmaps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download-ncbi-taxonomy

```bash
$ singularity exec <container> /usr/local/bin/download-ncbi-taxonomy
$ podman run --it --rm --entrypoint /usr/local/bin/download-ncbi-taxonomy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download-ncbi-taxonomy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metacache

```bash
$ singularity exec <container> /usr/local/bin/metacache
$ podman run --it --rm --entrypoint /usr/local/bin/metacache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metacache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metacache-build-refseq

```bash
$ singularity exec <container> /usr/local/bin/metacache-build-refseq
$ podman run --it --rm --entrypoint /usr/local/bin/metacache-build-refseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metacache-build-refseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metacache-db-info

```bash
$ singularity exec <container> /usr/local/bin/metacache-db-info
$ podman run --it --rm --entrypoint /usr/local/bin/metacache-db-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metacache-db-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metacache-partition-genomes

```bash
$ singularity exec <container> /usr/local/bin/metacache-partition-genomes
$ podman run --it --rm --entrypoint /usr/local/bin/metacache-partition-genomes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metacache-partition-genomes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### summarize-results

```bash
$ singularity exec <container> /usr/local/bin/summarize-results
$ podman run --it --rm --entrypoint /usr/local/bin/summarize-results   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/summarize-results   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.1.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### awk

```bash
$ singularity exec <container> /usr/local/bin/awk
$ podman run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk

```bash
$ singularity exec <container> /usr/local/bin/gawk
$ podman run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idn2

```bash
$ singularity exec <container> /usr/local/bin/idn2
$ podman run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2-config

```bash
$ singularity exec <container> /usr/local/bin/python2-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7-config

```bash
$ singularity exec <container> /usr/local/bin/python2.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2

```bash
$ singularity exec <container> /usr/local/bin/python2
$ podman run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7

```bash
$ singularity exec <container> /usr/local/bin/python2.7
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle

```bash
$ singularity exec <container> /usr/local/bin/idle
$ podman run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
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