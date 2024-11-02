---
layout: container
name:  "quay.io/biocontainers/nanosim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nanosim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nanosim/container.yaml"
updated_at: "2024-11-02 03:03:39.569942"
latest: "3.2.2--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/nanosim"

versions:
 - "v1.3.0--py35r3.4.1_0"
 - "3.1.0--hdfd78af_0"
 - "3.0.2--hdfd78af_0"
 - "2.6.0--hdfd78af_1"
 - "2.5.1--1"
 - "2.2.0--py_0"
 - "3.2.0--hdfd78af_0"
 - "3.2.1--hdfd78af_0"
 - "3.2.2--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for nanosim"
config: {"url": "https://biocontainers.pro/tools/nanosim", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nanosim", "latest": {"3.2.2--hdfd78af_0": "sha256:dc88183e320fe6b0e0a95da18962877221bc760e4f09fb5ce6d49d6086f06115"}, "tags": {"v1.3.0--py35r3.4.1_0": "sha256:b95e724c235f1617857b850a09490e2b218716c4219b700813179e30a664972b", "3.1.0--hdfd78af_0": "sha256:38e67a7d37e00b443ce4679193d7f18381ed75194a04f321b2d8003139b94800", "3.0.2--hdfd78af_0": "sha256:b3cdc9ffb111069b787c5b2f744f2db9ffe552acdf10ab34428bd4ffd9f179d0", "2.6.0--hdfd78af_1": "sha256:d99389f4fafd8a36547cf5c2a6996a97d929482090682b1a4d070c28069d199b", "2.5.1--1": "sha256:75a726761a22d6413360b364dc537f8d6c0ce3a8bfc7aa2cceb22462fb39df99", "2.2.0--py_0": "sha256:e0aa40ac85603964e11f2f5852adc4b5a9dff33f00291fd5190948fc86e6a9c7", "3.2.0--hdfd78af_0": "sha256:c10de4b00a8540b13f854f133b83d419abdc08ab6d294441046b640e24c646ab", "3.2.1--hdfd78af_0": "sha256:1c5cc83081b385bcd309519868130386ad236e71387cafb0854845ffb136a68a", "3.2.2--hdfd78af_0": "sha256:dc88183e320fe6b0e0a95da18962877221bc760e4f09fb5ce6d49d6086f06115"}, "docker": "quay.io/biocontainers/nanosim"}
---

This module is a singularity container wrapper for quay.io/biocontainers/nanosim.
shpc-registry automated BioContainers addition for nanosim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nanosim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nanosim:3.2.2--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nanosim/3.2.2--hdfd78af_0
$ module help quay.io/biocontainers/nanosim/3.2.2--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nanosim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nanosim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nanosim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nanosim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nanosim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nanosim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### nanosim

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