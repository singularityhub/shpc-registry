---
layout: container
name:  "quay.io/biocontainers/aliceasm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/aliceasm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/aliceasm/container.yaml"
updated_at: "2025-08-13 04:03:47.771860"
latest: "0.6.38--h9948957_0"
container_url: "https://biocontainers.pro/tools/aliceasm"
aliases:
 - "aliceasm"
 - "bcalm"
 - "gfatools"
 - "graphunzip"
 - "paf2gfa"
 - "reduce"
 - "h5cc"
versions:
 - "0.6.33--h9948957_0"
 - "0.6.34--h9948957_0"
 - "0.6.37--h9948957_0"
 - "0.6.38--h9948957_0"
description: "singularity registry hpc automated addition for aliceasm"
config: {"url": "https://biocontainers.pro/tools/aliceasm", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for aliceasm", "latest": {"0.6.38--h9948957_0": "sha256:4d24bd6094ce1c729f2beb2ae07310c7ebb60523c42ef06de9305a3e0c7fea7c"}, "tags": {"0.6.33--h9948957_0": "sha256:f170743918a626e1c11ac7578143edcd36208a0251b6fab334e333b8d0df3fa1", "0.6.34--h9948957_0": "sha256:4503307bf5b49211cd79488111d03a9283127e0d7d03629f42359906d75ec9e6", "0.6.37--h9948957_0": "sha256:b1128edda739bf5f6429b2138147f1354246c34533dd71e08b3087fb5da71a61", "0.6.38--h9948957_0": "sha256:4d24bd6094ce1c729f2beb2ae07310c7ebb60523c42ef06de9305a3e0c7fea7c"}, "docker": "quay.io/biocontainers/aliceasm", "aliases": {"aliceasm": "/usr/local/bin/aliceasm", "bcalm": "/usr/local/bin/bcalm", "gfatools": "/usr/local/bin/gfatools", "graphunzip": "/usr/local/bin/graphunzip", "paf2gfa": "/usr/local/bin/paf2gfa", "reduce": "/usr/local/bin/reduce", "h5cc": "/usr/local/bin/h5cc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/aliceasm.
singularity registry hpc automated addition for aliceasm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/aliceasm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/aliceasm:0.6.38--h9948957_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/aliceasm/0.6.38--h9948957_0
$ module help quay.io/biocontainers/aliceasm/0.6.38--h9948957_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### aliceasm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### aliceasm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### aliceasm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### aliceasm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### aliceasm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### aliceasm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aliceasm

```bash
$ singularity exec <container> /usr/local/bin/aliceasm
$ podman run --it --rm --entrypoint /usr/local/bin/aliceasm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aliceasm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bcalm

```bash
$ singularity exec <container> /usr/local/bin/bcalm
$ podman run --it --rm --entrypoint /usr/local/bin/bcalm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcalm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfatools

```bash
$ singularity exec <container> /usr/local/bin/gfatools
$ podman run --it --rm --entrypoint /usr/local/bin/gfatools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfatools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### graphunzip

```bash
$ singularity exec <container> /usr/local/bin/graphunzip
$ podman run --it --rm --entrypoint /usr/local/bin/graphunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/graphunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paf2gfa

```bash
$ singularity exec <container> /usr/local/bin/paf2gfa
$ podman run --it --rm --entrypoint /usr/local/bin/paf2gfa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paf2gfa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reduce

```bash
$ singularity exec <container> /usr/local/bin/reduce
$ podman run --it --rm --entrypoint /usr/local/bin/reduce   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reduce   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5cc

```bash
$ singularity exec <container> /usr/local/bin/h5cc
$ podman run --it --rm --entrypoint /usr/local/bin/h5cc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5cc   -v ${PWD} -w ${PWD} <container> -c " $@"
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