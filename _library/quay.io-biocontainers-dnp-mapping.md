---
layout: container
name:  "quay.io/biocontainers/dnp-mapping"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dnp-mapping/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dnp-mapping/container.yaml"
updated_at: "2024-08-23 02:58:25.835689"
latest: "1.0--h4ac6f70_3"
container_url: "https://biocontainers.pro/tools/dnp-mapping"
aliases:
 - "dnp-mapping"
versions:
 - "1.0--h9f5acd7_1"
 - "1.0--h9f5acd7_2"
 - "1.0--h4ac6f70_3"
description: "shpc-registry automated BioContainers addition for dnp-mapping"
config: {"url": "https://biocontainers.pro/tools/dnp-mapping", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dnp-mapping", "latest": {"1.0--h4ac6f70_3": "sha256:8b2915e87b3eaa955bb5733550a7320648d6ccdb38a61f59b254284562a90d5c"}, "tags": {"1.0--h9f5acd7_1": "sha256:61d02254f14045902e6fbfac0f75bab2ef5d6b0dd03de924be9a204de708364f", "1.0--h9f5acd7_2": "sha256:c297de031689c20b202bc674d615aa998181c382d9184ae2ef623015b9bcb24d", "1.0--h4ac6f70_3": "sha256:8b2915e87b3eaa955bb5733550a7320648d6ccdb38a61f59b254284562a90d5c"}, "docker": "quay.io/biocontainers/dnp-mapping", "aliases": {"dnp-mapping": "/usr/local/bin/dnp-mapping"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dnp-mapping.
shpc-registry automated BioContainers addition for dnp-mapping
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dnp-mapping
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dnp-mapping:1.0--h4ac6f70_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dnp-mapping/1.0--h4ac6f70_3
$ module help quay.io/biocontainers/dnp-mapping/1.0--h4ac6f70_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dnp-mapping-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dnp-mapping-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dnp-mapping-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dnp-mapping-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dnp-mapping-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dnp-mapping-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dnp-mapping

```bash
$ singularity exec <container> /usr/local/bin/dnp-mapping
$ podman run --it --rm --entrypoint /usr/local/bin/dnp-mapping   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnp-mapping   -v ${PWD} -w ${PWD} <container> -c " $@"
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