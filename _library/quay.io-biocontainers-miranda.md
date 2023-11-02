---
layout: container
name:  "quay.io/biocontainers/miranda"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/miranda/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/miranda/container.yaml"
updated_at: "2023-11-02 03:41:51.925285"
latest: "3.3a--h031d066_6"
container_url: "https://biocontainers.pro/tools/miranda"
aliases:
 - "miranda"
versions:
 - "3.3a--hec16e2b_4"
 - "3.3a--h031d066_6"
description: "shpc-registry automated BioContainers addition for miranda"
config: {"url": "https://biocontainers.pro/tools/miranda", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for miranda", "latest": {"3.3a--h031d066_6": "sha256:94665640c12048259d9e1edd3b582ae7ed4ce325b7c3bf52dd4e1720911f20f6"}, "tags": {"3.3a--hec16e2b_4": "sha256:5681a6107514bb7156eafba3e6784a4b83d768454dea9b14f93968640ac2f0aa", "3.3a--h031d066_6": "sha256:94665640c12048259d9e1edd3b582ae7ed4ce325b7c3bf52dd4e1720911f20f6"}, "docker": "quay.io/biocontainers/miranda", "aliases": {"miranda": "/usr/local/bin/miranda"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/miranda.
shpc-registry automated BioContainers addition for miranda
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/miranda
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/miranda:3.3a--h031d066_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/miranda/3.3a--h031d066_6
$ module help quay.io/biocontainers/miranda/3.3a--h031d066_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### miranda-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### miranda-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### miranda-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### miranda-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### miranda-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### miranda-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### miranda

```bash
$ singularity exec <container> /usr/local/bin/miranda
$ podman run --it --rm --entrypoint /usr/local/bin/miranda   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miranda   -v ${PWD} -w ${PWD} <container> -c " $@"
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