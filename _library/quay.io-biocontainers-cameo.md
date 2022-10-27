---
layout: container
name:  "quay.io/biocontainers/cameo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cameo/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/cameo/container.yaml"
updated_at: "2022-10-27 01:03:25.498858"
latest: "0.13.6--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/cameo"
aliases:
 - "cameo"
 - "grako"
 - "httpx"
versions:
 - "0.13.6--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for cameo"
config: {"url": "https://biocontainers.pro/tools/cameo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cameo", "latest": {"0.13.6--pyhdfd78af_0": "sha256:a87c3d8258e0c7d3d30285ae263833747983aaccf992c50e36e26415c4133d02"}, "tags": {"0.13.6--pyhdfd78af_0": "sha256:a87c3d8258e0c7d3d30285ae263833747983aaccf992c50e36e26415c4133d02"}, "docker": "quay.io/biocontainers/cameo", "aliases": {"cameo": "/usr/local/bin/cameo", "grako": "/usr/local/bin/grako", "httpx": "/usr/local/bin/httpx"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cameo.
shpc-registry automated BioContainers addition for cameo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cameo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cameo:0.13.6--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cameo/0.13.6--pyhdfd78af_0
$ module help quay.io/biocontainers/cameo/0.13.6--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cameo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cameo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cameo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cameo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cameo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cameo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cameo

```bash
$ singularity exec <container> /usr/local/bin/cameo
$ podman run --it --rm --entrypoint /usr/local/bin/cameo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cameo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grako

```bash
$ singularity exec <container> /usr/local/bin/grako
$ podman run --it --rm --entrypoint /usr/local/bin/grako   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grako   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### httpx

```bash
$ singularity exec <container> /usr/local/bin/httpx
$ podman run --it --rm --entrypoint /usr/local/bin/httpx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/httpx   -v ${PWD} -w ${PWD} <container> -c " $@"
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