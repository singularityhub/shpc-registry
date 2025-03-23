---
layout: container
name:  "quay.io/biocontainers/primalscheme"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/primalscheme/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/primalscheme/container.yaml"
updated_at: "2025-03-23 03:36:44.566641"
latest: "1.4.1--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/primalscheme"
aliases:
 - "primalscheme"
 - "f2py3.8"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
 - "jpgicc"
 - "linkicc"
 - "psicc"
 - "tificc"
versions:
 - "1.3.2--pyh3252c3a_0"
 - "1.4.0--pyh7cba7a3_0"
 - "1.4.1--pyh7cba7a3_0"
description: "shpc-registry automated BioContainers addition for primalscheme"
config: {"url": "https://biocontainers.pro/tools/primalscheme", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for primalscheme", "latest": {"1.4.1--pyh7cba7a3_0": "sha256:69a47ee9d1c5adac427d7c19360cb770438f7dfa2b24faf3bbd0377a2eb04b6d"}, "tags": {"1.3.2--pyh3252c3a_0": "sha256:aef1517bfd9f869a065d5e471940fe17d307a40cb8c496e761317633835bd18e", "1.4.0--pyh7cba7a3_0": "sha256:d3258982ff70267d67316b8695815c82a661600c5b589f47258114d4ac1f4033", "1.4.1--pyh7cba7a3_0": "sha256:69a47ee9d1c5adac427d7c19360cb770438f7dfa2b24faf3bbd0377a2eb04b6d"}, "docker": "quay.io/biocontainers/primalscheme", "aliases": {"primalscheme": "/usr/local/bin/primalscheme", "f2py3.8": "/usr/local/bin/f2py3.8", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config", "jpgicc": "/usr/local/bin/jpgicc", "linkicc": "/usr/local/bin/linkicc", "psicc": "/usr/local/bin/psicc", "tificc": "/usr/local/bin/tificc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/primalscheme.
shpc-registry automated BioContainers addition for primalscheme
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/primalscheme
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/primalscheme:1.4.1--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/primalscheme/1.4.1--pyh7cba7a3_0
$ module help quay.io/biocontainers/primalscheme/1.4.1--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### primalscheme-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### primalscheme-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### primalscheme-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### primalscheme-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### primalscheme-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### primalscheme-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### primalscheme

```bash
$ singularity exec <container> /usr/local/bin/primalscheme
$ podman run --it --rm --entrypoint /usr/local/bin/primalscheme   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/primalscheme   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.8

```bash
$ singularity exec <container> /usr/local/bin/f2py3.8
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### jpgicc

```bash
$ singularity exec <container> /usr/local/bin/jpgicc
$ podman run --it --rm --entrypoint /usr/local/bin/jpgicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jpgicc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### linkicc

```bash
$ singularity exec <container> /usr/local/bin/linkicc
$ podman run --it --rm --entrypoint /usr/local/bin/linkicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/linkicc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psicc

```bash
$ singularity exec <container> /usr/local/bin/psicc
$ podman run --it --rm --entrypoint /usr/local/bin/psicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psicc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tificc

```bash
$ singularity exec <container> /usr/local/bin/tificc
$ podman run --it --rm --entrypoint /usr/local/bin/tificc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tificc   -v ${PWD} -w ${PWD} <container> -c " $@"
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