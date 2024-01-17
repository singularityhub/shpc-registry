---
layout: container
name:  "quay.io/biocontainers/tpmcalculator"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tpmcalculator/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tpmcalculator/container.yaml"
updated_at: "2024-01-17 02:43:26.962577"
latest: "0.0.4--hf393df8_3"
container_url: "https://biocontainers.pro/tools/tpmcalculator"
aliases:
 - "TPMCalculator"
 - "bamtools"
versions:
 - "0.0.4--ha7703dc_2"
 - "0.0.4--hf393df8_3"
description: "shpc-registry automated BioContainers addition for tpmcalculator"
config: {"url": "https://biocontainers.pro/tools/tpmcalculator", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tpmcalculator", "latest": {"0.0.4--hf393df8_3": "sha256:8fd3dd640450ac4b954079bd00c3e466232f00032afcada5c0bb428efcda8790"}, "tags": {"0.0.4--ha7703dc_2": "sha256:ebb1671f09de2449f89efd4a1c92650f1bdf51952cf3e4b243f995c835e4fd3e", "0.0.4--hf393df8_3": "sha256:8fd3dd640450ac4b954079bd00c3e466232f00032afcada5c0bb428efcda8790"}, "docker": "quay.io/biocontainers/tpmcalculator", "aliases": {"TPMCalculator": "/usr/local/bin/TPMCalculator", "bamtools": "/usr/local/bin/bamtools"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tpmcalculator.
shpc-registry automated BioContainers addition for tpmcalculator
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tpmcalculator
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tpmcalculator:0.0.4--hf393df8_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tpmcalculator/0.0.4--hf393df8_3
$ module help quay.io/biocontainers/tpmcalculator/0.0.4--hf393df8_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tpmcalculator-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tpmcalculator-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tpmcalculator-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tpmcalculator-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tpmcalculator-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tpmcalculator-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### TPMCalculator

```bash
$ singularity exec <container> /usr/local/bin/TPMCalculator
$ podman run --it --rm --entrypoint /usr/local/bin/TPMCalculator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TPMCalculator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamtools

```bash
$ singularity exec <container> /usr/local/bin/bamtools
$ podman run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
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