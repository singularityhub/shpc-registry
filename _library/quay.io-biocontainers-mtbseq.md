---
layout: container
name:  "quay.io/biocontainers/mtbseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mtbseq/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/mtbseq/container.yaml"
updated_at: "2022-10-27 00:51:38.262557"
latest: "1.0.4--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/mtbseq"
aliases:
 - ".gatk-post-link.sh"
 - "GenomeAnalysisTK"
 - "MTBseq"
 - "gatk3"
versions:
 - "1.0.4--hdfd78af_2"
description: "shpc-registry automated BioContainers addition for mtbseq"
config: {"url": "https://biocontainers.pro/tools/mtbseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mtbseq", "latest": {"1.0.4--hdfd78af_2": "sha256:e043bc02993a7022b69f2710842108a8e3cfd87e136b252677d3e59821dd9948"}, "tags": {"1.0.4--hdfd78af_2": "sha256:e043bc02993a7022b69f2710842108a8e3cfd87e136b252677d3e59821dd9948"}, "docker": "quay.io/biocontainers/mtbseq", "aliases": {".gatk-post-link.sh": "/usr/local/bin/.gatk-post-link.sh", "GenomeAnalysisTK": "/usr/local/bin/GenomeAnalysisTK", "MTBseq": "/usr/local/bin/MTBseq", "gatk3": "/usr/local/bin/gatk3"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mtbseq.
shpc-registry automated BioContainers addition for mtbseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mtbseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mtbseq:1.0.4--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mtbseq/1.0.4--hdfd78af_2
$ module help quay.io/biocontainers/mtbseq/1.0.4--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mtbseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mtbseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mtbseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mtbseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mtbseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mtbseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .gatk-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.gatk-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.gatk-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.gatk-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GenomeAnalysisTK

```bash
$ singularity exec <container> /usr/local/bin/GenomeAnalysisTK
$ podman run --it --rm --entrypoint /usr/local/bin/GenomeAnalysisTK   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GenomeAnalysisTK   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MTBseq

```bash
$ singularity exec <container> /usr/local/bin/MTBseq
$ podman run --it --rm --entrypoint /usr/local/bin/MTBseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MTBseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gatk3

```bash
$ singularity exec <container> /usr/local/bin/gatk3
$ podman run --it --rm --entrypoint /usr/local/bin/gatk3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gatk3   -v ${PWD} -w ${PWD} <container> -c " $@"
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