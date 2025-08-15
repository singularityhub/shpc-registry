---
layout: container
name:  "quay.io/biocontainers/bioconductor-spatialdmelxsim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-spatialdmelxsim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-spatialdmelxsim/container.yaml"
updated_at: "2025-08-15 03:48:09.184721"
latest: "1.12.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-spatialdmelxsim"

versions:
 - "1.0.0--r41hdfd78af_1"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.1--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.12.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-spatialdmelxsim"
config: {"url": "https://biocontainers.pro/tools/bioconductor-spatialdmelxsim", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-spatialdmelxsim", "latest": {"1.12.0--r44hdfd78af_0": "sha256:2d1c88cb88600962644369dc26995301f7cf35a0779fdc64ef64b961d90347e0"}, "tags": {"1.0.0--r41hdfd78af_1": "sha256:5686f39ea070aeef48630512f6554086c61a850830bfd1e16f3b41408ba1b687", "1.4.0--r42hdfd78af_0": "sha256:49875f04b5f1c039c937ae3eefff436beeed60b002ea77281075e32fac07715d", "1.6.1--r43hdfd78af_0": "sha256:34862d36d2032f3dc62cba46797841d7ff9e0648f2ff2e311290edd383e2b200", "1.8.0--r43hdfd78af_0": "sha256:73f65a7ffca1779e7d076bb73d204fc42cd4815884254b7f9b7915f867ee90e7", "1.12.0--r44hdfd78af_0": "sha256:2d1c88cb88600962644369dc26995301f7cf35a0779fdc64ef64b961d90347e0"}, "docker": "quay.io/biocontainers/bioconductor-spatialdmelxsim"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-spatialdmelxsim.
shpc-registry automated BioContainers addition for bioconductor-spatialdmelxsim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-spatialdmelxsim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-spatialdmelxsim:1.12.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-spatialdmelxsim/1.12.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-spatialdmelxsim/1.12.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-spatialdmelxsim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spatialdmelxsim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spatialdmelxsim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-spatialdmelxsim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-spatialdmelxsim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-spatialdmelxsim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-spatialdmelxsim

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