---
layout: container
name:  "quay.io/biocontainers/r-pcalg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-pcalg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-pcalg/container.yaml"
updated_at: "2026-01-31 04:30:42.904473"
latest: "2.6_12--r44h40dc89f_7"
container_url: "https://biocontainers.pro/tools/r-pcalg"

versions:
 - "2.6_12--r41hecf12ef_3"
 - "2.6_12--r42hecf12ef_4"
 - "2.6_12--r42h21a89ab_5"
 - "2.6_12--r43h21a89ab_6"
 - "2.6_12--r44h40dc89f_7"
description: "shpc-registry automated BioContainers addition for r-pcalg"
config: {"url": "https://biocontainers.pro/tools/r-pcalg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-pcalg", "latest": {"2.6_12--r44h40dc89f_7": "sha256:0f070730ff79e38d525683bb980f9f760a4fde32e0735439040a45faf607f8f0"}, "tags": {"2.6_12--r41hecf12ef_3": "sha256:99a8d648ed39755fde267c869383902969702b58e14db5da49642dcf50c90629", "2.6_12--r42hecf12ef_4": "sha256:6d670743ea5b320d42d4db360c7ae3ada41c6c95014a520a57a8813310a6a32c", "2.6_12--r42h21a89ab_5": "sha256:3d0bf4224fb5ba08a7cf18ec8cae0e316d6f4092799a1909422b8769695be0e9", "2.6_12--r43h21a89ab_6": "sha256:0e2b1b0f465e452fffa1e19b4e6dd59fd8350517e0f9815cca96bb51118cc7ae", "2.6_12--r44h40dc89f_7": "sha256:0f070730ff79e38d525683bb980f9f760a4fde32e0735439040a45faf607f8f0"}, "docker": "quay.io/biocontainers/r-pcalg"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-pcalg.
shpc-registry automated BioContainers addition for r-pcalg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-pcalg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-pcalg:2.6_12--r44h40dc89f_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-pcalg/2.6_12--r44h40dc89f_7
$ module help quay.io/biocontainers/r-pcalg/2.6_12--r44h40dc89f_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-pcalg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-pcalg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-pcalg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-pcalg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-pcalg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-pcalg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-pcalg

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