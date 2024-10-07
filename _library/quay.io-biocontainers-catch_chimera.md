---
layout: container
name:  "quay.io/biocontainers/catch_chimera"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/catch_chimera/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/catch_chimera/container.yaml"
updated_at: "2024-10-07 16:37:03.797196"
latest: "1.0--pl5321hdfd78af_1"
container_url: "https://biocontainers.pro/tools/catch_chimera"
aliases:
 - "CATCh_v1.run"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.0--pl5321hdfd78af_1"
description: "shpc-registry automated BioContainers addition for catch_chimera"
config: {"url": "https://biocontainers.pro/tools/catch_chimera", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for catch_chimera", "latest": {"1.0--pl5321hdfd78af_1": "sha256:f9f8990d3dc440efc4825523acc0c942e58ce74b826d31cc74d98fab0d5debad"}, "tags": {"1.0--pl5321hdfd78af_1": "sha256:f9f8990d3dc440efc4825523acc0c942e58ce74b826d31cc74d98fab0d5debad"}, "docker": "quay.io/biocontainers/catch_chimera", "aliases": {"CATCh_v1.run": "/usr/local/bin/CATCh_v1.run", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/catch_chimera.
shpc-registry automated BioContainers addition for catch_chimera
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/catch_chimera
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/catch_chimera:1.0--pl5321hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/catch_chimera/1.0--pl5321hdfd78af_1
$ module help quay.io/biocontainers/catch_chimera/1.0--pl5321hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### catch_chimera-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### catch_chimera-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### catch_chimera-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### catch_chimera-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### catch_chimera-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### catch_chimera-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### CATCh_v1.run

```bash
$ singularity exec <container> /usr/local/bin/CATCh_v1.run
$ podman run --it --rm --entrypoint /usr/local/bin/CATCh_v1.run   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CATCh_v1.run   -v ${PWD} -w ${PWD} <container> -c " $@"
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