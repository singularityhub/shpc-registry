---
layout: container
name:  "quay.io/biocontainers/cs-tagger"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cs-tagger/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cs-tagger/container.yaml"
updated_at: "2026-06-30 06:16:50.923489"
latest: "0.3.0--h0feb368_0"
container_url: "https://biocontainers.pro/tools/cs-tagger"
aliases:
 - "cs-tagger"
versions:
 - "0.3.0--h0feb368_0"
description: "singularity registry hpc automated addition for cs-tagger"
config: {"url": "https://biocontainers.pro/tools/cs-tagger", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for cs-tagger", "latest": {"0.3.0--h0feb368_0": "sha256:6df2cabd088595add939d4f77820c1059cc5db8c0c9597f05d52370bf59a3ea5"}, "tags": {"0.3.0--h0feb368_0": "sha256:6df2cabd088595add939d4f77820c1059cc5db8c0c9597f05d52370bf59a3ea5"}, "docker": "quay.io/biocontainers/cs-tagger", "aliases": {"cs-tagger": "/usr/local/bin/cs-tagger"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cs-tagger.
singularity registry hpc automated addition for cs-tagger
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cs-tagger
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cs-tagger:0.3.0--h0feb368_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cs-tagger/0.3.0--h0feb368_0
$ module help quay.io/biocontainers/cs-tagger/0.3.0--h0feb368_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cs-tagger-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cs-tagger-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cs-tagger-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cs-tagger-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cs-tagger-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cs-tagger-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cs-tagger

```bash
$ singularity exec <container> /usr/local/bin/cs-tagger
$ podman run --it --rm --entrypoint /usr/local/bin/cs-tagger   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cs-tagger   -v ${PWD} -w ${PWD} <container> -c " $@"
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