---
layout: container
name:  "quay.io/biocontainers/sorted_nearest"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sorted_nearest/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sorted_nearest/container.yaml"
updated_at: "2024-10-13 10:44:21.131359"
latest: "0.0.39--py39hff71179_4"
container_url: "https://biocontainers.pro/tools/sorted_nearest"
aliases:
 - "f2py3.9"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.0.32--py39hcbe4a3b_1"
 - "0.0.39--py38he5da3d1_0"
 - "0.0.39--py39hf95cd2a_1"
 - "0.0.39--py312hf67a6ed_2"
 - "0.0.39--py39hff71179_4"
description: "shpc-registry automated BioContainers addition for sorted_nearest"
config: {"url": "https://biocontainers.pro/tools/sorted_nearest", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sorted_nearest", "latest": {"0.0.39--py39hff71179_4": "sha256:17512b04b5d06de08ee97a84db0efd739c236271f11f4c99bfba56cdfd4aa99f"}, "tags": {"0.0.32--py39hcbe4a3b_1": "sha256:5e99e777b488e799c00dbd8d15ea0438bfb30a452c1f1818520569f98d21f99d", "0.0.39--py38he5da3d1_0": "sha256:bb842653b4173f55583524eb8ebc50b474b5cd5ee0f925680ef2afb3e58a1f7a", "0.0.39--py39hf95cd2a_1": "sha256:64c49ae95c170dac20b00af6e5a1ff27917f40be07af7ca3820bb3b25d01bc76", "0.0.39--py312hf67a6ed_2": "sha256:119a1aacd0427582bdab9e1e4dae392ae48927ad7777411df43bf47642b70375", "0.0.39--py39hff71179_4": "sha256:17512b04b5d06de08ee97a84db0efd739c236271f11f4c99bfba56cdfd4aa99f"}, "docker": "quay.io/biocontainers/sorted_nearest", "aliases": {"f2py3.9": "/usr/local/bin/f2py3.9", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sorted_nearest.
shpc-registry automated BioContainers addition for sorted_nearest
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sorted_nearest
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sorted_nearest:0.0.39--py39hff71179_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sorted_nearest/0.0.39--py39hff71179_4
$ module help quay.io/biocontainers/sorted_nearest/0.0.39--py39hff71179_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sorted_nearest-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sorted_nearest-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sorted_nearest-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sorted_nearest-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sorted_nearest-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sorted_nearest-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
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