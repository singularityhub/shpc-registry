---
layout: container
name:  "quay.io/biocontainers/snakemake-interface-storage-plugins"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snakemake-interface-storage-plugins/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/snakemake-interface-storage-plugins/container.yaml"
updated_at: "2024-09-18 03:00:18.400059"
latest: "3.3.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/snakemake-interface-storage-plugins"
aliases:
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
versions:
 - "3.0.0--pyhdfd78af_0"
 - "3.1.0--pyhdfd78af_0"
 - "3.1.1--pyhdfd78af_0"
 - "3.2.2--pyhdfd78af_0"
 - "3.2.3--pyhdfd78af_0"
 - "3.3.0--pyhdfd78af_0"
 - "3.2.4--pyhdfd78af_0"
description: "singularity registry hpc automated addition for snakemake-interface-storage-plugins"
config: {"url": "https://biocontainers.pro/tools/snakemake-interface-storage-plugins", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for snakemake-interface-storage-plugins", "latest": {"3.3.0--pyhdfd78af_0": "sha256:30dca19f80892e96bb81eb7ac90f3abb97fb153171ac4516cbee1a6075bf2ca1"}, "tags": {"3.0.0--pyhdfd78af_0": "sha256:fff26829f5c349db37636618d67c71287ae45c140deb6f2ae6ba09cfb5f9e796", "3.1.0--pyhdfd78af_0": "sha256:16bc536bea4af31cfdc405ef702848fbe15b1027b6639a3311345f78676ca91d", "3.1.1--pyhdfd78af_0": "sha256:404acc66c566ca043863108888540b19111e5672a1741a08ed15aa26255f990a", "3.2.2--pyhdfd78af_0": "sha256:d0b7b9dec9a5e07a2e46173f752d0f29cedecd96e296d6b77963d48fba622ffb", "3.2.3--pyhdfd78af_0": "sha256:1da7b051f83fdba5b8cd73049367c550a73cb92cd2dbc381448e4a1ec552cef9", "3.3.0--pyhdfd78af_0": "sha256:30dca19f80892e96bb81eb7ac90f3abb97fb153171ac4516cbee1a6075bf2ca1", "3.2.4--pyhdfd78af_0": "sha256:9442636978a3a74369a40f6bb067c19f45a6e2596ad066a06bbe2b6f1c2478fc"}, "docker": "quay.io/biocontainers/snakemake-interface-storage-plugins", "aliases": {"2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snakemake-interface-storage-plugins.
singularity registry hpc automated addition for snakemake-interface-storage-plugins
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snakemake-interface-storage-plugins
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snakemake-interface-storage-plugins:3.3.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snakemake-interface-storage-plugins/3.3.0--pyhdfd78af_0
$ module help quay.io/biocontainers/snakemake-interface-storage-plugins/3.3.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snakemake-interface-storage-plugins-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snakemake-interface-storage-plugins-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snakemake-interface-storage-plugins-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snakemake-interface-storage-plugins-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snakemake-interface-storage-plugins-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snakemake-interface-storage-plugins-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.12

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.12
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.12

```bash
$ singularity exec <container> /usr/local/bin/idle3.12
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.12

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.12
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12

```bash
$ singularity exec <container> /usr/local/bin/python3.12
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12-config

```bash
$ singularity exec <container> /usr/local/bin/python3.12-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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