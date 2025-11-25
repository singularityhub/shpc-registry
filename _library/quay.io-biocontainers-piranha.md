---
layout: container
name:  "quay.io/biocontainers/piranha"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/piranha/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/piranha/container.yaml"
updated_at: "2025-11-25 03:38:45.513511"
latest: "1.2.1--ha5748cb_11"
container_url: "https://biocontainers.pro/tools/piranha"
aliases:
 - "Piranha"
 - "Simulate"
 - "bamtools-2.4.1"
 - "bamtools"
versions:
 - "1.2.1--gsl2.2_bamtools2.4.1_5"
 - "1.2.1--ha5748cb_11"
description: "shpc-registry automated BioContainers addition for piranha"
config: {"url": "https://biocontainers.pro/tools/piranha", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for piranha", "latest": {"1.2.1--ha5748cb_11": "sha256:71fabf9856ec42f00bf6df7162c077bfa0f977112e4581a903538e6e3e01ece2"}, "tags": {"1.2.1--gsl2.2_bamtools2.4.1_5": "sha256:2c56ba6254a84c1728b056a9314a615706c25a64ed446825bea022d01a3c03e4", "1.2.1--ha5748cb_11": "sha256:71fabf9856ec42f00bf6df7162c077bfa0f977112e4581a903538e6e3e01ece2"}, "docker": "quay.io/biocontainers/piranha", "aliases": {"Piranha": "/usr/local/bin/Piranha", "Simulate": "/usr/local/bin/Simulate", "bamtools-2.4.1": "/usr/local/bin/bamtools-2.4.1", "bamtools": "/usr/local/bin/bamtools"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/piranha.
shpc-registry automated BioContainers addition for piranha
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/piranha
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/piranha:1.2.1--ha5748cb_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/piranha/1.2.1--ha5748cb_11
$ module help quay.io/biocontainers/piranha/1.2.1--ha5748cb_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### piranha-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### piranha-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### piranha-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### piranha-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### piranha-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### piranha-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Piranha

```bash
$ singularity exec <container> /usr/local/bin/Piranha
$ podman run --it --rm --entrypoint /usr/local/bin/Piranha   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Piranha   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Simulate

```bash
$ singularity exec <container> /usr/local/bin/Simulate
$ podman run --it --rm --entrypoint /usr/local/bin/Simulate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Simulate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamtools-2.4.1

```bash
$ singularity exec <container> /usr/local/bin/bamtools-2.4.1
$ podman run --it --rm --entrypoint /usr/local/bin/bamtools-2.4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamtools-2.4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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