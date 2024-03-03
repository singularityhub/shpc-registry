---
layout: container
name:  "quay.io/biocontainers/bioconductor-all"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-all/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-all/container.yaml"
updated_at: "2024-03-03 02:34:37.389083"
latest: "1.44.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-all"

versions:
 - "1.36.0--r41hdfd78af_1"
 - "1.40.0--r42hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
 - "1.44.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-all"
config: {"url": "https://biocontainers.pro/tools/bioconductor-all", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-all", "latest": {"1.44.0--r43hdfd78af_0": "sha256:e6db8ca4fb223b35c04ab339b3400703ae6ef61eb67425e5cc2e3ff2767e4d37"}, "tags": {"1.36.0--r41hdfd78af_1": "sha256:e54f51e777e71d85e8477a906600ff3c12aedac42d7c3483632a7cc6102d8992", "1.40.0--r42hdfd78af_0": "sha256:f38ab64b3e5985ada6270bad422c657c177eccadc9838b58e2815def627b3c2a", "1.42.0--r43hdfd78af_0": "sha256:ac0fc046f38bf4ae9483b7014fe59474832fba6cc98b7f1f3287528657f91bb7", "1.44.0--r43hdfd78af_0": "sha256:e6db8ca4fb223b35c04ab339b3400703ae6ef61eb67425e5cc2e3ff2767e4d37"}, "docker": "quay.io/biocontainers/bioconductor-all"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-all.
shpc-registry automated BioContainers addition for bioconductor-all
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-all
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-all:1.44.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-all/1.44.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-all/1.44.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-all-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-all-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-all-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-all-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-all-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-all-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-all

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