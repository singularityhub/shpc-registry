---
layout: container
name:  "quay.io/biocontainers/bwa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bwa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bwa/container.yaml"
updated_at: "2023-12-07 02:37:14.226945"
latest: "0.7.17--h7132678_10"
container_url: "https://biocontainers.pro/tools/bwa"
aliases:
 - "bwa"
versions:
 - "0.7.17--h7132678_9"
 - "0.7.17--h7132678_10"
description: "shpc-registry automated BioContainers addition for bwa"
config: {"url": "https://biocontainers.pro/tools/bwa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bwa", "latest": {"0.7.17--h7132678_10": "sha256:f9063141d8c5da87da76392b3a152b927b2913d47373f1874d76f14634b3f684"}, "tags": {"0.7.17--h7132678_9": "sha256:07822e4293a8c59755b295c448b9541db6c9bdbfdedb010bdbdcc1e1e935370f", "0.7.17--h7132678_10": "sha256:f9063141d8c5da87da76392b3a152b927b2913d47373f1874d76f14634b3f684"}, "docker": "quay.io/biocontainers/bwa", "aliases": {"bwa": "/usr/local/bin/bwa"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bwa.
shpc-registry automated BioContainers addition for bwa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bwa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bwa:0.7.17--h7132678_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bwa/0.7.17--h7132678_10
$ module help quay.io/biocontainers/bwa/0.7.17--h7132678_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bwa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bwa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bwa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bwa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bwa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bwa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bwa

```bash
$ singularity exec <container> /usr/local/bin/bwa
$ podman run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
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