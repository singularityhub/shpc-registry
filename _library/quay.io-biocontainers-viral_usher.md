---
layout: container
name:  "quay.io/biocontainers/viral_usher"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/viral_usher/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/viral_usher/container.yaml"
updated_at: "2026-03-23 05:16:26.552467"
latest: "0.10.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/viral_usher"
aliases:
 - "inv"
 - "invoke"
 - "viral_usher"
 - "viral_usher_build"
 - "wsdump"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
 - "numpy-config"
 - "normalizer"
versions:
 - "0.10.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for viral_usher"
config: {"url": "https://biocontainers.pro/tools/viral_usher", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for viral_usher", "latest": {"0.10.1--pyhdfd78af_0": "sha256:ea9a11e014f969b424b51c08adbb02305875f76d9575f3aac18908535a0b5586"}, "tags": {"0.10.1--pyhdfd78af_0": "sha256:ea9a11e014f969b424b51c08adbb02305875f76d9575f3aac18908535a0b5586"}, "docker": "quay.io/biocontainers/viral_usher", "aliases": {"inv": "/usr/local/bin/inv", "invoke": "/usr/local/bin/invoke", "viral_usher": "/usr/local/bin/viral_usher", "viral_usher_build": "/usr/local/bin/viral_usher_build", "wsdump": "/usr/local/bin/wsdump", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config", "numpy-config": "/usr/local/bin/numpy-config", "normalizer": "/usr/local/bin/normalizer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/viral_usher.
singularity registry hpc automated addition for viral_usher
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/viral_usher
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/viral_usher:0.10.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/viral_usher/0.10.1--pyhdfd78af_0
$ module help quay.io/biocontainers/viral_usher/0.10.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### viral_usher-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### viral_usher-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### viral_usher-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### viral_usher-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### viral_usher-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### viral_usher-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### viral_usher

```bash
$ singularity exec <container> /usr/local/bin/viral_usher
$ podman run --it --rm --entrypoint /usr/local/bin/viral_usher   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/viral_usher   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### viral_usher_build

```bash
$ singularity exec <container> /usr/local/bin/viral_usher_build
$ podman run --it --rm --entrypoint /usr/local/bin/viral_usher_build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/viral_usher_build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wsdump

```bash
$ singularity exec <container> /usr/local/bin/wsdump
$ podman run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.14

```bash
$ singularity exec <container> /usr/local/bin/idle3.14
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.14

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.14
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14

```bash
$ singularity exec <container> /usr/local/bin/python3.14
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14-config

```bash
$ singularity exec <container> /usr/local/bin/python3.14-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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