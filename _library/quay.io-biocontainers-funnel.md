---
layout: container
name:  "quay.io/biocontainers/funnel"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/funnel/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/funnel/container.yaml"
updated_at: "2025-05-23 03:26:16.766908"
latest: "0.9.0--0"
container_url: "https://biocontainers.pro/tools/funnel"
aliases:
 - "funnel"
versions:
 - "0.9.0--0"
description: "shpc-registry automated BioContainers addition for funnel"
config: {"url": "https://biocontainers.pro/tools/funnel", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for funnel", "latest": {"0.9.0--0": "sha256:35c0536dd2283e197b83163a8518d0ffb7851f1c198790d14556f39f239cbe54"}, "tags": {"0.9.0--0": "sha256:35c0536dd2283e197b83163a8518d0ffb7851f1c198790d14556f39f239cbe54"}, "docker": "quay.io/biocontainers/funnel", "aliases": {"funnel": "/usr/local/bin/funnel"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/funnel.
shpc-registry automated BioContainers addition for funnel
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/funnel
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/funnel:0.9.0--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/funnel/0.9.0--0
$ module help quay.io/biocontainers/funnel/0.9.0--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### funnel-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### funnel-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### funnel-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### funnel-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### funnel-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### funnel-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### funnel

```bash
$ singularity exec <container> /usr/local/bin/funnel
$ podman run --it --rm --entrypoint /usr/local/bin/funnel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/funnel   -v ${PWD} -w ${PWD} <container> -c " $@"
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