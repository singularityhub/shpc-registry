---
layout: container
name:  "quay.io/biocontainers/codonw"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/codonw/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/codonw/container.yaml"
updated_at: "2025-05-18 04:01:25.929419"
latest: "1.4.4--h7b50bb2_7"
container_url: "https://biocontainers.pro/tools/codonw"
aliases:
 - "aau"
 - "base3s"
 - "bases"
 - "cbi"
 - "codonw"
 - "cu"
 - "cutab"
 - "cutot"
 - "dinuc"
 - "enc"
 - "fop"
 - "gc3s"
 - "raau"
 - "reader"
 - "rscu"
 - "tidy"
 - "transl"
 - "cai"
 - "gc"
versions:
 - "1.4.4--hec16e2b_4"
 - "1.4.4--hec16e2b_5"
 - "1.4.4--h031d066_6"
 - "1.4.4--h7b50bb2_7"
description: "shpc-registry automated BioContainers addition for codonw"
config: {"url": "https://biocontainers.pro/tools/codonw", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for codonw", "latest": {"1.4.4--h7b50bb2_7": "sha256:25b07dac047a4f6c1fa21f89d524253229e98f07f0ee603a9d371556a6088264"}, "tags": {"1.4.4--hec16e2b_4": "sha256:f25ea50420d73c881793d59af13e74e38f8f908f5d0031bb9a66010d26e41c74", "1.4.4--hec16e2b_5": "sha256:f0ef14381e1a14cdb435b06ed55710c6e8bb74978ff3abe96c7e570837fd0f2a", "1.4.4--h031d066_6": "sha256:9dfee3836181b1eb2b033c4734c7cb4e2362f0a9b7b7d843a2a0b8c6676db9f5", "1.4.4--h7b50bb2_7": "sha256:25b07dac047a4f6c1fa21f89d524253229e98f07f0ee603a9d371556a6088264"}, "docker": "quay.io/biocontainers/codonw", "aliases": {"aau": "/usr/local/bin/aau", "base3s": "/usr/local/bin/base3s", "bases": "/usr/local/bin/bases", "cbi": "/usr/local/bin/cbi", "codonw": "/usr/local/bin/codonw", "cu": "/usr/local/bin/cu", "cutab": "/usr/local/bin/cutab", "cutot": "/usr/local/bin/cutot", "dinuc": "/usr/local/bin/dinuc", "enc": "/usr/local/bin/enc", "fop": "/usr/local/bin/fop", "gc3s": "/usr/local/bin/gc3s", "raau": "/usr/local/bin/raau", "reader": "/usr/local/bin/reader", "rscu": "/usr/local/bin/rscu", "tidy": "/usr/local/bin/tidy", "transl": "/usr/local/bin/transl", "cai": "/usr/local/bin/cai", "gc": "/usr/local/bin/gc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/codonw.
shpc-registry automated BioContainers addition for codonw
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/codonw
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/codonw:1.4.4--h7b50bb2_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/codonw/1.4.4--h7b50bb2_7
$ module help quay.io/biocontainers/codonw/1.4.4--h7b50bb2_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### codonw-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### codonw-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### codonw-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### codonw-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### codonw-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### codonw-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aau

```bash
$ singularity exec <container> /usr/local/bin/aau
$ podman run --it --rm --entrypoint /usr/local/bin/aau   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aau   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### base3s

```bash
$ singularity exec <container> /usr/local/bin/base3s
$ podman run --it --rm --entrypoint /usr/local/bin/base3s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/base3s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bases

```bash
$ singularity exec <container> /usr/local/bin/bases
$ podman run --it --rm --entrypoint /usr/local/bin/bases   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bases   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbi

```bash
$ singularity exec <container> /usr/local/bin/cbi
$ podman run --it --rm --entrypoint /usr/local/bin/cbi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### codonw

```bash
$ singularity exec <container> /usr/local/bin/codonw
$ podman run --it --rm --entrypoint /usr/local/bin/codonw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/codonw   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cu

```bash
$ singularity exec <container> /usr/local/bin/cu
$ podman run --it --rm --entrypoint /usr/local/bin/cu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cu   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cutab

```bash
$ singularity exec <container> /usr/local/bin/cutab
$ podman run --it --rm --entrypoint /usr/local/bin/cutab   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cutab   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cutot

```bash
$ singularity exec <container> /usr/local/bin/cutot
$ podman run --it --rm --entrypoint /usr/local/bin/cutot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cutot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dinuc

```bash
$ singularity exec <container> /usr/local/bin/dinuc
$ podman run --it --rm --entrypoint /usr/local/bin/dinuc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dinuc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### enc

```bash
$ singularity exec <container> /usr/local/bin/enc
$ podman run --it --rm --entrypoint /usr/local/bin/enc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/enc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fop

```bash
$ singularity exec <container> /usr/local/bin/fop
$ podman run --it --rm --entrypoint /usr/local/bin/fop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gc3s

```bash
$ singularity exec <container> /usr/local/bin/gc3s
$ podman run --it --rm --entrypoint /usr/local/bin/gc3s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gc3s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raau

```bash
$ singularity exec <container> /usr/local/bin/raau
$ podman run --it --rm --entrypoint /usr/local/bin/raau   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raau   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reader

```bash
$ singularity exec <container> /usr/local/bin/reader
$ podman run --it --rm --entrypoint /usr/local/bin/reader   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reader   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rscu

```bash
$ singularity exec <container> /usr/local/bin/rscu
$ podman run --it --rm --entrypoint /usr/local/bin/rscu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rscu   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tidy

```bash
$ singularity exec <container> /usr/local/bin/tidy
$ podman run --it --rm --entrypoint /usr/local/bin/tidy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tidy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transl

```bash
$ singularity exec <container> /usr/local/bin/transl
$ podman run --it --rm --entrypoint /usr/local/bin/transl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cai

```bash
$ singularity exec <container> /usr/local/bin/cai
$ podman run --it --rm --entrypoint /usr/local/bin/cai   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cai   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gc

```bash
$ singularity exec <container> /usr/local/bin/gc
$ podman run --it --rm --entrypoint /usr/local/bin/gc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gc   -v ${PWD} -w ${PWD} <container> -c " $@"
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