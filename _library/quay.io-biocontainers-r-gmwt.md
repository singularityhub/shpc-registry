---
layout: container
name:  "quay.io/biocontainers/r-gmwt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-gmwt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-gmwt/container.yaml"
updated_at: "2024-05-21 03:07:13.923426"
latest: "1.2--r42h25def4e_1"
container_url: "https://biocontainers.pro/tools/r-gmwt"

versions:
 - "1.1.1--r41h25def4e_5"
 - "1.2--r42h25def4e_1"
description: "shpc-registry automated BioContainers addition for r-gmwt"
config: {"url": "https://biocontainers.pro/tools/r-gmwt", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-gmwt", "latest": {"1.2--r42h25def4e_1": "sha256:766ced7c8230e6079f6a1ce2bdc806d450457aea71982adf1777cb2669ae108b"}, "tags": {"1.1.1--r41h25def4e_5": "sha256:2fc0c75c7d600bd7444a3ef317f16ba38751b477c8a636a8b3ea76eba894956b", "1.2--r42h25def4e_1": "sha256:766ced7c8230e6079f6a1ce2bdc806d450457aea71982adf1777cb2669ae108b"}, "docker": "quay.io/biocontainers/r-gmwt"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-gmwt.
shpc-registry automated BioContainers addition for r-gmwt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-gmwt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-gmwt:1.2--r42h25def4e_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-gmwt/1.2--r42h25def4e_1
$ module help quay.io/biocontainers/r-gmwt/1.2--r42h25def4e_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-gmwt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-gmwt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-gmwt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-gmwt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-gmwt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-gmwt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-gmwt

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