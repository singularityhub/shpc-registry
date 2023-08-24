---
layout: container
name:  "quay.io/biocontainers/r-enchantr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-enchantr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-enchantr/container.yaml"
updated_at: "2023-08-24 02:21:51.999023"
latest: "0.1.3--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/r-enchantr"
aliases:
 - "pandoc-server"
 - "glpsol"
 - "pandoc"
versions:
 - "0.0.1--r41hdfd78af_0"
 - "0.0.4--r42hdfd78af_0"
 - "0.0.6--r42hdfd78af_0"
 - "0.1.1--r42hdfd78af_0"
 - "0.1.2--r42hdfd78af_0"
 - "0.1.3--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for r-enchantr"
config: {"url": "https://biocontainers.pro/tools/r-enchantr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-enchantr", "latest": {"0.1.3--r42hdfd78af_0": "sha256:dd6f109ef754c60fceb527cafc89aa11c8e7489e269482e5a707c654fd33b46f"}, "tags": {"0.0.1--r41hdfd78af_0": "sha256:332b49d3ba5d72a479a4b7115ee51bf05e9ff62fc912204b37af9819eb0ed994", "0.0.4--r42hdfd78af_0": "sha256:28aaec9bb7b062e9913e79d1dc0f99ee9dc402ac1979d1bdde966078548a6737", "0.0.6--r42hdfd78af_0": "sha256:76927a0247831813550f6bad11cfd35c462c4a391681274dba8170f07ae0fc9c", "0.1.1--r42hdfd78af_0": "sha256:9e0ef73ee5d54d8af4779aa0c05bdeb06d7f3b11a8c897dd1ca2c3374467acac", "0.1.2--r42hdfd78af_0": "sha256:41f3f403068446904e57c34bc1b81f7fbbed127955c2b0282bec17e3820ac11e", "0.1.3--r42hdfd78af_0": "sha256:dd6f109ef754c60fceb527cafc89aa11c8e7489e269482e5a707c654fd33b46f"}, "docker": "quay.io/biocontainers/r-enchantr", "aliases": {"pandoc-server": "/usr/local/bin/pandoc-server", "glpsol": "/usr/local/bin/glpsol", "pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-enchantr.
shpc-registry automated BioContainers addition for r-enchantr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-enchantr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-enchantr:0.1.3--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-enchantr/0.1.3--r42hdfd78af_0
$ module help quay.io/biocontainers/r-enchantr/0.1.3--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-enchantr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-enchantr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-enchantr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-enchantr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-enchantr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-enchantr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc-server

```bash
$ singularity exec <container> /usr/local/bin/pandoc-server
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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