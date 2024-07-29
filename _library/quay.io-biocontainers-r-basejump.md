---
layout: container
name:  "quay.io/biocontainers/r-basejump"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-basejump/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-basejump/container.yaml"
updated_at: "2024-07-29 17:24:01.376820"
latest: "0.18.0--r43hdfd78af_1"
container_url: "https://biocontainers.pro/tools/r-basejump"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "0.9.9--r351_0"
 - "0.14.17--r41hdfd78af_2"
 - "0.13.4--r40_0"
 - "0.12.16--r40_0"
 - "0.11.23--r36_0"
 - "0.10.9--r351_1"
 - "0.18.0--r43hdfd78af_1"
 - "0.17.0--r43hdfd78af_1"
 - "0.16.5--r42hdfd78af_1"
 - "0.15.0--r41hdfd78af_0"
 - "0.14.23--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for r-basejump"
config: {"url": "https://biocontainers.pro/tools/r-basejump", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-basejump", "latest": {"0.18.0--r43hdfd78af_1": "sha256:db8774079fc75102adace21b1890b659d65f78ac697d7455fa3f19b734d37649"}, "tags": {"0.9.9--r351_0": "sha256:f0c7c3481098a42f6871e31c894d26ad7564a07e3ef80ffa054b34bf09493f7c", "0.14.17--r41hdfd78af_2": "sha256:1f245e059fb6c0f1eb7620c33eca863ddcab9e7b996174a48206b34d4d20323e", "0.13.4--r40_0": "sha256:21058bd5f181f0fc131a93e3a13251060c3580085edd2918c88098e7906f38ce", "0.12.16--r40_0": "sha256:7c3fcd7e02d85c733b7ef78928bc93bd085279ea89fd460ebbc5fdd60b5a1dbb", "0.11.23--r36_0": "sha256:6b161f5ffb59dc6569157d53dc6245215b2ec9df488d054cc9d30601cf3c8491", "0.10.9--r351_1": "sha256:5b5445e92408140facf057ec50eb5ba09333efa414123f2f99b59f0aba41564e", "0.18.0--r43hdfd78af_1": "sha256:db8774079fc75102adace21b1890b659d65f78ac697d7455fa3f19b734d37649", "0.17.0--r43hdfd78af_1": "sha256:4559c56ae3fd6133bcd8b49450b7c16f5f26f6529f08e24601af808c0bea2426", "0.16.5--r42hdfd78af_1": "sha256:beb290528a3dfc9a8a1b6e0b3ac307aa33285eaaa0bbd9a1228b1639f7779289", "0.15.0--r41hdfd78af_0": "sha256:ac3aac61ec74895c33b45761438ebbc34754e2be841c53318193758f9a4b028c", "0.14.23--r41hdfd78af_0": "sha256:1aba157511543c69c78d847c8de465951d9054cf45ed9effc9ed64e90348b815"}, "docker": "quay.io/biocontainers/r-basejump", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-basejump.
shpc-registry automated BioContainers addition for r-basejump
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-basejump
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-basejump:0.18.0--r43hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-basejump/0.18.0--r43hdfd78af_1
$ module help quay.io/biocontainers/r-basejump/0.18.0--r43hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-basejump-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-basejump-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-basejump-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-basejump-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-basejump-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-basejump-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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