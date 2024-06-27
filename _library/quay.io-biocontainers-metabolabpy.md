---
layout: container
name:  "quay.io/biocontainers/metabolabpy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metabolabpy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metabolabpy/container.yaml"
updated_at: "2024-06-27 02:56:17.605063"
latest: "0.6.53--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/metabolabpy"
aliases:
 - "metabolabpy"
 - "pyside2-lupdate"
 - "pyside2-rcc"
 - "pyside2-uic"
 - "pyside_tool.py"
 - "shiboken2"
 - "shiboken_tool.py"
 - "vba_extract.py"
 - "xkbcli"
 - "pg_config"
 - "qdistancefieldgenerator"
 - "qmlpreview"
 - "qvkgen"
 - "certutil"
 - "nspr-config"
 - "nss-config"
 - "pk12util"
versions:
 - "0.6.53--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for metabolabpy"
config: {"url": "https://biocontainers.pro/tools/metabolabpy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metabolabpy", "latest": {"0.6.53--pyhdfd78af_0": "sha256:6b212bdc302726f737019f386d0ddef9a3e22c0d35292e64d24d41eda1b09e55"}, "tags": {"0.6.53--pyhdfd78af_0": "sha256:6b212bdc302726f737019f386d0ddef9a3e22c0d35292e64d24d41eda1b09e55"}, "docker": "quay.io/biocontainers/metabolabpy", "aliases": {"metabolabpy": "/usr/local/bin/metabolabpy", "pyside2-lupdate": "/usr/local/bin/pyside2-lupdate", "pyside2-rcc": "/usr/local/bin/pyside2-rcc", "pyside2-uic": "/usr/local/bin/pyside2-uic", "pyside_tool.py": "/usr/local/bin/pyside_tool.py", "shiboken2": "/usr/local/bin/shiboken2", "shiboken_tool.py": "/usr/local/bin/shiboken_tool.py", "vba_extract.py": "/usr/local/bin/vba_extract.py", "xkbcli": "/usr/local/bin/xkbcli", "pg_config": "/usr/local/bin/pg_config", "qdistancefieldgenerator": "/usr/local/bin/qdistancefieldgenerator", "qmlpreview": "/usr/local/bin/qmlpreview", "qvkgen": "/usr/local/bin/qvkgen", "certutil": "/usr/local/bin/certutil", "nspr-config": "/usr/local/bin/nspr-config", "nss-config": "/usr/local/bin/nss-config", "pk12util": "/usr/local/bin/pk12util"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metabolabpy.
shpc-registry automated BioContainers addition for metabolabpy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metabolabpy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metabolabpy:0.6.53--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metabolabpy/0.6.53--pyhdfd78af_0
$ module help quay.io/biocontainers/metabolabpy/0.6.53--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metabolabpy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metabolabpy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metabolabpy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metabolabpy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metabolabpy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metabolabpy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### metabolabpy

```bash
$ singularity exec <container> /usr/local/bin/metabolabpy
$ podman run --it --rm --entrypoint /usr/local/bin/metabolabpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metabolabpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyside2-lupdate

```bash
$ singularity exec <container> /usr/local/bin/pyside2-lupdate
$ podman run --it --rm --entrypoint /usr/local/bin/pyside2-lupdate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyside2-lupdate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyside2-rcc

```bash
$ singularity exec <container> /usr/local/bin/pyside2-rcc
$ podman run --it --rm --entrypoint /usr/local/bin/pyside2-rcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyside2-rcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyside2-uic

```bash
$ singularity exec <container> /usr/local/bin/pyside2-uic
$ podman run --it --rm --entrypoint /usr/local/bin/pyside2-uic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyside2-uic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyside_tool.py

```bash
$ singularity exec <container> /usr/local/bin/pyside_tool.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyside_tool.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyside_tool.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiboken2

```bash
$ singularity exec <container> /usr/local/bin/shiboken2
$ podman run --it --rm --entrypoint /usr/local/bin/shiboken2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiboken2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiboken_tool.py

```bash
$ singularity exec <container> /usr/local/bin/shiboken_tool.py
$ podman run --it --rm --entrypoint /usr/local/bin/shiboken_tool.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiboken_tool.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vba_extract.py

```bash
$ singularity exec <container> /usr/local/bin/vba_extract.py
$ podman run --it --rm --entrypoint /usr/local/bin/vba_extract.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vba_extract.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xkbcli

```bash
$ singularity exec <container> /usr/local/bin/xkbcli
$ podman run --it --rm --entrypoint /usr/local/bin/xkbcli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xkbcli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_config

```bash
$ singularity exec <container> /usr/local/bin/pg_config
$ podman run --it --rm --entrypoint /usr/local/bin/pg_config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdistancefieldgenerator

```bash
$ singularity exec <container> /usr/local/bin/qdistancefieldgenerator
$ podman run --it --rm --entrypoint /usr/local/bin/qdistancefieldgenerator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdistancefieldgenerator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qmlpreview

```bash
$ singularity exec <container> /usr/local/bin/qmlpreview
$ podman run --it --rm --entrypoint /usr/local/bin/qmlpreview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qmlpreview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qvkgen

```bash
$ singularity exec <container> /usr/local/bin/qvkgen
$ podman run --it --rm --entrypoint /usr/local/bin/qvkgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qvkgen   -v ${PWD} -w ${PWD} <container> -c " $@"
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