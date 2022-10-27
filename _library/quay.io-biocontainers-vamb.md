---
layout: container
name:  "quay.io/biocontainers/vamb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vamb/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/vamb/container.yaml"
updated_at: "2022-10-27 00:21:26.876382"
latest: "3.0.2--py37h8902056_2"
container_url: "https://biocontainers.pro/tools/vamb"
aliases:
 - "concatenate.py"
 - "vamb"
versions:
 - "3.0.2--py37h8902056_2"
description: "shpc-registry automated BioContainers addition for vamb"
config: {"url": "https://biocontainers.pro/tools/vamb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for vamb", "latest": {"3.0.2--py37h8902056_2": "sha256:f6c3eae18439c3bbdac47d72242a37e9df5ef82bfe1c54749dfaac1914202bf1"}, "tags": {"3.0.2--py37h8902056_2": "sha256:f6c3eae18439c3bbdac47d72242a37e9df5ef82bfe1c54749dfaac1914202bf1"}, "docker": "quay.io/biocontainers/vamb", "aliases": {"concatenate.py": "/usr/local/bin/concatenate.py", "vamb": "/usr/local/bin/vamb"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vamb.
shpc-registry automated BioContainers addition for vamb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vamb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vamb:3.0.2--py37h8902056_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vamb/3.0.2--py37h8902056_2
$ module help quay.io/biocontainers/vamb/3.0.2--py37h8902056_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vamb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vamb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vamb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vamb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vamb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vamb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### concatenate.py

```bash
$ singularity exec <container> /usr/local/bin/concatenate.py
$ podman run --it --rm --entrypoint /usr/local/bin/concatenate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/concatenate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vamb

```bash
$ singularity exec <container> /usr/local/bin/vamb
$ podman run --it --rm --entrypoint /usr/local/bin/vamb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vamb   -v ${PWD} -w ${PWD} <container> -c " $@"
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