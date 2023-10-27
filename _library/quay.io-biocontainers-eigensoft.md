---
layout: container
name:  "quay.io/biocontainers/eigensoft"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/eigensoft/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/eigensoft/container.yaml"
updated_at: "2023-10-27 02:43:24.100704"
latest: "8.0.0--h6a739c9_3"
container_url: "https://biocontainers.pro/tools/eigensoft"
aliases:
 - "baseprog"
 - "convertf"
 - "eigenstrat"
 - "eigenstratQTL"
 - "mergeit"
 - "pca"
 - "pcatoy"
 - "smarteigenstrat"
 - "smartpca"
 - "smartrel"
 - "smshrink"
 - "twstats"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "7.2.1--h2469040_5"
 - "8.0.0--h2469040_1"
 - "8.0.0--h6a739c9_3"
description: "shpc-registry automated BioContainers addition for eigensoft"
config: {"url": "https://biocontainers.pro/tools/eigensoft", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for eigensoft", "latest": {"8.0.0--h6a739c9_3": "sha256:cf1b307bb5395b1f39317f3c8c177f96f6adbb38b6237de7acad090e7a3bc6ba"}, "tags": {"7.2.1--h2469040_5": "sha256:9456610b45716dfa6c5dfad81b4ae981dd0662bf7ae4c2b5317d42a28db4946e", "8.0.0--h2469040_1": "sha256:3b9a72b2081b685fbb21802396c9a08436b5c333c87b1010899828cb4c81d02a", "8.0.0--h6a739c9_3": "sha256:cf1b307bb5395b1f39317f3c8c177f96f6adbb38b6237de7acad090e7a3bc6ba"}, "docker": "quay.io/biocontainers/eigensoft", "aliases": {"baseprog": "/usr/local/bin/baseprog", "convertf": "/usr/local/bin/convertf", "eigenstrat": "/usr/local/bin/eigenstrat", "eigenstratQTL": "/usr/local/bin/eigenstratQTL", "mergeit": "/usr/local/bin/mergeit", "pca": "/usr/local/bin/pca", "pcatoy": "/usr/local/bin/pcatoy", "smarteigenstrat": "/usr/local/bin/smarteigenstrat", "smartpca": "/usr/local/bin/smartpca", "smartrel": "/usr/local/bin/smartrel", "smshrink": "/usr/local/bin/smshrink", "twstats": "/usr/local/bin/twstats", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/eigensoft.
shpc-registry automated BioContainers addition for eigensoft
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/eigensoft
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/eigensoft:8.0.0--h6a739c9_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/eigensoft/8.0.0--h6a739c9_3
$ module help quay.io/biocontainers/eigensoft/8.0.0--h6a739c9_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### eigensoft-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### eigensoft-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### eigensoft-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### eigensoft-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### eigensoft-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### eigensoft-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### baseprog

```bash
$ singularity exec <container> /usr/local/bin/baseprog
$ podman run --it --rm --entrypoint /usr/local/bin/baseprog   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/baseprog   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convertf

```bash
$ singularity exec <container> /usr/local/bin/convertf
$ podman run --it --rm --entrypoint /usr/local/bin/convertf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eigenstrat

```bash
$ singularity exec <container> /usr/local/bin/eigenstrat
$ podman run --it --rm --entrypoint /usr/local/bin/eigenstrat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eigenstrat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eigenstratQTL

```bash
$ singularity exec <container> /usr/local/bin/eigenstratQTL
$ podman run --it --rm --entrypoint /usr/local/bin/eigenstratQTL   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eigenstratQTL   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mergeit

```bash
$ singularity exec <container> /usr/local/bin/mergeit
$ podman run --it --rm --entrypoint /usr/local/bin/mergeit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mergeit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pca

```bash
$ singularity exec <container> /usr/local/bin/pca
$ podman run --it --rm --entrypoint /usr/local/bin/pca   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pca   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pcatoy

```bash
$ singularity exec <container> /usr/local/bin/pcatoy
$ podman run --it --rm --entrypoint /usr/local/bin/pcatoy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pcatoy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smarteigenstrat

```bash
$ singularity exec <container> /usr/local/bin/smarteigenstrat
$ podman run --it --rm --entrypoint /usr/local/bin/smarteigenstrat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smarteigenstrat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smartpca

```bash
$ singularity exec <container> /usr/local/bin/smartpca
$ podman run --it --rm --entrypoint /usr/local/bin/smartpca   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smartpca   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smartrel

```bash
$ singularity exec <container> /usr/local/bin/smartrel
$ podman run --it --rm --entrypoint /usr/local/bin/smartrel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smartrel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smshrink

```bash
$ singularity exec <container> /usr/local/bin/smshrink
$ podman run --it --rm --entrypoint /usr/local/bin/smshrink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smshrink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### twstats

```bash
$ singularity exec <container> /usr/local/bin/twstats
$ podman run --it --rm --entrypoint /usr/local/bin/twstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/twstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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