---
layout: container
name:  "quay.io/biocontainers/sonicparanoid"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sonicparanoid/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/sonicparanoid/container.yaml"
updated_at: "2022-10-27 00:43:59.952498"
latest: "1.3.8--py38h8ded8fe_2"
container_url: "https://biocontainers.pro/tools/sonicparanoid"
aliases:
 - "filetype"
 - "sonic-debug-infer-ortho-table"
 - "sonicparanoid"
 - "sonicparanoid-extract"
 - "sonicparanoid-get-test-data"
versions:
 - "1.3.8--py38h8ded8fe_2"
description: "shpc-registry automated BioContainers addition for sonicparanoid"
config: {"url": "https://biocontainers.pro/tools/sonicparanoid", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sonicparanoid", "latest": {"1.3.8--py38h8ded8fe_2": "sha256:a3e11e21e19d938fb2b6e162411a18de6623231b97b0fea02fd322086bbe92a0"}, "tags": {"1.3.8--py38h8ded8fe_2": "sha256:a3e11e21e19d938fb2b6e162411a18de6623231b97b0fea02fd322086bbe92a0"}, "docker": "quay.io/biocontainers/sonicparanoid", "aliases": {"filetype": "/usr/local/bin/filetype", "sonic-debug-infer-ortho-table": "/usr/local/bin/sonic-debug-infer-ortho-table", "sonicparanoid": "/usr/local/bin/sonicparanoid", "sonicparanoid-extract": "/usr/local/bin/sonicparanoid-extract", "sonicparanoid-get-test-data": "/usr/local/bin/sonicparanoid-get-test-data"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sonicparanoid.
shpc-registry automated BioContainers addition for sonicparanoid
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sonicparanoid
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sonicparanoid:1.3.8--py38h8ded8fe_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sonicparanoid/1.3.8--py38h8ded8fe_2
$ module help quay.io/biocontainers/sonicparanoid/1.3.8--py38h8ded8fe_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sonicparanoid-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sonicparanoid-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sonicparanoid-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sonicparanoid-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sonicparanoid-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sonicparanoid-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### filetype

```bash
$ singularity exec <container> /usr/local/bin/filetype
$ podman run --it --rm --entrypoint /usr/local/bin/filetype   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filetype   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sonic-debug-infer-ortho-table

```bash
$ singularity exec <container> /usr/local/bin/sonic-debug-infer-ortho-table
$ podman run --it --rm --entrypoint /usr/local/bin/sonic-debug-infer-ortho-table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sonic-debug-infer-ortho-table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sonicparanoid

```bash
$ singularity exec <container> /usr/local/bin/sonicparanoid
$ podman run --it --rm --entrypoint /usr/local/bin/sonicparanoid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sonicparanoid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sonicparanoid-extract

```bash
$ singularity exec <container> /usr/local/bin/sonicparanoid-extract
$ podman run --it --rm --entrypoint /usr/local/bin/sonicparanoid-extract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sonicparanoid-extract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sonicparanoid-get-test-data

```bash
$ singularity exec <container> /usr/local/bin/sonicparanoid-get-test-data
$ podman run --it --rm --entrypoint /usr/local/bin/sonicparanoid-get-test-data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sonicparanoid-get-test-data   -v ${PWD} -w ${PWD} <container> -c " $@"
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