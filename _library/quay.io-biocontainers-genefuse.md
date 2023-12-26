---
layout: container
name:  "quay.io/biocontainers/genefuse"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genefuse/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/genefuse/container.yaml"
updated_at: "2023-12-26 03:05:28.174342"
latest: "0.8.0--h43eeafb_2"
container_url: "https://biocontainers.pro/tools/genefuse"
aliases:
 - "genefuse"
versions:
 - "0.8.0--h5b5514e_0"
 - "0.8.0--h43eeafb_2"
description: "shpc-registry automated BioContainers addition for genefuse"
config: {"url": "https://biocontainers.pro/tools/genefuse", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for genefuse", "latest": {"0.8.0--h43eeafb_2": "sha256:af3f5c0247c1fdf9aa899a94eb187843be41d74721219392aa3ab36545c94cde"}, "tags": {"0.8.0--h5b5514e_0": "sha256:72f2a460380436b279e621d476a303e55e48949ee7118e472382041e55515195", "0.8.0--h43eeafb_2": "sha256:af3f5c0247c1fdf9aa899a94eb187843be41d74721219392aa3ab36545c94cde"}, "docker": "quay.io/biocontainers/genefuse", "aliases": {"genefuse": "/usr/local/bin/genefuse"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genefuse.
shpc-registry automated BioContainers addition for genefuse
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genefuse
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genefuse:0.8.0--h43eeafb_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genefuse/0.8.0--h43eeafb_2
$ module help quay.io/biocontainers/genefuse/0.8.0--h43eeafb_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genefuse-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genefuse-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genefuse-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genefuse-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genefuse-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genefuse-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### genefuse

```bash
$ singularity exec <container> /usr/local/bin/genefuse
$ podman run --it --rm --entrypoint /usr/local/bin/genefuse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genefuse   -v ${PWD} -w ${PWD} <container> -c " $@"
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