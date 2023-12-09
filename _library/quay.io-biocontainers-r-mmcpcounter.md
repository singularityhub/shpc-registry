---
layout: container
name:  "quay.io/biocontainers/r-mmcpcounter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-mmcpcounter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-mmcpcounter/container.yaml"
updated_at: "2023-12-09 03:35:03.900553"
latest: "1.1.0--r43hdfd78af_2"
container_url: "https://biocontainers.pro/tools/r-mmcpcounter"

versions:
 - "1.1.0--r41hdfd78af_0"
 - "1.1.0--r42hdfd78af_1"
 - "1.1.0--r43hdfd78af_2"
description: "shpc-registry automated BioContainers addition for r-mmcpcounter"
config: {"url": "https://biocontainers.pro/tools/r-mmcpcounter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-mmcpcounter", "latest": {"1.1.0--r43hdfd78af_2": "sha256:a15e3910375e8f1cef5ca00b6d90d2abee4e8f487ead031ca12bb7aa3e135fc8"}, "tags": {"1.1.0--r41hdfd78af_0": "sha256:a14b894273cc7155b83d92a419005dd6a6916487a05b02e1a2fbc209e81ede55", "1.1.0--r42hdfd78af_1": "sha256:dda72dda1ffa8b6da60d8b3adbfc2ce6e8541491adef91996538371773ac62b0", "1.1.0--r43hdfd78af_2": "sha256:a15e3910375e8f1cef5ca00b6d90d2abee4e8f487ead031ca12bb7aa3e135fc8"}, "docker": "quay.io/biocontainers/r-mmcpcounter"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-mmcpcounter.
shpc-registry automated BioContainers addition for r-mmcpcounter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-mmcpcounter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-mmcpcounter:1.1.0--r43hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-mmcpcounter/1.1.0--r43hdfd78af_2
$ module help quay.io/biocontainers/r-mmcpcounter/1.1.0--r43hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-mmcpcounter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-mmcpcounter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-mmcpcounter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-mmcpcounter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-mmcpcounter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-mmcpcounter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-mmcpcounter

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