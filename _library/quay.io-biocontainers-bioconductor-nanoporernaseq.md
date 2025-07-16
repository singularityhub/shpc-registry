---
layout: container
name:  "quay.io/biocontainers/bioconductor-nanoporernaseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-nanoporernaseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-nanoporernaseq/container.yaml"
updated_at: "2025-07-16 04:29:32.007500"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-nanoporernaseq"

versions:
 - "1.4.0--r41hdfd78af_1"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-nanoporernaseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-nanoporernaseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-nanoporernaseq", "latest": {"1.12.0--r43hdfd78af_0": "sha256:b7fbd34cf7cabdc58b491f6e7330a86e7f14fd3a96d9817428efc2f305ac7c5e"}, "tags": {"1.4.0--r41hdfd78af_1": "sha256:e80063750fa419a75450e42284a726f3385473d60d3a8e91d5444dbe56c60e2a", "1.8.0--r42hdfd78af_0": "sha256:4eeccde6a68cd68e2b102961be764942ca98c1eb243cc57a94c34b48c4ce95de", "1.10.0--r43hdfd78af_0": "sha256:34e955b8b08001bd0a27781df1865ff1794adc058b93b99b192c4208d32fd199", "1.12.0--r43hdfd78af_0": "sha256:b7fbd34cf7cabdc58b491f6e7330a86e7f14fd3a96d9817428efc2f305ac7c5e"}, "docker": "quay.io/biocontainers/bioconductor-nanoporernaseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-nanoporernaseq.
shpc-registry automated BioContainers addition for bioconductor-nanoporernaseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-nanoporernaseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-nanoporernaseq:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-nanoporernaseq/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-nanoporernaseq/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-nanoporernaseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nanoporernaseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nanoporernaseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-nanoporernaseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-nanoporernaseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-nanoporernaseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-nanoporernaseq

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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