---
layout: container
name:  "quay.io/biocontainers/perl-estscan1"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-estscan1/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-estscan1/container.yaml"
updated_at: "2023-12-02 02:59:47.522660"
latest: "1.3--pl526_1"
container_url: "https://biocontainers.pro/tools/perl-estscan1"
aliases:
 - "ESTScan1"
 - "fetch"
 - "indexer"
 - "netfetch"
 - "perl5.22.0"
 - "c2ph"
 - "pstruct"
 - "perl5.26.2"
 - "podselect"
versions:
 - "1.3--pl526_1"
description: "shpc-registry automated BioContainers addition for perl-estscan1"
config: {"url": "https://biocontainers.pro/tools/perl-estscan1", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-estscan1", "latest": {"1.3--pl526_1": "sha256:8b8456b333d341a2a872448a25cbf5e80cc2f94f6a9d1fd4de9d6baa35a4c16b"}, "tags": {"1.3--pl526_1": "sha256:8b8456b333d341a2a872448a25cbf5e80cc2f94f6a9d1fd4de9d6baa35a4c16b"}, "docker": "quay.io/biocontainers/perl-estscan1", "aliases": {"ESTScan1": "/usr/local/bin/ESTScan1", "fetch": "/usr/local/bin/fetch", "indexer": "/usr/local/bin/indexer", "netfetch": "/usr/local/bin/netfetch", "perl5.22.0": "/usr/local/bin/perl5.22.0", "c2ph": "/usr/local/bin/c2ph", "pstruct": "/usr/local/bin/pstruct", "perl5.26.2": "/usr/local/bin/perl5.26.2", "podselect": "/usr/local/bin/podselect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-estscan1.
shpc-registry automated BioContainers addition for perl-estscan1
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-estscan1
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-estscan1:1.3--pl526_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-estscan1/1.3--pl526_1
$ module help quay.io/biocontainers/perl-estscan1/1.3--pl526_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-estscan1-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-estscan1-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-estscan1-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-estscan1-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-estscan1-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-estscan1-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ESTScan1

```bash
$ singularity exec <container> /usr/local/bin/ESTScan1
$ podman run --it --rm --entrypoint /usr/local/bin/ESTScan1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ESTScan1   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### perl5.26.2

```bash
$ singularity exec <container> /usr/local/bin/perl5.26.2
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.26.2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.26.2   -v ${PWD} -w ${PWD} <container> -c " $@"
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