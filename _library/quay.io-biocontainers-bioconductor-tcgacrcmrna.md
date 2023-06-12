---
layout: container
name:  "quay.io/biocontainers/bioconductor-tcgacrcmrna"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tcgacrcmrna/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tcgacrcmrna/container.yaml"
updated_at: "2023-06-12 04:54:20.812837"
latest: "1.18.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tcgacrcmrna"
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
description: "shpc-registry automated BioContainers addition for bioconductor-tcgacrcmrna"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tcgacrcmrna", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tcgacrcmrna", "latest": {"1.18.0--r42hdfd78af_0": "sha256:068c62f7f5f38c4e93155f219079779fb7141a58f17a759dfeed685574f20932"}, "tags": {"1.9.0--r40_0": "sha256:5443dfe2ac3f2398959cce08325a870fff818701829339a5ee9f3e9762607150", "1.18.0--r42hdfd78af_0": "sha256:068c62f7f5f38c4e93155f219079779fb7141a58f17a759dfeed685574f20932", "1.14.0--r41hdfd78af_1": "sha256:e44f7564735d6405e5fba6a46ceb9b5803a59d333df4c3b618cbb2617c173269", "1.12.0--r41hdfd78af_0": "sha256:0d6539fb199090807999609828b31d8ce0979fd377860201486c9c25b7d40b8f", "1.10.0--r40hdfd78af_1": "sha256:7ec47cd77f25483a0a43e6bfa11a4d00180a1fed4b2eb14081b40b8edd6717ed"}, "docker": "quay.io/biocontainers/bioconductor-tcgacrcmrna", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tcgacrcmrna.
shpc-registry automated BioContainers addition for bioconductor-tcgacrcmrna
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tcgacrcmrna
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tcgacrcmrna:1.18.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tcgacrcmrna/1.18.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tcgacrcmrna/1.18.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tcgacrcmrna-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tcgacrcmrna-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tcgacrcmrna-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tcgacrcmrna-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tcgacrcmrna-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tcgacrcmrna-inspect-deffile:

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