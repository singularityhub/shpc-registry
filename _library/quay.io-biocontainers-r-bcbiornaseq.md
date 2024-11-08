---
layout: container
name:  "quay.io/biocontainers/r-bcbiornaseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-bcbiornaseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-bcbiornaseq/container.yaml"
updated_at: "2024-11-08 02:50:55.499685"
latest: "0.6.2--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/r-bcbiornaseq"
aliases:
 - "pandoc"
versions:
 - "0.4.0--r41hdfd78af_0"
 - "0.5.1--r42hdfd78af_1"
 - "0.5.3--r42hdfd78af_0"
 - "0.5.3--r42hdfd78af_1"
 - "0.5.4--r42hdfd78af_1"
 - "0.5.4--r43hdfd78af_2"
 - "0.5.5--r43hdfd78af_0"
 - "0.6.0--r43hdfd78af_0"
 - "0.6.1--r43hdfd78af_0"
 - "0.6.2--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for r-bcbiornaseq"
config: {"url": "https://biocontainers.pro/tools/r-bcbiornaseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-bcbiornaseq", "latest": {"0.6.2--r43hdfd78af_0": "sha256:a815dce4cc7d6a0b57530c842ebafca52fac7c976fdaf4dd87ea3c5caccb57a3"}, "tags": {"0.4.0--r41hdfd78af_0": "sha256:95701957bc505b497ebdb56c6dbce92df8fae3b63de60ff776a00c4d246f2433", "0.5.1--r42hdfd78af_1": "sha256:f6a19ecd3caf672f7471dab63a33cfb847a4dd5e5423eb4fdeb89e4630f646d2", "0.5.3--r42hdfd78af_0": "sha256:e3181030eb8b0e5d6734df6ac3cda940cfb54630576c61fd837b503621e9bf96", "0.5.3--r42hdfd78af_1": "sha256:0fef783db654bab5d07e2474f021fc43b6b32f02355b8c44aac9a31731a09627", "0.5.4--r42hdfd78af_1": "sha256:6bce6a64e296d65b4950c47429f2c863ca38b2b352c73589cdcace93e3c54624", "0.5.4--r43hdfd78af_2": "sha256:7ad0ef1eb5526ba92cff1ee47aca0e949190058cfb2420acc7cf24e6731938cd", "0.5.5--r43hdfd78af_0": "sha256:55b8c85ed11880a8126a7588c0ec96815ead18e7acfb7750838aadb18a187dd6", "0.6.0--r43hdfd78af_0": "sha256:70ad59c328f7b3a594eaacfe75942ff0d431aba8d84c223721caa737c958cc45", "0.6.1--r43hdfd78af_0": "sha256:e14407b3e701007e8f1f6aacaedc2c79712fae0840b2cc38e6e4f29f03d76780", "0.6.2--r43hdfd78af_0": "sha256:a815dce4cc7d6a0b57530c842ebafca52fac7c976fdaf4dd87ea3c5caccb57a3"}, "docker": "quay.io/biocontainers/r-bcbiornaseq", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-bcbiornaseq.
shpc-registry automated BioContainers addition for r-bcbiornaseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-bcbiornaseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-bcbiornaseq:0.6.2--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-bcbiornaseq/0.6.2--r43hdfd78af_0
$ module help quay.io/biocontainers/r-bcbiornaseq/0.6.2--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-bcbiornaseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-bcbiornaseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-bcbiornaseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-bcbiornaseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-bcbiornaseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-bcbiornaseq-inspect-deffile:

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