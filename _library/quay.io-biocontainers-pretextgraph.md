---
layout: container
name:  "quay.io/biocontainers/pretextgraph"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pretextgraph/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pretextgraph/container.yaml"
updated_at: "2025-02-18 03:13:22.476538"
latest: "0.0.7--h9948957_1"
container_url: "https://biocontainers.pro/tools/pretextgraph"
aliases:
 - "PretextGraph"
 - "PretextGraph.avx"
 - "PretextGraph.avx2"
 - "PretextGraph.sse41"
 - "PretextGraph.sse42"
versions:
 - "0.0.6--h9f5acd7_1"
 - "0.0.6--h4ac6f70_3"
 - "0.0.7--h4ac6f70_0"
 - "0.0.7--h9948957_1"
description: "shpc-registry automated BioContainers addition for pretextgraph"
config: {"url": "https://biocontainers.pro/tools/pretextgraph", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pretextgraph", "latest": {"0.0.7--h9948957_1": "sha256:6913e24ecb50e62143d8ced2590d32b78aa0fed12e2ef1323ba9324020584642"}, "tags": {"0.0.6--h9f5acd7_1": "sha256:fa545efff60514e4798807c3d262ddb41e59a748b101905a7661bb22542b3341", "0.0.6--h4ac6f70_3": "sha256:7195c78d71b3c6fd74fea35338acdc3001cf90849fbca9d3f7256d99405d3d81", "0.0.7--h4ac6f70_0": "sha256:25c2b6f5558bc842d9294ee02844abceb0ec7716c9e299f7def8bf9dbe033d01", "0.0.7--h9948957_1": "sha256:6913e24ecb50e62143d8ced2590d32b78aa0fed12e2ef1323ba9324020584642"}, "docker": "quay.io/biocontainers/pretextgraph", "aliases": {"PretextGraph": "/usr/local/bin/PretextGraph", "PretextGraph.avx": "/usr/local/bin/PretextGraph.avx", "PretextGraph.avx2": "/usr/local/bin/PretextGraph.avx2", "PretextGraph.sse41": "/usr/local/bin/PretextGraph.sse41", "PretextGraph.sse42": "/usr/local/bin/PretextGraph.sse42"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pretextgraph.
shpc-registry automated BioContainers addition for pretextgraph
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pretextgraph
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pretextgraph:0.0.7--h9948957_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pretextgraph/0.0.7--h9948957_1
$ module help quay.io/biocontainers/pretextgraph/0.0.7--h9948957_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pretextgraph-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pretextgraph-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pretextgraph-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pretextgraph-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pretextgraph-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pretextgraph-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### PretextGraph

```bash
$ singularity exec <container> /usr/local/bin/PretextGraph
$ podman run --it --rm --entrypoint /usr/local/bin/PretextGraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextGraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PretextGraph.avx

```bash
$ singularity exec <container> /usr/local/bin/PretextGraph.avx
$ podman run --it --rm --entrypoint /usr/local/bin/PretextGraph.avx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextGraph.avx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PretextGraph.avx2

```bash
$ singularity exec <container> /usr/local/bin/PretextGraph.avx2
$ podman run --it --rm --entrypoint /usr/local/bin/PretextGraph.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextGraph.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PretextGraph.sse41

```bash
$ singularity exec <container> /usr/local/bin/PretextGraph.sse41
$ podman run --it --rm --entrypoint /usr/local/bin/PretextGraph.sse41   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextGraph.sse41   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PretextGraph.sse42

```bash
$ singularity exec <container> /usr/local/bin/PretextGraph.sse42
$ podman run --it --rm --entrypoint /usr/local/bin/PretextGraph.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PretextGraph.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
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