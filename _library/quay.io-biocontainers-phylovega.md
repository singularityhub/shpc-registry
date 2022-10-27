---
layout: container
name:  "quay.io/biocontainers/phylovega"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phylovega/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/phylovega/container.yaml"
updated_at: "2022-10-27 00:53:55.333912"
latest: "0.3--py_0"
container_url: "https://biocontainers.pro/tools/phylovega"
aliases:
 - ".vega-post-link.sh"
 - ".vega-pre-unlink.sh"
 - "jupyter-console"
 - "phylovega"
versions:
 - "0.3--py_0"
description: "shpc-registry automated BioContainers addition for phylovega"
config: {"url": "https://biocontainers.pro/tools/phylovega", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for phylovega", "latest": {"0.3--py_0": "sha256:5ce2084fc3dfcfff0d51961bdfe41d0295b7af57926834080bb8f3156105d7d8"}, "tags": {"0.3--py_0": "sha256:5ce2084fc3dfcfff0d51961bdfe41d0295b7af57926834080bb8f3156105d7d8"}, "docker": "quay.io/biocontainers/phylovega", "aliases": {".vega-post-link.sh": "/usr/local/bin/.vega-post-link.sh", ".vega-pre-unlink.sh": "/usr/local/bin/.vega-pre-unlink.sh", "jupyter-console": "/usr/local/bin/jupyter-console", "phylovega": "/usr/local/bin/phylovega"}}
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


#### .vega-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.vega-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.vega-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.vega-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .vega-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.vega-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.vega-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.vega-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-console

```bash
$ singularity exec <container> /usr/local/bin/jupyter-console
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-console   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-console   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phylovega

```bash
$ singularity exec <container> /usr/local/bin/phylovega
$ podman run --it --rm --entrypoint /usr/local/bin/phylovega   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phylovega   -v ${PWD} -w ${PWD} <container> -c " $@"
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