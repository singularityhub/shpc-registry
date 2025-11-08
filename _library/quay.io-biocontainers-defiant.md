---
layout: container
name:  "quay.io/biocontainers/defiant"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/defiant/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/defiant/container.yaml"
updated_at: "2025-11-08 03:31:21.962882"
latest: "1.1.4--h7b50bb2_6"
container_url: "https://biocontainers.pro/tools/defiant"
aliases:
 - "defiant"
 - "roi"
versions:
 - "1.1.4--hec16e2b_3"
 - "1.1.4--h031d066_5"
 - "1.1.4--h7b50bb2_6"
description: "shpc-registry automated BioContainers addition for defiant"
config: {"url": "https://biocontainers.pro/tools/defiant", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for defiant", "latest": {"1.1.4--h7b50bb2_6": "sha256:6d45a7d5188aa2a195068fdf043496d631d96a6ad01adbe819a45b8ddfd85d7b"}, "tags": {"1.1.4--hec16e2b_3": "sha256:6c2b5f1d6afac379a6ca33dee5b9d87cbb8b1418a3a481f5ccd069e1f9769f5e", "1.1.4--h031d066_5": "sha256:0f621cb5bbcaf9dc603f867464602093a26962d7a1ed61aa5ba365c0d54f8ac0", "1.1.4--h7b50bb2_6": "sha256:6d45a7d5188aa2a195068fdf043496d631d96a6ad01adbe819a45b8ddfd85d7b"}, "docker": "quay.io/biocontainers/defiant", "aliases": {"defiant": "/usr/local/bin/defiant", "roi": "/usr/local/bin/roi"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/defiant.
shpc-registry automated BioContainers addition for defiant
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/defiant
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/defiant:1.1.4--h7b50bb2_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/defiant/1.1.4--h7b50bb2_6
$ module help quay.io/biocontainers/defiant/1.1.4--h7b50bb2_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### defiant-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### defiant-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### defiant-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### defiant-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### defiant-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### defiant-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### defiant

```bash
$ singularity exec <container> /usr/local/bin/defiant
$ podman run --it --rm --entrypoint /usr/local/bin/defiant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/defiant   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### roi

```bash
$ singularity exec <container> /usr/local/bin/roi
$ podman run --it --rm --entrypoint /usr/local/bin/roi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/roi   -v ${PWD} -w ${PWD} <container> -c " $@"
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