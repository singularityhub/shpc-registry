---
layout: container
name:  "quay.io/biocontainers/gtfparse"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gtfparse/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gtfparse/container.yaml"
updated_at: "2025-04-25 02:43:37.321274"
latest: "2.5.0--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/gtfparse"
aliases:
 - "f2py3.8"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
versions:
 - "1.2.1--pyh864c0ab_0"
 - "2.0.1--pyh7cba7a3_0"
 - "2.0.1--pyh7cba7a3_1"
 - "2.4.1--pyh7cba7a3_0"
 - "2.3.0--pyh7cba7a3_0"
 - "2.1.0--pyh7cba7a3_0"
 - "2.5.0--pyh7cba7a3_0"
description: "shpc-registry automated BioContainers addition for gtfparse"
config: {"url": "https://biocontainers.pro/tools/gtfparse", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gtfparse", "latest": {"2.5.0--pyh7cba7a3_0": "sha256:3aed15c2a5457c7d21940e42d20982b77c14474313fc48d2dda99a006a6005e5"}, "tags": {"1.2.1--pyh864c0ab_0": "sha256:1a7bf400b3710a919b5ff4d188fc72bb9627430a1f83c719401fc4eac451e2f6", "2.0.1--pyh7cba7a3_0": "sha256:24b789270e606439b1b1e785904caa89216d639ff36c440edbaefcf20994afaa", "2.0.1--pyh7cba7a3_1": "sha256:faf8aecbcd8383e235f0287975c4addb91acafde9dffe1305e19b8fe034818ef", "2.4.1--pyh7cba7a3_0": "sha256:9ea61834d7cc39bcf296d91aedcb47843df566b7c2949ef3656a9aabe316e80f", "2.3.0--pyh7cba7a3_0": "sha256:b5b600f4363508f142c04fae4c25969ed8d0a41ff85c97837f1d44da570bf015", "2.1.0--pyh7cba7a3_0": "sha256:d3ba0167db211883fd8f0e61e9d700086186ab4016e56ffc597998833ce64bfb", "2.5.0--pyh7cba7a3_0": "sha256:3aed15c2a5457c7d21940e42d20982b77c14474313fc48d2dda99a006a6005e5"}, "docker": "quay.io/biocontainers/gtfparse", "aliases": {"f2py3.8": "/usr/local/bin/f2py3.8", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gtfparse.
shpc-registry automated BioContainers addition for gtfparse
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gtfparse
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gtfparse:2.5.0--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gtfparse/2.5.0--pyh7cba7a3_0
$ module help quay.io/biocontainers/gtfparse/2.5.0--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gtfparse-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gtfparse-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gtfparse-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gtfparse-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gtfparse-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gtfparse-inspect-deffile:

```bash
$ singularity inspect -d <container>
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