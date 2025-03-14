---
layout: container
name:  "quay.io/biocontainers/centrifuge-core"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/centrifuge-core/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/centrifuge-core/container.yaml"
updated_at: "2025-03-14 03:23:43.203391"
latest: "1.0.4_beta--h5b5514e_2"
container_url: "https://biocontainers.pro/tools/centrifuge-core"
aliases:
 - "centrifuge"
 - "centrifuge-BuildSharedSequence.pl"
 - "centrifuge-RemoveEmptySequence.pl"
 - "centrifuge-RemoveN.pl"
 - "centrifuge-build"
 - "centrifuge-build-bin"
 - "centrifuge-class"
 - "centrifuge-compress.pl"
 - "centrifuge-download"
 - "centrifuge-inspect"
 - "centrifuge-inspect-bin"
 - "centrifuge-kreport"
 - "centrifuge-sort-nt.pl"
 - "tar"
 - "idn2"
 - "wget"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.0.4_beta--h5b5514e_2"
 - "1.0.4--h43eeafb_2"
 - "1.0.4.2--h43eeafb_1"
 - "1.0.4.2--h5ca1c30_2"
description: "shpc-registry automated BioContainers addition for centrifuge-core"
config: {"url": "https://biocontainers.pro/tools/centrifuge-core", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for centrifuge-core", "latest": {"1.0.4_beta--h5b5514e_2": "sha256:7801552791c4b778bea9a544debff237f2383bee2718484a5bd574b9b89866d8"}, "tags": {"1.0.4_beta--h5b5514e_2": "sha256:7801552791c4b778bea9a544debff237f2383bee2718484a5bd574b9b89866d8", "1.0.4--h43eeafb_2": "sha256:a9b5a137912f45edc9a74b9bac4338e7b5a48edbc689b635c8d423c68966ac2f", "1.0.4.2--h43eeafb_1": "sha256:61519c11a2e0965671fa3ccba4a9362fb94ff6bb6f76293e219e71e6bdb1ff6f", "1.0.4.2--h5ca1c30_2": "sha256:18dd64c513fd3c3b45e93f60302eb84572c653238d90d5a10f194ee904948065"}, "docker": "quay.io/biocontainers/centrifuge-core", "aliases": {"centrifuge": "/usr/local/bin/centrifuge", "centrifuge-BuildSharedSequence.pl": "/usr/local/bin/centrifuge-BuildSharedSequence.pl", "centrifuge-RemoveEmptySequence.pl": "/usr/local/bin/centrifuge-RemoveEmptySequence.pl", "centrifuge-RemoveN.pl": "/usr/local/bin/centrifuge-RemoveN.pl", "centrifuge-build": "/usr/local/bin/centrifuge-build", "centrifuge-build-bin": "/usr/local/bin/centrifuge-build-bin", "centrifuge-class": "/usr/local/bin/centrifuge-class", "centrifuge-compress.pl": "/usr/local/bin/centrifuge-compress.pl", "centrifuge-download": "/usr/local/bin/centrifuge-download", "centrifuge-inspect": "/usr/local/bin/centrifuge-inspect", "centrifuge-inspect-bin": "/usr/local/bin/centrifuge-inspect-bin", "centrifuge-kreport": "/usr/local/bin/centrifuge-kreport", "centrifuge-sort-nt.pl": "/usr/local/bin/centrifuge-sort-nt.pl", "tar": "/usr/local/bin/tar", "idn2": "/usr/local/bin/idn2", "wget": "/usr/local/bin/wget", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/centrifuge-core.
shpc-registry automated BioContainers addition for centrifuge-core
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/centrifuge-core
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/centrifuge-core:1.0.4_beta--h5b5514e_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/centrifuge-core/1.0.4_beta--h5b5514e_2
$ module help quay.io/biocontainers/centrifuge-core/1.0.4_beta--h5b5514e_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### centrifuge-core-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### centrifuge-core-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### centrifuge-core-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### centrifuge-core-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### centrifuge-core-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### centrifuge-core-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### centrifuge

```bash
$ singularity exec <container> /usr/local/bin/centrifuge
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-BuildSharedSequence.pl

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-BuildSharedSequence.pl
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-BuildSharedSequence.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-BuildSharedSequence.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-RemoveEmptySequence.pl

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-RemoveEmptySequence.pl
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-RemoveEmptySequence.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-RemoveEmptySequence.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-RemoveN.pl

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-RemoveN.pl
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-RemoveN.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-RemoveN.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-build

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-build
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-build-bin

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-build-bin
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-build-bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-build-bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-class

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-class
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-class   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-class   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-compress.pl

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-compress.pl
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-compress.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-compress.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-download

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-download
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-download   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-download   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-inspect

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-inspect-bin

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-inspect-bin
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-inspect-bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-inspect-bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-kreport

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-kreport
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-kreport   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-kreport   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-sort-nt.pl

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-sort-nt.pl
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-sort-nt.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-sort-nt.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tar

```bash
$ singularity exec <container> /usr/local/bin/tar
$ podman run --it --rm --entrypoint /usr/local/bin/tar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idn2

```bash
$ singularity exec <container> /usr/local/bin/idn2
$ podman run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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