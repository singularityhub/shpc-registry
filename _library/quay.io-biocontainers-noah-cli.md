---
layout: container
name:  "quay.io/biocontainers/noah-cli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/noah-cli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/noah-cli/container.yaml"
updated_at: "2025-12-10 04:00:07.668681"
latest: "0.2.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/noah-cli"
aliases:
 - "fab"
 - "inv"
 - "invoke"
 - "noah"
 - "pysradb"
 - "markdown-it"
 - "f2py3.11"
 - "pygmentize"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "xslt-config"
 - "xsltproc"
 - "tqdm"
 - "normalizer"
 - "python3.1"
versions:
 - "0.2.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for noah-cli"
config: {"url": "https://biocontainers.pro/tools/noah-cli", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for noah-cli", "latest": {"0.2.0--pyhdfd78af_0": "sha256:89a7dc784c9b3ef9b9d65b0fb26bceec3579ad4aa3c67bd56328dfc71c28e967"}, "tags": {"0.2.0--pyhdfd78af_0": "sha256:89a7dc784c9b3ef9b9d65b0fb26bceec3579ad4aa3c67bd56328dfc71c28e967"}, "docker": "quay.io/biocontainers/noah-cli", "aliases": {"fab": "/usr/local/bin/fab", "inv": "/usr/local/bin/inv", "invoke": "/usr/local/bin/invoke", "noah": "/usr/local/bin/noah", "pysradb": "/usr/local/bin/pysradb", "markdown-it": "/usr/local/bin/markdown-it", "f2py3.11": "/usr/local/bin/f2py3.11", "pygmentize": "/usr/local/bin/pygmentize", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "xslt-config": "/usr/local/bin/xslt-config", "xsltproc": "/usr/local/bin/xsltproc", "tqdm": "/usr/local/bin/tqdm", "normalizer": "/usr/local/bin/normalizer", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/noah-cli.
singularity registry hpc automated addition for noah-cli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/noah-cli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/noah-cli:0.2.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/noah-cli/0.2.0--pyhdfd78af_0
$ module help quay.io/biocontainers/noah-cli/0.2.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### noah-cli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### noah-cli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### noah-cli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### noah-cli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### noah-cli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### noah-cli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fab

```bash
$ singularity exec <container> /usr/local/bin/fab
$ podman run --it --rm --entrypoint /usr/local/bin/fab   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fab   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### inv

```bash
$ singularity exec <container> /usr/local/bin/inv
$ podman run --it --rm --entrypoint /usr/local/bin/inv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/inv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### invoke

```bash
$ singularity exec <container> /usr/local/bin/invoke
$ podman run --it --rm --entrypoint /usr/local/bin/invoke   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/invoke   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### noah

```bash
$ singularity exec <container> /usr/local/bin/noah
$ podman run --it --rm --entrypoint /usr/local/bin/noah   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/noah   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pysradb

```bash
$ singularity exec <container> /usr/local/bin/pysradb
$ podman run --it --rm --entrypoint /usr/local/bin/pysradb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pysradb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdown-it

```bash
$ singularity exec <container> /usr/local/bin/markdown-it
$ podman run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.11

```bash
$ singularity exec <container> /usr/local/bin/f2py3.11
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pygmentize

```bash
$ singularity exec <container> /usr/local/bin/pygmentize
$ podman run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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