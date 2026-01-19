---
layout: container
name:  "quay.io/biocontainers/mlgenotype"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mlgenotype/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mlgenotype/container.yaml"
updated_at: "2026-01-19 05:18:40.088440"
latest: "0.1.12--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/mlgenotype"
aliases:
 - "figure1calcs"
 - "rfmodelpredict"
 - "rfmodeltrain"
 - "rftrainpredict"
 - "normalizer"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
 - "python3.1"
versions:
 - "0.1.12--pyhdfd78af_0"
description: "singularity registry hpc automated addition for mlgenotype"
config: {"url": "https://biocontainers.pro/tools/mlgenotype", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mlgenotype", "latest": {"0.1.12--pyhdfd78af_0": "sha256:9a7230bbcb3c7d4898f1bf5e19b55c133356faa261600ab049b96a071ee2efeb"}, "tags": {"0.1.12--pyhdfd78af_0": "sha256:9a7230bbcb3c7d4898f1bf5e19b55c133356faa261600ab049b96a071ee2efeb"}, "docker": "quay.io/biocontainers/mlgenotype", "aliases": {"figure1calcs": "/usr/local/bin/figure1calcs", "rfmodelpredict": "/usr/local/bin/rfmodelpredict", "rfmodeltrain": "/usr/local/bin/rfmodeltrain", "rftrainpredict": "/usr/local/bin/rftrainpredict", "normalizer": "/usr/local/bin/normalizer", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mlgenotype.
singularity registry hpc automated addition for mlgenotype
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mlgenotype
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mlgenotype:0.1.12--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mlgenotype/0.1.12--pyhdfd78af_0
$ module help quay.io/biocontainers/mlgenotype/0.1.12--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mlgenotype-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mlgenotype-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mlgenotype-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mlgenotype-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mlgenotype-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mlgenotype-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### figure1calcs

```bash
$ singularity exec <container> /usr/local/bin/figure1calcs
$ podman run --it --rm --entrypoint /usr/local/bin/figure1calcs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/figure1calcs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rfmodelpredict

```bash
$ singularity exec <container> /usr/local/bin/rfmodelpredict
$ podman run --it --rm --entrypoint /usr/local/bin/rfmodelpredict   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rfmodelpredict   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rfmodeltrain

```bash
$ singularity exec <container> /usr/local/bin/rfmodeltrain
$ podman run --it --rm --entrypoint /usr/local/bin/rfmodeltrain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rfmodeltrain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rftrainpredict

```bash
$ singularity exec <container> /usr/local/bin/rftrainpredict
$ podman run --it --rm --entrypoint /usr/local/bin/rftrainpredict   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rftrainpredict   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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