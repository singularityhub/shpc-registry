---
layout: container
name:  "quay.io/biocontainers/vcfsim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vcfsim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vcfsim/container.yaml"
updated_at: "2025-04-05 03:35:51.664443"
latest: "1.0.16.alpha--pyhdc42f0e_0"
container_url: "https://biocontainers.pro/tools/vcfsim"
aliases:
 - "demes"
 - "msp"
 - "mspms"
 - "tskit"
 - "vcfsim"
 - "ipython3"
 - "ipython"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
 - "jsonschema"
 - "pygmentize"
versions:
 - "1.0.8.alpha--pyhca03a8a_0"
 - "1.0.9.alpha--pyhca03a8a_0"
 - "1.0.10.alpha--pyhca03a8a_0"
 - "1.0.11.alpha--pyhca03a8a_0"
 - "1.0.12.alpha--pyhdc42f0e_0"
 - "1.0.13.alpha--pyhdc42f0e_0"
 - "1.0.16.alpha--pyhdc42f0e_0"
description: "singularity registry hpc automated addition for vcfsim"
config: {"url": "https://biocontainers.pro/tools/vcfsim", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for vcfsim", "latest": {"1.0.16.alpha--pyhdc42f0e_0": "sha256:aa799c31189e85102d94438a0e5b0e4bccf6c20efae71895331681213da4635c"}, "tags": {"1.0.8.alpha--pyhca03a8a_0": "sha256:4d690c5dd2fc88c5ce2a5279e6a431e0dd66be96a0fb12f20a0a310c7c79ea1e", "1.0.9.alpha--pyhca03a8a_0": "sha256:69b9c77a2067f6b0a5a1a3412132715f45946eba24834b1cb31b66edf9dc24c8", "1.0.10.alpha--pyhca03a8a_0": "sha256:a85195e80c1b48fbd677796a1673dc48e2253a80e119476ad5fbbbbae1afaf6e", "1.0.11.alpha--pyhca03a8a_0": "sha256:84c82dcfe282f5677e8dcd2d10f048d4acb2e95557fc0d4799e47a92828ed068", "1.0.12.alpha--pyhdc42f0e_0": "sha256:ddd4cc17c6f53547bcb7caa29980d400d224f4186e8367b566c2e3275cfe5ff3", "1.0.13.alpha--pyhdc42f0e_0": "sha256:2137a8330eda69709f0a211f7397618d884c48ed57e2988adcbc7c6f10b34f27", "1.0.16.alpha--pyhdc42f0e_0": "sha256:aa799c31189e85102d94438a0e5b0e4bccf6c20efae71895331681213da4635c"}, "docker": "quay.io/biocontainers/vcfsim", "aliases": {"demes": "/usr/local/bin/demes", "msp": "/usr/local/bin/msp", "mspms": "/usr/local/bin/mspms", "tskit": "/usr/local/bin/tskit", "vcfsim": "/usr/local/bin/vcfsim", "ipython3": "/usr/local/bin/ipython3", "ipython": "/usr/local/bin/ipython", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config", "jsonschema": "/usr/local/bin/jsonschema", "pygmentize": "/usr/local/bin/pygmentize"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vcfsim.
singularity registry hpc automated addition for vcfsim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vcfsim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vcfsim:1.0.16.alpha--pyhdc42f0e_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vcfsim/1.0.16.alpha--pyhdc42f0e_0
$ module help quay.io/biocontainers/vcfsim/1.0.16.alpha--pyhdc42f0e_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vcfsim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vcfsim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vcfsim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vcfsim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vcfsim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vcfsim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### demes

```bash
$ singularity exec <container> /usr/local/bin/demes
$ podman run --it --rm --entrypoint /usr/local/bin/demes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/demes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### msp

```bash
$ singularity exec <container> /usr/local/bin/msp
$ podman run --it --rm --entrypoint /usr/local/bin/msp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/msp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mspms

```bash
$ singularity exec <container> /usr/local/bin/mspms
$ podman run --it --rm --entrypoint /usr/local/bin/mspms   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mspms   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tskit

```bash
$ singularity exec <container> /usr/local/bin/tskit
$ podman run --it --rm --entrypoint /usr/local/bin/tskit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tskit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfsim

```bash
$ singularity exec <container> /usr/local/bin/vcfsim
$ podman run --it --rm --entrypoint /usr/local/bin/vcfsim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfsim   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### 2to3-3.12

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.12
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.12

```bash
$ singularity exec <container> /usr/local/bin/idle3.12
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.12

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.12
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12

```bash
$ singularity exec <container> /usr/local/bin/python3.12
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12-config

```bash
$ singularity exec <container> /usr/local/bin/python3.12-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonschema

```bash
$ singularity exec <container> /usr/local/bin/jsonschema
$ podman run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pygmentize

```bash
$ singularity exec <container> /usr/local/bin/pygmentize
$ podman run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
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