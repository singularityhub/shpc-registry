---
layout: container
name:  "quay.io/biocontainers/r-tcr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-tcr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-tcr/container.yaml"
updated_at: "2026-01-12 04:36:05.050944"
latest: "2.3.2--r44h40dc89f_7"
container_url: "https://biocontainers.pro/tools/r-tcr"

versions:
 - "2.3.2--r41hecf12ef_3"
 - "2.3.2--r42hecf12ef_4"
 - "2.3.2--r42h21a89ab_5"
 - "2.3.2--r43h21a89ab_6"
 - "2.3.2--r44h40dc89f_7"
description: "shpc-registry automated BioContainers addition for r-tcr"
config: {"url": "https://biocontainers.pro/tools/r-tcr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-tcr", "latest": {"2.3.2--r44h40dc89f_7": "sha256:300a186828447f23aebb3bb341f947eacb225e6ae7dad26f0930317ca9cad9d0"}, "tags": {"2.3.2--r41hecf12ef_3": "sha256:4829ab11db22d5d3eab1fb791552355fe50ab4fe854d54802376889ab98c9502", "2.3.2--r42hecf12ef_4": "sha256:aafb0f622d3b438d931ba3ea705c95a42982b247609c43bd1d778f3cc81f2385", "2.3.2--r42h21a89ab_5": "sha256:78c08ffda3478a2b51332bc74e29879404e2a0a0c9752f6d9f84e9cdb3de7c9b", "2.3.2--r43h21a89ab_6": "sha256:413dbfa18bb6d3199139b560240efb71ba0019e3f9a2a4b0cf5df3ea662194c3", "2.3.2--r44h40dc89f_7": "sha256:300a186828447f23aebb3bb341f947eacb225e6ae7dad26f0930317ca9cad9d0"}, "docker": "quay.io/biocontainers/r-tcr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-tcr.
shpc-registry automated BioContainers addition for r-tcr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-tcr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-tcr:2.3.2--r44h40dc89f_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-tcr/2.3.2--r44h40dc89f_7
$ module help quay.io/biocontainers/r-tcr/2.3.2--r44h40dc89f_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-tcr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-tcr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-tcr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-tcr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-tcr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-tcr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-tcr

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