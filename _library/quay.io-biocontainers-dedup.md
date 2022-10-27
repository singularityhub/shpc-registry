---
layout: container
name:  "quay.io/biocontainers/dedup"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dedup/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/dedup/container.yaml"
updated_at: "2022-10-27 00:33:30.665856"
latest: "0.12.8--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/dedup"
aliases:
 - "dedup"
versions:
 - "0.12.8--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for dedup"
config: {"url": "https://biocontainers.pro/tools/dedup", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dedup", "latest": {"0.12.8--hdfd78af_1": "sha256:f681e5168256c179431738ac720fc5b2cdec66555de8a84b918b041e19c79944"}, "tags": {"0.12.8--hdfd78af_1": "sha256:f681e5168256c179431738ac720fc5b2cdec66555de8a84b918b041e19c79944"}, "docker": "quay.io/biocontainers/dedup", "aliases": {"dedup": "/usr/local/bin/dedup"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dedup.
shpc-registry automated BioContainers addition for dedup
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dedup
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dedup:0.12.8--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dedup/0.12.8--hdfd78af_1
$ module help quay.io/biocontainers/dedup/0.12.8--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dedup-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dedup-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dedup-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dedup-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dedup-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dedup-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dedup

```bash
$ singularity exec <container> /usr/local/bin/dedup
$ podman run --it --rm --entrypoint /usr/local/bin/dedup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dedup   -v ${PWD} -w ${PWD} <container> -c " $@"
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