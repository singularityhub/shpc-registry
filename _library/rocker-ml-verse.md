---
layout: container
name:  "rocker/ml-verse"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/rocker/ml-verse/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/rocker/ml-verse/container.yaml"
updated_at: "2023-06-03 03:52:42.799433"
latest: "4.3.0"
container_url: "https://hub.docker.com/r/rocker/ml-verse"
aliases:
 - "R"
 - "Rscript"
 - "rocker-ml-run"
 - "rocker-ml-verse-run"
 - "rserver"
 - "rserver-pam"
 - "rsession"
 - "rstudio-server"
versions:
 - "4.2.2"
 - "4.2.3"
 - "4.3.0"
description: "Machine learning in R."
config: {"docker": "rocker/ml-verse", "url": "https://hub.docker.com/r/rocker/ml-verse", "maintainer": "@vsoch", "description": "Machine learning in R.", "latest": {"4.3.0": "sha256:6673a533b6f1e845ed017ebd4236a7fe3fc2436980080531a0e4f5b19ed8474b"}, "tags": {"4.2.2": "sha256:1d29115bcea61dab7197c113209051518d666f936239f38a360f61ab752f8fa8", "4.2.3": "sha256:52a54e8f9dd1c1a8937ee2d3af38e3fdaa2a5cb11115c8d25f6e82986fa958de", "4.3.0": "sha256:6673a533b6f1e845ed017ebd4236a7fe3fc2436980080531a0e4f5b19ed8474b"}, "filter": ["^[0-9]+[.][0-9]+[.][0-9]+$"], "aliases": {"R": "/usr/local/bin/R", "Rscript": "/usr/local/bin/Rscript", "rocker-ml-run": "/bin/bash", "rocker-ml-verse-run": "/bin/bash", "rserver": "/usr/lib/rstudio-server/bin/rserver", "rserver-pam": "/usr/lib/rstudio-server/bin/rserver-pam", "rsession": "/usr/lib/rstudio-server/bin/rsession", "rstudio-server": "/usr/lib/rstudio-server/bin/rstudio-server"}}
---

This module is a singularity container wrapper for rocker/ml-verse.
Machine learning in R.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install rocker/ml-verse
```

Or a specific version:

```bash
$ shpc install rocker/ml-verse:4.3.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load rocker/ml-verse/4.3.0
$ module help rocker/ml-verse/4.3.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ml-verse-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ml-verse-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ml-verse-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ml-verse-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ml-verse-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ml-verse-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### R

```bash
$ singularity exec <container> /usr/local/bin/R
$ podman run --it --rm --entrypoint /usr/local/bin/R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Rscript

```bash
$ singularity exec <container> /usr/local/bin/Rscript
$ podman run --it --rm --entrypoint /usr/local/bin/Rscript   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Rscript   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rocker-ml-run

```bash
$ singularity exec <container> /bin/bash
$ podman run --it --rm --entrypoint /bin/bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /bin/bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rocker-ml-verse-run

```bash
$ singularity exec <container> /bin/bash
$ podman run --it --rm --entrypoint /bin/bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /bin/bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rserver

```bash
$ singularity exec <container> /usr/lib/rstudio-server/bin/rserver
$ podman run --it --rm --entrypoint /usr/lib/rstudio-server/bin/rserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/rstudio-server/bin/rserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rserver-pam

```bash
$ singularity exec <container> /usr/lib/rstudio-server/bin/rserver-pam
$ podman run --it --rm --entrypoint /usr/lib/rstudio-server/bin/rserver-pam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/rstudio-server/bin/rserver-pam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsession

```bash
$ singularity exec <container> /usr/lib/rstudio-server/bin/rsession
$ podman run --it --rm --entrypoint /usr/lib/rstudio-server/bin/rsession   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/rstudio-server/bin/rsession   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rstudio-server

```bash
$ singularity exec <container> /usr/lib/rstudio-server/bin/rstudio-server
$ podman run --it --rm --entrypoint /usr/lib/rstudio-server/bin/rstudio-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/rstudio-server/bin/rstudio-server   -v ${PWD} -w ${PWD} <container> -c " $@"
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