---
layout: container
name:  "quay.io/biocontainers/sam2lca"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sam2lca/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/sam2lca/container.yaml"
updated_at: "2022-10-27 00:33:53.259760"
latest: "1.1.2--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/sam2lca"
aliases:
 - "sam2lca"
versions:
 - "1.1.2--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for sam2lca"
config: {"url": "https://biocontainers.pro/tools/sam2lca", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sam2lca", "latest": {"1.1.2--pyhdfd78af_1": "sha256:a0ce611f6e4d0ecbe70dbca9cc6fd3513f10d4a73aa6048439c8032924e469ac"}, "tags": {"1.1.2--pyhdfd78af_1": "sha256:a0ce611f6e4d0ecbe70dbca9cc6fd3513f10d4a73aa6048439c8032924e469ac"}, "docker": "quay.io/biocontainers/sam2lca", "aliases": {"sam2lca": "/usr/local/bin/sam2lca"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sam2lca.
shpc-registry automated BioContainers addition for sam2lca
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sam2lca
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sam2lca:1.1.2--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sam2lca/1.1.2--pyhdfd78af_1
$ module help quay.io/biocontainers/sam2lca/1.1.2--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sam2lca-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sam2lca-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sam2lca-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sam2lca-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sam2lca-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sam2lca-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sam2lca

```bash
$ singularity exec <container> /usr/local/bin/sam2lca
$ podman run --it --rm --entrypoint /usr/local/bin/sam2lca   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sam2lca   -v ${PWD} -w ${PWD} <container> -c " $@"
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