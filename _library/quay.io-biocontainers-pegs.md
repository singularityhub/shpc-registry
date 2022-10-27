---
layout: container
name:  "quay.io/biocontainers/pegs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pegs/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pegs/container.yaml"
updated_at: "2022-10-27 01:14:38.517964"
latest: "0.6.5--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/pegs"
aliases:
 - "mk_pegs_intervals"
 - "pegs"
versions:
 - "0.6.5--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for pegs"
config: {"url": "https://biocontainers.pro/tools/pegs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pegs", "latest": {"0.6.5--pyhdfd78af_0": "sha256:28a2396e216472ab8e4d62e6763ca87b34bab8c690ee412153bc5ca61bd5d48c"}, "tags": {"0.6.5--pyhdfd78af_0": "sha256:28a2396e216472ab8e4d62e6763ca87b34bab8c690ee412153bc5ca61bd5d48c"}, "docker": "quay.io/biocontainers/pegs", "aliases": {"mk_pegs_intervals": "/usr/local/bin/mk_pegs_intervals", "pegs": "/usr/local/bin/pegs"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pegs.
shpc-registry automated BioContainers addition for pegs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pegs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pegs:0.6.5--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pegs/0.6.5--pyhdfd78af_0
$ module help quay.io/biocontainers/pegs/0.6.5--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pegs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pegs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pegs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pegs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pegs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pegs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mk_pegs_intervals

```bash
$ singularity exec <container> /usr/local/bin/mk_pegs_intervals
$ podman run --it --rm --entrypoint /usr/local/bin/mk_pegs_intervals   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mk_pegs_intervals   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pegs

```bash
$ singularity exec <container> /usr/local/bin/pegs
$ podman run --it --rm --entrypoint /usr/local/bin/pegs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pegs   -v ${PWD} -w ${PWD} <container> -c " $@"
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