---
layout: container
name:  "quay.io/biocontainers/yara"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/yara/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/yara/container.yaml"
updated_at: "2026-01-24 04:02:12.868809"
latest: "1.0.5--haf24da9_0"
container_url: "https://biocontainers.pro/tools/yara"
aliases:
 - "yara_indexer"
 - "yara_mapper"
versions:
 - "1.0.2--h9ee0642_3"
 - "1.0.3--hd6d6fdc_0"
 - "1.0.5--haf24da9_0"
description: "shpc-registry automated BioContainers addition for yara"
config: {"url": "https://biocontainers.pro/tools/yara", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for yara", "latest": {"1.0.5--haf24da9_0": "sha256:8b8ea7d89289f9e40d6ab87490f42627a98590b2df69daf6a06c0455337f91ed"}, "tags": {"1.0.2--h9ee0642_3": "sha256:f67336baca2b0479e118507914e8daf70680c7b4e138d893f7281490fcd2e1ed", "1.0.3--hd6d6fdc_0": "sha256:7044b6e25fc49cec393cdb6fdd1816c4269cf75adea08ad172f996fa984b6394", "1.0.5--haf24da9_0": "sha256:8b8ea7d89289f9e40d6ab87490f42627a98590b2df69daf6a06c0455337f91ed"}, "docker": "quay.io/biocontainers/yara", "aliases": {"yara_indexer": "/usr/local/bin/yara_indexer", "yara_mapper": "/usr/local/bin/yara_mapper"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/yara.
shpc-registry automated BioContainers addition for yara
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/yara
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/yara:1.0.5--haf24da9_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/yara/1.0.5--haf24da9_0
$ module help quay.io/biocontainers/yara/1.0.5--haf24da9_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### yara-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### yara-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### yara-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### yara-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### yara-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### yara-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### yara_indexer

```bash
$ singularity exec <container> /usr/local/bin/yara_indexer
$ podman run --it --rm --entrypoint /usr/local/bin/yara_indexer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yara_indexer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yara_mapper

```bash
$ singularity exec <container> /usr/local/bin/yara_mapper
$ podman run --it --rm --entrypoint /usr/local/bin/yara_mapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yara_mapper   -v ${PWD} -w ${PWD} <container> -c " $@"
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