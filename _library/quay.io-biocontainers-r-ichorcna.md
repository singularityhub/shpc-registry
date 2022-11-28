---
layout: container
name:  "quay.io/biocontainers/r-ichorcna"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-ichorcna/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-ichorcna/container.yaml"
updated_at: "2022-11-27 23:56:12.490343"
latest: "0.3.2--r41hdfd78af_1"
container_url: "https://biocontainers.pro/tools/r-ichorcna"
aliases:
 - "createPanelOfNormals.R"
 - "runIchorCNA.R"
versions:
 - "0.3.2--r41hdfd78af_1"
description: "shpc-registry automated BioContainers addition for r-ichorcna"
config: {"url": "https://biocontainers.pro/tools/r-ichorcna", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-ichorcna", "latest": {"0.3.2--r41hdfd78af_1": "sha256:03e5a912ec6db75c41d7f8660b061cbda4b9256b9d5fce96de5560a96f43d8a7"}, "tags": {"0.3.2--r41hdfd78af_1": "sha256:03e5a912ec6db75c41d7f8660b061cbda4b9256b9d5fce96de5560a96f43d8a7"}, "docker": "quay.io/biocontainers/r-ichorcna", "aliases": {"createPanelOfNormals.R": "/usr/local/bin/createPanelOfNormals.R", "runIchorCNA.R": "/usr/local/bin/runIchorCNA.R"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-ichorcna.
shpc-registry automated BioContainers addition for r-ichorcna
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-ichorcna
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-ichorcna:0.3.2--r41hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-ichorcna/0.3.2--r41hdfd78af_1
$ module help quay.io/biocontainers/r-ichorcna/0.3.2--r41hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-ichorcna-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-ichorcna-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-ichorcna-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-ichorcna-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-ichorcna-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-ichorcna-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### createPanelOfNormals.R

```bash
$ singularity exec <container> /usr/local/bin/createPanelOfNormals.R
$ podman run --it --rm --entrypoint /usr/local/bin/createPanelOfNormals.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/createPanelOfNormals.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runIchorCNA.R

```bash
$ singularity exec <container> /usr/local/bin/runIchorCNA.R
$ podman run --it --rm --entrypoint /usr/local/bin/runIchorCNA.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runIchorCNA.R   -v ${PWD} -w ${PWD} <container> -c " $@"
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