---
layout: container
name:  "quay.io/biocontainers/integron_finder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/integron_finder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/integron_finder/container.yaml"
updated_at: "2025-04-21 03:36:11.422956"
latest: "2.0rc6--py_0"
container_url: "https://biocontainers.pro/tools/integron_finder"
aliases:
 - "integron_finder"
 - "integron_merge"
 - "integron_split"
 - "cmalign"
 - "cmbuild"
 - "cmcalibrate"
 - "cmconvert"
 - "cmemit"
 - "cmfetch"
 - "cmpress"
 - "cmscan"
 - "cmsearch"
 - "cmstat"
versions:
 - "2.0rc6--py_0"
description: "shpc-registry automated BioContainers addition for integron_finder"
config: {"url": "https://biocontainers.pro/tools/integron_finder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for integron_finder", "latest": {"2.0rc6--py_0": "sha256:d8142e6e03ddb12d02be189e62846803eee97161ca396125af83e33158d119dd"}, "tags": {"2.0rc6--py_0": "sha256:d8142e6e03ddb12d02be189e62846803eee97161ca396125af83e33158d119dd"}, "docker": "quay.io/biocontainers/integron_finder", "aliases": {"integron_finder": "/usr/local/bin/integron_finder", "integron_merge": "/usr/local/bin/integron_merge", "integron_split": "/usr/local/bin/integron_split", "cmalign": "/usr/local/bin/cmalign", "cmbuild": "/usr/local/bin/cmbuild", "cmcalibrate": "/usr/local/bin/cmcalibrate", "cmconvert": "/usr/local/bin/cmconvert", "cmemit": "/usr/local/bin/cmemit", "cmfetch": "/usr/local/bin/cmfetch", "cmpress": "/usr/local/bin/cmpress", "cmscan": "/usr/local/bin/cmscan", "cmsearch": "/usr/local/bin/cmsearch", "cmstat": "/usr/local/bin/cmstat"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/integron_finder.
shpc-registry automated BioContainers addition for integron_finder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/integron_finder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/integron_finder:2.0rc6--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/integron_finder/2.0rc6--py_0
$ module help quay.io/biocontainers/integron_finder/2.0rc6--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### integron_finder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### integron_finder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### integron_finder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### integron_finder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### integron_finder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### integron_finder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### integron_finder

```bash
$ singularity exec <container> /usr/local/bin/integron_finder
$ podman run --it --rm --entrypoint /usr/local/bin/integron_finder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/integron_finder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### integron_merge

```bash
$ singularity exec <container> /usr/local/bin/integron_merge
$ podman run --it --rm --entrypoint /usr/local/bin/integron_merge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/integron_merge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### integron_split

```bash
$ singularity exec <container> /usr/local/bin/integron_split
$ podman run --it --rm --entrypoint /usr/local/bin/integron_split   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/integron_split   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmalign

```bash
$ singularity exec <container> /usr/local/bin/cmalign
$ podman run --it --rm --entrypoint /usr/local/bin/cmalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmbuild

```bash
$ singularity exec <container> /usr/local/bin/cmbuild
$ podman run --it --rm --entrypoint /usr/local/bin/cmbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmcalibrate

```bash
$ singularity exec <container> /usr/local/bin/cmcalibrate
$ podman run --it --rm --entrypoint /usr/local/bin/cmcalibrate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmcalibrate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmconvert

```bash
$ singularity exec <container> /usr/local/bin/cmconvert
$ podman run --it --rm --entrypoint /usr/local/bin/cmconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmemit

```bash
$ singularity exec <container> /usr/local/bin/cmemit
$ podman run --it --rm --entrypoint /usr/local/bin/cmemit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmemit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmfetch

```bash
$ singularity exec <container> /usr/local/bin/cmfetch
$ podman run --it --rm --entrypoint /usr/local/bin/cmfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmpress

```bash
$ singularity exec <container> /usr/local/bin/cmpress
$ podman run --it --rm --entrypoint /usr/local/bin/cmpress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmpress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmscan

```bash
$ singularity exec <container> /usr/local/bin/cmscan
$ podman run --it --rm --entrypoint /usr/local/bin/cmscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmsearch

```bash
$ singularity exec <container> /usr/local/bin/cmsearch
$ podman run --it --rm --entrypoint /usr/local/bin/cmsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmstat

```bash
$ singularity exec <container> /usr/local/bin/cmstat
$ podman run --it --rm --entrypoint /usr/local/bin/cmstat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmstat   -v ${PWD} -w ${PWD} <container> -c " $@"
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