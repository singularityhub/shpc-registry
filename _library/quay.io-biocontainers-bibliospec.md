---
layout: container
name:  "quay.io/biocontainers/bibliospec"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bibliospec/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bibliospec/container.yaml"
updated_at: "2023-12-24 02:47:31.187261"
latest: "1.0--h2d50403_1"
container_url: "https://biocontainers.pro/tools/bibliospec"
aliases:
 - "BlibBuild"
 - "BlibFilter"
 - "BlibSearch"
 - "BlibToMs2"
versions:
 - "1.0--h2d50403_1"
description: "shpc-registry automated BioContainers addition for bibliospec"
config: {"url": "https://biocontainers.pro/tools/bibliospec", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bibliospec", "latest": {"1.0--h2d50403_1": "sha256:cda5a11f0102d6b0a2a14733aa933ab66831bb877eccd7826ef889a37dd34078"}, "tags": {"1.0--h2d50403_1": "sha256:cda5a11f0102d6b0a2a14733aa933ab66831bb877eccd7826ef889a37dd34078"}, "docker": "quay.io/biocontainers/bibliospec", "aliases": {"BlibBuild": "/usr/local/bin/BlibBuild", "BlibFilter": "/usr/local/bin/BlibFilter", "BlibSearch": "/usr/local/bin/BlibSearch", "BlibToMs2": "/usr/local/bin/BlibToMs2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bibliospec.
shpc-registry automated BioContainers addition for bibliospec
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bibliospec
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bibliospec:1.0--h2d50403_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bibliospec/1.0--h2d50403_1
$ module help quay.io/biocontainers/bibliospec/1.0--h2d50403_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bibliospec-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bibliospec-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bibliospec-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bibliospec-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bibliospec-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bibliospec-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### BlibBuild

```bash
$ singularity exec <container> /usr/local/bin/BlibBuild
$ podman run --it --rm --entrypoint /usr/local/bin/BlibBuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BlibBuild   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### BlibFilter

```bash
$ singularity exec <container> /usr/local/bin/BlibFilter
$ podman run --it --rm --entrypoint /usr/local/bin/BlibFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BlibFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### BlibSearch

```bash
$ singularity exec <container> /usr/local/bin/BlibSearch
$ podman run --it --rm --entrypoint /usr/local/bin/BlibSearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BlibSearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### BlibToMs2

```bash
$ singularity exec <container> /usr/local/bin/BlibToMs2
$ podman run --it --rm --entrypoint /usr/local/bin/BlibToMs2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BlibToMs2   -v ${PWD} -w ${PWD} <container> -c " $@"
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