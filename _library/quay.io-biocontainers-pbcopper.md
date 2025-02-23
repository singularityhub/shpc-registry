---
layout: container
name:  "quay.io/biocontainers/pbcopper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pbcopper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pbcopper/container.yaml"
updated_at: "2025-02-23 03:24:02.095907"
latest: "2.3.0--h4ac6f70_3"
container_url: "https://biocontainers.pro/tools/pbcopper"

versions:
 - "2.0.0--ha04c180_1"
 - "2.2.0--ha04c180_0"
 - "2.2.0--hfce7173_2"
 - "2.3.0--hfce7173_0"
 - "2.3.0--h4ac6f70_3"
description: "shpc-registry automated BioContainers addition for pbcopper"
config: {"url": "https://biocontainers.pro/tools/pbcopper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pbcopper", "latest": {"2.3.0--h4ac6f70_3": "sha256:5dafdf3bfc07074a92c8ef46f6db23dace86207d75a3ccf8c3e1fe17a1c01d03"}, "tags": {"2.0.0--ha04c180_1": "sha256:36a7dc44485e8c5103ca3528112c58d43e60c246d44e65ea270ffbfa144bee5f", "2.2.0--ha04c180_0": "sha256:f95994cca53ac39252bcd1af34d5382064eb644eb7087207bf53331a49f2962d", "2.2.0--hfce7173_2": "sha256:4a14941e4123cd8ac1272f9a373ed5c6515e25c514e180b2448f8a22bb262494", "2.3.0--hfce7173_0": "sha256:c7d15e5b3e5a0a4baa67bb4b9c5a3e334e64e2c1558fe22f2e94c295b479744b", "2.3.0--h4ac6f70_3": "sha256:5dafdf3bfc07074a92c8ef46f6db23dace86207d75a3ccf8c3e1fe17a1c01d03"}, "docker": "quay.io/biocontainers/pbcopper"}
---

This module is a singularity container wrapper for quay.io/biocontainers/pbcopper.
shpc-registry automated BioContainers addition for pbcopper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pbcopper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pbcopper:2.3.0--h4ac6f70_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pbcopper/2.3.0--h4ac6f70_3
$ module help quay.io/biocontainers/pbcopper/2.3.0--h4ac6f70_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pbcopper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pbcopper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pbcopper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pbcopper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pbcopper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pbcopper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### pbcopper

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