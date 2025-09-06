---
layout: container
name:  "quay.io/biocontainers/ccp4srs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ccp4srs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ccp4srs/container.yaml"
updated_at: "2025-09-06 03:33:45.394905"
latest: "2024.06.14--h077b44d_0"
container_url: "https://biocontainers.pro/tools/ccp4srs"
aliases:
 - "pdb2to3"
 - "srsgen"
 - "srsview"
 - "x86_64-conda-linux-gnu-pkg-config"
 - "pkg-config"
 - "pkg-config.bin"
versions:
 - "2024.06.14--h077b44d_0"
description: "singularity registry hpc automated addition for ccp4srs"
config: {"url": "https://biocontainers.pro/tools/ccp4srs", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ccp4srs", "latest": {"2024.06.14--h077b44d_0": "sha256:c0589ecfdf9cf21a8627edf3ba90222d630b15080929db810bcd7d61c1b8f0f4"}, "tags": {"2024.06.14--h077b44d_0": "sha256:c0589ecfdf9cf21a8627edf3ba90222d630b15080929db810bcd7d61c1b8f0f4"}, "docker": "quay.io/biocontainers/ccp4srs", "aliases": {"pdb2to3": "/usr/local/bin/pdb2to3", "srsgen": "/usr/local/bin/srsgen", "srsview": "/usr/local/bin/srsview", "x86_64-conda-linux-gnu-pkg-config": "/usr/local/bin/x86_64-conda-linux-gnu-pkg-config", "pkg-config": "/usr/local/bin/pkg-config", "pkg-config.bin": "/usr/local/bin/pkg-config.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ccp4srs.
singularity registry hpc automated addition for ccp4srs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ccp4srs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ccp4srs:2024.06.14--h077b44d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ccp4srs/2024.06.14--h077b44d_0
$ module help quay.io/biocontainers/ccp4srs/2024.06.14--h077b44d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ccp4srs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ccp4srs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ccp4srs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ccp4srs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ccp4srs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ccp4srs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pdb2to3

```bash
$ singularity exec <container> /usr/local/bin/pdb2to3
$ podman run --it --rm --entrypoint /usr/local/bin/pdb2to3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdb2to3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### srsgen

```bash
$ singularity exec <container> /usr/local/bin/srsgen
$ podman run --it --rm --entrypoint /usr/local/bin/srsgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/srsgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### srsview

```bash
$ singularity exec <container> /usr/local/bin/srsview
$ podman run --it --rm --entrypoint /usr/local/bin/srsview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/srsview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu-pkg-config

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-pkg-config
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pkg-config

```bash
$ singularity exec <container> /usr/local/bin/pkg-config
$ podman run --it --rm --entrypoint /usr/local/bin/pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pkg-config.bin

```bash
$ singularity exec <container> /usr/local/bin/pkg-config.bin
$ podman run --it --rm --entrypoint /usr/local/bin/pkg-config.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pkg-config.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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