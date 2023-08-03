---
layout: container
name:  "quay.io/biocontainers/r-bseqsc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-bseqsc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-bseqsc/container.yaml"
updated_at: "2023-08-03 03:23:57.957248"
latest: "1.0--r43hdfd78af_3"
container_url: "https://biocontainers.pro/tools/r-bseqsc"

versions:
 - "1.0--r41hdfd78af_1"
 - "1.0--r42hdfd78af_2"
 - "1.0--r43hdfd78af_3"
description: "shpc-registry automated BioContainers addition for r-bseqsc"
config: {"url": "https://biocontainers.pro/tools/r-bseqsc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-bseqsc", "latest": {"1.0--r43hdfd78af_3": "sha256:cd71a4c5f28427f142655a2703f9f3c403221e9959d7b193d8851f8e5d5271d9"}, "tags": {"1.0--r41hdfd78af_1": "sha256:4e4ecca76f5b96cf2285a31cafa8ab4576d5afc79a8274d91f449909f9d366a2", "1.0--r42hdfd78af_2": "sha256:2ecdf603b33718033c3e0d044460266cbce1efc8e8488838c4dda6ebcbee0dee", "1.0--r43hdfd78af_3": "sha256:cd71a4c5f28427f142655a2703f9f3c403221e9959d7b193d8851f8e5d5271d9"}, "docker": "quay.io/biocontainers/r-bseqsc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-bseqsc.
shpc-registry automated BioContainers addition for r-bseqsc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-bseqsc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-bseqsc:1.0--r43hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-bseqsc/1.0--r43hdfd78af_3
$ module help quay.io/biocontainers/r-bseqsc/1.0--r43hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-bseqsc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-bseqsc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-bseqsc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-bseqsc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-bseqsc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-bseqsc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-bseqsc

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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