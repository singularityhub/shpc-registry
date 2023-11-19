---
layout: container
name:  "quay.io/biocontainers/bioconductor-methylaid"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-methylaid/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-methylaid/container.yaml"
updated_at: "2023-11-19 03:06:32.240020"
latest: "1.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-methylaid"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-methylaid"
config: {"url": "https://biocontainers.pro/tools/bioconductor-methylaid", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-methylaid", "latest": {"1.34.0--r43hdfd78af_0": "sha256:fd21d77e7c018908192cdbafc803852c962a35f060066ca6c9bbf80e3a709294"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:b5723528c2c8be82b958584fcfa238ec5fa991f0e95ad0b8c1a2022582ef6611", "1.32.0--r42hdfd78af_0": "sha256:c8008ddbc4b820ccc5cd49758dd45ef2bb7c75efe470ae17c01fda6f907d8d39", "1.34.0--r43hdfd78af_0": "sha256:fd21d77e7c018908192cdbafc803852c962a35f060066ca6c9bbf80e3a709294"}, "docker": "quay.io/biocontainers/bioconductor-methylaid"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-methylaid.
shpc-registry automated BioContainers addition for bioconductor-methylaid
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-methylaid
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-methylaid:1.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-methylaid/1.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-methylaid/1.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-methylaid-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methylaid-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methylaid-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-methylaid-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-methylaid-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-methylaid-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-methylaid

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