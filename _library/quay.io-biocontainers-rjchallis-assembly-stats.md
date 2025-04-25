---
layout: container
name:  "quay.io/biocontainers/rjchallis-assembly-stats"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rjchallis-assembly-stats/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rjchallis-assembly-stats/container.yaml"
updated_at: "2025-04-25 03:39:43.396022"
latest: "17.02--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/rjchallis-assembly-stats"
aliases:
 - "asm2stats.minmaxgc.pl"
 - "asm2stats.minmaxgc.pl.bak"
 - "asm2stats.pl"
 - "json_xs"
 - "perl5.26.2"
 - "podselect"
versions:
 - "17.02--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for rjchallis-assembly-stats"
config: {"url": "https://biocontainers.pro/tools/rjchallis-assembly-stats", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rjchallis-assembly-stats", "latest": {"17.02--hdfd78af_0": "sha256:6646f1d94c93e04adacf2bd80f0eb0fd91a5bfde2421738892c66274840fbb50"}, "tags": {"17.02--hdfd78af_0": "sha256:6646f1d94c93e04adacf2bd80f0eb0fd91a5bfde2421738892c66274840fbb50"}, "docker": "quay.io/biocontainers/rjchallis-assembly-stats", "aliases": {"asm2stats.minmaxgc.pl": "/usr/local/bin/asm2stats.minmaxgc.pl", "asm2stats.minmaxgc.pl.bak": "/usr/local/bin/asm2stats.minmaxgc.pl.bak", "asm2stats.pl": "/usr/local/bin/asm2stats.pl", "json_xs": "/usr/local/bin/json_xs", "perl5.26.2": "/usr/local/bin/perl5.26.2", "podselect": "/usr/local/bin/podselect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rjchallis-assembly-stats.
shpc-registry automated BioContainers addition for rjchallis-assembly-stats
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rjchallis-assembly-stats
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rjchallis-assembly-stats:17.02--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rjchallis-assembly-stats/17.02--hdfd78af_0
$ module help quay.io/biocontainers/rjchallis-assembly-stats/17.02--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rjchallis-assembly-stats-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rjchallis-assembly-stats-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rjchallis-assembly-stats-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rjchallis-assembly-stats-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rjchallis-assembly-stats-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rjchallis-assembly-stats-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### asm2stats.minmaxgc.pl

```bash
$ singularity exec <container> /usr/local/bin/asm2stats.minmaxgc.pl
$ podman run --it --rm --entrypoint /usr/local/bin/asm2stats.minmaxgc.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asm2stats.minmaxgc.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asm2stats.minmaxgc.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/asm2stats.minmaxgc.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/asm2stats.minmaxgc.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asm2stats.minmaxgc.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asm2stats.pl

```bash
$ singularity exec <container> /usr/local/bin/asm2stats.pl
$ podman run --it --rm --entrypoint /usr/local/bin/asm2stats.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asm2stats.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### json_xs

```bash
$ singularity exec <container> /usr/local/bin/json_xs
$ podman run --it --rm --entrypoint /usr/local/bin/json_xs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/json_xs   -v ${PWD} -w ${PWD} <container> -c " $@"
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