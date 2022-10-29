---
layout: container
name:  "quay.io/biocontainers/flanker"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/flanker/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/flanker/container.yaml"
updated_at: "2022-10-29 05:36:24.607249"
latest: "0.1.5--py_0"
container_url: "https://biocontainers.pro/tools/flanker"
aliases:
 - "flanker"
 - "2to3-3.7"
 - "CA.pm"
 - "SOAPsh.pl"
 - "abricate"
 - "abricate-get_db"
 - "accn-at-a-time"
 - "ace.pl"
 - "acyclic"
 - "amino-acid-composition"
 - "annotate"
versions:
 - "0.1.5--py_0"
description: "shpc-registry automated BioContainers addition for flanker"
config: {"url": "https://biocontainers.pro/tools/flanker", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for flanker", "latest": {"0.1.5--py_0": "sha256:9bdedadf71d11b3003d0e406a27f23becb944c803aa52fd732ad5beaf608aa89"}, "tags": {"0.1.5--py_0": "sha256:9bdedadf71d11b3003d0e406a27f23becb944c803aa52fd732ad5beaf608aa89"}, "docker": "quay.io/biocontainers/flanker", "aliases": {"flanker": "/usr/local/bin/flanker", "2to3-3.7": "/usr/local/bin/2to3-3.7", "CA.pm": "/usr/local/bin/CA.pm", "SOAPsh.pl": "/usr/local/bin/SOAPsh.pl", "abricate": "/usr/local/bin/abricate", "abricate-get_db": "/usr/local/bin/abricate-get_db", "accn-at-a-time": "/usr/local/bin/accn-at-a-time", "ace.pl": "/usr/local/bin/ace.pl", "acyclic": "/usr/local/bin/acyclic", "amino-acid-composition": "/usr/local/bin/amino-acid-composition", "annotate": "/usr/local/bin/annotate"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/flanker.
shpc-registry automated BioContainers addition for flanker
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/flanker
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/flanker:0.1.5--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/flanker/0.1.5--py_0
$ module help quay.io/biocontainers/flanker/0.1.5--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### flanker-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### flanker-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### flanker-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### flanker-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### flanker-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### flanker-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### flanker

```bash
$ singularity exec <container> /usr/local/bin/flanker
$ podman run --it --rm --entrypoint /usr/local/bin/flanker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flanker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CA.pm

```bash
$ singularity exec <container> /usr/local/bin/CA.pm
$ podman run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SOAPsh.pl

```bash
$ singularity exec <container> /usr/local/bin/SOAPsh.pl
$ podman run --it --rm --entrypoint /usr/local/bin/SOAPsh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SOAPsh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abricate

```bash
$ singularity exec <container> /usr/local/bin/abricate
$ podman run --it --rm --entrypoint /usr/local/bin/abricate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abricate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abricate-get_db

```bash
$ singularity exec <container> /usr/local/bin/abricate-get_db
$ podman run --it --rm --entrypoint /usr/local/bin/abricate-get_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abricate-get_db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### accn-at-a-time

```bash
$ singularity exec <container> /usr/local/bin/accn-at-a-time
$ podman run --it --rm --entrypoint /usr/local/bin/accn-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/accn-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace.pl

```bash
$ singularity exec <container> /usr/local/bin/ace.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ace.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acyclic

```bash
$ singularity exec <container> /usr/local/bin/acyclic
$ podman run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amino-acid-composition

```bash
$ singularity exec <container> /usr/local/bin/amino-acid-composition
$ podman run --it --rm --entrypoint /usr/local/bin/amino-acid-composition   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amino-acid-composition   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotate

```bash
$ singularity exec <container> /usr/local/bin/annotate
$ podman run --it --rm --entrypoint /usr/local/bin/annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
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