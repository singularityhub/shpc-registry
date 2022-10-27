---
layout: container
name:  "quay.io/biocontainers/submission-tool-validator"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/submission-tool-validator/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/submission-tool-validator/container.yaml"
updated_at: "2022-10-27 01:03:28.949952"
latest: "1.0.7--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/submission-tool-validator"
aliases:
 - "submission-tool-validator"
versions:
 - "1.0.7--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for submission-tool-validator"
config: {"url": "https://biocontainers.pro/tools/submission-tool-validator", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for submission-tool-validator", "latest": {"1.0.7--hdfd78af_0": "sha256:397fbf415b7637596626b61d6a4046bf3facf0b707d587e3b80affea67f95a02"}, "tags": {"1.0.7--hdfd78af_0": "sha256:397fbf415b7637596626b61d6a4046bf3facf0b707d587e3b80affea67f95a02"}, "docker": "quay.io/biocontainers/submission-tool-validator", "aliases": {"submission-tool-validator": "/usr/local/bin/submission-tool-validator"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/submission-tool-validator.
shpc-registry automated BioContainers addition for submission-tool-validator
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/submission-tool-validator
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/submission-tool-validator:1.0.7--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/submission-tool-validator/1.0.7--hdfd78af_0
$ module help quay.io/biocontainers/submission-tool-validator/1.0.7--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### submission-tool-validator-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### submission-tool-validator-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### submission-tool-validator-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### submission-tool-validator-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### submission-tool-validator-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### submission-tool-validator-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### submission-tool-validator

```bash
$ singularity exec <container> /usr/local/bin/submission-tool-validator
$ podman run --it --rm --entrypoint /usr/local/bin/submission-tool-validator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/submission-tool-validator   -v ${PWD} -w ${PWD} <container> -c " $@"
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