---
layout: container
name:  "quay.io/biocontainers/bioconductor-tartare"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tartare/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tartare/container.yaml"
updated_at: "2023-10-24 03:00:09.559721"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tartare"

versions:
 - "1.8.0--r41hdfd78af_1"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tartare"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tartare", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tartare", "latest": {"1.14.0--r43hdfd78af_0": "sha256:d6e42574082fcd870a2dd69401faf2dae99ea4801cc4d5d395f4eec47a386893"}, "tags": {"1.8.0--r41hdfd78af_1": "sha256:72c99c967fb892ed3c7ba2988b89a2e138a24013c2c3b5293f5f62199e5a1822", "1.12.0--r42hdfd78af_0": "sha256:bc94dad95643989f00f949c7658967dba9244e24b3aa0f2ff0c8f4a387826920", "1.14.0--r43hdfd78af_0": "sha256:d6e42574082fcd870a2dd69401faf2dae99ea4801cc4d5d395f4eec47a386893"}, "docker": "quay.io/biocontainers/bioconductor-tartare"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tartare.
shpc-registry automated BioContainers addition for bioconductor-tartare
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tartare
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tartare:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tartare/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tartare/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tartare-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tartare-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tartare-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tartare-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tartare-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tartare-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tartare

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