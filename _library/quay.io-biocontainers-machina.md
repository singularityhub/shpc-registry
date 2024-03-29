---
layout: container
name:  "quay.io/biocontainers/machina"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/machina/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/machina/container.yaml"
updated_at: "2024-03-29 02:55:57.548317"
latest: "1.2--h21ec9f0_7"
container_url: "https://biocontainers.pro/tools/machina"
aliases:
 - "dimacs-solver"
 - "dimacs-to-lgf"
 - "generatemigrationtrees"
 - "generatemutationtrees"
 - "lemon-0.x-to-1.x.sh"
 - "lgf-gen"
 - "ms"
 - "pmh"
 - "pmh_sankoff"
 - "pmh_ti"
 - "pmh_tr"
 - "visualizeclonetree"
 - "visualizemigrationgraph"
 - "cbc"
 - "clp"
 - "glpsol"
 - "cluster"
versions:
 - "1.2--h7ff8a90_4"
 - "1.2--h7ff8a90_5"
 - "1.2--h21ec9f0_7"
description: "shpc-registry automated BioContainers addition for machina"
config: {"url": "https://biocontainers.pro/tools/machina", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for machina", "latest": {"1.2--h21ec9f0_7": "sha256:aaf3497b4bf7942be7174c0d7c54f262e6abcc5ebccfc7194644a7b5a4333d80"}, "tags": {"1.2--h7ff8a90_4": "sha256:e8e3b1c68d42fd8ae63a6c7fc7e25352b35d069fb0e647513db8e3e31ad8eb89", "1.2--h7ff8a90_5": "sha256:68f19a4158f839682debcefcb46b0fe89dc6de1b8114e684fb58eed05d7a4c8a", "1.2--h21ec9f0_7": "sha256:aaf3497b4bf7942be7174c0d7c54f262e6abcc5ebccfc7194644a7b5a4333d80"}, "docker": "quay.io/biocontainers/machina", "aliases": {"dimacs-solver": "/usr/local/bin/dimacs-solver", "dimacs-to-lgf": "/usr/local/bin/dimacs-to-lgf", "generatemigrationtrees": "/usr/local/bin/generatemigrationtrees", "generatemutationtrees": "/usr/local/bin/generatemutationtrees", "lemon-0.x-to-1.x.sh": "/usr/local/bin/lemon-0.x-to-1.x.sh", "lgf-gen": "/usr/local/bin/lgf-gen", "ms": "/usr/local/bin/ms", "pmh": "/usr/local/bin/pmh", "pmh_sankoff": "/usr/local/bin/pmh_sankoff", "pmh_ti": "/usr/local/bin/pmh_ti", "pmh_tr": "/usr/local/bin/pmh_tr", "visualizeclonetree": "/usr/local/bin/visualizeclonetree", "visualizemigrationgraph": "/usr/local/bin/visualizemigrationgraph", "cbc": "/usr/local/bin/cbc", "clp": "/usr/local/bin/clp", "glpsol": "/usr/local/bin/glpsol", "cluster": "/usr/local/bin/cluster"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/machina.
shpc-registry automated BioContainers addition for machina
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/machina
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/machina:1.2--h21ec9f0_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/machina/1.2--h21ec9f0_7
$ module help quay.io/biocontainers/machina/1.2--h21ec9f0_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### machina-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### machina-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### machina-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### machina-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### machina-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### machina-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dimacs-solver

```bash
$ singularity exec <container> /usr/local/bin/dimacs-solver
$ podman run --it --rm --entrypoint /usr/local/bin/dimacs-solver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dimacs-solver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dimacs-to-lgf

```bash
$ singularity exec <container> /usr/local/bin/dimacs-to-lgf
$ podman run --it --rm --entrypoint /usr/local/bin/dimacs-to-lgf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dimacs-to-lgf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generatemigrationtrees

```bash
$ singularity exec <container> /usr/local/bin/generatemigrationtrees
$ podman run --it --rm --entrypoint /usr/local/bin/generatemigrationtrees   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generatemigrationtrees   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generatemutationtrees

```bash
$ singularity exec <container> /usr/local/bin/generatemutationtrees
$ podman run --it --rm --entrypoint /usr/local/bin/generatemutationtrees   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generatemutationtrees   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lemon-0.x-to-1.x.sh

```bash
$ singularity exec <container> /usr/local/bin/lemon-0.x-to-1.x.sh
$ podman run --it --rm --entrypoint /usr/local/bin/lemon-0.x-to-1.x.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lemon-0.x-to-1.x.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lgf-gen

```bash
$ singularity exec <container> /usr/local/bin/lgf-gen
$ podman run --it --rm --entrypoint /usr/local/bin/lgf-gen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lgf-gen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ms

```bash
$ singularity exec <container> /usr/local/bin/ms
$ podman run --it --rm --entrypoint /usr/local/bin/ms   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ms   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pmh

```bash
$ singularity exec <container> /usr/local/bin/pmh
$ podman run --it --rm --entrypoint /usr/local/bin/pmh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pmh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pmh_sankoff

```bash
$ singularity exec <container> /usr/local/bin/pmh_sankoff
$ podman run --it --rm --entrypoint /usr/local/bin/pmh_sankoff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pmh_sankoff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pmh_ti

```bash
$ singularity exec <container> /usr/local/bin/pmh_ti
$ podman run --it --rm --entrypoint /usr/local/bin/pmh_ti   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pmh_ti   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pmh_tr

```bash
$ singularity exec <container> /usr/local/bin/pmh_tr
$ podman run --it --rm --entrypoint /usr/local/bin/pmh_tr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pmh_tr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### visualizeclonetree

```bash
$ singularity exec <container> /usr/local/bin/visualizeclonetree
$ podman run --it --rm --entrypoint /usr/local/bin/visualizeclonetree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/visualizeclonetree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### visualizemigrationgraph

```bash
$ singularity exec <container> /usr/local/bin/visualizemigrationgraph
$ podman run --it --rm --entrypoint /usr/local/bin/visualizemigrationgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/visualizemigrationgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbc

```bash
$ singularity exec <container> /usr/local/bin/cbc
$ podman run --it --rm --entrypoint /usr/local/bin/cbc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clp

```bash
$ singularity exec <container> /usr/local/bin/clp
$ podman run --it --rm --entrypoint /usr/local/bin/clp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cluster

```bash
$ singularity exec <container> /usr/local/bin/cluster
$ podman run --it --rm --entrypoint /usr/local/bin/cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
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