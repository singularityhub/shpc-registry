---
layout: container
name:  "quay.io/biocontainers/fastagap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastagap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastagap/container.yaml"
updated_at: "2025-09-16 04:45:54.106053"
latest: "1.0.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/fastagap"
aliases:
 - "fastagap"
versions:
 - "1.0--hdfd78af_0"
 - "1.0.1--hdfd78af_0"
description: "singularity registry hpc automated addition for fastagap"
config: {"url": "https://biocontainers.pro/tools/fastagap", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fastagap", "latest": {"1.0.1--hdfd78af_0": "sha256:9dc2b7e7019f682fbcff410eca22a0177beeddd3623597b535eb165bc87aab43"}, "tags": {"1.0--hdfd78af_0": "sha256:1d57fa6a763b9aac38d14d54c26fa7e7bc6dfd862829b60ea50b25bf2427d900", "1.0.1--hdfd78af_0": "sha256:9dc2b7e7019f682fbcff410eca22a0177beeddd3623597b535eb165bc87aab43"}, "docker": "quay.io/biocontainers/fastagap", "aliases": {"fastagap": "/usr/local/bin/fastagap"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastagap.
singularity registry hpc automated addition for fastagap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastagap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastagap:1.0.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastagap/1.0.1--hdfd78af_0
$ module help quay.io/biocontainers/fastagap/1.0.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastagap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastagap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastagap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastagap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastagap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastagap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastagap

```bash
$ singularity exec <container> /usr/local/bin/fastagap
$ podman run --it --rm --entrypoint /usr/local/bin/fastagap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastagap   -v ${PWD} -w ${PWD} <container> -c " $@"
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