---
layout: container
name:  "quay.io/biocontainers/clawbio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/clawbio/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/clawbio/container.yaml"
updated_at: "2026-06-24 06:10:56.582853"
latest: "0.5.2--pyh106432d_0"
container_url: "https://biocontainers.pro/tools/clawbio"
aliases:
 - "clawbio"
 - "conda-lock"
 - "dul-receive-pack"
 - "dul-upload-pack"
 - "dulwich"
 - "ensureconda"
 - "pyproject-build"
 - "pysemver"
 - "python-build"
 - "rocrate"
 - "trove-classifiers"
 - "jlpm"
 - "jupyter-events"
 - "jupyter-lab"
 - "jupyter-labextension"
 - "jupyter-labhub"
 - "session-info2"
 - "pkginfo"
 - "pyjson5"
 - "debugpy-adapter"
 - "jupyter-server"
 - "session-info"
 - "distro"
 - "debugpy"
 - "jupyter-console"
 - "keyring"
 - "virtualenv"
 - "idna"
 - "zarr"
 - "jsonpointer"
 - "send2trash"
 - "wsdump"
 - "jupyter-dejavu"
 - "jupyter-execute"
 - "jupyter-notebook"
 - "doesitcache"
versions:
 - "0.5.2--pyh106432d_0"
description: "singularity registry hpc automated addition for clawbio"
config: {"url": "https://biocontainers.pro/tools/clawbio", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for clawbio", "latest": {"0.5.2--pyh106432d_0": "sha256:2c09c6d88e664c7762f5cb31e0824cea0aeb4e0ea2810277dabb6f4b71a5d9fe"}, "tags": {"0.5.2--pyh106432d_0": "sha256:2c09c6d88e664c7762f5cb31e0824cea0aeb4e0ea2810277dabb6f4b71a5d9fe"}, "docker": "quay.io/biocontainers/clawbio", "aliases": {"clawbio": "/usr/local/bin/clawbio", "conda-lock": "/usr/local/bin/conda-lock", "dul-receive-pack": "/usr/local/bin/dul-receive-pack", "dul-upload-pack": "/usr/local/bin/dul-upload-pack", "dulwich": "/usr/local/bin/dulwich", "ensureconda": "/usr/local/bin/ensureconda", "pyproject-build": "/usr/local/bin/pyproject-build", "pysemver": "/usr/local/bin/pysemver", "python-build": "/usr/local/bin/python-build", "rocrate": "/usr/local/bin/rocrate", "trove-classifiers": "/usr/local/bin/trove-classifiers", "jlpm": "/usr/local/bin/jlpm", "jupyter-events": "/usr/local/bin/jupyter-events", "jupyter-lab": "/usr/local/bin/jupyter-lab", "jupyter-labextension": "/usr/local/bin/jupyter-labextension", "jupyter-labhub": "/usr/local/bin/jupyter-labhub", "session-info2": "/usr/local/bin/session-info2", "pkginfo": "/usr/local/bin/pkginfo", "pyjson5": "/usr/local/bin/pyjson5", "debugpy-adapter": "/usr/local/bin/debugpy-adapter", "jupyter-server": "/usr/local/bin/jupyter-server", "session-info": "/usr/local/bin/session-info", "distro": "/usr/local/bin/distro", "debugpy": "/usr/local/bin/debugpy", "jupyter-console": "/usr/local/bin/jupyter-console", "keyring": "/usr/local/bin/keyring", "virtualenv": "/usr/local/bin/virtualenv", "idna": "/usr/local/bin/idna", "zarr": "/usr/local/bin/zarr", "jsonpointer": "/usr/local/bin/jsonpointer", "send2trash": "/usr/local/bin/send2trash", "wsdump": "/usr/local/bin/wsdump", "jupyter-dejavu": "/usr/local/bin/jupyter-dejavu", "jupyter-execute": "/usr/local/bin/jupyter-execute", "jupyter-notebook": "/usr/local/bin/jupyter-notebook", "doesitcache": "/usr/local/bin/doesitcache"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/clawbio.
singularity registry hpc automated addition for clawbio
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/clawbio
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/clawbio:0.5.2--pyh106432d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/clawbio/0.5.2--pyh106432d_0
$ module help quay.io/biocontainers/clawbio/0.5.2--pyh106432d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### clawbio-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### clawbio-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### clawbio-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### clawbio-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### clawbio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### clawbio-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### clawbio

```bash
$ singularity exec <container> /usr/local/bin/clawbio
$ podman run --it --rm --entrypoint /usr/local/bin/clawbio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clawbio   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda-lock

```bash
$ singularity exec <container> /usr/local/bin/conda-lock
$ podman run --it --rm --entrypoint /usr/local/bin/conda-lock   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda-lock   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dul-receive-pack

```bash
$ singularity exec <container> /usr/local/bin/dul-receive-pack
$ podman run --it --rm --entrypoint /usr/local/bin/dul-receive-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dul-receive-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dul-upload-pack

```bash
$ singularity exec <container> /usr/local/bin/dul-upload-pack
$ podman run --it --rm --entrypoint /usr/local/bin/dul-upload-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dul-upload-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dulwich

```bash
$ singularity exec <container> /usr/local/bin/dulwich
$ podman run --it --rm --entrypoint /usr/local/bin/dulwich   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dulwich   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ensureconda

```bash
$ singularity exec <container> /usr/local/bin/ensureconda
$ podman run --it --rm --entrypoint /usr/local/bin/ensureconda   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ensureconda   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyproject-build

```bash
$ singularity exec <container> /usr/local/bin/pyproject-build
$ podman run --it --rm --entrypoint /usr/local/bin/pyproject-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyproject-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pysemver

```bash
$ singularity exec <container> /usr/local/bin/pysemver
$ podman run --it --rm --entrypoint /usr/local/bin/pysemver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pysemver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-build

```bash
$ singularity exec <container> /usr/local/bin/python-build
$ podman run --it --rm --entrypoint /usr/local/bin/python-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rocrate

```bash
$ singularity exec <container> /usr/local/bin/rocrate
$ podman run --it --rm --entrypoint /usr/local/bin/rocrate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rocrate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trove-classifiers

```bash
$ singularity exec <container> /usr/local/bin/trove-classifiers
$ podman run --it --rm --entrypoint /usr/local/bin/trove-classifiers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trove-classifiers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jlpm

```bash
$ singularity exec <container> /usr/local/bin/jlpm
$ podman run --it --rm --entrypoint /usr/local/bin/jlpm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jlpm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-events

```bash
$ singularity exec <container> /usr/local/bin/jupyter-events
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-events   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-events   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-lab

```bash
$ singularity exec <container> /usr/local/bin/jupyter-lab
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-lab   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-lab   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-labextension

```bash
$ singularity exec <container> /usr/local/bin/jupyter-labextension
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-labextension   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-labextension   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-labhub

```bash
$ singularity exec <container> /usr/local/bin/jupyter-labhub
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-labhub   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-labhub   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### session-info2

```bash
$ singularity exec <container> /usr/local/bin/session-info2
$ podman run --it --rm --entrypoint /usr/local/bin/session-info2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/session-info2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pkginfo

```bash
$ singularity exec <container> /usr/local/bin/pkginfo
$ podman run --it --rm --entrypoint /usr/local/bin/pkginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pkginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyjson5

```bash
$ singularity exec <container> /usr/local/bin/pyjson5
$ podman run --it --rm --entrypoint /usr/local/bin/pyjson5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyjson5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debugpy-adapter

```bash
$ singularity exec <container> /usr/local/bin/debugpy-adapter
$ podman run --it --rm --entrypoint /usr/local/bin/debugpy-adapter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debugpy-adapter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-server

```bash
$ singularity exec <container> /usr/local/bin/jupyter-server
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### session-info

```bash
$ singularity exec <container> /usr/local/bin/session-info
$ podman run --it --rm --entrypoint /usr/local/bin/session-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/session-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### distro

```bash
$ singularity exec <container> /usr/local/bin/distro
$ podman run --it --rm --entrypoint /usr/local/bin/distro   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/distro   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debugpy

```bash
$ singularity exec <container> /usr/local/bin/debugpy
$ podman run --it --rm --entrypoint /usr/local/bin/debugpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debugpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-console

```bash
$ singularity exec <container> /usr/local/bin/jupyter-console
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-console   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-console   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### keyring

```bash
$ singularity exec <container> /usr/local/bin/keyring
$ podman run --it --rm --entrypoint /usr/local/bin/keyring   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/keyring   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### virtualenv

```bash
$ singularity exec <container> /usr/local/bin/virtualenv
$ podman run --it --rm --entrypoint /usr/local/bin/virtualenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/virtualenv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idna

```bash
$ singularity exec <container> /usr/local/bin/idna
$ podman run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zarr

```bash
$ singularity exec <container> /usr/local/bin/zarr
$ podman run --it --rm --entrypoint /usr/local/bin/zarr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zarr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonpointer

```bash
$ singularity exec <container> /usr/local/bin/jsonpointer
$ podman run --it --rm --entrypoint /usr/local/bin/jsonpointer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonpointer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### send2trash

```bash
$ singularity exec <container> /usr/local/bin/send2trash
$ podman run --it --rm --entrypoint /usr/local/bin/send2trash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/send2trash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wsdump

```bash
$ singularity exec <container> /usr/local/bin/wsdump
$ podman run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-dejavu

```bash
$ singularity exec <container> /usr/local/bin/jupyter-dejavu
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-dejavu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-dejavu   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-execute

```bash
$ singularity exec <container> /usr/local/bin/jupyter-execute
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-execute   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-execute   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-notebook

```bash
$ singularity exec <container> /usr/local/bin/jupyter-notebook
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-notebook   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-notebook   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### doesitcache

```bash
$ singularity exec <container> /usr/local/bin/doesitcache
$ podman run --it --rm --entrypoint /usr/local/bin/doesitcache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/doesitcache   -v ${PWD} -w ${PWD} <container> -c " $@"
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