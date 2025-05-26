---
layout: container
name:  "quay.io/biocontainers/elector"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/elector/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/elector/container.yaml"
updated_at: "2025-05-26 12:18:48.827694"
latest: "1.0.4--py312h719dbc0_5"
container_url: "https://biocontainers.pro/tools/elector"
aliases:
 - "Donatello"
 - "elector"
 - "fq2fa"
 - "masterSplitter"
 - "poa"
 - "simulator"
 - "sdust"
 - "paftools.js"
 - "minimap2"
 - "k8"
 - "f2py3.6"
 - "fasta-sanitize.pl"
 - "plot-ampliconstats"
 - "2to3-3.6"
 - "idle3.6"
 - "pydoc3.6"
versions:
 - "1.0.4--py36h4aaaa08_3"
 - "1.0.4--py39he10ea66_4"
 - "1.0.4--py38hcbe9525_4"
 - "1.0.4--py312h719dbc0_5"
description: "shpc-registry automated BioContainers addition for elector"
config: {"url": "https://biocontainers.pro/tools/elector", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for elector", "latest": {"1.0.4--py312h719dbc0_5": "sha256:19a6e75fe55467b5b639720aede62b8d75f18d3b5e283dd0811663dbec12c464"}, "tags": {"1.0.4--py36h4aaaa08_3": "sha256:b4894ff41be1b3e1f94cdac9e67f25a3289427d1b03765306dcb9920c7d24f72", "1.0.4--py39he10ea66_4": "sha256:4a17b0622469603426802e70d5298578f1aa5075c2b266d52b90b922ce74b390", "1.0.4--py38hcbe9525_4": "sha256:11f7e53a0879eaf29cb32da6fa406a9feb8c340c5bef44f41ec22c11ecc368ee", "1.0.4--py312h719dbc0_5": "sha256:19a6e75fe55467b5b639720aede62b8d75f18d3b5e283dd0811663dbec12c464"}, "docker": "quay.io/biocontainers/elector", "aliases": {"Donatello": "/usr/local/bin/Donatello", "elector": "/usr/local/bin/elector", "fq2fa": "/usr/local/bin/fq2fa", "masterSplitter": "/usr/local/bin/masterSplitter", "poa": "/usr/local/bin/poa", "simulator": "/usr/local/bin/simulator", "sdust": "/usr/local/bin/sdust", "paftools.js": "/usr/local/bin/paftools.js", "minimap2": "/usr/local/bin/minimap2", "k8": "/usr/local/bin/k8", "f2py3.6": "/usr/local/bin/f2py3.6", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/elector.
shpc-registry automated BioContainers addition for elector
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/elector
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/elector:1.0.4--py312h719dbc0_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/elector/1.0.4--py312h719dbc0_5
$ module help quay.io/biocontainers/elector/1.0.4--py312h719dbc0_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### elector-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### elector-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### elector-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### elector-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### elector-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### elector-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Donatello

```bash
$ singularity exec <container> /usr/local/bin/Donatello
$ podman run --it --rm --entrypoint /usr/local/bin/Donatello   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Donatello   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elector

```bash
$ singularity exec <container> /usr/local/bin/elector
$ podman run --it --rm --entrypoint /usr/local/bin/elector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elector   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fq2fa

```bash
$ singularity exec <container> /usr/local/bin/fq2fa
$ podman run --it --rm --entrypoint /usr/local/bin/fq2fa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fq2fa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### masterSplitter

```bash
$ singularity exec <container> /usr/local/bin/masterSplitter
$ podman run --it --rm --entrypoint /usr/local/bin/masterSplitter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/masterSplitter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### poa

```bash
$ singularity exec <container> /usr/local/bin/poa
$ podman run --it --rm --entrypoint /usr/local/bin/poa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/poa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simulator

```bash
$ singularity exec <container> /usr/local/bin/simulator
$ podman run --it --rm --entrypoint /usr/local/bin/simulator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simulator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdust

```bash
$ singularity exec <container> /usr/local/bin/sdust
$ podman run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paftools.js

```bash
$ singularity exec <container> /usr/local/bin/paftools.js
$ podman run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2

```bash
$ singularity exec <container> /usr/local/bin/minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### k8

```bash
$ singularity exec <container> /usr/local/bin/k8
$ podman run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.6

```bash
$ singularity exec <container> /usr/local/bin/f2py3.6
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-sanitize.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta-sanitize.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-ampliconstats

```bash
$ singularity exec <container> /usr/local/bin/plot-ampliconstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.6

```bash
$ singularity exec <container> /usr/local/bin/idle3.6
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.6

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
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