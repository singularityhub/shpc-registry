---
layout: container
name:  "quay.io/biocontainers/sbg-cwl-runner"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sbg-cwl-runner/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/sbg-cwl-runner/container.yaml"
updated_at: "2022-10-27 00:21:47.368856"
latest: "2018.11--py_1"
container_url: "https://biocontainers.pro/tools/sbg-cwl-runner"
aliases:
 - "sbg-cwl-runner"
versions:
 - "2018.11--py_1"
description: "shpc-registry automated BioContainers addition for sbg-cwl-runner"
config: {"url": "https://biocontainers.pro/tools/sbg-cwl-runner", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sbg-cwl-runner", "latest": {"2018.11--py_1": "sha256:3f6d5bb90e4ac0e8274396484b3efb3c2eae2360fd02c05bb51939b7d7377cfa"}, "tags": {"2018.11--py_1": "sha256:3f6d5bb90e4ac0e8274396484b3efb3c2eae2360fd02c05bb51939b7d7377cfa"}, "docker": "quay.io/biocontainers/sbg-cwl-runner", "aliases": {"sbg-cwl-runner": "/usr/local/bin/sbg-cwl-runner"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sbg-cwl-runner.
shpc-registry automated BioContainers addition for sbg-cwl-runner
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sbg-cwl-runner
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sbg-cwl-runner:2018.11--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sbg-cwl-runner/2018.11--py_1
$ module help quay.io/biocontainers/sbg-cwl-runner/2018.11--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sbg-cwl-runner-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sbg-cwl-runner-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sbg-cwl-runner-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sbg-cwl-runner-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sbg-cwl-runner-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sbg-cwl-runner-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sbg-cwl-runner

```bash
$ singularity exec <container> /usr/local/bin/sbg-cwl-runner
$ podman run --it --rm --entrypoint /usr/local/bin/sbg-cwl-runner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sbg-cwl-runner   -v ${PWD} -w ${PWD} <container> -c " $@"
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