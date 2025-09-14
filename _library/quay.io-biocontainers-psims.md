---
layout: container
name:  "quay.io/biocontainers/psims"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/psims/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/psims/container.yaml"
updated_at: "2025-09-14 03:17:24.895858"
latest: "1.3.5--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/psims"
aliases:
 - "f2py3.11"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "xslt-config"
 - "xsltproc"
 - "python3.1"
versions:
 - "1.2.3--pyh7cba7a3_0"
 - "1.2.5--pyh7cba7a3_0"
 - "1.2.6--pyh7cba7a3_0"
 - "1.2.7--pyh7cba7a3_0"
 - "1.3.1--pyhdfd78af_0"
 - "1.2.9--pyhdfd78af_0"
 - "1.3.2--pyhdfd78af_0"
 - "1.3.3--pyhdfd78af_0"
 - "1.3.4--pyhdfd78af_0"
 - "1.3.5--pyhdfd78af_0"
description: "singularity registry hpc automated addition for psims"
config: {"url": "https://biocontainers.pro/tools/psims", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for psims", "latest": {"1.3.5--pyhdfd78af_0": "sha256:46f265682307eda926fabadba5ca51d24edb7cac2f97d0b495389f3e7bf83a4f"}, "tags": {"1.2.3--pyh7cba7a3_0": "sha256:55aa3ccf2998d9f5c0130878db5a583e2a15506453244120992b512b1dcb54cf", "1.2.5--pyh7cba7a3_0": "sha256:bd620d64d25183408150c1abc89c6241fc374b2d6b446b18f1e168fd18930e19", "1.2.6--pyh7cba7a3_0": "sha256:5f8133d20b7bbd99e7033d1add59bf8830fd029d8024b6db918195bbb1f35cc8", "1.2.7--pyh7cba7a3_0": "sha256:ccdfbcdbfdb04b4e0a7c06da9ecb7aeb589b5829603d80778effd3e973696db8", "1.3.1--pyhdfd78af_0": "sha256:5c3eb42146c13f593f988e72cf3cbac967654cb137d58732426ea52b8675440e", "1.2.9--pyhdfd78af_0": "sha256:a8bbc795e94e178a20882b267f34098f24894cc760d376bbd426e56bf61433ce", "1.3.2--pyhdfd78af_0": "sha256:8c0b737a5705c63f357230940620fbce42dc0d1b3579e2221fe3749b365e5df2", "1.3.3--pyhdfd78af_0": "sha256:cf344b73edc51bb9d1b4bac2ca973d3fa981a8f14e04e384763f074bd11a2b9a", "1.3.4--pyhdfd78af_0": "sha256:194051cf248d745ae1618c1cebb7336db8894611ddfd3f98764d9d4fd58771df", "1.3.5--pyhdfd78af_0": "sha256:46f265682307eda926fabadba5ca51d24edb7cac2f97d0b495389f3e7bf83a4f"}, "docker": "quay.io/biocontainers/psims", "aliases": {"f2py3.11": "/usr/local/bin/f2py3.11", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "xslt-config": "/usr/local/bin/xslt-config", "xsltproc": "/usr/local/bin/xsltproc", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/psims.
singularity registry hpc automated addition for psims
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/psims
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/psims:1.3.5--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/psims/1.3.5--pyhdfd78af_0
$ module help quay.io/biocontainers/psims/1.3.5--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### psims-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### psims-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### psims-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### psims-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### psims-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### psims-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### f2py3.11

```bash
$ singularity exec <container> /usr/local/bin/f2py3.11
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### xslt-config

```bash
$ singularity exec <container> /usr/local/bin/xslt-config
$ podman run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xsltproc

```bash
$ singularity exec <container> /usr/local/bin/xsltproc
$ podman run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
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