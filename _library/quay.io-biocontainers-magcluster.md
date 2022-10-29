---
layout: container
name:  "quay.io/biocontainers/magcluster"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/magcluster/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/magcluster/container.yaml"
updated_at: "2022-10-29 05:52:02.781220"
latest: "0.2.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/magcluster"
aliases:
 - "clinker"
 - "magcluster"
 - "2to3-3.7"
 - "SOAPsh.pl"
 - "accn-at-a-time"
 - "ace.pl"
 - "activate-global-python-argcomplete"
 - "acyclic"
 - "align-columns"
 - "alimask"
 - "amino-acid-composition"
 - "annotate"
versions:
 - "0.2.2--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for magcluster"
config: {"url": "https://biocontainers.pro/tools/magcluster", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for magcluster", "latest": {"0.2.2--pyhdfd78af_0": "sha256:8b2fc39941c2aa679e313e1061956ddba48d8d89fc5ea294615190349e1fe52d"}, "tags": {"0.2.2--pyhdfd78af_0": "sha256:8b2fc39941c2aa679e313e1061956ddba48d8d89fc5ea294615190349e1fe52d"}, "docker": "quay.io/biocontainers/magcluster", "aliases": {"clinker": "/usr/local/bin/clinker", "magcluster": "/usr/local/bin/magcluster", "2to3-3.7": "/usr/local/bin/2to3-3.7", "SOAPsh.pl": "/usr/local/bin/SOAPsh.pl", "accn-at-a-time": "/usr/local/bin/accn-at-a-time", "ace.pl": "/usr/local/bin/ace.pl", "activate-global-python-argcomplete": "/usr/local/bin/activate-global-python-argcomplete", "acyclic": "/usr/local/bin/acyclic", "align-columns": "/usr/local/bin/align-columns", "alimask": "/usr/local/bin/alimask", "amino-acid-composition": "/usr/local/bin/amino-acid-composition", "annotate": "/usr/local/bin/annotate"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/magcluster.
shpc-registry automated BioContainers addition for magcluster
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/magcluster
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/magcluster:0.2.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/magcluster/0.2.2--pyhdfd78af_0
$ module help quay.io/biocontainers/magcluster/0.2.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### magcluster-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### magcluster-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### magcluster-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### magcluster-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### magcluster-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### magcluster-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### clinker

```bash
$ singularity exec <container> /usr/local/bin/clinker
$ podman run --it --rm --entrypoint /usr/local/bin/clinker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clinker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### magcluster

```bash
$ singularity exec <container> /usr/local/bin/magcluster
$ podman run --it --rm --entrypoint /usr/local/bin/magcluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/magcluster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SOAPsh.pl

```bash
$ singularity exec <container> /usr/local/bin/SOAPsh.pl
$ podman run --it --rm --entrypoint /usr/local/bin/SOAPsh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SOAPsh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### activate-global-python-argcomplete

```bash
$ singularity exec <container> /usr/local/bin/activate-global-python-argcomplete
$ podman run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acyclic

```bash
$ singularity exec <container> /usr/local/bin/acyclic
$ podman run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### align-columns

```bash
$ singularity exec <container> /usr/local/bin/align-columns
$ podman run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alimask

```bash
$ singularity exec <container> /usr/local/bin/alimask
$ podman run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
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