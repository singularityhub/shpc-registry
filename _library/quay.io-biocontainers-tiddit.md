---
layout: container
name:  "quay.io/biocontainers/tiddit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tiddit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tiddit/container.yaml"
updated_at: "2025-10-28 03:51:40.323596"
latest: "3.9.3--py39hff726c5_1"
container_url: "https://biocontainers.pro/tools/tiddit"
aliases:
 - "bfc"
 - "fermi2"
 - "fermi2.pl"
 - "ropebwt2"
 - "tiddit"
 - "seqtk"
 - "qualfa2fq.pl"
 - "xa2multi.pl"
 - "bwa"
 - "f2py3.9"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "3.1.0--py39h59fae87_0"
 - "3.6.1--py38h24c8ff8_0"
 - "3.4.0--py310hc2b7f4b_0"
 - "3.3.2--py310hc2b7f4b_0"
 - "3.2.1--py310hc2b7f4b_0"
 - "3.1.0--py39hc2b7f4b_1"
 - "3.7.0--py39h24fbfe6_0"
 - "3.6.1--py39h24fbfe6_2"
 - "3.9.0--py311h93dcfea_0"
 - "3.9.2--py39hff726c5_0"
 - "3.9.3--py311h93dcfea_0"
 - "3.9.3--py39hff726c5_1"
description: "shpc-registry automated BioContainers addition for tiddit"
config: {"url": "https://biocontainers.pro/tools/tiddit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tiddit", "latest": {"3.9.3--py39hff726c5_1": "sha256:776f2f3d51606180f1de99b792813eb6aae72057a7532e03d3d8684995369bff"}, "tags": {"3.1.0--py39h59fae87_0": "sha256:34f33e811439d931815c1afff963ac8b7cccb02d26d69fbb6eb166804ecc2a34", "3.6.1--py38h24c8ff8_0": "sha256:2ad9f14dfdaf233430fea67805795c69dc4cb8cbe7fbb0ef8555558a42261f84", "3.4.0--py310hc2b7f4b_0": "sha256:dcbc084269f91692ec158cfe9c8939dcbd1f64e97b8ab6863fb3fe1b0aa03611", "3.3.2--py310hc2b7f4b_0": "sha256:79ac44f66f0d3cc704e8ac2fcd2f737d261738e0889bf43a3a170ea949c6b734", "3.2.1--py310hc2b7f4b_0": "sha256:b2601b6a0f38b44d1fd0963aec28e3443a5e0ff71ad801da30164b7e7618b799", "3.1.0--py39hc2b7f4b_1": "sha256:24c1ed1479ad2a9881383b05a8fa85ad63349cb6886430b8bb1e2687bbcb7aea", "3.7.0--py39h24fbfe6_0": "sha256:3d12c557c0ceda8f3b44eefd216af2e15fa1ca6b1e1b75fcb8bd4044221e9c2b", "3.6.1--py39h24fbfe6_2": "sha256:30b024042f1ec39909923c131a1dce6c5a643701e52a375dc87af759fa222b8c", "3.9.0--py311h93dcfea_0": "sha256:3747ba79beb01e9e794b998ae59ad6b683f87ef53807122437a2741c2e2d5396", "3.9.2--py39hff726c5_0": "sha256:b44b2b17463dfb9914f764d57a1a833b071269d70271f533f169d2566ff0d49a", "3.9.3--py311h93dcfea_0": "sha256:76b8450ef4612ea6a6f182bb0776dea1e1839db821f119d99e757768de2af7de", "3.9.3--py39hff726c5_1": "sha256:776f2f3d51606180f1de99b792813eb6aae72057a7532e03d3d8684995369bff"}, "docker": "quay.io/biocontainers/tiddit", "aliases": {"bfc": "/usr/local/bin/bfc", "fermi2": "/usr/local/bin/fermi2", "fermi2.pl": "/usr/local/bin/fermi2.pl", "ropebwt2": "/usr/local/bin/ropebwt2", "tiddit": "/usr/local/bin/tiddit", "seqtk": "/usr/local/bin/seqtk", "qualfa2fq.pl": "/usr/local/bin/qualfa2fq.pl", "xa2multi.pl": "/usr/local/bin/xa2multi.pl", "bwa": "/usr/local/bin/bwa", "f2py3.9": "/usr/local/bin/f2py3.9", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tiddit.
shpc-registry automated BioContainers addition for tiddit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tiddit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tiddit:3.9.3--py39hff726c5_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tiddit/3.9.3--py39hff726c5_1
$ module help quay.io/biocontainers/tiddit/3.9.3--py39hff726c5_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tiddit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tiddit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tiddit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tiddit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tiddit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tiddit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bfc

```bash
$ singularity exec <container> /usr/local/bin/bfc
$ podman run --it --rm --entrypoint /usr/local/bin/bfc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bfc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fermi2

```bash
$ singularity exec <container> /usr/local/bin/fermi2
$ podman run --it --rm --entrypoint /usr/local/bin/fermi2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fermi2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fermi2.pl

```bash
$ singularity exec <container> /usr/local/bin/fermi2.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fermi2.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fermi2.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ropebwt2

```bash
$ singularity exec <container> /usr/local/bin/ropebwt2
$ podman run --it --rm --entrypoint /usr/local/bin/ropebwt2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ropebwt2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiddit

```bash
$ singularity exec <container> /usr/local/bin/tiddit
$ podman run --it --rm --entrypoint /usr/local/bin/tiddit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tiddit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqtk

```bash
$ singularity exec <container> /usr/local/bin/seqtk
$ podman run --it --rm --entrypoint /usr/local/bin/seqtk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqtk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qualfa2fq.pl

```bash
$ singularity exec <container> /usr/local/bin/qualfa2fq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/qualfa2fq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qualfa2fq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xa2multi.pl

```bash
$ singularity exec <container> /usr/local/bin/xa2multi.pl
$ podman run --it --rm --entrypoint /usr/local/bin/xa2multi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xa2multi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa

```bash
$ singularity exec <container> /usr/local/bin/bwa
$ podman run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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