---
layout: container
name:  "quay.io/biocontainers/tr-trimmer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tr-trimmer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tr-trimmer/container.yaml"
updated_at: "2025-08-14 03:55:17.001529"
latest: "0.4.0--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/tr-trimmer"
aliases:
 - "tr-trimmer"
versions:
 - "0.1.0--h4349ce8_0"
 - "0.2.0--h4349ce8_0"
 - "0.4.0--h4349ce8_0"
 - "0.3.0--h4349ce8_0"
description: "singularity registry hpc automated addition for tr-trimmer"
config: {"url": "https://biocontainers.pro/tools/tr-trimmer", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for tr-trimmer", "latest": {"0.4.0--h4349ce8_0": "sha256:8dd15f8d569a22c63f1e28f6bc032878cddc1649897a382cb6a596dfd560dd6f"}, "tags": {"0.1.0--h4349ce8_0": "sha256:48c33d78b12c93ff421f8ad5e925839a241fd34d29ee2e66a41c27e696b7da44", "0.2.0--h4349ce8_0": "sha256:5e1f6e4d80f364d343f2bf3ca4754346f54064f866f198b7b95b1ad178acfa8f", "0.4.0--h4349ce8_0": "sha256:8dd15f8d569a22c63f1e28f6bc032878cddc1649897a382cb6a596dfd560dd6f", "0.3.0--h4349ce8_0": "sha256:471c6bb8e8d6194018ef50413ae98065f7fbc1a1eb9b58972d6dd4e940760cbf"}, "docker": "quay.io/biocontainers/tr-trimmer", "aliases": {"tr-trimmer": "/usr/local/bin/tr-trimmer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tr-trimmer.
singularity registry hpc automated addition for tr-trimmer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tr-trimmer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tr-trimmer:0.4.0--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tr-trimmer/0.4.0--h4349ce8_0
$ module help quay.io/biocontainers/tr-trimmer/0.4.0--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tr-trimmer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tr-trimmer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tr-trimmer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tr-trimmer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tr-trimmer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tr-trimmer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tr-trimmer

```bash
$ singularity exec <container> /usr/local/bin/tr-trimmer
$ podman run --it --rm --entrypoint /usr/local/bin/tr-trimmer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tr-trimmer   -v ${PWD} -w ${PWD} <container> -c " $@"
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