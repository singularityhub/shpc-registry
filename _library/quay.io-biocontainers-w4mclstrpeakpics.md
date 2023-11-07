---
layout: container
name:  "quay.io/biocontainers/w4mclstrpeakpics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/w4mclstrpeakpics/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/w4mclstrpeakpics/container.yaml"
updated_at: "2023-11-07 02:47:31.327930"
latest: "0.98.1--r351_1"
container_url: "https://biocontainers.pro/tools/w4mclstrpeakpics"

versions:
 - "0.98.1--r351_1"
description: "shpc-registry automated BioContainers addition for w4mclstrpeakpics"
config: {"url": "https://biocontainers.pro/tools/w4mclstrpeakpics", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for w4mclstrpeakpics", "latest": {"0.98.1--r351_1": "sha256:c474a6bf024776b3fb303c8bc8325ee4dda57ec3efb72b2629d3b55024eb042a"}, "tags": {"0.98.1--r351_1": "sha256:c474a6bf024776b3fb303c8bc8325ee4dda57ec3efb72b2629d3b55024eb042a"}, "docker": "quay.io/biocontainers/w4mclstrpeakpics"}
---

This module is a singularity container wrapper for quay.io/biocontainers/w4mclstrpeakpics.
shpc-registry automated BioContainers addition for w4mclstrpeakpics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/w4mclstrpeakpics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/w4mclstrpeakpics:0.98.1--r351_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/w4mclstrpeakpics/0.98.1--r351_1
$ module help quay.io/biocontainers/w4mclstrpeakpics/0.98.1--r351_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### w4mclstrpeakpics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### w4mclstrpeakpics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### w4mclstrpeakpics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### w4mclstrpeakpics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### w4mclstrpeakpics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### w4mclstrpeakpics-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### w4mclstrpeakpics

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