---
layout: container
name:  "quay.io/biocontainers/pbtk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pbtk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pbtk/container.yaml"
updated_at: "2024-09-09 03:12:55.687007"
latest: "3.1.1--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/pbtk"
aliases:
 - "ccs-kinetics-bystrandify"
 - "extracthifi"
 - "pbindex"
 - "pbindexdump"
 - "pbmerge"
 - "zmwfilter"
versions:
 - "1.0.0--h9ee0642_0"
 - "3.1.0--h9ee0642_0"
 - "3.0.0--h9ee0642_0"
 - "3.1.1--h9ee0642_0"
description: "singularity registry hpc automated addition for pbtk"
config: {"url": "https://biocontainers.pro/tools/pbtk", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pbtk", "latest": {"3.1.1--h9ee0642_0": "sha256:bfa948482986ca9a86419e7cbb9850e93a770ddf6e7a10170967ed3777efcaff"}, "tags": {"1.0.0--h9ee0642_0": "sha256:d37dfd307c36268f3cc4c5a19c3d5903c1917567eb30ccabe2d8d6e68dc22979", "3.1.0--h9ee0642_0": "sha256:9226f4c3cb7abd306affc1db314b80f99d4f93926cae8bb3dcb64e1ca37309d8", "3.0.0--h9ee0642_0": "sha256:1cee79b083bf2d9d21a15da0a37e2aeed51502920843615315076dc4471b9d11", "3.1.1--h9ee0642_0": "sha256:bfa948482986ca9a86419e7cbb9850e93a770ddf6e7a10170967ed3777efcaff"}, "docker": "quay.io/biocontainers/pbtk", "aliases": {"ccs-kinetics-bystrandify": "/usr/local/bin/ccs-kinetics-bystrandify", "extracthifi": "/usr/local/bin/extracthifi", "pbindex": "/usr/local/bin/pbindex", "pbindexdump": "/usr/local/bin/pbindexdump", "pbmerge": "/usr/local/bin/pbmerge", "zmwfilter": "/usr/local/bin/zmwfilter"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pbtk.
singularity registry hpc automated addition for pbtk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pbtk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pbtk:3.1.1--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pbtk/3.1.1--h9ee0642_0
$ module help quay.io/biocontainers/pbtk/3.1.1--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pbtk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pbtk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pbtk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pbtk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pbtk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pbtk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ccs-kinetics-bystrandify

```bash
$ singularity exec <container> /usr/local/bin/ccs-kinetics-bystrandify
$ podman run --it --rm --entrypoint /usr/local/bin/ccs-kinetics-bystrandify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccs-kinetics-bystrandify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extracthifi

```bash
$ singularity exec <container> /usr/local/bin/extracthifi
$ podman run --it --rm --entrypoint /usr/local/bin/extracthifi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extracthifi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbindex

```bash
$ singularity exec <container> /usr/local/bin/pbindex
$ podman run --it --rm --entrypoint /usr/local/bin/pbindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbindexdump

```bash
$ singularity exec <container> /usr/local/bin/pbindexdump
$ podman run --it --rm --entrypoint /usr/local/bin/pbindexdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbindexdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbmerge

```bash
$ singularity exec <container> /usr/local/bin/pbmerge
$ podman run --it --rm --entrypoint /usr/local/bin/pbmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zmwfilter

```bash
$ singularity exec <container> /usr/local/bin/zmwfilter
$ podman run --it --rm --entrypoint /usr/local/bin/zmwfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zmwfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
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