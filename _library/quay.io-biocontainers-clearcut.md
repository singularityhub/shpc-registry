---
layout: container
name:  "quay.io/biocontainers/clearcut"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/clearcut/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/clearcut/container.yaml"
updated_at: "2025-06-18 03:29:03.084811"
latest: "1.0.9--h7b50bb2_7"
container_url: "https://biocontainers.pro/tools/clearcut"
aliases:
 - "clearcut"
versions:
 - "1.0.9--hec16e2b_4"
 - "1.0.9--h031d066_6"
 - "1.0.9--h7b50bb2_7"
description: "shpc-registry automated BioContainers addition for clearcut"
config: {"url": "https://biocontainers.pro/tools/clearcut", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for clearcut", "latest": {"1.0.9--h7b50bb2_7": "sha256:7b40f29bedd6e2f9f333ddf45f993cf4aa3b02ffc3f4b12636eded9a5e3b2657"}, "tags": {"1.0.9--hec16e2b_4": "sha256:3301cd7dff0967d52a44b23f79cc6c6c4ce141d57110c19ca74f59f9db256e41", "1.0.9--h031d066_6": "sha256:5bcc4d0be237284834b07870efa0146680816657a50502a2ecf0f3e56b966239", "1.0.9--h7b50bb2_7": "sha256:7b40f29bedd6e2f9f333ddf45f993cf4aa3b02ffc3f4b12636eded9a5e3b2657"}, "docker": "quay.io/biocontainers/clearcut", "aliases": {"clearcut": "/usr/local/bin/clearcut"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/clearcut.
shpc-registry automated BioContainers addition for clearcut
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/clearcut
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/clearcut:1.0.9--h7b50bb2_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/clearcut/1.0.9--h7b50bb2_7
$ module help quay.io/biocontainers/clearcut/1.0.9--h7b50bb2_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### clearcut-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### clearcut-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### clearcut-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### clearcut-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### clearcut-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### clearcut-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### clearcut

```bash
$ singularity exec <container> /usr/local/bin/clearcut
$ podman run --it --rm --entrypoint /usr/local/bin/clearcut   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clearcut   -v ${PWD} -w ${PWD} <container> -c " $@"
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