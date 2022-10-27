---
layout: container
name:  "quay.io/biocontainers/ppanggolin"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ppanggolin/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ppanggolin/container.yaml"
updated_at: "2022-10-27 01:13:19.101093"
latest: "v0.3.88--py36h516909a_1"
container_url: "https://biocontainers.pro/tools/ppanggolin"
aliases:
 - "gawk-5.0.1"
 - "ppanggolin"
versions:
 - "v0.3.88--py36h516909a_1"
description: "shpc-registry automated BioContainers addition for ppanggolin"
config: {"url": "https://biocontainers.pro/tools/ppanggolin", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ppanggolin", "latest": {"v0.3.88--py36h516909a_1": "sha256:042eac580f6968117ee323c4840d0478333a6c0595561c21632b08675b95e54a"}, "tags": {"v0.3.88--py36h516909a_1": "sha256:042eac580f6968117ee323c4840d0478333a6c0595561c21632b08675b95e54a"}, "docker": "quay.io/biocontainers/ppanggolin", "aliases": {"gawk-5.0.1": "/usr/local/bin/gawk-5.0.1", "ppanggolin": "/usr/local/bin/ppanggolin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ppanggolin.
shpc-registry automated BioContainers addition for ppanggolin
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ppanggolin
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ppanggolin:v0.3.88--py36h516909a_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ppanggolin/v0.3.88--py36h516909a_1
$ module help quay.io/biocontainers/ppanggolin/v0.3.88--py36h516909a_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ppanggolin-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ppanggolin-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ppanggolin-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ppanggolin-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ppanggolin-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ppanggolin-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gawk-5.0.1

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.0.1
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.0.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.0.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ppanggolin

```bash
$ singularity exec <container> /usr/local/bin/ppanggolin
$ podman run --it --rm --entrypoint /usr/local/bin/ppanggolin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ppanggolin   -v ${PWD} -w ${PWD} <container> -c " $@"
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