---
layout: container
name:  "quay.io/biocontainers/bammmotif2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bammmotif2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bammmotif2/container.yaml"
updated_at: "2026-08-21 18:33:01.555230"
latest: "2.0.0--hc52dbad_0"
container_url: "https://biocontainers.pro/tools/bammmotif2"
aliases:
 - "BaMMScan"
 - "BaMMSimu"
 - "BaMMmotif"
 - "FDR"
 - "evaluateBaMM.R"
 - "plotBaMMLogo.R"
 - "plotMotifDistribution.R"
versions:
 - "2.0.0--hc52dbad_0"
description: "singularity registry hpc automated addition for bammmotif2"
config: {"url": "https://biocontainers.pro/tools/bammmotif2", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bammmotif2", "latest": {"2.0.0--hc52dbad_0": "sha256:0519541da0dace3d65f6189586b4c93583a1cc5d5d8bc7c6dc84e6a04bd32005"}, "tags": {"2.0.0--hc52dbad_0": "sha256:0519541da0dace3d65f6189586b4c93583a1cc5d5d8bc7c6dc84e6a04bd32005"}, "docker": "quay.io/biocontainers/bammmotif2", "aliases": {"BaMMScan": "/usr/local/bin/BaMMScan", "BaMMSimu": "/usr/local/bin/BaMMSimu", "BaMMmotif": "/usr/local/bin/BaMMmotif", "FDR": "/usr/local/bin/FDR", "evaluateBaMM.R": "/usr/local/bin/evaluateBaMM.R", "plotBaMMLogo.R": "/usr/local/bin/plotBaMMLogo.R", "plotMotifDistribution.R": "/usr/local/bin/plotMotifDistribution.R"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bammmotif2.
singularity registry hpc automated addition for bammmotif2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bammmotif2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bammmotif2:2.0.0--hc52dbad_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bammmotif2/2.0.0--hc52dbad_0
$ module help quay.io/biocontainers/bammmotif2/2.0.0--hc52dbad_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bammmotif2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bammmotif2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bammmotif2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bammmotif2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bammmotif2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bammmotif2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### BaMMScan

```bash
$ singularity exec <container> /usr/local/bin/BaMMScan
$ podman run --it --rm --entrypoint /usr/local/bin/BaMMScan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BaMMScan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### BaMMSimu

```bash
$ singularity exec <container> /usr/local/bin/BaMMSimu
$ podman run --it --rm --entrypoint /usr/local/bin/BaMMSimu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BaMMSimu   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### BaMMmotif

```bash
$ singularity exec <container> /usr/local/bin/BaMMmotif
$ podman run --it --rm --entrypoint /usr/local/bin/BaMMmotif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BaMMmotif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FDR

```bash
$ singularity exec <container> /usr/local/bin/FDR
$ podman run --it --rm --entrypoint /usr/local/bin/FDR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FDR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### evaluateBaMM.R

```bash
$ singularity exec <container> /usr/local/bin/evaluateBaMM.R
$ podman run --it --rm --entrypoint /usr/local/bin/evaluateBaMM.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/evaluateBaMM.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotBaMMLogo.R

```bash
$ singularity exec <container> /usr/local/bin/plotBaMMLogo.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotBaMMLogo.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotBaMMLogo.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotMotifDistribution.R

```bash
$ singularity exec <container> /usr/local/bin/plotMotifDistribution.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotMotifDistribution.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotMotifDistribution.R   -v ${PWD} -w ${PWD} <container> -c " $@"
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