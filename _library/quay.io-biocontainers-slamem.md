---
layout: container
name:  "quay.io/biocontainers/slamem"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/slamem/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/slamem/container.yaml"
updated_at: "2024-05-25 03:05:58.369875"
latest: "0.8.5--h031d066_3"
container_url: "https://biocontainers.pro/tools/slamem"
aliases:
 - "slaMEM"
versions:
 - "v0.8.5--h779adbc_0"
 - "0.8.5--hec16e2b_1"
 - "0.8.5--h031d066_3"
description: "shpc-registry automated BioContainers addition for slamem"
config: {"url": "https://biocontainers.pro/tools/slamem", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for slamem", "latest": {"0.8.5--h031d066_3": "sha256:1a2cfb207df29a3f4597a1950b3cdf6cb6c6689e668bdbd9bca59c5138fb2091"}, "tags": {"v0.8.5--h779adbc_0": "sha256:839a7025e184d553021d1aac43d305b0b4b09c5f8205ebbff8431cdb6e1b9684", "0.8.5--hec16e2b_1": "sha256:a74c2b46db94b4489e18dd4d1eba268a9c0fed658680af875a79693159261ae8", "0.8.5--h031d066_3": "sha256:1a2cfb207df29a3f4597a1950b3cdf6cb6c6689e668bdbd9bca59c5138fb2091"}, "docker": "quay.io/biocontainers/slamem", "aliases": {"slaMEM": "/usr/local/bin/slaMEM"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/slamem.
shpc-registry automated BioContainers addition for slamem
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/slamem
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/slamem:0.8.5--h031d066_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/slamem/0.8.5--h031d066_3
$ module help quay.io/biocontainers/slamem/0.8.5--h031d066_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### slamem-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### slamem-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### slamem-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### slamem-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### slamem-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### slamem-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### slaMEM

```bash
$ singularity exec <container> /usr/local/bin/slaMEM
$ podman run --it --rm --entrypoint /usr/local/bin/slaMEM   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slaMEM   -v ${PWD} -w ${PWD} <container> -c " $@"
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