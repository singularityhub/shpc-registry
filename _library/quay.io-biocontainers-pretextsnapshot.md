---
layout: container
name:  "quay.io/biocontainers/pretextsnapshot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pretextsnapshot/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pretextsnapshot/container.yaml"
updated_at: "2025-12-01 04:16:55.990096"
latest: "0.0.5--h9948957_0"
container_url: "https://biocontainers.pro/tools/pretextsnapshot"
aliases:
 - "PretextSnapshot"
 - "PretextSnapshot.avx"
 - "PretextSnapshot.avx2"
 - "PretextSnapshot.sse41"
 - "PretextSnapshot.sse42"
versions:
 - "0.0.4--h9f5acd7_1"
 - "0.0.4--h4ac6f70_3"
 - "0.0.4--h9948957_4"
 - "0.0.5--h9948957_0"
description: "shpc-registry automated BioContainers addition for pretextsnapshot"
config: {"url": "https://biocontainers.pro/tools/pretextsnapshot", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pretextsnapshot", "latest": {"0.0.5--h9948957_0": "sha256:bea58228fd19b677cf49e3600ee04ed904e968a492da892ecb48dbf7995ab0d5"}, "tags": {"0.0.4--h9f5acd7_1": "sha256:a38608ebccf66184e54602d681f833f211ecbc08a910cf996227930fcc214977", "0.0.4--h4ac6f70_3": "sha256:b205e2ffc312d9aefc342f735e311d018ef1aadfadf170a12ada1a97e557195e", "0.0.4--h9948957_4": "sha256:84b2810da9c327fe0c605e40e2060a5059b4f47df208d03c836bb9da1ab83e5b", "0.0.5--h9948957_0": "sha256:bea58228fd19b677cf49e3600ee04ed904e968a492da892ecb48dbf7995ab0d5"}, "docker": "quay.io/biocontainers/pretextsnapshot", "aliases": {"PretextSnapshot": "/usr/local/bin/PretextSnapshot", "PretextSnapshot.avx": "/usr/local/bin/PretextSnapshot.avx", "PretextSnapshot.avx2": "/usr/local/bin/PretextSnapshot.avx2", "PretextSnapshot.sse41": "/usr/local/bin/PretextSnapshot.sse41", "PretextSnapshot.sse42": "/usr/local/bin/PretextSnapshot.sse42"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pretextsnapshot.
shpc-registry automated BioContainers addition for pretextsnapshot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pretextsnapshot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pretextsnapshot:0.0.5--h9948957_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pretextsnapshot/0.0.5--h9948957_0
$ module help quay.io/biocontainers/pretextsnapshot/0.0.5--h9948957_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pretextsnapshot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pretextsnapshot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pretextsnapshot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pretextsnapshot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pretextsnapshot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pretextsnapshot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### PretextSnapshot

```bash
$ singularity exec <container> /usr/local/bin/PretextSnapshot
$ podman run --it --rm --entrypoint /usr/local/bin/PretextSnapshot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextSnapshot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PretextSnapshot.avx

```bash
$ singularity exec <container> /usr/local/bin/PretextSnapshot.avx
$ podman run --it --rm --entrypoint /usr/local/bin/PretextSnapshot.avx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextSnapshot.avx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PretextSnapshot.avx2

```bash
$ singularity exec <container> /usr/local/bin/PretextSnapshot.avx2
$ podman run --it --rm --entrypoint /usr/local/bin/PretextSnapshot.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextSnapshot.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PretextSnapshot.sse41

```bash
$ singularity exec <container> /usr/local/bin/PretextSnapshot.sse41
$ podman run --it --rm --entrypoint /usr/local/bin/PretextSnapshot.sse41   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextSnapshot.sse41   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PretextSnapshot.sse42

```bash
$ singularity exec <container> /usr/local/bin/PretextSnapshot.sse42
$ podman run --it --rm --entrypoint /usr/local/bin/PretextSnapshot.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextSnapshot.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
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