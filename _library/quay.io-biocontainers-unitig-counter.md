---
layout: container
name:  "quay.io/biocontainers/unitig-counter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/unitig-counter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/unitig-counter/container.yaml"
updated_at: "2023-10-05 02:53:54.777408"
latest: "1.1.0--h56fc30b_0"
container_url: "https://biocontainers.pro/tools/unitig-counter"
aliases:
 - "cdbg-ops"
 - "gatb-h5dump"
 - "unitig-counter"
versions:
 - "1.1.0--h56fc30b_0"
description: "shpc-registry automated BioContainers addition for unitig-counter"
config: {"url": "https://biocontainers.pro/tools/unitig-counter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for unitig-counter", "latest": {"1.1.0--h56fc30b_0": "sha256:ae6f8424538cf528728dfa0979619e3b742b67551bd8b34007768949d1ac4d19"}, "tags": {"1.1.0--h56fc30b_0": "sha256:ae6f8424538cf528728dfa0979619e3b742b67551bd8b34007768949d1ac4d19"}, "docker": "quay.io/biocontainers/unitig-counter", "aliases": {"cdbg-ops": "/usr/local/bin/cdbg-ops", "gatb-h5dump": "/usr/local/bin/gatb-h5dump", "unitig-counter": "/usr/local/bin/unitig-counter"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/unitig-counter.
shpc-registry automated BioContainers addition for unitig-counter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/unitig-counter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/unitig-counter:1.1.0--h56fc30b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/unitig-counter/1.1.0--h56fc30b_0
$ module help quay.io/biocontainers/unitig-counter/1.1.0--h56fc30b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### unitig-counter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### unitig-counter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### unitig-counter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### unitig-counter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### unitig-counter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### unitig-counter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cdbg-ops

```bash
$ singularity exec <container> /usr/local/bin/cdbg-ops
$ podman run --it --rm --entrypoint /usr/local/bin/cdbg-ops   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cdbg-ops   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gatb-h5dump

```bash
$ singularity exec <container> /usr/local/bin/gatb-h5dump
$ podman run --it --rm --entrypoint /usr/local/bin/gatb-h5dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gatb-h5dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unitig-counter

```bash
$ singularity exec <container> /usr/local/bin/unitig-counter
$ podman run --it --rm --entrypoint /usr/local/bin/unitig-counter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unitig-counter   -v ${PWD} -w ${PWD} <container> -c " $@"
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