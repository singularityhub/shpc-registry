---
layout: container
name:  "quay.io/biocontainers/start-asap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/start-asap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/start-asap/container.yaml"
updated_at: "2025-09-28 03:48:33.884891"
latest: "1.3.0--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/start-asap"
aliases:
 - "start-asap"
 - "chartex"
 - "perl5.26.2"
 - "podselect"
versions:
 - "1.3.0--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for start-asap"
config: {"url": "https://biocontainers.pro/tools/start-asap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for start-asap", "latest": {"1.3.0--hdfd78af_1": "sha256:9608cf0862e248038c56ab1c7fbe1cf4a4c1361849bf1f2f71a3678395a38490"}, "tags": {"1.3.0--hdfd78af_1": "sha256:9608cf0862e248038c56ab1c7fbe1cf4a4c1361849bf1f2f71a3678395a38490"}, "docker": "quay.io/biocontainers/start-asap", "aliases": {"start-asap": "/usr/local/bin/start-asap", "chartex": "/usr/local/bin/chartex", "perl5.26.2": "/usr/local/bin/perl5.26.2", "podselect": "/usr/local/bin/podselect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/start-asap.
shpc-registry automated BioContainers addition for start-asap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/start-asap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/start-asap:1.3.0--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/start-asap/1.3.0--hdfd78af_1
$ module help quay.io/biocontainers/start-asap/1.3.0--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### start-asap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### start-asap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### start-asap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### start-asap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### start-asap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### start-asap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### start-asap

```bash
$ singularity exec <container> /usr/local/bin/start-asap
$ podman run --it --rm --entrypoint /usr/local/bin/start-asap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/start-asap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chartex

```bash
$ singularity exec <container> /usr/local/bin/chartex
$ podman run --it --rm --entrypoint /usr/local/bin/chartex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chartex   -v ${PWD} -w ${PWD} <container> -c " $@"
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