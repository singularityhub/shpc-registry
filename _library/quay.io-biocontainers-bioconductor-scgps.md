---
layout: container
name:  "quay.io/biocontainers/bioconductor-scgps"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scgps/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scgps/container.yaml"
updated_at: "2025-10-09 04:39:04.427596"
latest: "1.20.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scgps"

versions:
 - "1.8.0--r41hc247a5b_2"
 - "1.12.0--r42hc247a5b_0"
 - "1.12.0--r42hf17093f_1"
 - "1.14.1--r43hf17093f_0"
 - "1.16.0--r43hf17093f_0"
 - "1.20.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scgps"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scgps", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scgps", "latest": {"1.20.0--r44he5774e6_0": "sha256:6716a497fa93a9a770d8c9904447cf2179667cefb837eab839662d913fbbd5e5"}, "tags": {"1.8.0--r41hc247a5b_2": "sha256:2cf721c12b5a034157637b687ff328821dcc6718eae6315df861f4da3a84af4c", "1.12.0--r42hc247a5b_0": "sha256:f3fb7c6e372f633df61f69b8b915439eece0f28977996b8734c1a596f0effc4d", "1.12.0--r42hf17093f_1": "sha256:3f5e38abe8b8d845dbdae40f9d5720fda5343856b687f6baaa4c9f148c6075d4", "1.14.1--r43hf17093f_0": "sha256:17e5beccefcdedf853930dfb36f5829d781fbf8c5b95003e455de77e8f448035", "1.16.0--r43hf17093f_0": "sha256:e8efadba5cf655af2ee59d823f7213e35911104838379f372578bc9fc989d025", "1.20.0--r44he5774e6_0": "sha256:6716a497fa93a9a770d8c9904447cf2179667cefb837eab839662d913fbbd5e5"}, "docker": "quay.io/biocontainers/bioconductor-scgps"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scgps.
shpc-registry automated BioContainers addition for bioconductor-scgps
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scgps
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scgps:1.20.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scgps/1.20.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-scgps/1.20.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scgps-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scgps-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scgps-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scgps-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scgps-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scgps-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-scgps

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