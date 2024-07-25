---
layout: container
name:  "quay.io/biocontainers/genrich"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genrich/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/genrich/container.yaml"
updated_at: "2024-07-25 03:22:46.066503"
latest: "0.6.1--he4a0461_4"
container_url: "https://biocontainers.pro/tools/genrich"
aliases:
 - "Genrich"
versions:
 - "0.6.1--h7132678_2"
 - "0.6.1--h7132678_3"
 - "0.6.1--he4a0461_4"
description: "shpc-registry automated BioContainers addition for genrich"
config: {"url": "https://biocontainers.pro/tools/genrich", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for genrich", "latest": {"0.6.1--he4a0461_4": "sha256:a3c00a97bc4eee75ce1481eccbd6977ce9d11ac3153ad31217774ac4cecb8455"}, "tags": {"0.6.1--h7132678_2": "sha256:f6aa2933a4cb8829b7ffa452deffc7a3b79a40f4b04647740d17504a7f86c295", "0.6.1--h7132678_3": "sha256:6808acb0f07c36cfbdb8384bd9124564a522b4b3e66fcbe3fdf0a5eeb844086d", "0.6.1--he4a0461_4": "sha256:a3c00a97bc4eee75ce1481eccbd6977ce9d11ac3153ad31217774ac4cecb8455"}, "docker": "quay.io/biocontainers/genrich", "aliases": {"Genrich": "/usr/local/bin/Genrich"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genrich.
shpc-registry automated BioContainers addition for genrich
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genrich
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genrich:0.6.1--he4a0461_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genrich/0.6.1--he4a0461_4
$ module help quay.io/biocontainers/genrich/0.6.1--he4a0461_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genrich-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genrich-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genrich-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genrich-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genrich-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genrich-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Genrich

```bash
$ singularity exec <container> /usr/local/bin/Genrich
$ podman run --it --rm --entrypoint /usr/local/bin/Genrich   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Genrich   -v ${PWD} -w ${PWD} <container> -c " $@"
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