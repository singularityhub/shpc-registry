---
layout: container
name:  "quay.io/biocontainers/cblaster"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cblaster/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cblaster/container.yaml"
updated_at: "2026-01-07 04:27:54.496186"
latest: "1.3.20--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/cblaster"
aliases:
 - "cblaster"
 - "clinker"
 - "gffutils-cli"
 - "activate-global-python-argcomplete"
 - "python-argcomplete-check-easy-install-script"
 - "python-argcomplete-tcsh"
 - "register-python-argcomplete"
 - "diamond"
 - "faidx"
 - "normalizer"
 - "chardetect"
 - "f2py3.9"
versions:
 - "1.3.9--pyhb7b1952_0"
 - "1.3.16--pyhdfd78af_0"
 - "1.3.17--pyhdfd78af_0"
 - "1.3.18--pyhdfd78af_0"
 - "1.3.19--pyhdfd78af_0"
 - "1.3.20--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for cblaster"
config: {"url": "https://biocontainers.pro/tools/cblaster", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cblaster", "latest": {"1.3.20--pyhdfd78af_0": "sha256:66e7e58f9be48d80a64e69a192bd6359b95e22d59a30ab8525aef043825b6c49"}, "tags": {"1.3.9--pyhb7b1952_0": "sha256:3b41c02e0ae141309bda49bfc64ceecf5737118436dafbce5c5695e33fec776b", "1.3.16--pyhdfd78af_0": "sha256:bc940c124299436f1bf2ec0f0169c153f708e5da2ee4805ff3e04afa72aa4878", "1.3.17--pyhdfd78af_0": "sha256:fcf904d71c58e1b4a063e962adcf420733353096a26219138456342cb0d8b6d7", "1.3.18--pyhdfd78af_0": "sha256:724ab0b3320fa54284569c2ad7475b4eb68295b9d586f39047311868a2044cac", "1.3.19--pyhdfd78af_0": "sha256:98cfb5fa8bc4689402d23f7fed6b17e8b736efedfecfb57afe56107c92c80ad7", "1.3.20--pyhdfd78af_0": "sha256:66e7e58f9be48d80a64e69a192bd6359b95e22d59a30ab8525aef043825b6c49"}, "docker": "quay.io/biocontainers/cblaster", "aliases": {"cblaster": "/usr/local/bin/cblaster", "clinker": "/usr/local/bin/clinker", "gffutils-cli": "/usr/local/bin/gffutils-cli", "activate-global-python-argcomplete": "/usr/local/bin/activate-global-python-argcomplete", "python-argcomplete-check-easy-install-script": "/usr/local/bin/python-argcomplete-check-easy-install-script", "python-argcomplete-tcsh": "/usr/local/bin/python-argcomplete-tcsh", "register-python-argcomplete": "/usr/local/bin/register-python-argcomplete", "diamond": "/usr/local/bin/diamond", "faidx": "/usr/local/bin/faidx", "normalizer": "/usr/local/bin/normalizer", "chardetect": "/usr/local/bin/chardetect", "f2py3.9": "/usr/local/bin/f2py3.9"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cblaster.
shpc-registry automated BioContainers addition for cblaster
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cblaster
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cblaster:1.3.20--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cblaster/1.3.20--pyhdfd78af_0
$ module help quay.io/biocontainers/cblaster/1.3.20--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cblaster-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cblaster-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cblaster-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cblaster-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cblaster-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cblaster-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cblaster

```bash
$ singularity exec <container> /usr/local/bin/cblaster
$ podman run --it --rm --entrypoint /usr/local/bin/cblaster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cblaster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clinker

```bash
$ singularity exec <container> /usr/local/bin/clinker
$ podman run --it --rm --entrypoint /usr/local/bin/clinker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clinker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gffutils-cli

```bash
$ singularity exec <container> /usr/local/bin/gffutils-cli
$ podman run --it --rm --entrypoint /usr/local/bin/gffutils-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gffutils-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### activate-global-python-argcomplete

```bash
$ singularity exec <container> /usr/local/bin/activate-global-python-argcomplete
$ podman run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-argcomplete-check-easy-install-script

```bash
$ singularity exec <container> /usr/local/bin/python-argcomplete-check-easy-install-script
$ podman run --it --rm --entrypoint /usr/local/bin/python-argcomplete-check-easy-install-script   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-argcomplete-check-easy-install-script   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-argcomplete-tcsh

```bash
$ singularity exec <container> /usr/local/bin/python-argcomplete-tcsh
$ podman run --it --rm --entrypoint /usr/local/bin/python-argcomplete-tcsh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-argcomplete-tcsh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### register-python-argcomplete

```bash
$ singularity exec <container> /usr/local/bin/register-python-argcomplete
$ podman run --it --rm --entrypoint /usr/local/bin/register-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/register-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diamond

```bash
$ singularity exec <container> /usr/local/bin/diamond
$ podman run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faidx

```bash
$ singularity exec <container> /usr/local/bin/faidx
$ podman run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
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