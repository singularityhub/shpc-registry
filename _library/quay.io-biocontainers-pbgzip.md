---
layout: container
name:  "quay.io/biocontainers/pbgzip"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pbgzip/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pbgzip/container.yaml"
updated_at: "2023-08-28 09:36:13.860185"
latest: "2016.08.04--h9d449c0_4"
container_url: "https://biocontainers.pro/tools/pbgzip"
aliases:
 - "pbgzip"
versions:
 - "2016.08.04--h67092d7_3"
 - "2016.08.04--h9d449c0_4"
description: "shpc-registry automated BioContainers addition for pbgzip"
config: {"url": "https://biocontainers.pro/tools/pbgzip", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pbgzip", "latest": {"2016.08.04--h9d449c0_4": "sha256:dfef1b7444ee57396c805060b1f7edc1d8042e00a8f70eec4191c77054ff7be3"}, "tags": {"2016.08.04--h67092d7_3": "sha256:a3259f6de5fb63cf9e07e546aec7c9086a6a04f88ab736ff84608a5b9385706f", "2016.08.04--h9d449c0_4": "sha256:dfef1b7444ee57396c805060b1f7edc1d8042e00a8f70eec4191c77054ff7be3"}, "docker": "quay.io/biocontainers/pbgzip", "aliases": {"pbgzip": "/usr/local/bin/pbgzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pbgzip.
shpc-registry automated BioContainers addition for pbgzip
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pbgzip
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pbgzip:2016.08.04--h9d449c0_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pbgzip/2016.08.04--h9d449c0_4
$ module help quay.io/biocontainers/pbgzip/2016.08.04--h9d449c0_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pbgzip-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pbgzip-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pbgzip-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pbgzip-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pbgzip-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pbgzip-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pbgzip

```bash
$ singularity exec <container> /usr/local/bin/pbgzip
$ podman run --it --rm --entrypoint /usr/local/bin/pbgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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