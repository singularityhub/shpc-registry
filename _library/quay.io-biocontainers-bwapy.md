---
layout: container
name:  "quay.io/biocontainers/bwapy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bwapy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bwapy/container.yaml"
updated_at: "2025-05-25 04:08:56.527444"
latest: "0.1.4--py311h384fd50_10"
container_url: "https://biocontainers.pro/tools/bwapy"
aliases:
 - "bwamempy"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
versions:
 - "0.1.4--py38h4c6a040_4"
 - "0.1.4--py38h7cf9df2_7"
 - "0.1.4--py39h3d4b85c_7"
 - "0.1.4--py39he47c912_8"
 - "0.1.4--py310h397c9d8_9"
 - "0.1.4--py311h384fd50_10"
description: "shpc-registry automated BioContainers addition for bwapy"
config: {"url": "https://biocontainers.pro/tools/bwapy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bwapy", "latest": {"0.1.4--py311h384fd50_10": "sha256:ab5a4fd32e49c5e5ca05c49bd9bebaf4cbfef2e28a5daaf97d351ec890835762"}, "tags": {"0.1.4--py38h4c6a040_4": "sha256:6f599a6ca627e20a7bbda59aefe2f54f987a94584f83006813e7f12862bbca8e", "0.1.4--py38h7cf9df2_7": "sha256:f316ac5c2ebcf6edccd457e2f3742dbdcc3bab0d426412510918ce510798b256", "0.1.4--py39h3d4b85c_7": "sha256:0b767194c5ed3b6131fab786d1f548ba8bf92dec3a1aff3bcd7f690ae962c4fd", "0.1.4--py39he47c912_8": "sha256:66469fd8184c104af0fc406d360a00d824c7fa9aac82aae15dab6effbd2dbfbe", "0.1.4--py310h397c9d8_9": "sha256:86024a018f97a7b8373af7c1f6bdb30226a2673acc15c898d27c076fc15cc38b", "0.1.4--py311h384fd50_10": "sha256:ab5a4fd32e49c5e5ca05c49bd9bebaf4cbfef2e28a5daaf97d351ec890835762"}, "docker": "quay.io/biocontainers/bwapy", "aliases": {"bwamempy": "/usr/local/bin/bwamempy", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bwapy.
shpc-registry automated BioContainers addition for bwapy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bwapy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bwapy:0.1.4--py311h384fd50_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bwapy/0.1.4--py311h384fd50_10
$ module help quay.io/biocontainers/bwapy/0.1.4--py311h384fd50_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bwapy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bwapy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bwapy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bwapy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bwapy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bwapy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bwamempy

```bash
$ singularity exec <container> /usr/local/bin/bwamempy
$ podman run --it --rm --entrypoint /usr/local/bin/bwamempy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwamempy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.8
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8

```bash
$ singularity exec <container> /usr/local/bin/python3.8
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8-config

```bash
$ singularity exec <container> /usr/local/bin/python3.8-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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