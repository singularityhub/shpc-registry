---
layout: container
name:  "quay.io/biocontainers/jccirc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/jccirc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/jccirc/container.yaml"
updated_at: "2024-10-17 03:38:06.108154"
latest: "1.0.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/jccirc"
aliases:
 - "CircSimu"
 - "CircSimu.pl"
 - "JCcirc"
 - "JCcirc.pl"
 - "qualfa2fq.pl"
 - "xa2multi.pl"
 - "bwa"
versions:
 - "1.0.0--hdfd78af_0"
description: "singularity registry hpc automated addition for jccirc"
config: {"url": "https://biocontainers.pro/tools/jccirc", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for jccirc", "latest": {"1.0.0--hdfd78af_0": "sha256:d3d0085306e9a5c6790bb915c0bd9557572d3050962a257284dd55fff70d5edf"}, "tags": {"1.0.0--hdfd78af_0": "sha256:d3d0085306e9a5c6790bb915c0bd9557572d3050962a257284dd55fff70d5edf"}, "docker": "quay.io/biocontainers/jccirc", "aliases": {"CircSimu": "/usr/local/bin/CircSimu", "CircSimu.pl": "/usr/local/bin/CircSimu.pl", "JCcirc": "/usr/local/bin/JCcirc", "JCcirc.pl": "/usr/local/bin/JCcirc.pl", "qualfa2fq.pl": "/usr/local/bin/qualfa2fq.pl", "xa2multi.pl": "/usr/local/bin/xa2multi.pl", "bwa": "/usr/local/bin/bwa"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/jccirc.
singularity registry hpc automated addition for jccirc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/jccirc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/jccirc:1.0.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/jccirc/1.0.0--hdfd78af_0
$ module help quay.io/biocontainers/jccirc/1.0.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### jccirc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### jccirc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### jccirc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### jccirc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### jccirc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### jccirc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### CircSimu

```bash
$ singularity exec <container> /usr/local/bin/CircSimu
$ podman run --it --rm --entrypoint /usr/local/bin/CircSimu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CircSimu   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CircSimu.pl

```bash
$ singularity exec <container> /usr/local/bin/CircSimu.pl
$ podman run --it --rm --entrypoint /usr/local/bin/CircSimu.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CircSimu.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### JCcirc

```bash
$ singularity exec <container> /usr/local/bin/JCcirc
$ podman run --it --rm --entrypoint /usr/local/bin/JCcirc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/JCcirc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### JCcirc.pl

```bash
$ singularity exec <container> /usr/local/bin/JCcirc.pl
$ podman run --it --rm --entrypoint /usr/local/bin/JCcirc.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/JCcirc.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qualfa2fq.pl

```bash
$ singularity exec <container> /usr/local/bin/qualfa2fq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/qualfa2fq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qualfa2fq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xa2multi.pl

```bash
$ singularity exec <container> /usr/local/bin/xa2multi.pl
$ podman run --it --rm --entrypoint /usr/local/bin/xa2multi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xa2multi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa

```bash
$ singularity exec <container> /usr/local/bin/bwa
$ podman run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
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