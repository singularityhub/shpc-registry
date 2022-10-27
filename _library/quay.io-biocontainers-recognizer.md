---
layout: container
name:  "quay.io/biocontainers/recognizer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/recognizer/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/recognizer/container.yaml"
updated_at: "2022-10-27 00:19:20.656150"
latest: "1.8.3--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/recognizer"
aliases:
 - "recognizer.py"
versions:
 - "1.8.3--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for recognizer"
config: {"url": "https://biocontainers.pro/tools/recognizer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for recognizer", "latest": {"1.8.3--hdfd78af_0": "sha256:60847fe452ed6e4f4c30a677c8ecea0b4f788acbcc8ab44514a6355c0b4e5275"}, "tags": {"1.8.3--hdfd78af_0": "sha256:60847fe452ed6e4f4c30a677c8ecea0b4f788acbcc8ab44514a6355c0b4e5275"}, "docker": "quay.io/biocontainers/recognizer", "aliases": {"recognizer.py": "/usr/local/bin/recognizer.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/recognizer.
shpc-registry automated BioContainers addition for recognizer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/recognizer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/recognizer:1.8.3--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/recognizer/1.8.3--hdfd78af_0
$ module help quay.io/biocontainers/recognizer/1.8.3--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### recognizer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### recognizer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### recognizer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### recognizer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### recognizer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### recognizer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### recognizer.py

```bash
$ singularity exec <container> /usr/local/bin/recognizer.py
$ podman run --it --rm --entrypoint /usr/local/bin/recognizer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/recognizer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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