---
layout: container
name:  "quay.io/biocontainers/bamdash"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bamdash/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bamdash/container.yaml"
updated_at: "2024-10-19 03:32:31.563089"
latest: "0.3.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/bamdash"
aliases:
 - "bamdash"
 - "kaleido"
 - "mathjax-path"
 - "certutil"
 - "nspr-config"
 - "nss-config"
 - "pk12util"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
versions:
 - "0.2.1--pyhdfd78af_0"
 - "0.2.2--pyhdfd78af_0"
 - "0.2.3--pyhdfd78af_0"
 - "0.2.4--pyhdfd78af_0"
 - "0.3.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for bamdash"
config: {"url": "https://biocontainers.pro/tools/bamdash", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bamdash", "latest": {"0.3.1--pyhdfd78af_0": "sha256:616c90010dcc1c9841ee2ba721f2001ceec40c6a5ab01dcbf53a523cbc2248d9"}, "tags": {"0.2.1--pyhdfd78af_0": "sha256:80f8539104b23829726bd2d12b12bece869a619153fd30028d0a7564e34c3e89", "0.2.2--pyhdfd78af_0": "sha256:19a0d354a4f8af8198cc77976f545fdf2ab288913f36a1931e26bfb9f46dbe62", "0.2.3--pyhdfd78af_0": "sha256:8ae7b5d05d47492a0038ba9c5bdef9d2b5b3e4214b7ebddc06c84b3ff59f384a", "0.2.4--pyhdfd78af_0": "sha256:5448bef748798f6ab7bd013049319fec12c011e678593af9a98f265701504bd9", "0.3.1--pyhdfd78af_0": "sha256:616c90010dcc1c9841ee2ba721f2001ceec40c6a5ab01dcbf53a523cbc2248d9"}, "docker": "quay.io/biocontainers/bamdash", "aliases": {"bamdash": "/usr/local/bin/bamdash", "kaleido": "/usr/local/bin/kaleido", "mathjax-path": "/usr/local/bin/mathjax-path", "certutil": "/usr/local/bin/certutil", "nspr-config": "/usr/local/bin/nspr-config", "nss-config": "/usr/local/bin/nss-config", "pk12util": "/usr/local/bin/pk12util", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bamdash.
singularity registry hpc automated addition for bamdash
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bamdash
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bamdash:0.3.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bamdash/0.3.1--pyhdfd78af_0
$ module help quay.io/biocontainers/bamdash/0.3.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bamdash-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bamdash-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bamdash-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bamdash-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bamdash-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bamdash-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bamdash

```bash
$ singularity exec <container> /usr/local/bin/bamdash
$ podman run --it --rm --entrypoint /usr/local/bin/bamdash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamdash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaleido

```bash
$ singularity exec <container> /usr/local/bin/kaleido
$ podman run --it --rm --entrypoint /usr/local/bin/kaleido   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaleido   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mathjax-path

```bash
$ singularity exec <container> /usr/local/bin/mathjax-path
$ podman run --it --rm --entrypoint /usr/local/bin/mathjax-path   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mathjax-path   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### certutil

```bash
$ singularity exec <container> /usr/local/bin/certutil
$ podman run --it --rm --entrypoint /usr/local/bin/certutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/certutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nspr-config

```bash
$ singularity exec <container> /usr/local/bin/nspr-config
$ podman run --it --rm --entrypoint /usr/local/bin/nspr-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nspr-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nss-config

```bash
$ singularity exec <container> /usr/local/bin/nss-config
$ podman run --it --rm --entrypoint /usr/local/bin/nss-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nss-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pk12util

```bash
$ singularity exec <container> /usr/local/bin/pk12util
$ podman run --it --rm --entrypoint /usr/local/bin/pk12util   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pk12util   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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