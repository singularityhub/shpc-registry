---
layout: container
name:  "quay.io/biocontainers/rectify-rna"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rectify-rna/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rectify-rna/container.yaml"
updated_at: "2026-06-23 06:55:03.715150"
latest: "2.7.8--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/rectify-rna"
aliases:
 - "jlpm"
 - "jupyter-events"
 - "jupyter-lab"
 - "jupyter-labextension"
 - "jupyter-labhub"
 - "rectify"
 - "debugpy-adapter"
 - "pyjson5"
 - "jupyter-server"
 - "debugpy"
 - "jupyter-console"
 - "zarr"
 - "jsonpointer"
 - "wsdump"
 - "send2trash"
 - "jupyter-dejavu"
 - "jupyter-execute"
 - "jupyter-notebook"
 - "h2benchmark"
 - "httpx"
 - "jupyter-nbconvert"
 - "pybabel"
 - "checksum-profile"
 - "jupyter-kernel"
 - "jupyter-kernelspec"
 - "jupyter-run"
 - "curve_keygen"
 - "ipython3"
 - "ipython"
 - "elasticurl"
 - "jupyter-trust"
versions:
 - "2.7.8--pyhdfd78af_0"
description: "singularity registry hpc automated addition for rectify-rna"
config: {"url": "https://biocontainers.pro/tools/rectify-rna", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for rectify-rna", "latest": {"2.7.8--pyhdfd78af_0": "sha256:ff240b1ea2f63eb180ec8c064ff39ae723c7a975a833f52b022abc335b30a7d5"}, "tags": {"2.7.8--pyhdfd78af_0": "sha256:ff240b1ea2f63eb180ec8c064ff39ae723c7a975a833f52b022abc335b30a7d5"}, "docker": "quay.io/biocontainers/rectify-rna", "aliases": {"jlpm": "/usr/local/bin/jlpm", "jupyter-events": "/usr/local/bin/jupyter-events", "jupyter-lab": "/usr/local/bin/jupyter-lab", "jupyter-labextension": "/usr/local/bin/jupyter-labextension", "jupyter-labhub": "/usr/local/bin/jupyter-labhub", "rectify": "/usr/local/bin/rectify", "debugpy-adapter": "/usr/local/bin/debugpy-adapter", "pyjson5": "/usr/local/bin/pyjson5", "jupyter-server": "/usr/local/bin/jupyter-server", "debugpy": "/usr/local/bin/debugpy", "jupyter-console": "/usr/local/bin/jupyter-console", "zarr": "/usr/local/bin/zarr", "jsonpointer": "/usr/local/bin/jsonpointer", "wsdump": "/usr/local/bin/wsdump", "send2trash": "/usr/local/bin/send2trash", "jupyter-dejavu": "/usr/local/bin/jupyter-dejavu", "jupyter-execute": "/usr/local/bin/jupyter-execute", "jupyter-notebook": "/usr/local/bin/jupyter-notebook", "h2benchmark": "/usr/local/bin/h2benchmark", "httpx": "/usr/local/bin/httpx", "jupyter-nbconvert": "/usr/local/bin/jupyter-nbconvert", "pybabel": "/usr/local/bin/pybabel", "checksum-profile": "/usr/local/bin/checksum-profile", "jupyter-kernel": "/usr/local/bin/jupyter-kernel", "jupyter-kernelspec": "/usr/local/bin/jupyter-kernelspec", "jupyter-run": "/usr/local/bin/jupyter-run", "curve_keygen": "/usr/local/bin/curve_keygen", "ipython3": "/usr/local/bin/ipython3", "ipython": "/usr/local/bin/ipython", "elasticurl": "/usr/local/bin/elasticurl", "jupyter-trust": "/usr/local/bin/jupyter-trust"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rectify-rna.
singularity registry hpc automated addition for rectify-rna
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rectify-rna
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rectify-rna:2.7.8--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rectify-rna/2.7.8--pyhdfd78af_0
$ module help quay.io/biocontainers/rectify-rna/2.7.8--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rectify-rna-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rectify-rna-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rectify-rna-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rectify-rna-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rectify-rna-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rectify-rna-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### rectify

```bash
$ singularity exec <container> /usr/local/bin/rectify
$ podman run --it --rm --entrypoint /usr/local/bin/rectify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rectify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debugpy-adapter

```bash
$ singularity exec <container> /usr/local/bin/debugpy-adapter
$ podman run --it --rm --entrypoint /usr/local/bin/debugpy-adapter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debugpy-adapter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyjson5

```bash
$ singularity exec <container> /usr/local/bin/pyjson5
$ podman run --it --rm --entrypoint /usr/local/bin/pyjson5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyjson5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-server

```bash
$ singularity exec <container> /usr/local/bin/jupyter-server
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-server   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### wsdump

```bash
$ singularity exec <container> /usr/local/bin/wsdump
$ podman run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### send2trash

```bash
$ singularity exec <container> /usr/local/bin/send2trash
$ podman run --it --rm --entrypoint /usr/local/bin/send2trash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/send2trash   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### h2benchmark

```bash
$ singularity exec <container> /usr/local/bin/h2benchmark
$ podman run --it --rm --entrypoint /usr/local/bin/h2benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h2benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### httpx

```bash
$ singularity exec <container> /usr/local/bin/httpx
$ podman run --it --rm --entrypoint /usr/local/bin/httpx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/httpx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-nbconvert

```bash
$ singularity exec <container> /usr/local/bin/jupyter-nbconvert
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-nbconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-nbconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybabel

```bash
$ singularity exec <container> /usr/local/bin/pybabel
$ podman run --it --rm --entrypoint /usr/local/bin/pybabel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybabel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checksum-profile

```bash
$ singularity exec <container> /usr/local/bin/checksum-profile
$ podman run --it --rm --entrypoint /usr/local/bin/checksum-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checksum-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-kernel

```bash
$ singularity exec <container> /usr/local/bin/jupyter-kernel
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-kernel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-kernel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-kernelspec

```bash
$ singularity exec <container> /usr/local/bin/jupyter-kernelspec
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-kernelspec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-kernelspec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-run

```bash
$ singularity exec <container> /usr/local/bin/jupyter-run
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-run   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-run   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### curve_keygen

```bash
$ singularity exec <container> /usr/local/bin/curve_keygen
$ podman run --it --rm --entrypoint /usr/local/bin/curve_keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/curve_keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### elasticurl

```bash
$ singularity exec <container> /usr/local/bin/elasticurl
$ podman run --it --rm --entrypoint /usr/local/bin/elasticurl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elasticurl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-trust

```bash
$ singularity exec <container> /usr/local/bin/jupyter-trust
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-trust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-trust   -v ${PWD} -w ${PWD} <container> -c " $@"
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