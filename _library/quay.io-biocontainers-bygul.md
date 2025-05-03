---
layout: container
name:  "quay.io/biocontainers/bygul"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bygul/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bygul/container.yaml"
updated_at: "2025-05-03 03:45:27.805368"
latest: "1.0.4--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/bygul"
aliases:
 - "bygul"
 - "mason_frag_sequencing"
 - "mason_genome"
 - "mason_materializer"
 - "mason_methylation"
 - "mason_simulator"
 - "mason_splicing"
 - "mason_variator"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "numpy-config"
 - "tqdm"
 - "wgsim"
 - "wgsim_eval.pl"
versions:
 - "1.0.4--pyhdfd78af_0"
description: "singularity registry hpc automated addition for bygul"
config: {"url": "https://biocontainers.pro/tools/bygul", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bygul", "latest": {"1.0.4--pyhdfd78af_0": "sha256:e60d75b98a932f5e52453bbbb130228680d7c75445518bae7553c6ca3a05ab66"}, "tags": {"1.0.4--pyhdfd78af_0": "sha256:e60d75b98a932f5e52453bbbb130228680d7c75445518bae7553c6ca3a05ab66"}, "docker": "quay.io/biocontainers/bygul", "aliases": {"bygul": "/usr/local/bin/bygul", "mason_frag_sequencing": "/usr/local/bin/mason_frag_sequencing", "mason_genome": "/usr/local/bin/mason_genome", "mason_materializer": "/usr/local/bin/mason_materializer", "mason_methylation": "/usr/local/bin/mason_methylation", "mason_simulator": "/usr/local/bin/mason_simulator", "mason_splicing": "/usr/local/bin/mason_splicing", "mason_variator": "/usr/local/bin/mason_variator", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "numpy-config": "/usr/local/bin/numpy-config", "tqdm": "/usr/local/bin/tqdm", "wgsim": "/usr/local/bin/wgsim", "wgsim_eval.pl": "/usr/local/bin/wgsim_eval.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bygul.
singularity registry hpc automated addition for bygul
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bygul
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bygul:1.0.4--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bygul/1.0.4--pyhdfd78af_0
$ module help quay.io/biocontainers/bygul/1.0.4--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bygul-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bygul-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bygul-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bygul-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bygul-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bygul-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bygul

```bash
$ singularity exec <container> /usr/local/bin/bygul
$ podman run --it --rm --entrypoint /usr/local/bin/bygul   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bygul   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mason_frag_sequencing

```bash
$ singularity exec <container> /usr/local/bin/mason_frag_sequencing
$ podman run --it --rm --entrypoint /usr/local/bin/mason_frag_sequencing   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mason_frag_sequencing   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mason_genome

```bash
$ singularity exec <container> /usr/local/bin/mason_genome
$ podman run --it --rm --entrypoint /usr/local/bin/mason_genome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mason_genome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mason_materializer

```bash
$ singularity exec <container> /usr/local/bin/mason_materializer
$ podman run --it --rm --entrypoint /usr/local/bin/mason_materializer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mason_materializer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mason_methylation

```bash
$ singularity exec <container> /usr/local/bin/mason_methylation
$ podman run --it --rm --entrypoint /usr/local/bin/mason_methylation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mason_methylation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mason_simulator

```bash
$ singularity exec <container> /usr/local/bin/mason_simulator
$ podman run --it --rm --entrypoint /usr/local/bin/mason_simulator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mason_simulator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mason_splicing

```bash
$ singularity exec <container> /usr/local/bin/mason_splicing
$ podman run --it --rm --entrypoint /usr/local/bin/mason_splicing   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mason_splicing   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mason_variator

```bash
$ singularity exec <container> /usr/local/bin/mason_variator
$ podman run --it --rm --entrypoint /usr/local/bin/mason_variator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mason_variator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.13

```bash
$ singularity exec <container> /usr/local/bin/idle3.13
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.13

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.13
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13

```bash
$ singularity exec <container> /usr/local/bin/python3.13
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13-config

```bash
$ singularity exec <container> /usr/local/bin/python3.13-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wgsim

```bash
$ singularity exec <container> /usr/local/bin/wgsim
$ podman run --it --rm --entrypoint /usr/local/bin/wgsim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wgsim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wgsim_eval.pl

```bash
$ singularity exec <container> /usr/local/bin/wgsim_eval.pl
$ podman run --it --rm --entrypoint /usr/local/bin/wgsim_eval.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wgsim_eval.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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