---
layout: container
name:  "quay.io/biocontainers/compalignp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/compalignp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/compalignp/container.yaml"
updated_at: "2025-08-07 03:52:22.552564"
latest: "1.0--h516909a_2"
container_url: "https://biocontainers.pro/tools/compalignp"
aliases:
 - "afetch"
 - "alistat"
 - "compalign"
 - "compalignp"
 - "compstruct"
 - "revcomp"
 - "seqsplit"
 - "seqstat"
 - "sfetch"
 - "shuffle"
 - "sindex"
 - "sreformat"
 - "translate"
 - "weight"
versions:
 - "1.0--h516909a_2"
description: "shpc-registry automated BioContainers addition for compalignp"
config: {"url": "https://biocontainers.pro/tools/compalignp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for compalignp", "latest": {"1.0--h516909a_2": "sha256:3c47ec2fb3cf54d395056629eca6e53da4428b8b27e8473800cbf123262b36db"}, "tags": {"1.0--h516909a_2": "sha256:3c47ec2fb3cf54d395056629eca6e53da4428b8b27e8473800cbf123262b36db"}, "docker": "quay.io/biocontainers/compalignp", "aliases": {"afetch": "/usr/local/bin/afetch", "alistat": "/usr/local/bin/alistat", "compalign": "/usr/local/bin/compalign", "compalignp": "/usr/local/bin/compalignp", "compstruct": "/usr/local/bin/compstruct", "revcomp": "/usr/local/bin/revcomp", "seqsplit": "/usr/local/bin/seqsplit", "seqstat": "/usr/local/bin/seqstat", "sfetch": "/usr/local/bin/sfetch", "shuffle": "/usr/local/bin/shuffle", "sindex": "/usr/local/bin/sindex", "sreformat": "/usr/local/bin/sreformat", "translate": "/usr/local/bin/translate", "weight": "/usr/local/bin/weight"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/compalignp.
shpc-registry automated BioContainers addition for compalignp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/compalignp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/compalignp:1.0--h516909a_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/compalignp/1.0--h516909a_2
$ module help quay.io/biocontainers/compalignp/1.0--h516909a_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### compalignp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### compalignp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### compalignp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### compalignp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### compalignp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### compalignp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### afetch

```bash
$ singularity exec <container> /usr/local/bin/afetch
$ podman run --it --rm --entrypoint /usr/local/bin/afetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/afetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alistat

```bash
$ singularity exec <container> /usr/local/bin/alistat
$ podman run --it --rm --entrypoint /usr/local/bin/alistat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alistat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compalign

```bash
$ singularity exec <container> /usr/local/bin/compalign
$ podman run --it --rm --entrypoint /usr/local/bin/compalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compalignp

```bash
$ singularity exec <container> /usr/local/bin/compalignp
$ podman run --it --rm --entrypoint /usr/local/bin/compalignp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compalignp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compstruct

```bash
$ singularity exec <container> /usr/local/bin/compstruct
$ podman run --it --rm --entrypoint /usr/local/bin/compstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### revcomp

```bash
$ singularity exec <container> /usr/local/bin/revcomp
$ podman run --it --rm --entrypoint /usr/local/bin/revcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/revcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqsplit

```bash
$ singularity exec <container> /usr/local/bin/seqsplit
$ podman run --it --rm --entrypoint /usr/local/bin/seqsplit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqsplit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqstat

```bash
$ singularity exec <container> /usr/local/bin/seqstat
$ podman run --it --rm --entrypoint /usr/local/bin/seqstat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqstat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sfetch

```bash
$ singularity exec <container> /usr/local/bin/sfetch
$ podman run --it --rm --entrypoint /usr/local/bin/sfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shuffle

```bash
$ singularity exec <container> /usr/local/bin/shuffle
$ podman run --it --rm --entrypoint /usr/local/bin/shuffle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shuffle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sindex

```bash
$ singularity exec <container> /usr/local/bin/sindex
$ podman run --it --rm --entrypoint /usr/local/bin/sindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sreformat

```bash
$ singularity exec <container> /usr/local/bin/sreformat
$ podman run --it --rm --entrypoint /usr/local/bin/sreformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sreformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### translate

```bash
$ singularity exec <container> /usr/local/bin/translate
$ podman run --it --rm --entrypoint /usr/local/bin/translate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/translate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### weight

```bash
$ singularity exec <container> /usr/local/bin/weight
$ podman run --it --rm --entrypoint /usr/local/bin/weight   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/weight   -v ${PWD} -w ${PWD} <container> -c " $@"
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