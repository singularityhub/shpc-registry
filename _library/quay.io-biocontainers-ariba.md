---
layout: container
name:  "quay.io/biocontainers/ariba"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ariba/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ariba/container.yaml"
updated_at: "2022-11-04 00:22:13.147497"
latest: "2.5.1--py35_0"
container_url: "https://biocontainers.pro/tools/ariba"
aliases:
 - "ariba"
 - "bwa-spades"
 - "corrector"
 - "dipspades"
 - "dipspades.py"
 - "hammer"
 - "ionhammer"
 - "scaffold_correction"
 - "spades"
 - "fastaq"
 - "cd-hit"
 - "cd-hit-2d"
 - "cd-hit-2d-para.pl"
 - "cd-hit-454"
 - "cd-hit-div"
 - "cd-hit-div.pl"
 - "cd-hit-est-2d"
 - "cd-hit-para.pl"
 - "clstr2tree.pl"
versions:
 - "2.5.1--py35_0"
description: "shpc-registry automated BioContainers addition for ariba"
config: {"url": "https://biocontainers.pro/tools/ariba", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ariba", "latest": {"2.5.1--py35_0": "sha256:c82cedd434b7c43357f0cd90ee276992f864af8010504d8562baaf4e991d6644"}, "tags": {"2.5.1--py35_0": "sha256:c82cedd434b7c43357f0cd90ee276992f864af8010504d8562baaf4e991d6644"}, "docker": "quay.io/biocontainers/ariba", "aliases": {"ariba": "/usr/local/bin/ariba", "bwa-spades": "/usr/local/bin/bwa-spades", "corrector": "/usr/local/bin/corrector", "dipspades": "/usr/local/bin/dipspades", "dipspades.py": "/usr/local/bin/dipspades.py", "hammer": "/usr/local/bin/hammer", "ionhammer": "/usr/local/bin/ionhammer", "scaffold_correction": "/usr/local/bin/scaffold_correction", "spades": "/usr/local/bin/spades", "fastaq": "/usr/local/bin/fastaq", "cd-hit": "/usr/local/bin/cd-hit", "cd-hit-2d": "/usr/local/bin/cd-hit-2d", "cd-hit-2d-para.pl": "/usr/local/bin/cd-hit-2d-para.pl", "cd-hit-454": "/usr/local/bin/cd-hit-454", "cd-hit-div": "/usr/local/bin/cd-hit-div", "cd-hit-div.pl": "/usr/local/bin/cd-hit-div.pl", "cd-hit-est-2d": "/usr/local/bin/cd-hit-est-2d", "cd-hit-para.pl": "/usr/local/bin/cd-hit-para.pl", "clstr2tree.pl": "/usr/local/bin/clstr2tree.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ariba.
shpc-registry automated BioContainers addition for ariba
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ariba
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ariba:2.5.1--py35_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ariba/2.5.1--py35_0
$ module help quay.io/biocontainers/ariba/2.5.1--py35_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ariba-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ariba-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ariba-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ariba-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ariba-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ariba-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ariba

```bash
$ singularity exec <container> /usr/local/bin/ariba
$ podman run --it --rm --entrypoint /usr/local/bin/ariba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ariba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-spades

```bash
$ singularity exec <container> /usr/local/bin/bwa-spades
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-spades   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-spades   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### corrector

```bash
$ singularity exec <container> /usr/local/bin/corrector
$ podman run --it --rm --entrypoint /usr/local/bin/corrector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/corrector   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dipspades

```bash
$ singularity exec <container> /usr/local/bin/dipspades
$ podman run --it --rm --entrypoint /usr/local/bin/dipspades   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dipspades   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dipspades.py

```bash
$ singularity exec <container> /usr/local/bin/dipspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/dipspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dipspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hammer

```bash
$ singularity exec <container> /usr/local/bin/hammer
$ podman run --it --rm --entrypoint /usr/local/bin/hammer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hammer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ionhammer

```bash
$ singularity exec <container> /usr/local/bin/ionhammer
$ podman run --it --rm --entrypoint /usr/local/bin/ionhammer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ionhammer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scaffold_correction

```bash
$ singularity exec <container> /usr/local/bin/scaffold_correction
$ podman run --it --rm --entrypoint /usr/local/bin/scaffold_correction   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scaffold_correction   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades

```bash
$ singularity exec <container> /usr/local/bin/spades
$ podman run --it --rm --entrypoint /usr/local/bin/spades   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaq

```bash
$ singularity exec <container> /usr/local/bin/fastaq
$ podman run --it --rm --entrypoint /usr/local/bin/fastaq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit

```bash
$ singularity exec <container> /usr/local/bin/cd-hit
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-2d

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-2d
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-2d   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-2d   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-2d-para.pl

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-2d-para.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-2d-para.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-2d-para.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-454

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-454
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-454   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-454   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-div

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-div
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-div   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-div   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-div.pl

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-div.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-div.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-div.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-est-2d

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-est-2d
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-est-2d   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-est-2d   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-para.pl

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-para.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-para.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-para.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clstr2tree.pl

```bash
$ singularity exec <container> /usr/local/bin/clstr2tree.pl
$ podman run --it --rm --entrypoint /usr/local/bin/clstr2tree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clstr2tree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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