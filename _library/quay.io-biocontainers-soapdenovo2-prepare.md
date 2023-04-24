---
layout: container
name:  "quay.io/biocontainers/soapdenovo2-prepare"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/soapdenovo2-prepare/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/soapdenovo2-prepare/container.yaml"
updated_at: "2023-04-24 03:07:55.363456"
latest: "2.0--h7132678_6"
container_url: "https://biocontainers.pro/tools/soapdenovo2-prepare"
aliases:
 - "finalFusion"
versions:
 - "2.0--h7132678_6"
description: "shpc-registry automated BioContainers addition for soapdenovo2-prepare"
config: {"url": "https://biocontainers.pro/tools/soapdenovo2-prepare", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for soapdenovo2-prepare", "latest": {"2.0--h7132678_6": "sha256:d25bea9c5457bb13a0ad5254599bb545f555d99900ac9e01c13431443dd76d61"}, "tags": {"2.0--h7132678_6": "sha256:d25bea9c5457bb13a0ad5254599bb545f555d99900ac9e01c13431443dd76d61"}, "docker": "quay.io/biocontainers/soapdenovo2-prepare", "aliases": {"finalFusion": "/usr/local/bin/finalFusion"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/soapdenovo2-prepare.
shpc-registry automated BioContainers addition for soapdenovo2-prepare
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/soapdenovo2-prepare
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/soapdenovo2-prepare:2.0--h7132678_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/soapdenovo2-prepare/2.0--h7132678_6
$ module help quay.io/biocontainers/soapdenovo2-prepare/2.0--h7132678_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### soapdenovo2-prepare-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### soapdenovo2-prepare-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### soapdenovo2-prepare-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### soapdenovo2-prepare-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### soapdenovo2-prepare-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### soapdenovo2-prepare-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### finalFusion

```bash
$ singularity exec <container> /usr/local/bin/finalFusion
$ podman run --it --rm --entrypoint /usr/local/bin/finalFusion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/finalFusion   -v ${PWD} -w ${PWD} <container> -c " $@"
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