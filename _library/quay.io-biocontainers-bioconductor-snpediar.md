---
layout: container
name:  "quay.io/biocontainers/bioconductor-snpediar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-snpediar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-snpediar/container.yaml"
updated_at: "2024-02-25 02:38:47.635859"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-snpediar"
aliases:
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-snpediar"
config: {"url": "https://biocontainers.pro/tools/bioconductor-snpediar", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-snpediar", "latest": {"1.28.0--r43hdfd78af_0": "sha256:574024ed8def73076cc4f48fe2a4ff13cb647995a319fe7e53bf8e04573ac34e"}, "tags": {"1.8.0--r351_0": "sha256:ce2227d687c01576789838b40782a86288397ae84c6af49abf2f1629dff16211", "1.24.0--r42hdfd78af_0": "sha256:b8fddde3deacfe63c6eea6296bf5a88150af18bfc1ff97f15c335311b59fbdd7", "1.20.0--r41hdfd78af_0": "sha256:e43580184dd81661d479c46ba9b7511eed9fb76420234e40f197ab557a225ea3", "1.18.0--r41hdfd78af_0": "sha256:5e9f99ff1561c5ddcb64b66b68cad0362a7ebf83315b3e882d78c7dd16aa2759", "1.16.0--r40hdfd78af_1": "sha256:9313289e13a6d3b0c5b9f93fe3181645dfc052a5c5b8a1cf567873a25dd63877", "1.14.0--r40_0": "sha256:98ecb755a0bc173c5e4bd8ef103ece0f956922dbca7ba1da77e2966b85328b19", "1.26.0--r43hdfd78af_0": "sha256:f7918226927fcf646e7fa7a03570e90e077db4b96c2e63f62e180a27f3554be4", "1.28.0--r43hdfd78af_0": "sha256:574024ed8def73076cc4f48fe2a4ff13cb647995a319fe7e53bf8e04573ac34e"}, "docker": "quay.io/biocontainers/bioconductor-snpediar", "aliases": {"c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-snpediar.
shpc-registry automated BioContainers addition for bioconductor-snpediar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-snpediar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-snpediar:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-snpediar/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-snpediar/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-snpediar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-snpediar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-snpediar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-snpediar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-snpediar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-snpediar-inspect-deffile:

```bash
$ singularity inspect -d <container>
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