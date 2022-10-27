---
layout: container
name:  "quay.io/biocontainers/svanalyzer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/svanalyzer/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/svanalyzer/container.yaml"
updated_at: "2022-10-27 00:23:30.332865"
latest: "0.36--pl5321hdfd78af_2"
container_url: "https://biocontainers.pro/tools/svanalyzer"
aliases:
 - "SVbenchmark"
 - "SVcomp"
 - "SVmerge"
 - "SVrefine"
 - "SVwiden"
 - "svanalyzer"
versions:
 - "0.36--pl5321hdfd78af_2"
description: "shpc-registry automated BioContainers addition for svanalyzer"
config: {"url": "https://biocontainers.pro/tools/svanalyzer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for svanalyzer", "latest": {"0.36--pl5321hdfd78af_2": "sha256:d5ddfe600cb2c6b0db9f16cfd6e4e8cffe7d708e7aa51012cb3e4fd24801af2b"}, "tags": {"0.36--pl5321hdfd78af_2": "sha256:d5ddfe600cb2c6b0db9f16cfd6e4e8cffe7d708e7aa51012cb3e4fd24801af2b"}, "docker": "quay.io/biocontainers/svanalyzer", "aliases": {"SVbenchmark": "/usr/local/bin/SVbenchmark", "SVcomp": "/usr/local/bin/SVcomp", "SVmerge": "/usr/local/bin/SVmerge", "SVrefine": "/usr/local/bin/SVrefine", "SVwiden": "/usr/local/bin/SVwiden", "svanalyzer": "/usr/local/bin/svanalyzer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/svanalyzer.
shpc-registry automated BioContainers addition for svanalyzer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/svanalyzer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/svanalyzer:0.36--pl5321hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/svanalyzer/0.36--pl5321hdfd78af_2
$ module help quay.io/biocontainers/svanalyzer/0.36--pl5321hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### svanalyzer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### svanalyzer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### svanalyzer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### svanalyzer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### svanalyzer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### svanalyzer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SVbenchmark

```bash
$ singularity exec <container> /usr/local/bin/SVbenchmark
$ podman run --it --rm --entrypoint /usr/local/bin/SVbenchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SVbenchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SVcomp

```bash
$ singularity exec <container> /usr/local/bin/SVcomp
$ podman run --it --rm --entrypoint /usr/local/bin/SVcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SVcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SVmerge

```bash
$ singularity exec <container> /usr/local/bin/SVmerge
$ podman run --it --rm --entrypoint /usr/local/bin/SVmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SVmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SVrefine

```bash
$ singularity exec <container> /usr/local/bin/SVrefine
$ podman run --it --rm --entrypoint /usr/local/bin/SVrefine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SVrefine   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SVwiden

```bash
$ singularity exec <container> /usr/local/bin/SVwiden
$ podman run --it --rm --entrypoint /usr/local/bin/SVwiden   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SVwiden   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svanalyzer

```bash
$ singularity exec <container> /usr/local/bin/svanalyzer
$ podman run --it --rm --entrypoint /usr/local/bin/svanalyzer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svanalyzer   -v ${PWD} -w ${PWD} <container> -c " $@"
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