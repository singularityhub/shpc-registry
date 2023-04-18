---
layout: container
name:  "quay.io/biocontainers/minia"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/minia/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/minia/container.yaml"
updated_at: "2023-04-18 03:17:52.112972"
latest: "3.2.6--hd03093a_1"
container_url: "https://biocontainers.pro/tools/minia"
aliases:
 - "gatb-h5dump"
 - "merci"
 - "minia"
versions:
 - "3.2.6--hd03093a_1"
description: "shpc-registry automated BioContainers addition for minia"
config: {"url": "https://biocontainers.pro/tools/minia", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for minia", "latest": {"3.2.6--hd03093a_1": "sha256:3378184951a6e726e80b9ccacaebbca1218530c46703b860f3c15ae8b1c1ab4b"}, "tags": {"3.2.6--hd03093a_1": "sha256:3378184951a6e726e80b9ccacaebbca1218530c46703b860f3c15ae8b1c1ab4b"}, "docker": "quay.io/biocontainers/minia", "aliases": {"gatb-h5dump": "/usr/local/bin/gatb-h5dump", "merci": "/usr/local/bin/merci", "minia": "/usr/local/bin/minia"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/minia.
shpc-registry automated BioContainers addition for minia
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/minia
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/minia:3.2.6--hd03093a_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/minia/3.2.6--hd03093a_1
$ module help quay.io/biocontainers/minia/3.2.6--hd03093a_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### minia-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### minia-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### minia-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### minia-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### minia-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### minia-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gatb-h5dump

```bash
$ singularity exec <container> /usr/local/bin/gatb-h5dump
$ podman run --it --rm --entrypoint /usr/local/bin/gatb-h5dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gatb-h5dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merci

```bash
$ singularity exec <container> /usr/local/bin/merci
$ podman run --it --rm --entrypoint /usr/local/bin/merci   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merci   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minia

```bash
$ singularity exec <container> /usr/local/bin/minia
$ podman run --it --rm --entrypoint /usr/local/bin/minia   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minia   -v ${PWD} -w ${PWD} <container> -c " $@"
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