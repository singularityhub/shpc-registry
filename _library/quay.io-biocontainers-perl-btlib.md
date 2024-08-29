---
layout: container
name:  "quay.io/biocontainers/perl-btlib"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-btlib/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-btlib/container.yaml"
updated_at: "2024-08-29 02:50:42.587840"
latest: "0.19--0"
container_url: "https://biocontainers.pro/tools/perl-btlib"
aliases:
 - "fetch"
 - "indexer"
 - "netfetch"
 - "perl5.22.0"
 - "c2ph"
 - "pstruct"
 - "podselect"
versions:
 - "0.19--0"
description: "shpc-registry automated BioContainers addition for perl-btlib"
config: {"url": "https://biocontainers.pro/tools/perl-btlib", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-btlib", "latest": {"0.19--0": "sha256:43a01fe79d549316e49ed40b6c69a91bd0c650d086c992ff36eb20542a33f7f7"}, "tags": {"0.19--0": "sha256:43a01fe79d549316e49ed40b6c69a91bd0c650d086c992ff36eb20542a33f7f7"}, "docker": "quay.io/biocontainers/perl-btlib", "aliases": {"fetch": "/usr/local/bin/fetch", "indexer": "/usr/local/bin/indexer", "netfetch": "/usr/local/bin/netfetch", "perl5.22.0": "/usr/local/bin/perl5.22.0", "c2ph": "/usr/local/bin/c2ph", "pstruct": "/usr/local/bin/pstruct", "podselect": "/usr/local/bin/podselect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-btlib.
shpc-registry automated BioContainers addition for perl-btlib
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-btlib
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-btlib:0.19--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-btlib/0.19--0
$ module help quay.io/biocontainers/perl-btlib/0.19--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-btlib-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-btlib-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-btlib-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-btlib-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-btlib-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-btlib-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fetch

```bash
$ singularity exec <container> /usr/local/bin/fetch
$ podman run --it --rm --entrypoint /usr/local/bin/fetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### indexer

```bash
$ singularity exec <container> /usr/local/bin/indexer
$ podman run --it --rm --entrypoint /usr/local/bin/indexer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/indexer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### netfetch

```bash
$ singularity exec <container> /usr/local/bin/netfetch
$ podman run --it --rm --entrypoint /usr/local/bin/netfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/netfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.22.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.22.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.22.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.22.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c2ph

```bash
$ singularity exec <container> /usr/local/bin/c2ph
$ podman run --it --rm --entrypoint /usr/local/bin/c2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pstruct

```bash
$ singularity exec <container> /usr/local/bin/pstruct
$ podman run --it --rm --entrypoint /usr/local/bin/pstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### podselect

```bash
$ singularity exec <container> /usr/local/bin/podselect
$ podman run --it --rm --entrypoint /usr/local/bin/podselect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/podselect   -v ${PWD} -w ${PWD} <container> -c " $@"
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