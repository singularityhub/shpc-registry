---
layout: container
name:  "quay.io/biocontainers/spoa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/spoa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/spoa/container.yaml"
updated_at: "2024-04-07 02:56:11.957359"
latest: "4.1.4--hdcf5f25_0"
container_url: "https://biocontainers.pro/tools/spoa"
aliases:
 - "spoa"
versions:
 - "4.0.7--hd03093a_3"
 - "4.0.7--hd03093a_4"
 - "4.0.7--hdcf5f25_5"
 - "4.0.8--hdcf5f25_0"
 - "4.1.2--hdcf5f25_0"
 - "4.1.3--hdcf5f25_0"
 - "4.1.4--hdcf5f25_0"
description: "shpc-registry automated BioContainers addition for spoa"
config: {"url": "https://biocontainers.pro/tools/spoa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for spoa", "latest": {"4.1.4--hdcf5f25_0": "sha256:c066476d110e5780b1dacbc50d110254a48fb7edf014adc35df1363af9b7a4bf"}, "tags": {"4.0.7--hd03093a_3": "sha256:5a2fd9bee52f97f543cc2036767268e67d73ce21be6bfdc1863ea0f04bc0341c", "4.0.7--hd03093a_4": "sha256:4e098a4866e6b860c334cd47dcfe11c0e0c3110936dd87c1c6f37a276957920d", "4.0.7--hdcf5f25_5": "sha256:0d3f093053262b9e973eecaa2a9c6cb61ab39e695957284a0bfb4f289b171602", "4.0.8--hdcf5f25_0": "sha256:211616908bcb8ce65bd43b4c3f7beb10184a54193e276c25f989288daa12aa75", "4.1.2--hdcf5f25_0": "sha256:edb0e8daa9eef17d61f80efdc7f36f8b46751dc6d1a24894d6abb4a2219f0e46", "4.1.3--hdcf5f25_0": "sha256:a32d65d313b4f3bc716343b648b65c4c381708f7cf70456504fe61aea015ef01", "4.1.4--hdcf5f25_0": "sha256:c066476d110e5780b1dacbc50d110254a48fb7edf014adc35df1363af9b7a4bf"}, "docker": "quay.io/biocontainers/spoa", "aliases": {"spoa": "/usr/local/bin/spoa"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/spoa.
shpc-registry automated BioContainers addition for spoa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/spoa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/spoa:4.1.4--hdcf5f25_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/spoa/4.1.4--hdcf5f25_0
$ module help quay.io/biocontainers/spoa/4.1.4--hdcf5f25_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### spoa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### spoa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### spoa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### spoa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### spoa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### spoa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### spoa

```bash
$ singularity exec <container> /usr/local/bin/spoa
$ podman run --it --rm --entrypoint /usr/local/bin/spoa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spoa   -v ${PWD} -w ${PWD} <container> -c " $@"
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