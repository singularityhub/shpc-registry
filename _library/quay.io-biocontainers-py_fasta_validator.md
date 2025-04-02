---
layout: container
name:  "quay.io/biocontainers/py_fasta_validator"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/py_fasta_validator/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/py_fasta_validator/container.yaml"
updated_at: "2025-04-02 03:32:44.268761"
latest: "0.6--py39h475c85d_6"
container_url: "https://biocontainers.pro/tools/py_fasta_validator"
aliases:
 - "py_fasta_validator"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
versions:
 - "0.5--py38h4a32c8e_3"
 - "0.6--py39h6935b12_0"
 - "0.6--py39hd65a603_3"
 - "0.6--py310h2b6aa90_3"
 - "0.5--py310h30d9df9_3"
 - "0.6--py38hd638cd3_4"
 - "0.6--py39h475c85d_5"
 - "0.6--py39h475c85d_6"
description: "singularity registry hpc automated addition for py_fasta_validator"
config: {"url": "https://biocontainers.pro/tools/py_fasta_validator", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for py_fasta_validator", "latest": {"0.6--py39h475c85d_6": "sha256:22e34610a86266bb10a7a1c62d44eaa044fbfbb0786bf3d48cf54f3447758f35"}, "tags": {"0.5--py38h4a32c8e_3": "sha256:a9e80e766f3cb5917faec86d426463017d36ab566451ef5c437a2570ee25d582", "0.6--py39h6935b12_0": "sha256:f5274a5bf7b3e8c1a7b8e47a2e62333daa04cd33e163399755802da3ffbb23d1", "0.6--py39hd65a603_3": "sha256:941dd9f0469a53304c376faa1eb9672b77dddb0334d8033414e1742d08926264", "0.6--py310h2b6aa90_3": "sha256:ed3f428e981ed6b5ab1dd27c36482718c6912193eba95c224c105a4da01fec90", "0.5--py310h30d9df9_3": "sha256:6b049e34905949d5f91575b17e3ef190072a4874a5856daac9168e11d9999847", "0.6--py38hd638cd3_4": "sha256:b5538c5320a6d0dc562696f4720b906b2b3b1762fea7131c631357d999323358", "0.6--py39h475c85d_5": "sha256:7ecb533932a718771e90899a6959567263d33a7fa5c313f7f2f3649d499cd178", "0.6--py39h475c85d_6": "sha256:22e34610a86266bb10a7a1c62d44eaa044fbfbb0786bf3d48cf54f3447758f35"}, "docker": "quay.io/biocontainers/py_fasta_validator", "aliases": {"py_fasta_validator": "/usr/local/bin/py_fasta_validator", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/py_fasta_validator.
singularity registry hpc automated addition for py_fasta_validator
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/py_fasta_validator
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/py_fasta_validator:0.6--py39h475c85d_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/py_fasta_validator/0.6--py39h475c85d_6
$ module help quay.io/biocontainers/py_fasta_validator/0.6--py39h475c85d_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### py_fasta_validator-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### py_fasta_validator-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### py_fasta_validator-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### py_fasta_validator-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### py_fasta_validator-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### py_fasta_validator-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### py_fasta_validator

```bash
$ singularity exec <container> /usr/local/bin/py_fasta_validator
$ podman run --it --rm --entrypoint /usr/local/bin/py_fasta_validator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/py_fasta_validator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.8
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8

```bash
$ singularity exec <container> /usr/local/bin/python3.8
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8-config

```bash
$ singularity exec <container> /usr/local/bin/python3.8-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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