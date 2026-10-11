---
layout: container
name:  "quay.io/biocontainers/sativa-epang"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sativa-epang/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sativa-epang/container.yaml"
updated_at: "2026-10-11 08:30:43.323337"
latest: "0.9.3.4--py314hab16a5f_0"
container_url: "https://biocontainers.pro/tools/sativa-epang"
aliases:
 - "epa-ng"
 - "sativa-epang"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
versions:
 - "0.9.3.4--py314hab16a5f_0"
description: "singularity registry hpc automated addition for sativa-epang"
config: {"url": "https://biocontainers.pro/tools/sativa-epang", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sativa-epang", "latest": {"0.9.3.4--py314hab16a5f_0": "sha256:cbf6c158860970a5807758a60a0450542f788de0ad3e34c272bbdb92f2b3dbaf"}, "tags": {"0.9.3.4--py314hab16a5f_0": "sha256:cbf6c158860970a5807758a60a0450542f788de0ad3e34c272bbdb92f2b3dbaf"}, "docker": "quay.io/biocontainers/sativa-epang", "aliases": {"epa-ng": "/usr/local/bin/epa-ng", "sativa-epang": "/usr/local/bin/sativa-epang", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sativa-epang.
singularity registry hpc automated addition for sativa-epang
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sativa-epang
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sativa-epang:0.9.3.4--py314hab16a5f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sativa-epang/0.9.3.4--py314hab16a5f_0
$ module help quay.io/biocontainers/sativa-epang/0.9.3.4--py314hab16a5f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sativa-epang-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sativa-epang-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sativa-epang-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sativa-epang-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sativa-epang-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sativa-epang-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### epa-ng

```bash
$ singularity exec <container> /usr/local/bin/epa-ng
$ podman run --it --rm --entrypoint /usr/local/bin/epa-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/epa-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sativa-epang

```bash
$ singularity exec <container> /usr/local/bin/sativa-epang
$ podman run --it --rm --entrypoint /usr/local/bin/sativa-epang   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sativa-epang   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.14

```bash
$ singularity exec <container> /usr/local/bin/idle3.14
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.14

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.14
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14

```bash
$ singularity exec <container> /usr/local/bin/python3.14
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14-config

```bash
$ singularity exec <container> /usr/local/bin/python3.14-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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