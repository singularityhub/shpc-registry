---
layout: container
name:  "quay.io/biocontainers/randfold"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/randfold/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/randfold/container.yaml"
updated_at: "2024-07-31 02:29:53.386269"
latest: "2.0.1--h031d066_6"
container_url: "https://biocontainers.pro/tools/randfold"
aliases:
 - "afetch"
 - "alistat"
 - "compalign"
 - "compstruct"
 - "randfold"
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
 - "2.0.1--hec16e2b_4"
 - "2.0.1--h031d066_6"
description: "shpc-registry automated BioContainers addition for randfold"
config: {"url": "https://biocontainers.pro/tools/randfold", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for randfold", "latest": {"2.0.1--h031d066_6": "sha256:5b470be8852a813976fa17b3260f4685f662a83865708a9760197c9091c01278"}, "tags": {"2.0.1--hec16e2b_4": "sha256:c392a31446a0cc452d7f0b0b0c2d570e98d005b9c29aa3897c4302b2c9e26316", "2.0.1--h031d066_6": "sha256:5b470be8852a813976fa17b3260f4685f662a83865708a9760197c9091c01278"}, "docker": "quay.io/biocontainers/randfold", "aliases": {"afetch": "/usr/local/bin/afetch", "alistat": "/usr/local/bin/alistat", "compalign": "/usr/local/bin/compalign", "compstruct": "/usr/local/bin/compstruct", "randfold": "/usr/local/bin/randfold", "revcomp": "/usr/local/bin/revcomp", "seqsplit": "/usr/local/bin/seqsplit", "seqstat": "/usr/local/bin/seqstat", "sfetch": "/usr/local/bin/sfetch", "shuffle": "/usr/local/bin/shuffle", "sindex": "/usr/local/bin/sindex", "sreformat": "/usr/local/bin/sreformat", "translate": "/usr/local/bin/translate", "weight": "/usr/local/bin/weight"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/randfold.
shpc-registry automated BioContainers addition for randfold
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/randfold
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/randfold:2.0.1--h031d066_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/randfold/2.0.1--h031d066_6
$ module help quay.io/biocontainers/randfold/2.0.1--h031d066_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### randfold-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### randfold-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### randfold-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### randfold-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### randfold-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### randfold-inspect-deffile:

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


#### compstruct

```bash
$ singularity exec <container> /usr/local/bin/compstruct
$ podman run --it --rm --entrypoint /usr/local/bin/compstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### randfold

```bash
$ singularity exec <container> /usr/local/bin/randfold
$ podman run --it --rm --entrypoint /usr/local/bin/randfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/randfold   -v ${PWD} -w ${PWD} <container> -c " $@"
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