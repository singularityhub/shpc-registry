---
layout: container
name:  "quay.io/biocontainers/bioconductor-keggandmetacoredzpathwaysgeo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-keggandmetacoredzpathwaysgeo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-keggandmetacoredzpathwaysgeo/container.yaml"
updated_at: "2023-11-25 02:57:25.492554"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-keggandmetacoredzpathwaysgeo"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
 - "c89"
 - "c99"
versions:
 - "1.9.0--r40_0"
 - "1.18.0--r42hdfd78af_0"
 - "1.14.0--r41hdfd78af_1"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r40hdfd78af_1"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-keggandmetacoredzpathwaysgeo"
config: {"url": "https://biocontainers.pro/tools/bioconductor-keggandmetacoredzpathwaysgeo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-keggandmetacoredzpathwaysgeo", "latest": {"1.20.0--r43hdfd78af_0": "sha256:c945420436b644d5dc52e7700d8a156dfa0285c8bf1b014b167d11198b520bfa"}, "tags": {"1.9.0--r40_0": "sha256:f1d718a90b99123199ab8673e855e07727de2dce9e4970c2440cba4f00e94d89", "1.18.0--r42hdfd78af_0": "sha256:8383c6b4258973544612d184e6dc1776e0785f1e1786d3391a5675b1c73b5f9e", "1.14.0--r41hdfd78af_1": "sha256:69527d5a39f1cdc65e47085a7fb058970c5b62d3742ea914109434f4147a1c25", "1.12.0--r41hdfd78af_0": "sha256:1d3dd48612b5543d68a64636b2f5166ac1e9e837ada5357e1e3a88221ac2c5f9", "1.10.0--r40hdfd78af_1": "sha256:56323c78628db30bba3c8b53ec9331e7dec549e3a89941589b23b112e6de1a3c", "1.20.0--r43hdfd78af_0": "sha256:c945420436b644d5dc52e7700d8a156dfa0285c8bf1b014b167d11198b520bfa"}, "docker": "quay.io/biocontainers/bioconductor-keggandmetacoredzpathwaysgeo", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-keggandmetacoredzpathwaysgeo.
shpc-registry automated BioContainers addition for bioconductor-keggandmetacoredzpathwaysgeo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-keggandmetacoredzpathwaysgeo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-keggandmetacoredzpathwaysgeo:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-keggandmetacoredzpathwaysgeo/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-keggandmetacoredzpathwaysgeo/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-keggandmetacoredzpathwaysgeo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-keggandmetacoredzpathwaysgeo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-keggandmetacoredzpathwaysgeo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-keggandmetacoredzpathwaysgeo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-keggandmetacoredzpathwaysgeo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-keggandmetacoredzpathwaysgeo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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