---
layout: container
name:  "quay.io/biocontainers/bioconductor-systempipeshiny"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-systempipeshiny/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-systempipeshiny/container.yaml"
updated_at: "2025-04-21 03:26:20.805951"
latest: "1.16.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-systempipeshiny"
aliases:
 - "pandoc"
versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.16.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-systempipeshiny"
config: {"url": "https://biocontainers.pro/tools/bioconductor-systempipeshiny", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-systempipeshiny", "latest": {"1.16.0--r44hdfd78af_0": "sha256:3d65744e1a45a291fe64ce04aceada0d692c35faa2538b8bc00a9cad6cd1a142"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:2a8c4f17594b3d5d30993d4f26135613c7946609fefbaff128ede574211ea202", "1.8.0--r42hdfd78af_0": "sha256:8cfff051bf0a652fc400c76434f575da466b41f513d20619cf12ecf0b1071d40", "1.10.0--r43hdfd78af_0": "sha256:7f18dc3d20b009fadffbc571139eb71fa8bb510bf0549a9a3806b68d193a26c3", "1.12.0--r43hdfd78af_0": "sha256:60e7f38f3266100bb55ceb61e6c0e9f42f21f9c819f2ce8e7840877ed1c46338", "1.16.0--r44hdfd78af_0": "sha256:3d65744e1a45a291fe64ce04aceada0d692c35faa2538b8bc00a9cad6cd1a142"}, "docker": "quay.io/biocontainers/bioconductor-systempipeshiny", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-systempipeshiny.
shpc-registry automated BioContainers addition for bioconductor-systempipeshiny
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-systempipeshiny
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-systempipeshiny:1.16.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-systempipeshiny/1.16.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-systempipeshiny/1.16.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-systempipeshiny-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-systempipeshiny-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-systempipeshiny-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-systempipeshiny-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-systempipeshiny-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-systempipeshiny-inspect-deffile:

```bash
$ singularity inspect -d <container>
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