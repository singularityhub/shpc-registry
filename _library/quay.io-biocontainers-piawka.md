---
layout: container
name:  "quay.io/biocontainers/piawka"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/piawka/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/piawka/container.yaml"
updated_at: "2024-12-03 04:38:53.093345"
latest: "0.8.8--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/piawka"
aliases:
 - "aggregate_regions.awk"
 - "bash"
 - "bashbug"
 - "mawk"
 - "piawka"
 - "piawka_par.sh"
 - "summarize_blks.awk"
 - "annot-tsv"
 - "parsort"
 - "env_parallel"
 - "env_parallel.ash"
 - "env_parallel.bash"
 - "env_parallel.csh"
 - "env_parallel.dash"
 - "env_parallel.fish"
 - "env_parallel.ksh"
 - "env_parallel.mksh"
 - "env_parallel.pdksh"
 - "env_parallel.sh"
 - "env_parallel.tcsh"
 - "env_parallel.zsh"
 - "niceload"
 - "parcat"
 - "parset"
 - "sem"
 - "sql"
 - "parallel"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.7.10--hdfd78af_0"
 - "0.8.8--hdfd78af_0"
description: "singularity registry hpc automated addition for piawka"
config: {"url": "https://biocontainers.pro/tools/piawka", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for piawka", "latest": {"0.8.8--hdfd78af_0": "sha256:67ea298a691a4a216224357c93cb4e20450318e256bc5e3b81d7f99c6ee27cd0"}, "tags": {"0.7.10--hdfd78af_0": "sha256:d29ebab4fe7aa9adbb0aaa33d7d3ccb9db02df435046de568238e185f21e70db", "0.8.8--hdfd78af_0": "sha256:67ea298a691a4a216224357c93cb4e20450318e256bc5e3b81d7f99c6ee27cd0"}, "docker": "quay.io/biocontainers/piawka", "aliases": {"aggregate_regions.awk": "/usr/local/bin/aggregate_regions.awk", "bash": "/usr/local/bin/bash", "bashbug": "/usr/local/bin/bashbug", "mawk": "/usr/local/bin/mawk", "piawka": "/usr/local/bin/piawka", "piawka_par.sh": "/usr/local/bin/piawka_par.sh", "summarize_blks.awk": "/usr/local/bin/summarize_blks.awk", "annot-tsv": "/usr/local/bin/annot-tsv", "parsort": "/usr/local/bin/parsort", "env_parallel": "/usr/local/bin/env_parallel", "env_parallel.ash": "/usr/local/bin/env_parallel.ash", "env_parallel.bash": "/usr/local/bin/env_parallel.bash", "env_parallel.csh": "/usr/local/bin/env_parallel.csh", "env_parallel.dash": "/usr/local/bin/env_parallel.dash", "env_parallel.fish": "/usr/local/bin/env_parallel.fish", "env_parallel.ksh": "/usr/local/bin/env_parallel.ksh", "env_parallel.mksh": "/usr/local/bin/env_parallel.mksh", "env_parallel.pdksh": "/usr/local/bin/env_parallel.pdksh", "env_parallel.sh": "/usr/local/bin/env_parallel.sh", "env_parallel.tcsh": "/usr/local/bin/env_parallel.tcsh", "env_parallel.zsh": "/usr/local/bin/env_parallel.zsh", "niceload": "/usr/local/bin/niceload", "parcat": "/usr/local/bin/parcat", "parset": "/usr/local/bin/parset", "sem": "/usr/local/bin/sem", "sql": "/usr/local/bin/sql", "parallel": "/usr/local/bin/parallel", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/piawka.
singularity registry hpc automated addition for piawka
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/piawka
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/piawka:0.8.8--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/piawka/0.8.8--hdfd78af_0
$ module help quay.io/biocontainers/piawka/0.8.8--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### piawka-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### piawka-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### piawka-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### piawka-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### piawka-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### piawka-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aggregate_regions.awk

```bash
$ singularity exec <container> /usr/local/bin/aggregate_regions.awk
$ podman run --it --rm --entrypoint /usr/local/bin/aggregate_regions.awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aggregate_regions.awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bash

```bash
$ singularity exec <container> /usr/local/bin/bash
$ podman run --it --rm --entrypoint /usr/local/bin/bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bashbug

```bash
$ singularity exec <container> /usr/local/bin/bashbug
$ podman run --it --rm --entrypoint /usr/local/bin/bashbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bashbug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mawk

```bash
$ singularity exec <container> /usr/local/bin/mawk
$ podman run --it --rm --entrypoint /usr/local/bin/mawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mawk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### piawka

```bash
$ singularity exec <container> /usr/local/bin/piawka
$ podman run --it --rm --entrypoint /usr/local/bin/piawka   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/piawka   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### piawka_par.sh

```bash
$ singularity exec <container> /usr/local/bin/piawka_par.sh
$ podman run --it --rm --entrypoint /usr/local/bin/piawka_par.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/piawka_par.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### summarize_blks.awk

```bash
$ singularity exec <container> /usr/local/bin/summarize_blks.awk
$ podman run --it --rm --entrypoint /usr/local/bin/summarize_blks.awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/summarize_blks.awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parsort

```bash
$ singularity exec <container> /usr/local/bin/parsort
$ podman run --it --rm --entrypoint /usr/local/bin/parsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel

```bash
$ singularity exec <container> /usr/local/bin/env_parallel
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.ash

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.ash
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.ash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.ash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.bash

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.bash
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.csh

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.csh
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.dash

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.dash
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.dash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.dash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.fish

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.fish
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.fish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.fish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.ksh

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.ksh
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.ksh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.ksh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.mksh

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.mksh
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.mksh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.mksh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.pdksh

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.pdksh
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.pdksh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.pdksh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.sh

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.sh
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.tcsh

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.tcsh
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.tcsh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.tcsh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.zsh

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.zsh
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.zsh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.zsh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### niceload

```bash
$ singularity exec <container> /usr/local/bin/niceload
$ podman run --it --rm --entrypoint /usr/local/bin/niceload   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/niceload   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parcat

```bash
$ singularity exec <container> /usr/local/bin/parcat
$ podman run --it --rm --entrypoint /usr/local/bin/parcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parset

```bash
$ singularity exec <container> /usr/local/bin/parset
$ podman run --it --rm --entrypoint /usr/local/bin/parset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sem

```bash
$ singularity exec <container> /usr/local/bin/sem
$ podman run --it --rm --entrypoint /usr/local/bin/sem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sql

```bash
$ singularity exec <container> /usr/local/bin/sql
$ podman run --it --rm --entrypoint /usr/local/bin/sql   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sql   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parallel

```bash
$ singularity exec <container> /usr/local/bin/parallel
$ podman run --it --rm --entrypoint /usr/local/bin/parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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