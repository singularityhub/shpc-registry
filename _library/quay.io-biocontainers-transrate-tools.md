---
layout: container
name:  "quay.io/biocontainers/transrate-tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/transrate-tools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/transrate-tools/container.yaml"
updated_at: "2025-10-14 03:29:06.449523"
latest: "1.0.0--h2bd4fab_10"
container_url: "https://biocontainers.pro/tools/transrate-tools"
aliases:
 - "bam-read"
versions:
 - "1.0.0--ha7703dc_8"
 - "1.0.0--h2bd4fab_10"
description: "shpc-registry automated BioContainers addition for transrate-tools"
config: {"url": "https://biocontainers.pro/tools/transrate-tools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for transrate-tools", "latest": {"1.0.0--h2bd4fab_10": "sha256:765f220e7476a867073489fb25f548034d0b55827d9d9729582c12df375122b9"}, "tags": {"1.0.0--ha7703dc_8": "sha256:6137af01b3ad7c6431b47e62a823bfb34b018900316154d0aa634065e24c29ec", "1.0.0--h2bd4fab_10": "sha256:765f220e7476a867073489fb25f548034d0b55827d9d9729582c12df375122b9"}, "docker": "quay.io/biocontainers/transrate-tools", "aliases": {"bam-read": "/usr/local/bin/bam-read"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/transrate-tools.
shpc-registry automated BioContainers addition for transrate-tools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/transrate-tools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/transrate-tools:1.0.0--h2bd4fab_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/transrate-tools/1.0.0--h2bd4fab_10
$ module help quay.io/biocontainers/transrate-tools/1.0.0--h2bd4fab_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### transrate-tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### transrate-tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### transrate-tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### transrate-tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### transrate-tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### transrate-tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bam-read

```bash
$ singularity exec <container> /usr/local/bin/bam-read
$ podman run --it --rm --entrypoint /usr/local/bin/bam-read   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam-read   -v ${PWD} -w ${PWD} <container> -c " $@"
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