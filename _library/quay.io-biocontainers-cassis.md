---
layout: container
name:  "quay.io/biocontainers/cassis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cassis/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/cassis/container.yaml"
updated_at: "2022-10-27 00:28:46.332317"
latest: "0.0.20120106--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/cassis"
aliases:
 - "cassis"
 - "lastz"
 - "lastz_32"
 - "lastz_D"
versions:
 - "0.0.20120106--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for cassis"
config: {"url": "https://biocontainers.pro/tools/cassis", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cassis", "latest": {"0.0.20120106--hdfd78af_1": "sha256:454ce1cec842f4622a8d55fe3b59a2b0008a7252739ab819191f186565c7c0cb"}, "tags": {"0.0.20120106--hdfd78af_1": "sha256:454ce1cec842f4622a8d55fe3b59a2b0008a7252739ab819191f186565c7c0cb"}, "docker": "quay.io/biocontainers/cassis", "aliases": {"cassis": "/usr/local/bin/cassis", "lastz": "/usr/local/bin/lastz", "lastz_32": "/usr/local/bin/lastz_32", "lastz_D": "/usr/local/bin/lastz_D"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cassis.
shpc-registry automated BioContainers addition for cassis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cassis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cassis:0.0.20120106--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cassis/0.0.20120106--hdfd78af_1
$ module help quay.io/biocontainers/cassis/0.0.20120106--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cassis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cassis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cassis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cassis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cassis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cassis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cassis

```bash
$ singularity exec <container> /usr/local/bin/cassis
$ podman run --it --rm --entrypoint /usr/local/bin/cassis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cassis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lastz

```bash
$ singularity exec <container> /usr/local/bin/lastz
$ podman run --it --rm --entrypoint /usr/local/bin/lastz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lastz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lastz_32

```bash
$ singularity exec <container> /usr/local/bin/lastz_32
$ podman run --it --rm --entrypoint /usr/local/bin/lastz_32   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lastz_32   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lastz_D

```bash
$ singularity exec <container> /usr/local/bin/lastz_D
$ podman run --it --rm --entrypoint /usr/local/bin/lastz_D   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lastz_D   -v ${PWD} -w ${PWD} <container> -c " $@"
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