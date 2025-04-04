---
layout: container
name:  "quay.io/biocontainers/pretextmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pretextmap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pretextmap/container.yaml"
updated_at: "2025-04-04 03:21:06.152795"
latest: "0.1.9--h9948957_4"
container_url: "https://biocontainers.pro/tools/pretextmap"
aliases:
 - "PretextMap"
 - "PretextMap.avx"
 - "PretextMap.avx2"
 - "PretextMap.noext"
 - "PretextMap.sse41"
 - "PretextMap.sse42"
versions:
 - "0.1.9--h9f5acd7_1"
 - "0.1.9--h4ac6f70_3"
 - "0.1.9--h9948957_4"
description: "shpc-registry automated BioContainers addition for pretextmap"
config: {"url": "https://biocontainers.pro/tools/pretextmap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pretextmap", "latest": {"0.1.9--h9948957_4": "sha256:7d25faef12eccb15508573e215a05a892c14e3e1a01cc7a8045b03612fd08c78"}, "tags": {"0.1.9--h9f5acd7_1": "sha256:2ea29e078166daa95ea28d500cd2df46eec77cebc9d100ed986f797e3a282ae1", "0.1.9--h4ac6f70_3": "sha256:f154ad10859562ffea6cbaec96764d0c454ee74a82f0b5cacd1edc1a6375c739", "0.1.9--h9948957_4": "sha256:7d25faef12eccb15508573e215a05a892c14e3e1a01cc7a8045b03612fd08c78"}, "docker": "quay.io/biocontainers/pretextmap", "aliases": {"PretextMap": "/usr/local/bin/PretextMap", "PretextMap.avx": "/usr/local/bin/PretextMap.avx", "PretextMap.avx2": "/usr/local/bin/PretextMap.avx2", "PretextMap.noext": "/usr/local/bin/PretextMap.noext", "PretextMap.sse41": "/usr/local/bin/PretextMap.sse41", "PretextMap.sse42": "/usr/local/bin/PretextMap.sse42"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pretextmap.
shpc-registry automated BioContainers addition for pretextmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pretextmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pretextmap:0.1.9--h9948957_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pretextmap/0.1.9--h9948957_4
$ module help quay.io/biocontainers/pretextmap/0.1.9--h9948957_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pretextmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pretextmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pretextmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pretextmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pretextmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pretextmap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### PretextMap

```bash
$ singularity exec <container> /usr/local/bin/PretextMap
$ podman run --it --rm --entrypoint /usr/local/bin/PretextMap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextMap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PretextMap.avx

```bash
$ singularity exec <container> /usr/local/bin/PretextMap.avx
$ podman run --it --rm --entrypoint /usr/local/bin/PretextMap.avx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextMap.avx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PretextMap.avx2

```bash
$ singularity exec <container> /usr/local/bin/PretextMap.avx2
$ podman run --it --rm --entrypoint /usr/local/bin/PretextMap.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextMap.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PretextMap.noext

```bash
$ singularity exec <container> /usr/local/bin/PretextMap.noext
$ podman run --it --rm --entrypoint /usr/local/bin/PretextMap.noext   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextMap.noext   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PretextMap.sse41

```bash
$ singularity exec <container> /usr/local/bin/PretextMap.sse41
$ podman run --it --rm --entrypoint /usr/local/bin/PretextMap.sse41   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextMap.sse41   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PretextMap.sse42

```bash
$ singularity exec <container> /usr/local/bin/PretextMap.sse42
$ podman run --it --rm --entrypoint /usr/local/bin/PretextMap.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextMap.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
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