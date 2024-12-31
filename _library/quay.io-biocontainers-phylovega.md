---
layout: container
name:  "quay.io/biocontainers/phylovega"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phylovega/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/phylovega/container.yaml"
updated_at: "2024-12-31 02:55:13.133842"
latest: "0.3--py_0"
container_url: "https://biocontainers.pro/tools/phylovega"
aliases:
 - "jupyter-console"
 - "jupyter-qtconsole"
 - "phylovega"
 - "jupyter-bundlerextension"
 - "jupyter-nbextension"
 - "jupyter-notebook"
 - "jupyter-serverextension"
 - "jupyter-nbconvert"
 - "jupyter-kernel"
 - "jupyter-kernelspec"
 - "jupyter-run"
 - "iptest3"
 - "sumlabels.py"
versions:
 - "0.3--py_0"
description: "shpc-registry automated BioContainers addition for phylovega"
config: {"url": "https://biocontainers.pro/tools/phylovega", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for phylovega", "latest": {"0.3--py_0": "sha256:196cb175e70816cc17bf7603de006eedd93384c46897b964b7bb7db70f216054"}, "tags": {"0.3--py_0": "sha256:196cb175e70816cc17bf7603de006eedd93384c46897b964b7bb7db70f216054"}, "docker": "quay.io/biocontainers/phylovega", "aliases": {"jupyter-console": "/usr/local/bin/jupyter-console", "jupyter-qtconsole": "/usr/local/bin/jupyter-qtconsole", "phylovega": "/usr/local/bin/phylovega", "jupyter-bundlerextension": "/usr/local/bin/jupyter-bundlerextension", "jupyter-nbextension": "/usr/local/bin/jupyter-nbextension", "jupyter-notebook": "/usr/local/bin/jupyter-notebook", "jupyter-serverextension": "/usr/local/bin/jupyter-serverextension", "jupyter-nbconvert": "/usr/local/bin/jupyter-nbconvert", "jupyter-kernel": "/usr/local/bin/jupyter-kernel", "jupyter-kernelspec": "/usr/local/bin/jupyter-kernelspec", "jupyter-run": "/usr/local/bin/jupyter-run", "iptest3": "/usr/local/bin/iptest3", "sumlabels.py": "/usr/local/bin/sumlabels.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/phylovega.
shpc-registry automated BioContainers addition for phylovega
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/phylovega
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/phylovega:0.3--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/phylovega/0.3--py_0
$ module help quay.io/biocontainers/phylovega/0.3--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### phylovega-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### phylovega-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### phylovega-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### phylovega-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### phylovega-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### phylovega-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### jupyter-console

```bash
$ singularity exec <container> /usr/local/bin/jupyter-console
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-console   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-console   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-qtconsole

```bash
$ singularity exec <container> /usr/local/bin/jupyter-qtconsole
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-qtconsole   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-qtconsole   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phylovega

```bash
$ singularity exec <container> /usr/local/bin/phylovega
$ podman run --it --rm --entrypoint /usr/local/bin/phylovega   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phylovega   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### jupyter-notebook

```bash
$ singularity exec <container> /usr/local/bin/jupyter-notebook
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-notebook   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-notebook   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-serverextension

```bash
$ singularity exec <container> /usr/local/bin/jupyter-serverextension
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-serverextension   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-serverextension   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-nbconvert

```bash
$ singularity exec <container> /usr/local/bin/jupyter-nbconvert
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-nbconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-nbconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### iptest3

```bash
$ singularity exec <container> /usr/local/bin/iptest3
$ podman run --it --rm --entrypoint /usr/local/bin/iptest3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iptest3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sumlabels.py

```bash
$ singularity exec <container> /usr/local/bin/sumlabels.py
$ podman run --it --rm --entrypoint /usr/local/bin/sumlabels.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumlabels.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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