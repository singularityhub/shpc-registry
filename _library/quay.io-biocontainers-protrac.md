---
layout: container
name:  "quay.io/biocontainers/protrac"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/protrac/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/protrac/container.yaml"
updated_at: "2022-10-27 00:45:06.330902"
latest: "2.4.2--pl5321hdfd78af_3"
container_url: "https://biocontainers.pro/tools/protrac"
aliases:
 - "bdf2gdfont.PLS"
 - "cvtbdf.pl"
 - "proTRAC_2.4.2.pl"
versions:
 - "2.4.2--pl5321hdfd78af_3"
description: "shpc-registry automated BioContainers addition for protrac"
config: {"url": "https://biocontainers.pro/tools/protrac", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for protrac", "latest": {"2.4.2--pl5321hdfd78af_3": "sha256:b5ac9c1655f235537a52b840120f8b0d7c715b3996b6548370d21091213a3cc8"}, "tags": {"2.4.2--pl5321hdfd78af_3": "sha256:b5ac9c1655f235537a52b840120f8b0d7c715b3996b6548370d21091213a3cc8"}, "docker": "quay.io/biocontainers/protrac", "aliases": {"bdf2gdfont.PLS": "/usr/local/bin/bdf2gdfont.PLS", "cvtbdf.pl": "/usr/local/bin/cvtbdf.pl", "proTRAC_2.4.2.pl": "/usr/local/bin/proTRAC_2.4.2.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/protrac.
shpc-registry automated BioContainers addition for protrac
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/protrac
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/protrac:2.4.2--pl5321hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/protrac/2.4.2--pl5321hdfd78af_3
$ module help quay.io/biocontainers/protrac/2.4.2--pl5321hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### protrac-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### protrac-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### protrac-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### protrac-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### protrac-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### protrac-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bdf2gdfont.PLS

```bash
$ singularity exec <container> /usr/local/bin/bdf2gdfont.PLS
$ podman run --it --rm --entrypoint /usr/local/bin/bdf2gdfont.PLS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bdf2gdfont.PLS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cvtbdf.pl

```bash
$ singularity exec <container> /usr/local/bin/cvtbdf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cvtbdf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cvtbdf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proTRAC_2.4.2.pl

```bash
$ singularity exec <container> /usr/local/bin/proTRAC_2.4.2.pl
$ podman run --it --rm --entrypoint /usr/local/bin/proTRAC_2.4.2.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proTRAC_2.4.2.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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