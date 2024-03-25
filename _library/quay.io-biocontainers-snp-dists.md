---
layout: container
name:  "quay.io/biocontainers/snp-dists"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snp-dists/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/snp-dists/container.yaml"
updated_at: "2024-03-25 03:22:19.651018"
latest: "0.8.2--he4a0461_3"
container_url: "https://biocontainers.pro/tools/snp-dists"
aliases:
 - "snp-dists"
versions:
 - "0.8.2--h7132678_1"
 - "0.8.2--h7132678_2"
 - "0.8.2--he4a0461_3"
description: "shpc-registry automated BioContainers addition for snp-dists"
config: {"url": "https://biocontainers.pro/tools/snp-dists", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for snp-dists", "latest": {"0.8.2--he4a0461_3": "sha256:aacd4f13d614ae6bac0a07c132f49f4c071ccca858400b08f271ae9047a9cc76"}, "tags": {"0.8.2--h7132678_1": "sha256:6b76ed35d97bc655daeb0cd0d164c45124cc1b514a3b93796a97c94c988509e9", "0.8.2--h7132678_2": "sha256:87842feba601f88192a3cb2ba931b71477de8877fcd6c5d885a6ad2ae1c3f55c", "0.8.2--he4a0461_3": "sha256:aacd4f13d614ae6bac0a07c132f49f4c071ccca858400b08f271ae9047a9cc76"}, "docker": "quay.io/biocontainers/snp-dists", "aliases": {"snp-dists": "/usr/local/bin/snp-dists"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snp-dists.
shpc-registry automated BioContainers addition for snp-dists
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snp-dists
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snp-dists:0.8.2--he4a0461_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snp-dists/0.8.2--he4a0461_3
$ module help quay.io/biocontainers/snp-dists/0.8.2--he4a0461_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snp-dists-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snp-dists-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snp-dists-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snp-dists-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snp-dists-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snp-dists-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### snp-dists

```bash
$ singularity exec <container> /usr/local/bin/snp-dists
$ podman run --it --rm --entrypoint /usr/local/bin/snp-dists   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snp-dists   -v ${PWD} -w ${PWD} <container> -c " $@"
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