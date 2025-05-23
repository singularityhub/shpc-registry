---
layout: container
name:  "quay.io/biocontainers/kb-python"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kb-python/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kb-python/container.yaml"
updated_at: "2025-05-23 03:42:23.141963"
latest: "0.29.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/kb-python"
aliases:
 - "bustools"
 - "jupyter-dejavu"
 - "jupyter-execute"
 - "kallisto"
 - "kb"
 - "loompy"
 - "shortuuid"
 - "scanpy"
 - "jupyter-nbconvert"
 - "sphinx-apidoc"
 - "sphinx-autogen"
 - "sphinx-build"
 - "sphinx-quickstart"
 - "jupyter-kernel"
 - "jupyter-kernelspec"
 - "jupyter-run"
 - "pybabel"
versions:
 - "0.27.3--pyhdfd78af_0"
 - "0.27.3--pyhdfd78af_1"
 - "0.28.0--pyhdfd78af_0"
 - "0.28.1--pyhdfd78af_0"
 - "0.28.2--pyhdfd78af_0"
 - "0.28.2--pyhdfd78af_2"
 - "0.29.1--pyhdfd78af_0"
 - "0.29.3--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for kb-python"
config: {"url": "https://biocontainers.pro/tools/kb-python", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kb-python", "latest": {"0.29.3--pyhdfd78af_0": "sha256:9304597edb15fa4fe20ddb223e6cf448ead0e6373ca862d48c631050d0cc7bef"}, "tags": {"0.27.3--pyhdfd78af_0": "sha256:cdfb73adb53db24d183a03951c8ae2bfacaa37c1fe64bad57ebff4c0cf0c834a", "0.27.3--pyhdfd78af_1": "sha256:ec22f7e4d0cbb1f0e4856d7de62a8c82f106d2897c940c50f2394da1ea58af63", "0.28.0--pyhdfd78af_0": "sha256:4b8b9588b00f694342401daad1ba384cd04fd3ee5ac1413ab18c90652161b833", "0.28.1--pyhdfd78af_0": "sha256:bd2193b1a024ca1cc03af72a64fbffd874d7973b2972229c0174205bfc5c78d8", "0.28.2--pyhdfd78af_0": "sha256:eb9c7f93fe47ed2ce57cee452dc0e8bc4142aeba12cb376b29d0d7efaf4e4700", "0.28.2--pyhdfd78af_2": "sha256:4b5ff9a8f7387c9614d45aeccdd077c68a4de53a0e5aa97ab06e445e3b84eab7", "0.29.1--pyhdfd78af_0": "sha256:7bac25a30feb697a63fe525cb56716c7a3868789169259666d044082a4981492", "0.29.3--pyhdfd78af_0": "sha256:9304597edb15fa4fe20ddb223e6cf448ead0e6373ca862d48c631050d0cc7bef"}, "docker": "quay.io/biocontainers/kb-python", "aliases": {"bustools": "/usr/local/bin/bustools", "jupyter-dejavu": "/usr/local/bin/jupyter-dejavu", "jupyter-execute": "/usr/local/bin/jupyter-execute", "kallisto": "/usr/local/bin/kallisto", "kb": "/usr/local/bin/kb", "loompy": "/usr/local/bin/loompy", "shortuuid": "/usr/local/bin/shortuuid", "scanpy": "/usr/local/bin/scanpy", "jupyter-nbconvert": "/usr/local/bin/jupyter-nbconvert", "sphinx-apidoc": "/usr/local/bin/sphinx-apidoc", "sphinx-autogen": "/usr/local/bin/sphinx-autogen", "sphinx-build": "/usr/local/bin/sphinx-build", "sphinx-quickstart": "/usr/local/bin/sphinx-quickstart", "jupyter-kernel": "/usr/local/bin/jupyter-kernel", "jupyter-kernelspec": "/usr/local/bin/jupyter-kernelspec", "jupyter-run": "/usr/local/bin/jupyter-run", "pybabel": "/usr/local/bin/pybabel"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kb-python.
shpc-registry automated BioContainers addition for kb-python
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kb-python
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kb-python:0.29.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kb-python/0.29.3--pyhdfd78af_0
$ module help quay.io/biocontainers/kb-python/0.29.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kb-python-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kb-python-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kb-python-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kb-python-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kb-python-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kb-python-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bustools

```bash
$ singularity exec <container> /usr/local/bin/bustools
$ podman run --it --rm --entrypoint /usr/local/bin/bustools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bustools   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### kallisto

```bash
$ singularity exec <container> /usr/local/bin/kallisto
$ podman run --it --rm --entrypoint /usr/local/bin/kallisto   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kallisto   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kb

```bash
$ singularity exec <container> /usr/local/bin/kb
$ podman run --it --rm --entrypoint /usr/local/bin/kb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### loompy

```bash
$ singularity exec <container> /usr/local/bin/loompy
$ podman run --it --rm --entrypoint /usr/local/bin/loompy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/loompy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shortuuid

```bash
$ singularity exec <container> /usr/local/bin/shortuuid
$ podman run --it --rm --entrypoint /usr/local/bin/shortuuid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shortuuid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanpy

```bash
$ singularity exec <container> /usr/local/bin/scanpy
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-nbconvert

```bash
$ singularity exec <container> /usr/local/bin/jupyter-nbconvert
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-nbconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-nbconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-apidoc

```bash
$ singularity exec <container> /usr/local/bin/sphinx-apidoc
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-apidoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-apidoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-autogen

```bash
$ singularity exec <container> /usr/local/bin/sphinx-autogen
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-autogen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-autogen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-build

```bash
$ singularity exec <container> /usr/local/bin/sphinx-build
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-quickstart

```bash
$ singularity exec <container> /usr/local/bin/sphinx-quickstart
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-quickstart   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-quickstart   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### pybabel

```bash
$ singularity exec <container> /usr/local/bin/pybabel
$ podman run --it --rm --entrypoint /usr/local/bin/pybabel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybabel   -v ${PWD} -w ${PWD} <container> -c " $@"
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