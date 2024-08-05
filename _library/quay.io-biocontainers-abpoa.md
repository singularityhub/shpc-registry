---
layout: container
name:  "quay.io/biocontainers/abpoa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/abpoa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/abpoa/container.yaml"
updated_at: "2024-08-05 02:39:19.301055"
latest: "1.5.2--he4a0461_0"
container_url: "https://biocontainers.pro/tools/abpoa"
aliases:
 - "abpoa"
versions:
 - "1.4.1--h7132678_1"
 - "1.4.1--h7132678_2"
 - "1.4.1--he4a0461_4"
 - "1.4.3--he4a0461_0"
 - "1.5.1--he4a0461_0"
 - "1.5.1--he4a0461_1"
 - "1.5.2--he4a0461_0"
description: "shpc-registry automated BioContainers addition for abpoa"
config: {"url": "https://biocontainers.pro/tools/abpoa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for abpoa", "latest": {"1.5.2--he4a0461_0": "sha256:5d89e7b279782ced33cbafd681e627cafd9557064cd0ffe44f5db4365bdf20f5"}, "tags": {"1.4.1--h7132678_1": "sha256:5648a89bda11703b9419176b17ae7858465dfe9261444a15a7fb65d5a895945d", "1.4.1--h7132678_2": "sha256:c0b499af682159c7aa76b6fe79055c6bbe66d7a79aeac679eaae7cef15d9b1f4", "1.4.1--he4a0461_4": "sha256:89c787fbf4c610eb058f0f480986e1c3cdb6d95e35088361b265e03ae8c2d6f0", "1.4.3--he4a0461_0": "sha256:3e694e716ff2d1211f501057e01ca9f19f24e3bb0557ea45c5cacc2243abf8ed", "1.5.1--he4a0461_0": "sha256:8d1290119026abc4d8a9adf1ecb3f644da51f32554c786735fafddf2aea5322d", "1.5.1--he4a0461_1": "sha256:a96f35644dc8e8b468f68bfb6c7bc7fc8c36f5e8fbaa2f8231210b6fcea0efb3", "1.5.2--he4a0461_0": "sha256:5d89e7b279782ced33cbafd681e627cafd9557064cd0ffe44f5db4365bdf20f5"}, "docker": "quay.io/biocontainers/abpoa", "aliases": {"abpoa": "/usr/local/bin/abpoa"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/abpoa.
shpc-registry automated BioContainers addition for abpoa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/abpoa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/abpoa:1.5.2--he4a0461_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/abpoa/1.5.2--he4a0461_0
$ module help quay.io/biocontainers/abpoa/1.5.2--he4a0461_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### abpoa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### abpoa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### abpoa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### abpoa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### abpoa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### abpoa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### abpoa

```bash
$ singularity exec <container> /usr/local/bin/abpoa
$ podman run --it --rm --entrypoint /usr/local/bin/abpoa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abpoa   -v ${PWD} -w ${PWD} <container> -c " $@"
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