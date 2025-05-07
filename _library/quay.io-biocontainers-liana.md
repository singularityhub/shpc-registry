---
layout: container
name:  "quay.io/biocontainers/liana"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/liana/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/liana/container.yaml"
updated_at: "2025-05-07 03:29:24.747894"
latest: "1.5.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/liana"
aliases:
 - "debugpy"
 - "gseapy"
 - "hypothesis"
 - "identify-cli"
 - "jlpm"
 - "jupyter-events"
 - "jupyter-lab"
 - "jupyter-labextension"
 - "jupyter-labhub"
 - "jupyter-nbclassic"
 - "jupyter-nbclassic-bundlerextension"
 - "jupyter-nbclassic-extension"
 - "jupyter-nbclassic-serverextension"
 - "jupyter-server"
 - "nodeenv"
 - "osqp_demo"
 - "osqp_tester"
 - "pre-commit"
 - "pyjson5"
 - "virtualenv"
 - "jsonpointer"
 - "jupyter-console"
 - "wsdump"
 - "runxlrd.py"
 - "send2trash"
 - "httpx"
 - "jupyter-dejavu"
 - "jupyter-execute"
 - "jupyter-bundlerextension"
 - "jupyter-nbextension"
 - "jupyter-serverextension"
 - "jupyter-notebook"
 - "jupyter-nbconvert"
 - "pybabel"
 - "jupyter-kernel"
 - "jupyter-kernelspec"
 - "jupyter-run"
 - "h5tools_test_utils"
 - "scanpy"
 - "curve_keygen"
 - "h5fuse.sh"
 - "hwloc-gather-cpuid"
 - "hwloc-annotate"
 - "hwloc-bind"
 - "hwloc-calc"
versions:
 - "1.4.0--pyhdfd78af_0"
 - "1.4.0--pyhdfd78af_1"
 - "1.5.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for liana"
config: {"url": "https://biocontainers.pro/tools/liana", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for liana", "latest": {"1.5.1--pyhdfd78af_0": "sha256:6a02ebf1f4de8afac7b13ef4fd7424f66082c335c23aa2dc105b8eb8b32399cc"}, "tags": {"1.4.0--pyhdfd78af_0": "sha256:e1a4c873070e4320384a2649fb9c267cf7d5c3fe1c0e846ec8acf984fedc6a89", "1.4.0--pyhdfd78af_1": "sha256:1f360edcc260a713f9c67f5806147bd1c3b5ecddd82aa09bf39a2dbcbc50d4e1", "1.5.1--pyhdfd78af_0": "sha256:6a02ebf1f4de8afac7b13ef4fd7424f66082c335c23aa2dc105b8eb8b32399cc"}, "docker": "quay.io/biocontainers/liana", "aliases": {"debugpy": "/usr/local/bin/debugpy", "gseapy": "/usr/local/bin/gseapy", "hypothesis": "/usr/local/bin/hypothesis", "identify-cli": "/usr/local/bin/identify-cli", "jlpm": "/usr/local/bin/jlpm", "jupyter-events": "/usr/local/bin/jupyter-events", "jupyter-lab": "/usr/local/bin/jupyter-lab", "jupyter-labextension": "/usr/local/bin/jupyter-labextension", "jupyter-labhub": "/usr/local/bin/jupyter-labhub", "jupyter-nbclassic": "/usr/local/bin/jupyter-nbclassic", "jupyter-nbclassic-bundlerextension": "/usr/local/bin/jupyter-nbclassic-bundlerextension", "jupyter-nbclassic-extension": "/usr/local/bin/jupyter-nbclassic-extension", "jupyter-nbclassic-serverextension": "/usr/local/bin/jupyter-nbclassic-serverextension", "jupyter-server": "/usr/local/bin/jupyter-server", "nodeenv": "/usr/local/bin/nodeenv", "osqp_demo": "/usr/local/bin/osqp_demo", "osqp_tester": "/usr/local/bin/osqp_tester", "pre-commit": "/usr/local/bin/pre-commit", "pyjson5": "/usr/local/bin/pyjson5", "virtualenv": "/usr/local/bin/virtualenv", "jsonpointer": "/usr/local/bin/jsonpointer", "jupyter-console": "/usr/local/bin/jupyter-console", "wsdump": "/usr/local/bin/wsdump", "runxlrd.py": "/usr/local/bin/runxlrd.py", "send2trash": "/usr/local/bin/send2trash", "httpx": "/usr/local/bin/httpx", "jupyter-dejavu": "/usr/local/bin/jupyter-dejavu", "jupyter-execute": "/usr/local/bin/jupyter-execute", "jupyter-bundlerextension": "/usr/local/bin/jupyter-bundlerextension", "jupyter-nbextension": "/usr/local/bin/jupyter-nbextension", "jupyter-serverextension": "/usr/local/bin/jupyter-serverextension", "jupyter-notebook": "/usr/local/bin/jupyter-notebook", "jupyter-nbconvert": "/usr/local/bin/jupyter-nbconvert", "pybabel": "/usr/local/bin/pybabel", "jupyter-kernel": "/usr/local/bin/jupyter-kernel", "jupyter-kernelspec": "/usr/local/bin/jupyter-kernelspec", "jupyter-run": "/usr/local/bin/jupyter-run", "h5tools_test_utils": "/usr/local/bin/h5tools_test_utils", "scanpy": "/usr/local/bin/scanpy", "curve_keygen": "/usr/local/bin/curve_keygen", "h5fuse.sh": "/usr/local/bin/h5fuse.sh", "hwloc-gather-cpuid": "/usr/local/bin/hwloc-gather-cpuid", "hwloc-annotate": "/usr/local/bin/hwloc-annotate", "hwloc-bind": "/usr/local/bin/hwloc-bind", "hwloc-calc": "/usr/local/bin/hwloc-calc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/liana.
singularity registry hpc automated addition for liana
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/liana
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/liana:1.5.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/liana/1.5.1--pyhdfd78af_0
$ module help quay.io/biocontainers/liana/1.5.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### liana-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### liana-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### liana-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### liana-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### liana-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### liana-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### debugpy

```bash
$ singularity exec <container> /usr/local/bin/debugpy
$ podman run --it --rm --entrypoint /usr/local/bin/debugpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debugpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gseapy

```bash
$ singularity exec <container> /usr/local/bin/gseapy
$ podman run --it --rm --entrypoint /usr/local/bin/gseapy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gseapy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hypothesis

```bash
$ singularity exec <container> /usr/local/bin/hypothesis
$ podman run --it --rm --entrypoint /usr/local/bin/hypothesis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hypothesis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### identify-cli

```bash
$ singularity exec <container> /usr/local/bin/identify-cli
$ podman run --it --rm --entrypoint /usr/local/bin/identify-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/identify-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### jupyter-nbclassic

```bash
$ singularity exec <container> /usr/local/bin/jupyter-nbclassic
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-nbclassic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-nbclassic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-nbclassic-bundlerextension

```bash
$ singularity exec <container> /usr/local/bin/jupyter-nbclassic-bundlerextension
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-nbclassic-bundlerextension   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-nbclassic-bundlerextension   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-nbclassic-extension

```bash
$ singularity exec <container> /usr/local/bin/jupyter-nbclassic-extension
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-nbclassic-extension   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-nbclassic-extension   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-nbclassic-serverextension

```bash
$ singularity exec <container> /usr/local/bin/jupyter-nbclassic-serverextension
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-nbclassic-serverextension   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-nbclassic-serverextension   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-server

```bash
$ singularity exec <container> /usr/local/bin/jupyter-server
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nodeenv

```bash
$ singularity exec <container> /usr/local/bin/nodeenv
$ podman run --it --rm --entrypoint /usr/local/bin/nodeenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nodeenv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### osqp_demo

```bash
$ singularity exec <container> /usr/local/bin/osqp_demo
$ podman run --it --rm --entrypoint /usr/local/bin/osqp_demo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/osqp_demo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### osqp_tester

```bash
$ singularity exec <container> /usr/local/bin/osqp_tester
$ podman run --it --rm --entrypoint /usr/local/bin/osqp_tester   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/osqp_tester   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pre-commit

```bash
$ singularity exec <container> /usr/local/bin/pre-commit
$ podman run --it --rm --entrypoint /usr/local/bin/pre-commit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pre-commit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyjson5

```bash
$ singularity exec <container> /usr/local/bin/pyjson5
$ podman run --it --rm --entrypoint /usr/local/bin/pyjson5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyjson5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### virtualenv

```bash
$ singularity exec <container> /usr/local/bin/virtualenv
$ podman run --it --rm --entrypoint /usr/local/bin/virtualenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/virtualenv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonpointer

```bash
$ singularity exec <container> /usr/local/bin/jsonpointer
$ podman run --it --rm --entrypoint /usr/local/bin/jsonpointer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonpointer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-console

```bash
$ singularity exec <container> /usr/local/bin/jupyter-console
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-console   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-console   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wsdump

```bash
$ singularity exec <container> /usr/local/bin/wsdump
$ podman run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runxlrd.py

```bash
$ singularity exec <container> /usr/local/bin/runxlrd.py
$ podman run --it --rm --entrypoint /usr/local/bin/runxlrd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runxlrd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### send2trash

```bash
$ singularity exec <container> /usr/local/bin/send2trash
$ podman run --it --rm --entrypoint /usr/local/bin/send2trash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/send2trash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### httpx

```bash
$ singularity exec <container> /usr/local/bin/httpx
$ podman run --it --rm --entrypoint /usr/local/bin/httpx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/httpx   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### jupyter-bundlerextension

```bash
$ singularity exec <container> /usr/local/bin/jupyter-bundlerextension
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-bundlerextension   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-bundlerextension   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-nbextension

```bash
$ singularity exec <container> /usr/local/bin/jupyter-nbextension
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-nbextension   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-nbextension   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-serverextension

```bash
$ singularity exec <container> /usr/local/bin/jupyter-serverextension
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-serverextension   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-serverextension   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-notebook

```bash
$ singularity exec <container> /usr/local/bin/jupyter-notebook
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-notebook   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-notebook   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### h5tools_test_utils

```bash
$ singularity exec <container> /usr/local/bin/h5tools_test_utils
$ podman run --it --rm --entrypoint /usr/local/bin/h5tools_test_utils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5tools_test_utils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanpy

```bash
$ singularity exec <container> /usr/local/bin/scanpy
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### curve_keygen

```bash
$ singularity exec <container> /usr/local/bin/curve_keygen
$ podman run --it --rm --entrypoint /usr/local/bin/curve_keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/curve_keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5fuse.sh

```bash
$ singularity exec <container> /usr/local/bin/h5fuse.sh
$ podman run --it --rm --entrypoint /usr/local/bin/h5fuse.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5fuse.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-gather-cpuid

```bash
$ singularity exec <container> /usr/local/bin/hwloc-gather-cpuid
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-gather-cpuid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-gather-cpuid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-annotate

```bash
$ singularity exec <container> /usr/local/bin/hwloc-annotate
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-bind

```bash
$ singularity exec <container> /usr/local/bin/hwloc-bind
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-bind   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-bind   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-calc

```bash
$ singularity exec <container> /usr/local/bin/hwloc-calc
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-calc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-calc   -v ${PWD} -w ${PWD} <container> -c " $@"
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