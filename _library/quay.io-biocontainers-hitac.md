---
layout: container
name:  "quay.io/biocontainers/hitac"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hitac/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hitac/container.yaml"
updated_at: "2024-12-17 03:13:53.968028"
latest: "2.2.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/hitac"
aliases:
 - "hiclass"
 - "doesitcache"
 - "ipython3"
 - "ipython"
 - "cygdb"
 - "cython"
 - "cythonize"
 - "py.test"
 - "pytest"
 - "natsort"
 - "mirror_server"
versions:
 - "2.0.9--pyhdfd78af_1"
 - "2.0.21--pyhdfd78af_0"
 - "2.0.23--pyhdfd78af_0"
 - "2.0.28--pyhdfd78af_0"
 - "2.0.30--pyhdfd78af_0"
 - "2.2.1--pyhdfd78af_0"
 - "2.1.1--pyhdfd78af_0"
 - "2.2.2--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for hitac"
config: {"url": "https://biocontainers.pro/tools/hitac", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hitac", "latest": {"2.2.2--pyhdfd78af_0": "sha256:7676960d7075a115d46cc86379bcf701106ca7ba7e1bc4bb56a7ca84f4400920"}, "tags": {"2.0.9--pyhdfd78af_1": "sha256:93e8fbf4c59aec2d7144867b2ccf5efb3d8895de6a1cdd25aec13f077536fdd4", "2.0.21--pyhdfd78af_0": "sha256:a5fa1532708e157cc37614dcff5294da86c2260aa10b8305612409d5fb9d339d", "2.0.23--pyhdfd78af_0": "sha256:c27a6c5243fa97fb5f32945abda8c36cfa53802ece59ae79ee5cb0a54014684a", "2.0.28--pyhdfd78af_0": "sha256:a4dbd62a173cdcf4e08c03ad4509e8fdbac4a48bb1590a29fae960bcead1e1e3", "2.0.30--pyhdfd78af_0": "sha256:b6c5dbdbc955089b3ea8309093e5bbe324020e5a208e7e5d1d53c4478ae064a3", "2.2.1--pyhdfd78af_0": "sha256:97fd50cff28b9e2fd4c497dc478205cf16cdc078b56bd045eb14eaeac31c36a2", "2.1.1--pyhdfd78af_0": "sha256:8889c7ab7fe82ff8c16e2324d57fc4102dbab977aff79ede31ab0dd7ba369f70", "2.2.2--pyhdfd78af_0": "sha256:7676960d7075a115d46cc86379bcf701106ca7ba7e1bc4bb56a7ca84f4400920"}, "docker": "quay.io/biocontainers/hitac", "aliases": {"hiclass": "/usr/local/bin/hiclass", "doesitcache": "/usr/local/bin/doesitcache", "ipython3": "/usr/local/bin/ipython3", "ipython": "/usr/local/bin/ipython", "cygdb": "/usr/local/bin/cygdb", "cython": "/usr/local/bin/cython", "cythonize": "/usr/local/bin/cythonize", "py.test": "/usr/local/bin/py.test", "pytest": "/usr/local/bin/pytest", "natsort": "/usr/local/bin/natsort", "mirror_server": "/usr/local/bin/mirror_server"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hitac.
shpc-registry automated BioContainers addition for hitac
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hitac
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hitac:2.2.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hitac/2.2.2--pyhdfd78af_0
$ module help quay.io/biocontainers/hitac/2.2.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hitac-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hitac-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hitac-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hitac-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hitac-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hitac-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hiclass

```bash
$ singularity exec <container> /usr/local/bin/hiclass
$ podman run --it --rm --entrypoint /usr/local/bin/hiclass   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hiclass   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### doesitcache

```bash
$ singularity exec <container> /usr/local/bin/doesitcache
$ podman run --it --rm --entrypoint /usr/local/bin/doesitcache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/doesitcache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython3

```bash
$ singularity exec <container> /usr/local/bin/ipython3
$ podman run --it --rm --entrypoint /usr/local/bin/ipython3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython

```bash
$ singularity exec <container> /usr/local/bin/ipython
$ podman run --it --rm --entrypoint /usr/local/bin/ipython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cygdb

```bash
$ singularity exec <container> /usr/local/bin/cygdb
$ podman run --it --rm --entrypoint /usr/local/bin/cygdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cygdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cython

```bash
$ singularity exec <container> /usr/local/bin/cython
$ podman run --it --rm --entrypoint /usr/local/bin/cython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cythonize

```bash
$ singularity exec <container> /usr/local/bin/cythonize
$ podman run --it --rm --entrypoint /usr/local/bin/cythonize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cythonize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### py.test

```bash
$ singularity exec <container> /usr/local/bin/py.test
$ podman run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pytest

```bash
$ singularity exec <container> /usr/local/bin/pytest
$ podman run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### natsort

```bash
$ singularity exec <container> /usr/local/bin/natsort
$ podman run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mirror_server

```bash
$ singularity exec <container> /usr/local/bin/mirror_server
$ podman run --it --rm --entrypoint /usr/local/bin/mirror_server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mirror_server   -v ${PWD} -w ${PWD} <container> -c " $@"
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