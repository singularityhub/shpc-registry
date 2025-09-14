---
layout: container
name:  "quay.io/biocontainers/symbiontscreener"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/symbiontscreener/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/symbiontscreener/container.yaml"
updated_at: "2025-09-14 03:09:37.461472"
latest: "1.0.0--h5ca1c30_2"
container_url: "https://biocontainers.pro/tools/symbiontscreener"
aliases:
 - "existDB"
 - "f2py3.11"
 - "kmer-mask"
 - "mapMers"
 - "mapMers-depth"
 - "mt19937ar-test"
 - "positionDB"
 - "simple"
 - "sysc"
 - "test-merStream"
 - "test-seqCache"
 - "test-seqStream"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "meryl"
 - "seqkit"
 - "jellyfish"
 - "python3.1"
versions:
 - "1.0.0--h5b5514e_0"
 - "1.0.0--h43eeafb_1"
 - "1.0.0--h5ca1c30_2"
description: "singularity registry hpc automated addition for symbiontscreener"
config: {"url": "https://biocontainers.pro/tools/symbiontscreener", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for symbiontscreener", "latest": {"1.0.0--h5ca1c30_2": "sha256:019a3173f5f4979bed38a523600cdbf081ca5bc7389d96cfd84fd38f2f706733"}, "tags": {"1.0.0--h5b5514e_0": "sha256:e76cc7f707fbbcde08e7bd40f6544bcaa5d479193fe8007431a0a10a462ebbc6", "1.0.0--h43eeafb_1": "sha256:3910e2ef083f113ef9ce37af2107e87dc7f70eb30527741da4db7bfa0e713b64", "1.0.0--h5ca1c30_2": "sha256:019a3173f5f4979bed38a523600cdbf081ca5bc7389d96cfd84fd38f2f706733"}, "docker": "quay.io/biocontainers/symbiontscreener", "aliases": {"existDB": "/usr/local/bin/existDB", "f2py3.11": "/usr/local/bin/f2py3.11", "kmer-mask": "/usr/local/bin/kmer-mask", "mapMers": "/usr/local/bin/mapMers", "mapMers-depth": "/usr/local/bin/mapMers-depth", "mt19937ar-test": "/usr/local/bin/mt19937ar-test", "positionDB": "/usr/local/bin/positionDB", "simple": "/usr/local/bin/simple", "sysc": "/usr/local/bin/sysc", "test-merStream": "/usr/local/bin/test-merStream", "test-seqCache": "/usr/local/bin/test-seqCache", "test-seqStream": "/usr/local/bin/test-seqStream", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "meryl": "/usr/local/bin/meryl", "seqkit": "/usr/local/bin/seqkit", "jellyfish": "/usr/local/bin/jellyfish", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/symbiontscreener.
singularity registry hpc automated addition for symbiontscreener
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/symbiontscreener
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/symbiontscreener:1.0.0--h5ca1c30_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/symbiontscreener/1.0.0--h5ca1c30_2
$ module help quay.io/biocontainers/symbiontscreener/1.0.0--h5ca1c30_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### symbiontscreener-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### symbiontscreener-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### symbiontscreener-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### symbiontscreener-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### symbiontscreener-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### symbiontscreener-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### existDB

```bash
$ singularity exec <container> /usr/local/bin/existDB
$ podman run --it --rm --entrypoint /usr/local/bin/existDB   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/existDB   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.11

```bash
$ singularity exec <container> /usr/local/bin/f2py3.11
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmer-mask

```bash
$ singularity exec <container> /usr/local/bin/kmer-mask
$ podman run --it --rm --entrypoint /usr/local/bin/kmer-mask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmer-mask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapMers

```bash
$ singularity exec <container> /usr/local/bin/mapMers
$ podman run --it --rm --entrypoint /usr/local/bin/mapMers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapMers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapMers-depth

```bash
$ singularity exec <container> /usr/local/bin/mapMers-depth
$ podman run --it --rm --entrypoint /usr/local/bin/mapMers-depth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapMers-depth   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mt19937ar-test

```bash
$ singularity exec <container> /usr/local/bin/mt19937ar-test
$ podman run --it --rm --entrypoint /usr/local/bin/mt19937ar-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mt19937ar-test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### positionDB

```bash
$ singularity exec <container> /usr/local/bin/positionDB
$ podman run --it --rm --entrypoint /usr/local/bin/positionDB   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/positionDB   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simple

```bash
$ singularity exec <container> /usr/local/bin/simple
$ podman run --it --rm --entrypoint /usr/local/bin/simple   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simple   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sysc

```bash
$ singularity exec <container> /usr/local/bin/sysc
$ podman run --it --rm --entrypoint /usr/local/bin/sysc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sysc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test-merStream

```bash
$ singularity exec <container> /usr/local/bin/test-merStream
$ podman run --it --rm --entrypoint /usr/local/bin/test-merStream   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test-merStream   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test-seqCache

```bash
$ singularity exec <container> /usr/local/bin/test-seqCache
$ podman run --it --rm --entrypoint /usr/local/bin/test-seqCache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test-seqCache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test-seqStream

```bash
$ singularity exec <container> /usr/local/bin/test-seqStream
$ podman run --it --rm --entrypoint /usr/local/bin/test-seqStream   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test-seqStream   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.11

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.11
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.11

```bash
$ singularity exec <container> /usr/local/bin/idle3.11
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.11

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.11
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11

```bash
$ singularity exec <container> /usr/local/bin/python3.11
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11-config

```bash
$ singularity exec <container> /usr/local/bin/python3.11-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meryl

```bash
$ singularity exec <container> /usr/local/bin/meryl
$ podman run --it --rm --entrypoint /usr/local/bin/meryl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meryl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqkit

```bash
$ singularity exec <container> /usr/local/bin/seqkit
$ podman run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jellyfish

```bash
$ singularity exec <container> /usr/local/bin/jellyfish
$ podman run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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