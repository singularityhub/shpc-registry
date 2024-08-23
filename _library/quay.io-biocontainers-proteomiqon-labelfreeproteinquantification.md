---
layout: container
name:  "quay.io/biocontainers/proteomiqon-labelfreeproteinquantification"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/proteomiqon-labelfreeproteinquantification/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/proteomiqon-labelfreeproteinquantification/container.yaml"
updated_at: "2024-08-23 03:06:34.855671"
latest: "0.0.3--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/proteomiqon-labelfreeproteinquantification"
aliases:
 - "lttng-gen-tp"
 - "proteomiqon-labelfreeproteinquantification"
versions:
 - "0.0.1--hdfd78af_1"
 - "0.0.3--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for proteomiqon-labelfreeproteinquantification"
config: {"url": "https://biocontainers.pro/tools/proteomiqon-labelfreeproteinquantification", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for proteomiqon-labelfreeproteinquantification", "latest": {"0.0.3--hdfd78af_1": "sha256:c16fbdbc5d2827f04e6f740a3f705b82776c76dd950cc73b0d36420372454c17"}, "tags": {"0.0.1--hdfd78af_1": "sha256:a88aeba5bc8bcf845f389a7d29baa084a60fcb83e95acd21768c4a086f705677", "0.0.3--hdfd78af_1": "sha256:c16fbdbc5d2827f04e6f740a3f705b82776c76dd950cc73b0d36420372454c17"}, "docker": "quay.io/biocontainers/proteomiqon-labelfreeproteinquantification", "aliases": {"lttng-gen-tp": "/usr/local/bin/lttng-gen-tp", "proteomiqon-labelfreeproteinquantification": "/usr/local/bin/proteomiqon-labelfreeproteinquantification"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/proteomiqon-labelfreeproteinquantification.
shpc-registry automated BioContainers addition for proteomiqon-labelfreeproteinquantification
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/proteomiqon-labelfreeproteinquantification
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/proteomiqon-labelfreeproteinquantification:0.0.3--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/proteomiqon-labelfreeproteinquantification/0.0.3--hdfd78af_1
$ module help quay.io/biocontainers/proteomiqon-labelfreeproteinquantification/0.0.3--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### proteomiqon-labelfreeproteinquantification-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### proteomiqon-labelfreeproteinquantification-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### proteomiqon-labelfreeproteinquantification-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### proteomiqon-labelfreeproteinquantification-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### proteomiqon-labelfreeproteinquantification-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### proteomiqon-labelfreeproteinquantification-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lttng-gen-tp

```bash
$ singularity exec <container> /usr/local/bin/lttng-gen-tp
$ podman run --it --rm --entrypoint /usr/local/bin/lttng-gen-tp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lttng-gen-tp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proteomiqon-labelfreeproteinquantification

```bash
$ singularity exec <container> /usr/local/bin/proteomiqon-labelfreeproteinquantification
$ podman run --it --rm --entrypoint /usr/local/bin/proteomiqon-labelfreeproteinquantification   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proteomiqon-labelfreeproteinquantification   -v ${PWD} -w ${PWD} <container> -c " $@"
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