---
layout: container
name:  "quay.io/biocontainers/qsignature"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/qsignature/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/qsignature/container.yaml"
updated_at: "2022-10-27 00:18:17.613486"
latest: "0.1pre--hdfd78af_5"
container_url: "https://biocontainers.pro/tools/qsignature"
aliases:
 - "qsignature"
versions:
 - "0.1pre--hdfd78af_5"
description: "shpc-registry automated BioContainers addition for qsignature"
config: {"url": "https://biocontainers.pro/tools/qsignature", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for qsignature", "latest": {"0.1pre--hdfd78af_5": "sha256:d3498ae1ab91cab4c06fb2e6c502ddd332ba0ae89903311b13f34879058a6bff"}, "tags": {"0.1pre--hdfd78af_5": "sha256:d3498ae1ab91cab4c06fb2e6c502ddd332ba0ae89903311b13f34879058a6bff"}, "docker": "quay.io/biocontainers/qsignature", "aliases": {"qsignature": "/usr/local/bin/qsignature"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/qsignature.
shpc-registry automated BioContainers addition for qsignature
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/qsignature
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/qsignature:0.1pre--hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/qsignature/0.1pre--hdfd78af_5
$ module help quay.io/biocontainers/qsignature/0.1pre--hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### qsignature-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### qsignature-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### qsignature-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### qsignature-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### qsignature-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### qsignature-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### qsignature

```bash
$ singularity exec <container> /usr/local/bin/qsignature
$ podman run --it --rm --entrypoint /usr/local/bin/qsignature   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qsignature   -v ${PWD} -w ${PWD} <container> -c " $@"
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