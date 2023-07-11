---
layout: container
name:  "quay.io/biocontainers/fwdpy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fwdpy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fwdpy/container.yaml"
updated_at: "2023-07-11 03:37:44.397771"
latest: "0.0.4pre1--py35_gsl1.16_0"
container_url: "https://biocontainers.pro/tools/fwdpy"

versions:
 - "0.0.4pre1--py35_gsl1.16_0"
description: "shpc-registry automated BioContainers addition for fwdpy"
config: {"url": "https://biocontainers.pro/tools/fwdpy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fwdpy", "latest": {"0.0.4pre1--py35_gsl1.16_0": "sha256:d1c54dd798ce34ff6a717f3412cdcc47af58e85bb9cf4d9255f2000931cf16e0"}, "tags": {"0.0.4pre1--py35_gsl1.16_0": "sha256:d1c54dd798ce34ff6a717f3412cdcc47af58e85bb9cf4d9255f2000931cf16e0"}, "docker": "quay.io/biocontainers/fwdpy"}
---

This module is a singularity container wrapper for quay.io/biocontainers/fwdpy.
shpc-registry automated BioContainers addition for fwdpy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fwdpy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fwdpy:0.0.4pre1--py35_gsl1.16_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fwdpy/0.0.4pre1--py35_gsl1.16_0
$ module help quay.io/biocontainers/fwdpy/0.0.4pre1--py35_gsl1.16_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fwdpy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fwdpy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fwdpy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fwdpy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fwdpy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fwdpy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### fwdpy

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