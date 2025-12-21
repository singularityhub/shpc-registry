---
layout: container
name:  "quay.io/biocontainers/fastlin"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastlin/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastlin/container.yaml"
updated_at: "2025-12-21 04:09:06.455681"
latest: "0.4.2.1--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/fastlin"
aliases:
 - "fastlin"
versions:
 - "0.1.0--h4349ce8_0"
 - "0.2.1--h4349ce8_0"
 - "0.2.2.1--h4349ce8_0"
 - "0.2.3--h4349ce8_0"
 - "0.4.1--h4349ce8_0"
 - "0.3.0--h4349ce8_1"
 - "0.4.2--h4349ce8_0"
 - "0.4.2.1--h4349ce8_0"
description: "singularity registry hpc automated addition for fastlin"
config: {"url": "https://biocontainers.pro/tools/fastlin", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fastlin", "latest": {"0.4.2.1--h4349ce8_0": "sha256:976d9dd2ef1dc638e4d62a64566977690e4a38b8752c9b5c6325f3b40e59377c"}, "tags": {"0.1.0--h4349ce8_0": "sha256:93de3f55be37f5e365a5ab5436cbfa2cfe7ee48c79fb64e2cb86cfddfedafb9f", "0.2.1--h4349ce8_0": "sha256:b565e47d99a9caa196133d230a98fae92a30e3ad0d40721782efa0be12f33f99", "0.2.2.1--h4349ce8_0": "sha256:e63c487d1435dc1b1d420db34e6f4251492cd59a471cdac4813fae15b53c428c", "0.2.3--h4349ce8_0": "sha256:02b64254f7a4c187b2c268fb4dfe88d38e66c241b86f0a9e131bbaa397d133c5", "0.4.1--h4349ce8_0": "sha256:adf2c4dfd96c114ff2f544290520f1e76f5e6d88b7b702a211f6acacc3d552cb", "0.3.0--h4349ce8_1": "sha256:1308699a30d62dab5e6d0851f550618d3e627babe95316e7869f22ee98a57bed", "0.4.2--h4349ce8_0": "sha256:8c0a53158ce93f8fc27d1a2970c3c87be285809d37d519ade17e9ea2750aee11", "0.4.2.1--h4349ce8_0": "sha256:976d9dd2ef1dc638e4d62a64566977690e4a38b8752c9b5c6325f3b40e59377c"}, "docker": "quay.io/biocontainers/fastlin", "aliases": {"fastlin": "/usr/local/bin/fastlin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastlin.
singularity registry hpc automated addition for fastlin
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastlin
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastlin:0.4.2.1--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastlin/0.4.2.1--h4349ce8_0
$ module help quay.io/biocontainers/fastlin/0.4.2.1--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastlin-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastlin-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastlin-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastlin-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastlin-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastlin-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastlin

```bash
$ singularity exec <container> /usr/local/bin/fastlin
$ podman run --it --rm --entrypoint /usr/local/bin/fastlin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastlin   -v ${PWD} -w ${PWD} <container> -c " $@"
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