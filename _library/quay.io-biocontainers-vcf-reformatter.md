---
layout: container
name:  "quay.io/biocontainers/vcf-reformatter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vcf-reformatter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vcf-reformatter/container.yaml"
updated_at: "2025-12-03 03:26:47.671717"
latest: "0.3.0--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/vcf-reformatter"
aliases:
 - "vcf-reformatter"
versions:
 - "0.2.0--h4349ce8_0"
 - "0.3.0--h4349ce8_0"
description: "singularity registry hpc automated addition for vcf-reformatter"
config: {"url": "https://biocontainers.pro/tools/vcf-reformatter", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for vcf-reformatter", "latest": {"0.3.0--h4349ce8_0": "sha256:73f367e9821e970167ce91701675bf81b97f1d09bd485f0a6865e3f2183ba4dd"}, "tags": {"0.2.0--h4349ce8_0": "sha256:49d7f8c78d6024b7483f7fed1f4e0ece8af8905fac64b606210854072f237783", "0.3.0--h4349ce8_0": "sha256:73f367e9821e970167ce91701675bf81b97f1d09bd485f0a6865e3f2183ba4dd"}, "docker": "quay.io/biocontainers/vcf-reformatter", "aliases": {"vcf-reformatter": "/usr/local/bin/vcf-reformatter"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vcf-reformatter.
singularity registry hpc automated addition for vcf-reformatter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vcf-reformatter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vcf-reformatter:0.3.0--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vcf-reformatter/0.3.0--h4349ce8_0
$ module help quay.io/biocontainers/vcf-reformatter/0.3.0--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vcf-reformatter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vcf-reformatter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vcf-reformatter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vcf-reformatter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vcf-reformatter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vcf-reformatter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vcf-reformatter

```bash
$ singularity exec <container> /usr/local/bin/vcf-reformatter
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-reformatter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-reformatter   -v ${PWD} -w ${PWD} <container> -c " $@"
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