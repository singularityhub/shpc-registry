---
layout: container
name:  "quay.io/biocontainers/pifcosm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pifcosm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pifcosm/container.yaml"
updated_at: "2023-12-20 03:29:55.345806"
latest: "0.1.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/pifcosm"
aliases:
 - "Gblocks"
 - "PifCoSm.pl"
 - "RogueNaRok"
 - "RogueNaRok-parallel"
 - "contree"
 - "pairalign"
 - "rnr-lsi"
 - "rnr-mast"
 - "rnr-prune"
 - "rnr-tii"
 - "treeator"
 - "treebender"
 - "raxmlHPC"
 - "raxmlHPC-AVX2"
 - "raxmlHPC-PTHREADS"
 - "raxmlHPC-PTHREADS-AVX2"
 - "raxmlHPC-PTHREADS-SSE3"
 - "raxmlHPC-SSE3"
 - "FastTree-2.1.10.c"
 - "FET.pl"
 - "cd-hit-clstr_2_blm8.pl"
 - "clstr_list.pl"
versions:
 - "0.1.1--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for pifcosm"
config: {"url": "https://biocontainers.pro/tools/pifcosm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pifcosm", "latest": {"0.1.1--hdfd78af_0": "sha256:0cb75571e7af84689706b1118a262fc937a9ebe0ad381a0e4dae9c53f706b388"}, "tags": {"0.1.1--hdfd78af_0": "sha256:0cb75571e7af84689706b1118a262fc937a9ebe0ad381a0e4dae9c53f706b388"}, "docker": "quay.io/biocontainers/pifcosm", "aliases": {"Gblocks": "/usr/local/bin/Gblocks", "PifCoSm.pl": "/usr/local/bin/PifCoSm.pl", "RogueNaRok": "/usr/local/bin/RogueNaRok", "RogueNaRok-parallel": "/usr/local/bin/RogueNaRok-parallel", "contree": "/usr/local/bin/contree", "pairalign": "/usr/local/bin/pairalign", "rnr-lsi": "/usr/local/bin/rnr-lsi", "rnr-mast": "/usr/local/bin/rnr-mast", "rnr-prune": "/usr/local/bin/rnr-prune", "rnr-tii": "/usr/local/bin/rnr-tii", "treeator": "/usr/local/bin/treeator", "treebender": "/usr/local/bin/treebender", "raxmlHPC": "/usr/local/bin/raxmlHPC", "raxmlHPC-AVX2": "/usr/local/bin/raxmlHPC-AVX2", "raxmlHPC-PTHREADS": "/usr/local/bin/raxmlHPC-PTHREADS", "raxmlHPC-PTHREADS-AVX2": "/usr/local/bin/raxmlHPC-PTHREADS-AVX2", "raxmlHPC-PTHREADS-SSE3": "/usr/local/bin/raxmlHPC-PTHREADS-SSE3", "raxmlHPC-SSE3": "/usr/local/bin/raxmlHPC-SSE3", "FastTree-2.1.10.c": "/usr/local/bin/FastTree-2.1.10.c", "FET.pl": "/usr/local/bin/FET.pl", "cd-hit-clstr_2_blm8.pl": "/usr/local/bin/cd-hit-clstr_2_blm8.pl", "clstr_list.pl": "/usr/local/bin/clstr_list.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pifcosm.
shpc-registry automated BioContainers addition for pifcosm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pifcosm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pifcosm:0.1.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pifcosm/0.1.1--hdfd78af_0
$ module help quay.io/biocontainers/pifcosm/0.1.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pifcosm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pifcosm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pifcosm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pifcosm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pifcosm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pifcosm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Gblocks

```bash
$ singularity exec <container> /usr/local/bin/Gblocks
$ podman run --it --rm --entrypoint /usr/local/bin/Gblocks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Gblocks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PifCoSm.pl

```bash
$ singularity exec <container> /usr/local/bin/PifCoSm.pl
$ podman run --it --rm --entrypoint /usr/local/bin/PifCoSm.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PifCoSm.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RogueNaRok

```bash
$ singularity exec <container> /usr/local/bin/RogueNaRok
$ podman run --it --rm --entrypoint /usr/local/bin/RogueNaRok   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RogueNaRok   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RogueNaRok-parallel

```bash
$ singularity exec <container> /usr/local/bin/RogueNaRok-parallel
$ podman run --it --rm --entrypoint /usr/local/bin/RogueNaRok-parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RogueNaRok-parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### contree

```bash
$ singularity exec <container> /usr/local/bin/contree
$ podman run --it --rm --entrypoint /usr/local/bin/contree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/contree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pairalign

```bash
$ singularity exec <container> /usr/local/bin/pairalign
$ podman run --it --rm --entrypoint /usr/local/bin/pairalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pairalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnr-lsi

```bash
$ singularity exec <container> /usr/local/bin/rnr-lsi
$ podman run --it --rm --entrypoint /usr/local/bin/rnr-lsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnr-lsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnr-mast

```bash
$ singularity exec <container> /usr/local/bin/rnr-mast
$ podman run --it --rm --entrypoint /usr/local/bin/rnr-mast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnr-mast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnr-prune

```bash
$ singularity exec <container> /usr/local/bin/rnr-prune
$ podman run --it --rm --entrypoint /usr/local/bin/rnr-prune   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnr-prune   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnr-tii

```bash
$ singularity exec <container> /usr/local/bin/rnr-tii
$ podman run --it --rm --entrypoint /usr/local/bin/rnr-tii   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnr-tii   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### treeator

```bash
$ singularity exec <container> /usr/local/bin/treeator
$ podman run --it --rm --entrypoint /usr/local/bin/treeator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/treeator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### treebender

```bash
$ singularity exec <container> /usr/local/bin/treebender
$ podman run --it --rm --entrypoint /usr/local/bin/treebender   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/treebender   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC-AVX2

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC-AVX2
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC-AVX2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC-AVX2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC-PTHREADS

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC-PTHREADS
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC-PTHREADS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC-PTHREADS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC-PTHREADS-AVX2

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC-PTHREADS-AVX2
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC-PTHREADS-AVX2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC-PTHREADS-AVX2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC-PTHREADS-SSE3

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC-PTHREADS-SSE3
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC-PTHREADS-SSE3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC-PTHREADS-SSE3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC-SSE3

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC-SSE3
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC-SSE3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC-SSE3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTree-2.1.10.c

```bash
$ singularity exec <container> /usr/local/bin/FastTree-2.1.10.c
$ podman run --it --rm --entrypoint /usr/local/bin/FastTree-2.1.10.c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTree-2.1.10.c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FET.pl

```bash
$ singularity exec <container> /usr/local/bin/FET.pl
$ podman run --it --rm --entrypoint /usr/local/bin/FET.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FET.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-clstr_2_blm8.pl

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-clstr_2_blm8.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-clstr_2_blm8.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-clstr_2_blm8.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clstr_list.pl

```bash
$ singularity exec <container> /usr/local/bin/clstr_list.pl
$ podman run --it --rm --entrypoint /usr/local/bin/clstr_list.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clstr_list.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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