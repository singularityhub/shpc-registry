---
layout: container
name:  "quay.io/biocontainers/bioconductor-bert"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bert/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bert/container.yaml"
updated_at: "2026-11-05 09:29:05.145954"
latest: "1.6.0--r45hdfd78af_0-amd64"
container_url: "https://biocontainers.pro/tools/bioconductor-bert"
aliases:
 - "gmake"
 - "fc-genconf"
 - "x86_64-conda-linux-gnu.cfg"
versions:
 - "1.6.0--r45hdfd78af_0-amd64"
description: "singularity registry hpc automated addition for bioconductor-bert"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bert", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-bert", "latest": {"1.6.0--r45hdfd78af_0-amd64": "sha256:a5911a6c2c5438caf68868e6b1f1d528748a1c34f1ebe01f1789d1e347d10bfd"}, "tags": {"1.6.0--r45hdfd78af_0-amd64": "sha256:a5911a6c2c5438caf68868e6b1f1d528748a1c34f1ebe01f1789d1e347d10bfd"}, "docker": "quay.io/biocontainers/bioconductor-bert", "aliases": {"gmake": "/usr/local/bin/gmake", "fc-genconf": "/usr/local/bin/fc-genconf", "x86_64-conda-linux-gnu.cfg": "/usr/local/bin/x86_64-conda-linux-gnu.cfg"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bert.
singularity registry hpc automated addition for bioconductor-bert
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bert
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bert:1.6.0--r45hdfd78af_0-amd64
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bert/1.6.0--r45hdfd78af_0-amd64
$ module help quay.io/biocontainers/bioconductor-bert/1.6.0--r45hdfd78af_0-amd64
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bert-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bert-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bert-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bert-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bert-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bert-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gmake

```bash
$ singularity exec <container> /usr/local/bin/gmake
$ podman run --it --rm --entrypoint /usr/local/bin/gmake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-genconf

```bash
$ singularity exec <container> /usr/local/bin/fc-genconf
$ podman run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu.cfg

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu.cfg
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
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