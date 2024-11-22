---
layout: container
name:  "quay.io/biocontainers/ratatosk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ratatosk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ratatosk/container.yaml"
updated_at: "2024-11-22 04:13:53.571265"
latest: "0.9.0--hdcf5f25_1"
container_url: "https://biocontainers.pro/tools/ratatosk"
aliases:
 - "Ratatosk"
versions:
 - "0.7.6.3--h5b5514e_0"
 - "0.7.6.3--h43eeafb_2"
 - "0.9.0--hdcf5f25_0"
 - "0.9.0--hdcf5f25_1"
description: "singularity registry hpc automated addition for ratatosk"
config: {"url": "https://biocontainers.pro/tools/ratatosk", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ratatosk", "latest": {"0.9.0--hdcf5f25_1": "sha256:a97dbf26fa2ab5e52e9ae198213512b7c3f93dfcbaf2865a5696a7d45571d768"}, "tags": {"0.7.6.3--h5b5514e_0": "sha256:19319f6b739e7fa05c5e25eb1f22effdf02b14c0fffe0f5f38f484d4f4fc1572", "0.7.6.3--h43eeafb_2": "sha256:19db80414eb8daa0a190d8d8a71c5a89f6253fa1f2968ba69b71661b07ba6b07", "0.9.0--hdcf5f25_0": "sha256:48a9f930a37ead3ac1365ad32ddd5ef8153a196bda773fea7e30ffd6f40f2ad4", "0.9.0--hdcf5f25_1": "sha256:a97dbf26fa2ab5e52e9ae198213512b7c3f93dfcbaf2865a5696a7d45571d768"}, "docker": "quay.io/biocontainers/ratatosk", "aliases": {"Ratatosk": "/usr/local/bin/Ratatosk"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ratatosk.
singularity registry hpc automated addition for ratatosk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ratatosk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ratatosk:0.9.0--hdcf5f25_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ratatosk/0.9.0--hdcf5f25_1
$ module help quay.io/biocontainers/ratatosk/0.9.0--hdcf5f25_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ratatosk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ratatosk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ratatosk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ratatosk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ratatosk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ratatosk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Ratatosk

```bash
$ singularity exec <container> /usr/local/bin/Ratatosk
$ podman run --it --rm --entrypoint /usr/local/bin/Ratatosk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Ratatosk   -v ${PWD} -w ${PWD} <container> -c " $@"
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