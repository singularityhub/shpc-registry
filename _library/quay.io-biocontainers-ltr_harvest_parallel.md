---
layout: container
name:  "quay.io/biocontainers/ltr_harvest_parallel"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ltr_harvest_parallel/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ltr_harvest_parallel/container.yaml"
updated_at: "2025-12-19 05:03:38.843756"
latest: "1.2--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/ltr_harvest_parallel"
aliases:
 - "LTR_HARVEST_parallel"
 - "genometools-config"
 - "gt"
 - "pcre2posix_test"
 - "hb-info"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
versions:
 - "1.1--hdfd78af_0"
 - "1.1--hdfd78af_1"
 - "1.2--hdfd78af_0"
 - "1.2--hdfd78af_2"
description: "singularity registry hpc automated addition for ltr_harvest_parallel"
config: {"url": "https://biocontainers.pro/tools/ltr_harvest_parallel", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ltr_harvest_parallel", "latest": {"1.2--hdfd78af_2": "sha256:df2dea0676c2345c69c8aa719f74254815ba82728e64617c83c3d5bd26e6baab"}, "tags": {"1.1--hdfd78af_0": "sha256:5ed99acdb518e848a69a71b04a2ec7c6d898a23021c93474b4ffa66532b91755", "1.1--hdfd78af_1": "sha256:90da79dc3f17f8feb4fa2563fc449f18084b4dc3e379f70ca3130ee90e253d10", "1.2--hdfd78af_0": "sha256:892cf3f54a0e85761c0b94c4fb935e73db3ffa3a01d35d8702c37f37f540c806", "1.2--hdfd78af_2": "sha256:df2dea0676c2345c69c8aa719f74254815ba82728e64617c83c3d5bd26e6baab"}, "docker": "quay.io/biocontainers/ltr_harvest_parallel", "aliases": {"LTR_HARVEST_parallel": "/usr/local/bin/LTR_HARVEST_parallel", "genometools-config": "/usr/local/bin/genometools-config", "gt": "/usr/local/bin/gt", "pcre2posix_test": "/usr/local/bin/pcre2posix_test", "hb-info": "/usr/local/bin/hb-info", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ltr_harvest_parallel.
singularity registry hpc automated addition for ltr_harvest_parallel
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ltr_harvest_parallel
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ltr_harvest_parallel:1.2--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ltr_harvest_parallel/1.2--hdfd78af_2
$ module help quay.io/biocontainers/ltr_harvest_parallel/1.2--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ltr_harvest_parallel-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ltr_harvest_parallel-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ltr_harvest_parallel-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ltr_harvest_parallel-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ltr_harvest_parallel-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ltr_harvest_parallel-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### LTR_HARVEST_parallel

```bash
$ singularity exec <container> /usr/local/bin/LTR_HARVEST_parallel
$ podman run --it --rm --entrypoint /usr/local/bin/LTR_HARVEST_parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LTR_HARVEST_parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genometools-config

```bash
$ singularity exec <container> /usr/local/bin/genometools-config
$ podman run --it --rm --entrypoint /usr/local/bin/genometools-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genometools-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gt

```bash
$ singularity exec <container> /usr/local/bin/gt
$ podman run --it --rm --entrypoint /usr/local/bin/gt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pcre2posix_test

```bash
$ singularity exec <container> /usr/local/bin/pcre2posix_test
$ podman run --it --rm --entrypoint /usr/local/bin/pcre2posix_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pcre2posix_test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
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