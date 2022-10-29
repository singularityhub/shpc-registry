---
layout: container
name:  "quay.io/biocontainers/grid"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/grid/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/grid/container.yaml"
updated_at: "2022-10-29 05:46:39.304724"
latest: "1.3--hdfd78af_3"
container_url: "https://biocontainers.pro/tools/grid"
aliases:
 - "grid"
 - "mosdepth"
 - "pathoscope"
 - "update_database"
 - "CA.pm"
 - "accn-at-a-time"
 - "amino-acid-composition"
 - "annotateBed"
 - "archive-pubmed"
 - "asp-cp"
 - "asp-ls"
 - "bamToBed"
 - "bamToFastq"
 - "bamtools"
versions:
 - "1.3--hdfd78af_3"
description: "shpc-registry automated BioContainers addition for grid"
config: {"url": "https://biocontainers.pro/tools/grid", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for grid", "latest": {"1.3--hdfd78af_3": "sha256:e46fd424a12bdcb86f8e98ee81cc03ba46cdcf7fcffb34b4451390b451d82b6d"}, "tags": {"1.3--hdfd78af_3": "sha256:e46fd424a12bdcb86f8e98ee81cc03ba46cdcf7fcffb34b4451390b451d82b6d"}, "docker": "quay.io/biocontainers/grid", "aliases": {"grid": "/usr/local/bin/grid", "mosdepth": "/usr/local/bin/mosdepth", "pathoscope": "/usr/local/bin/pathoscope", "update_database": "/usr/local/bin/update_database", "CA.pm": "/usr/local/bin/CA.pm", "accn-at-a-time": "/usr/local/bin/accn-at-a-time", "amino-acid-composition": "/usr/local/bin/amino-acid-composition", "annotateBed": "/usr/local/bin/annotateBed", "archive-pubmed": "/usr/local/bin/archive-pubmed", "asp-cp": "/usr/local/bin/asp-cp", "asp-ls": "/usr/local/bin/asp-ls", "bamToBed": "/usr/local/bin/bamToBed", "bamToFastq": "/usr/local/bin/bamToFastq", "bamtools": "/usr/local/bin/bamtools"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/grid.
shpc-registry automated BioContainers addition for grid
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/grid
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/grid:1.3--hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/grid/1.3--hdfd78af_3
$ module help quay.io/biocontainers/grid/1.3--hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### grid-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### grid-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### grid-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### grid-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### grid-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### grid-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### grid

```bash
$ singularity exec <container> /usr/local/bin/grid
$ podman run --it --rm --entrypoint /usr/local/bin/grid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mosdepth

```bash
$ singularity exec <container> /usr/local/bin/mosdepth
$ podman run --it --rm --entrypoint /usr/local/bin/mosdepth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mosdepth   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pathoscope

```bash
$ singularity exec <container> /usr/local/bin/pathoscope
$ podman run --it --rm --entrypoint /usr/local/bin/pathoscope   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pathoscope   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### update_database

```bash
$ singularity exec <container> /usr/local/bin/update_database
$ podman run --it --rm --entrypoint /usr/local/bin/update_database   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/update_database   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CA.pm

```bash
$ singularity exec <container> /usr/local/bin/CA.pm
$ podman run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### accn-at-a-time

```bash
$ singularity exec <container> /usr/local/bin/accn-at-a-time
$ podman run --it --rm --entrypoint /usr/local/bin/accn-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/accn-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amino-acid-composition

```bash
$ singularity exec <container> /usr/local/bin/amino-acid-composition
$ podman run --it --rm --entrypoint /usr/local/bin/amino-acid-composition   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amino-acid-composition   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotateBed

```bash
$ singularity exec <container> /usr/local/bin/annotateBed
$ podman run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-pubmed

```bash
$ singularity exec <container> /usr/local/bin/archive-pubmed
$ podman run --it --rm --entrypoint /usr/local/bin/archive-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asp-cp

```bash
$ singularity exec <container> /usr/local/bin/asp-cp
$ podman run --it --rm --entrypoint /usr/local/bin/asp-cp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asp-cp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asp-ls

```bash
$ singularity exec <container> /usr/local/bin/asp-ls
$ podman run --it --rm --entrypoint /usr/local/bin/asp-ls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asp-ls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToBed

```bash
$ singularity exec <container> /usr/local/bin/bamToBed
$ podman run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToFastq

```bash
$ singularity exec <container> /usr/local/bin/bamToFastq
$ podman run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamtools

```bash
$ singularity exec <container> /usr/local/bin/bamtools
$ podman run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
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