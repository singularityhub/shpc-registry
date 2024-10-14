---
layout: container
name:  "quay.io/biocontainers/unifrac-binaries"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/unifrac-binaries/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/unifrac-binaries/container.yaml"
updated_at: "2024-10-14 03:24:29.335297"
latest: "1.4--h1d423cb_0"
container_url: "https://biocontainers.pro/tools/unifrac-binaries"
aliases:
 - "faithpd"
 - "ssu"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "python3.1"
versions:
 - "1.2.1--h73f19ed_0"
 - "1.2--h73f19ed_1"
 - "1.3--h73f19ed_0"
 - "1.3.1--h73f19ed_0"
 - "1.3.2--hb7a8b62_2"
 - "1.4--h1d423cb_0"
description: "singularity registry hpc automated addition for unifrac-binaries"
config: {"url": "https://biocontainers.pro/tools/unifrac-binaries", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for unifrac-binaries", "latest": {"1.4--h1d423cb_0": "sha256:2a98180824014efc2f860101e4f7ac6c980a9ec9d60d32a7fbfde431cce0a6f4"}, "tags": {"1.2.1--h73f19ed_0": "sha256:a50076a5c603fd35b838dc8fa34e9795286f20cfe6963e436ac4ac1a715aff82", "1.2--h73f19ed_1": "sha256:abf06bfaa768b6445729da95163f7d2cb5de0ed24a342f8cdf0abf627f0a668e", "1.3--h73f19ed_0": "sha256:0f4151fe3507771bd2c253dc60dfc76b52d22cecfbcfa84e05883f31d5676107", "1.3.1--h73f19ed_0": "sha256:160867dc5dbf8f102827dabf330f59d0ef4fcef94d2ab3b51f7b600a3539d773", "1.3.2--hb7a8b62_2": "sha256:2e9d25bf4ee145311464aa55e0fda00120130db35e6bfe4d8c50262673e44190", "1.4--h1d423cb_0": "sha256:2a98180824014efc2f860101e4f7ac6c980a9ec9d60d32a7fbfde431cce0a6f4"}, "docker": "quay.io/biocontainers/unifrac-binaries", "aliases": {"faithpd": "/usr/local/bin/faithpd", "ssu": "/usr/local/bin/ssu", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/unifrac-binaries.
singularity registry hpc automated addition for unifrac-binaries
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/unifrac-binaries
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/unifrac-binaries:1.4--h1d423cb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/unifrac-binaries/1.4--h1d423cb_0
$ module help quay.io/biocontainers/unifrac-binaries/1.4--h1d423cb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### unifrac-binaries-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### unifrac-binaries-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### unifrac-binaries-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### unifrac-binaries-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### unifrac-binaries-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### unifrac-binaries-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### faithpd

```bash
$ singularity exec <container> /usr/local/bin/faithpd
$ podman run --it --rm --entrypoint /usr/local/bin/faithpd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faithpd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ssu

```bash
$ singularity exec <container> /usr/local/bin/ssu
$ podman run --it --rm --entrypoint /usr/local/bin/ssu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ssu   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.11

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.11
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.11

```bash
$ singularity exec <container> /usr/local/bin/idle3.11
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.11

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.11
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11

```bash
$ singularity exec <container> /usr/local/bin/python3.11
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11-config

```bash
$ singularity exec <container> /usr/local/bin/python3.11-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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