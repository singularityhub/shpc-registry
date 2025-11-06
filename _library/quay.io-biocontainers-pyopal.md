---
layout: container
name:  "quay.io/biocontainers/pyopal"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyopal/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pyopal/container.yaml"
updated_at: "2025-11-06 03:59:41.945676"
latest: "0.7.3--py312h9c9b0c2_0"
container_url: "https://biocontainers.pro/tools/pyopal"
aliases:
 - "archspec"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
versions:
 - "0.3.0--py38hcbe9525_0"
 - "0.4.0--py39he10ea66_0"
 - "0.4.1--py38hcbe9525_0"
 - "0.5.1--py310h068649b_0"
 - "0.5.2--py38hcbe9525_0"
 - "0.5.2--py39he10ea66_0"
 - "0.4.1--py310h068649b_0"
 - "0.3.0--py310h068649b_0"
 - "0.6.0--py38hcbe9525_0"
 - "0.6.1--py312h719dbc0_1"
 - "0.7.0--py38hfe239e1_0"
 - "0.7.0--py310h8ea774a_1"
 - "0.7.1--py39he88f293_0"
 - "0.7.2--py312h9c9b0c2_0"
 - "0.7.3--py312h9c9b0c2_0"
description: "singularity registry hpc automated addition for pyopal"
config: {"url": "https://biocontainers.pro/tools/pyopal", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pyopal", "latest": {"0.7.3--py312h9c9b0c2_0": "sha256:85c73942ce74558bfabc6e3ab8af89f28f82ad8de1c9b31fa76f445d2fc3dc6f"}, "tags": {"0.3.0--py38hcbe9525_0": "sha256:f40fa611d0a9f2b710641934b5285ff8aa5d614145eabde81e34673223b947db", "0.4.0--py39he10ea66_0": "sha256:b563fc9590cb1cf13374ddf8e5782e258ffd8db832fb916a7257bf01a9f1a238", "0.4.1--py38hcbe9525_0": "sha256:a215607eba82ca074619fb0ca71861fe159c06f2ac01640009fa1e359128077b", "0.5.1--py310h068649b_0": "sha256:903d33d5abb353a4740ea1c63fae5b66e6c514101e8a7a0e68a322b32f1559a8", "0.5.2--py38hcbe9525_0": "sha256:22399d1c986fdeef504bd3cf8099e3abbf21948cc3463859ff4becb8aecef9ba", "0.5.2--py39he10ea66_0": "sha256:bc5e9b06b2e7360eaef2401a84fb2a447f77aae34ac989d21d89121a755dd43d", "0.4.1--py310h068649b_0": "sha256:b95bd19daaf527439652caec1ae573a8e625505522d69698360d3722eedbf8c4", "0.3.0--py310h068649b_0": "sha256:71e39c00f1db835247f47b632131b44ab2cabf475c63a582b58c303db25447de", "0.6.0--py38hcbe9525_0": "sha256:33b46218c1f512a3517e02200122f1824aed949f92aab40cc3f74bd0f2ac5a19", "0.6.1--py312h719dbc0_1": "sha256:f1a7120c5433a5dbaf3e7f7be88a91f24e99bd16f68fffc22b97a9609adf5e2a", "0.7.0--py38hfe239e1_0": "sha256:a299eb8c4fd383b35fa3d74884b6ab477960fd6fe73ce3bf263e948f278ac204", "0.7.0--py310h8ea774a_1": "sha256:253e121bbeb5d3aa1445bcd4efd1ef54f451e776c796f3cd434b43baee7f19af", "0.7.1--py39he88f293_0": "sha256:20d2d37771ad969a56406f2bae71a84bfc3220aa622b433e458a25e2904896cc", "0.7.2--py312h9c9b0c2_0": "sha256:175d95f40cdb0aa4724b2249ebd97f5332c6a74b090246953ff9121dcb0ffd4b", "0.7.3--py312h9c9b0c2_0": "sha256:85c73942ce74558bfabc6e3ab8af89f28f82ad8de1c9b31fa76f445d2fc3dc6f"}, "docker": "quay.io/biocontainers/pyopal", "aliases": {"archspec": "/usr/local/bin/archspec", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyopal.
singularity registry hpc automated addition for pyopal
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyopal
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyopal:0.7.3--py312h9c9b0c2_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyopal/0.7.3--py312h9c9b0c2_0
$ module help quay.io/biocontainers/pyopal/0.7.3--py312h9c9b0c2_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyopal-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyopal-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyopal-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyopal-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyopal-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyopal-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### archspec

```bash
$ singularity exec <container> /usr/local/bin/archspec
$ podman run --it --rm --entrypoint /usr/local/bin/archspec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archspec   -v ${PWD} -w ${PWD} <container> -c " $@"
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