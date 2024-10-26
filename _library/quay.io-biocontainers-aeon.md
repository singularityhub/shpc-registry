---
layout: container
name:  "quay.io/biocontainers/aeon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/aeon/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/aeon/container.yaml"
updated_at: "2024-10-26 03:26:28.725609"
latest: "0.1.1--py310h4b6de7c_2"
container_url: "https://biocontainers.pro/tools/aeon"
aliases:
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.1.1--py39h3b2373f_0"
 - "0.1.1--py39h3b2373f_1"
 - "0.1.1--py310h4b6de7c_2"
 - "0.1.1--py39hb377b6a_2"
description: "singularity registry hpc automated addition for aeon"
config: {"url": "https://biocontainers.pro/tools/aeon", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for aeon", "latest": {"0.1.1--py310h4b6de7c_2": "sha256:a04ff094578b08bc1d3b92d424aa634c08c018b5a079c85cac23a8d7fd13b51a"}, "tags": {"0.1.1--py39h3b2373f_0": "sha256:947800f8b7cbccf4e0620bd09707dfe3878b0335a4d0a70753fdf7846985b0a7", "0.1.1--py39h3b2373f_1": "sha256:ce5a017491aaf37bda3c01498d3ab05c808f4d3295521daa584f444bea3e834c", "0.1.1--py310h4b6de7c_2": "sha256:a04ff094578b08bc1d3b92d424aa634c08c018b5a079c85cac23a8d7fd13b51a", "0.1.1--py39hb377b6a_2": "sha256:e8685403fa9309c9183fb9b867423544f9d453c158ed1b2304c67d790b251b22"}, "docker": "quay.io/biocontainers/aeon", "aliases": {"2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/aeon.
singularity registry hpc automated addition for aeon
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/aeon
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/aeon:0.1.1--py310h4b6de7c_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/aeon/0.1.1--py310h4b6de7c_2
$ module help quay.io/biocontainers/aeon/0.1.1--py310h4b6de7c_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### aeon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### aeon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### aeon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### aeon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### aeon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### aeon-inspect-deffile:

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