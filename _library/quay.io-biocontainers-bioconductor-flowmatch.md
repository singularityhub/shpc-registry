---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowmatch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowmatch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowmatch/container.yaml"
updated_at: "2023-02-09 03:13:19.817939"
latest: "1.34.0--r42hc247a5b_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flowmatch"

versions:
 - "1.30.0--r41hc247a5b_2"
 - "1.34.0--r42hc247a5b_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flowmatch"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowmatch", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowmatch", "latest": {"1.34.0--r42hc247a5b_0": "sha256:ebd16a5956c7c3983341be7045cb17cd5b9ee91e622d58c8b76f5177fdb79f6f"}, "tags": {"1.30.0--r41hc247a5b_2": "sha256:aa7ba3de9b624ac2a3bc015f624fdaa8f5dd3f93f3fb1eb36a228deb597a4677", "1.34.0--r42hc247a5b_0": "sha256:ebd16a5956c7c3983341be7045cb17cd5b9ee91e622d58c8b76f5177fdb79f6f"}, "docker": "quay.io/biocontainers/bioconductor-flowmatch"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowmatch.
shpc-registry automated BioContainers addition for bioconductor-flowmatch
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowmatch
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowmatch:1.34.0--r42hc247a5b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowmatch/1.34.0--r42hc247a5b_0
$ module help quay.io/biocontainers/bioconductor-flowmatch/1.34.0--r42hc247a5b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowmatch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowmatch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowmatch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowmatch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowmatch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowmatch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-flowmatch

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