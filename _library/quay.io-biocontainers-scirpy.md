---
layout: container
name:  "quay.io/biocontainers/scirpy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scirpy/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/scirpy/container.yaml"
updated_at: "2022-10-29 05:37:24.733985"
latest: "0.9.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/scirpy"
aliases:
 - "airr-tools"
 - "2to3-3.9"
 - "chardetect"
 - "cmpfillin"
 - "dunamai"
 - "f2py3.9"
 - "gif2h5"
 - "glpsol"
 - "gpmetis"
 - "graphchk"
 - "h52gif"
versions:
 - "0.9.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for scirpy"
config: {"url": "https://biocontainers.pro/tools/scirpy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for scirpy", "latest": {"0.9.1--pyhdfd78af_0": "sha256:b9c7892ee076733df38e6d66abacdce0a5900964a9391437cf5923d5afc89bd8"}, "tags": {"0.9.1--pyhdfd78af_0": "sha256:b9c7892ee076733df38e6d66abacdce0a5900964a9391437cf5923d5afc89bd8"}, "docker": "quay.io/biocontainers/scirpy", "aliases": {"airr-tools": "/usr/local/bin/airr-tools", "2to3-3.9": "/usr/local/bin/2to3-3.9", "chardetect": "/usr/local/bin/chardetect", "cmpfillin": "/usr/local/bin/cmpfillin", "dunamai": "/usr/local/bin/dunamai", "f2py3.9": "/usr/local/bin/f2py3.9", "gif2h5": "/usr/local/bin/gif2h5", "glpsol": "/usr/local/bin/glpsol", "gpmetis": "/usr/local/bin/gpmetis", "graphchk": "/usr/local/bin/graphchk", "h52gif": "/usr/local/bin/h52gif"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/scirpy.
shpc-registry automated BioContainers addition for scirpy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scirpy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scirpy:0.9.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scirpy/0.9.1--pyhdfd78af_0
$ module help quay.io/biocontainers/scirpy/0.9.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scirpy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scirpy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scirpy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scirpy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scirpy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scirpy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### airr-tools

```bash
$ singularity exec <container> /usr/local/bin/airr-tools
$ podman run --it --rm --entrypoint /usr/local/bin/airr-tools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/airr-tools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmpfillin

```bash
$ singularity exec <container> /usr/local/bin/cmpfillin
$ podman run --it --rm --entrypoint /usr/local/bin/cmpfillin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmpfillin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dunamai

```bash
$ singularity exec <container> /usr/local/bin/dunamai
$ podman run --it --rm --entrypoint /usr/local/bin/dunamai   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dunamai   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2h5

```bash
$ singularity exec <container> /usr/local/bin/gif2h5
$ podman run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpmetis

```bash
$ singularity exec <container> /usr/local/bin/gpmetis
$ podman run --it --rm --entrypoint /usr/local/bin/gpmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### graphchk

```bash
$ singularity exec <container> /usr/local/bin/graphchk
$ podman run --it --rm --entrypoint /usr/local/bin/graphchk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/graphchk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h52gif

```bash
$ singularity exec <container> /usr/local/bin/h52gif
$ podman run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
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