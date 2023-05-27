---
layout: container
name:  "quay.io/biocontainers/smartdenovo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/smartdenovo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/smartdenovo/container.yaml"
updated_at: "2023-05-27 02:55:19.212886"
latest: "1.0.0--h031d066_7"
container_url: "https://biocontainers.pro/tools/smartdenovo"
aliases:
 - "pairaln"
 - "smartdenovo.pl"
 - "wtclp"
 - "wtcns"
 - "wtcyc"
 - "wtext"
 - "wtgbo"
 - "wtlay"
 - "wtmer"
 - "wtmsa"
 - "wtobt"
 - "wtpre"
 - "wtzmo"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.0.0--hec16e2b_5"
 - "1.0.0--h031d066_7"
description: "shpc-registry automated BioContainers addition for smartdenovo"
config: {"url": "https://biocontainers.pro/tools/smartdenovo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for smartdenovo", "latest": {"1.0.0--h031d066_7": "sha256:e98d67ff989b2707d04247395a800d8e18178e56689ef315f333872ca82bddc4"}, "tags": {"1.0.0--hec16e2b_5": "sha256:0d45291b3ba458ea76b2a8aaa0f2b94b2a064721ac62e47ac053c80d55e4b13b", "1.0.0--h031d066_7": "sha256:e98d67ff989b2707d04247395a800d8e18178e56689ef315f333872ca82bddc4"}, "docker": "quay.io/biocontainers/smartdenovo", "aliases": {"pairaln": "/usr/local/bin/pairaln", "smartdenovo.pl": "/usr/local/bin/smartdenovo.pl", "wtclp": "/usr/local/bin/wtclp", "wtcns": "/usr/local/bin/wtcns", "wtcyc": "/usr/local/bin/wtcyc", "wtext": "/usr/local/bin/wtext", "wtgbo": "/usr/local/bin/wtgbo", "wtlay": "/usr/local/bin/wtlay", "wtmer": "/usr/local/bin/wtmer", "wtmsa": "/usr/local/bin/wtmsa", "wtobt": "/usr/local/bin/wtobt", "wtpre": "/usr/local/bin/wtpre", "wtzmo": "/usr/local/bin/wtzmo", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/smartdenovo.
shpc-registry automated BioContainers addition for smartdenovo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/smartdenovo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/smartdenovo:1.0.0--h031d066_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/smartdenovo/1.0.0--h031d066_7
$ module help quay.io/biocontainers/smartdenovo/1.0.0--h031d066_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### smartdenovo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### smartdenovo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### smartdenovo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### smartdenovo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### smartdenovo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### smartdenovo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pairaln

```bash
$ singularity exec <container> /usr/local/bin/pairaln
$ podman run --it --rm --entrypoint /usr/local/bin/pairaln   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pairaln   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smartdenovo.pl

```bash
$ singularity exec <container> /usr/local/bin/smartdenovo.pl
$ podman run --it --rm --entrypoint /usr/local/bin/smartdenovo.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smartdenovo.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wtclp

```bash
$ singularity exec <container> /usr/local/bin/wtclp
$ podman run --it --rm --entrypoint /usr/local/bin/wtclp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtclp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wtcns

```bash
$ singularity exec <container> /usr/local/bin/wtcns
$ podman run --it --rm --entrypoint /usr/local/bin/wtcns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtcns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wtcyc

```bash
$ singularity exec <container> /usr/local/bin/wtcyc
$ podman run --it --rm --entrypoint /usr/local/bin/wtcyc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtcyc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wtext

```bash
$ singularity exec <container> /usr/local/bin/wtext
$ podman run --it --rm --entrypoint /usr/local/bin/wtext   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtext   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wtgbo

```bash
$ singularity exec <container> /usr/local/bin/wtgbo
$ podman run --it --rm --entrypoint /usr/local/bin/wtgbo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtgbo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wtlay

```bash
$ singularity exec <container> /usr/local/bin/wtlay
$ podman run --it --rm --entrypoint /usr/local/bin/wtlay   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtlay   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wtmer

```bash
$ singularity exec <container> /usr/local/bin/wtmer
$ podman run --it --rm --entrypoint /usr/local/bin/wtmer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtmer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wtmsa

```bash
$ singularity exec <container> /usr/local/bin/wtmsa
$ podman run --it --rm --entrypoint /usr/local/bin/wtmsa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtmsa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wtobt

```bash
$ singularity exec <container> /usr/local/bin/wtobt
$ podman run --it --rm --entrypoint /usr/local/bin/wtobt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtobt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wtpre

```bash
$ singularity exec <container> /usr/local/bin/wtpre
$ podman run --it --rm --entrypoint /usr/local/bin/wtpre   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtpre   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wtzmo

```bash
$ singularity exec <container> /usr/local/bin/wtzmo
$ podman run --it --rm --entrypoint /usr/local/bin/wtzmo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtzmo   -v ${PWD} -w ${PWD} <container> -c " $@"
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