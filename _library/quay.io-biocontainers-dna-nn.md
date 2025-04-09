---
layout: container
name:  "quay.io/biocontainers/dna-nn"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dna-nn/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dna-nn/container.yaml"
updated_at: "2025-04-09 03:15:44.523118"
latest: "0.1--h077b44d_2"
container_url: "https://biocontainers.pro/tools/dna-nn"
aliases:
 - "dna-brnn"
 - "dna-cnn"
 - "gen-fq"
 - "parse-rm.js"
 - "k8"
versions:
 - "0.1--hdcf5f25_1"
 - "0.1--h077b44d_2"
description: "singularity registry hpc automated addition for dna-nn"
config: {"url": "https://biocontainers.pro/tools/dna-nn", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for dna-nn", "latest": {"0.1--h077b44d_2": "sha256:250a75501f486881314819c576418f514b642365c56b24a3544fe90344971572"}, "tags": {"0.1--hdcf5f25_1": "sha256:4280b6531853bd3794eafc0e1af334c0f030fd242abc91f30fc985faab5f309d", "0.1--h077b44d_2": "sha256:250a75501f486881314819c576418f514b642365c56b24a3544fe90344971572"}, "docker": "quay.io/biocontainers/dna-nn", "aliases": {"dna-brnn": "/usr/local/bin/dna-brnn", "dna-cnn": "/usr/local/bin/dna-cnn", "gen-fq": "/usr/local/bin/gen-fq", "parse-rm.js": "/usr/local/bin/parse-rm.js", "k8": "/usr/local/bin/k8"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dna-nn.
singularity registry hpc automated addition for dna-nn
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dna-nn
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dna-nn:0.1--h077b44d_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dna-nn/0.1--h077b44d_2
$ module help quay.io/biocontainers/dna-nn/0.1--h077b44d_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dna-nn-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dna-nn-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dna-nn-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dna-nn-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dna-nn-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dna-nn-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dna-brnn

```bash
$ singularity exec <container> /usr/local/bin/dna-brnn
$ podman run --it --rm --entrypoint /usr/local/bin/dna-brnn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dna-brnn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dna-cnn

```bash
$ singularity exec <container> /usr/local/bin/dna-cnn
$ podman run --it --rm --entrypoint /usr/local/bin/dna-cnn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dna-cnn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gen-fq

```bash
$ singularity exec <container> /usr/local/bin/gen-fq
$ podman run --it --rm --entrypoint /usr/local/bin/gen-fq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gen-fq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parse-rm.js

```bash
$ singularity exec <container> /usr/local/bin/parse-rm.js
$ podman run --it --rm --entrypoint /usr/local/bin/parse-rm.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parse-rm.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### k8

```bash
$ singularity exec <container> /usr/local/bin/k8
$ podman run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
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