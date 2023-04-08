---
layout: container
name:  "quay.io/biocontainers/bioconductor-saigegds"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-saigegds/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-saigegds/container.yaml"
updated_at: "2023-04-08 03:12:36.585118"
latest: "1.12.0--r42hc247a5b_0"
container_url: "https://biocontainers.pro/tools/bioconductor-saigegds"

versions:
 - "1.8.1--r41hc247a5b_0"
 - "1.12.0--r42hc247a5b_0"
description: "shpc-registry automated BioContainers addition for bioconductor-saigegds"
config: {"url": "https://biocontainers.pro/tools/bioconductor-saigegds", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-saigegds", "latest": {"1.12.0--r42hc247a5b_0": "sha256:20c8ed9bdbc82a8bf1755d6657f85c52ae6056a28bb1a7a88849ffab15ed416a"}, "tags": {"1.8.1--r41hc247a5b_0": "sha256:d771d815703ac3b404466d9b0c6056736db71a36e68ad3b51cd597756745e388", "1.12.0--r42hc247a5b_0": "sha256:20c8ed9bdbc82a8bf1755d6657f85c52ae6056a28bb1a7a88849ffab15ed416a"}, "docker": "quay.io/biocontainers/bioconductor-saigegds"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-saigegds.
shpc-registry automated BioContainers addition for bioconductor-saigegds
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-saigegds
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-saigegds:1.12.0--r42hc247a5b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-saigegds/1.12.0--r42hc247a5b_0
$ module help quay.io/biocontainers/bioconductor-saigegds/1.12.0--r42hc247a5b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-saigegds-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-saigegds-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-saigegds-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-saigegds-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-saigegds-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-saigegds-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-saigegds

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