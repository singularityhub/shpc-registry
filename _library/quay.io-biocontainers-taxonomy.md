---
layout: container
name:  "quay.io/biocontainers/taxonomy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/taxonomy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/taxonomy/container.yaml"
updated_at: "2024-06-17 02:39:48.383650"
latest: "0.10.0--py38h61b5871_1"
container_url: "https://biocontainers.pro/tools/taxonomy"
aliases:
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.9.0--py39hbf8eff0_0"
 - "0.10.0--py39hb377b6a_0"
 - "0.10.0--py310h4b6de7c_0"
 - "0.9.0--py310h1425a21_0"
 - "0.10.0--py38h61b5871_1"
description: "shpc-registry automated BioContainers addition for taxonomy"
config: {"url": "https://biocontainers.pro/tools/taxonomy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for taxonomy", "latest": {"0.10.0--py38h61b5871_1": "sha256:f7fe3ca70d20cf7a4e801b3ba500ca590cd78dc76d06fdce09afd66669c2fc03"}, "tags": {"0.9.0--py39hbf8eff0_0": "sha256:df1f9c27aa0e002acd8ed0422170005175424855ae697197f0bde3eb00c9a0c4", "0.10.0--py39hb377b6a_0": "sha256:653bfd162ceb21839a2d2515a3ed6bc5c4eb33357ea3b19256cab5b589c472b0", "0.10.0--py310h4b6de7c_0": "sha256:6e11b08d499cdc4f7a3542010998c581c3cd2ac1211d870f8da6de183e509605", "0.9.0--py310h1425a21_0": "sha256:9d6515a7f248ed8dbdfec69f3baa0554403a41b540bbf5d24f4ab9672263d6ed", "0.10.0--py38h61b5871_1": "sha256:f7fe3ca70d20cf7a4e801b3ba500ca590cd78dc76d06fdce09afd66669c2fc03"}, "docker": "quay.io/biocontainers/taxonomy", "aliases": {"2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/taxonomy.
shpc-registry automated BioContainers addition for taxonomy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/taxonomy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/taxonomy:0.10.0--py38h61b5871_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/taxonomy/0.10.0--py38h61b5871_1
$ module help quay.io/biocontainers/taxonomy/0.10.0--py38h61b5871_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### taxonomy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### taxonomy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### taxonomy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### taxonomy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### taxonomy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### taxonomy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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