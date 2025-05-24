---
layout: container
name:  "quay.io/biocontainers/peregrine-2021"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/peregrine-2021/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/peregrine-2021/container.yaml"
updated_at: "2025-05-24 03:38:01.826458"
latest: "0.4.13--h503566f_4"
container_url: "https://biocontainers.pro/tools/peregrine-2021"
aliases:
 - "pg_asm"
 - "pg_build_idx"
 - "pg_build_sdb"
 - "pg_dedup"
 - "pg_dp_graph"
 - "pg_getreads"
 - "pg_graph"
 - "pg_layout"
 - "pg_ovlp"
 - "pg_ovlp_ec"
 - "pg_resolve"
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
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.4.13--h87f3376_1"
 - "0.4.13--hdbdd923_3"
 - "0.4.13--h503566f_4"
description: "singularity registry hpc automated addition for peregrine-2021"
config: {"url": "https://biocontainers.pro/tools/peregrine-2021", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for peregrine-2021", "latest": {"0.4.13--h503566f_4": "sha256:d1d08b08d89133bc42bd524c06187540023460d52d8a5ac49f25ec8e84723141"}, "tags": {"0.4.13--h87f3376_1": "sha256:8bc7ced847c021c7e82739362ac30b2a7bb91c2806dc95c8c0d91d8356cc3a15", "0.4.13--hdbdd923_3": "sha256:e4b5868ebffc3f5deeb75225cff3eb8df10692885123be140889a1d3ffa2868e", "0.4.13--h503566f_4": "sha256:d1d08b08d89133bc42bd524c06187540023460d52d8a5ac49f25ec8e84723141"}, "docker": "quay.io/biocontainers/peregrine-2021", "aliases": {"pg_asm": "/usr/local/bin/pg_asm", "pg_build_idx": "/usr/local/bin/pg_build_idx", "pg_build_sdb": "/usr/local/bin/pg_build_sdb", "pg_dedup": "/usr/local/bin/pg_dedup", "pg_dp_graph": "/usr/local/bin/pg_dp_graph", "pg_getreads": "/usr/local/bin/pg_getreads", "pg_graph": "/usr/local/bin/pg_graph", "pg_layout": "/usr/local/bin/pg_layout", "pg_ovlp": "/usr/local/bin/pg_ovlp", "pg_ovlp_ec": "/usr/local/bin/pg_ovlp_ec", "pg_resolve": "/usr/local/bin/pg_resolve", "parsort": "/usr/local/bin/parsort", "env_parallel": "/usr/local/bin/env_parallel", "env_parallel.ash": "/usr/local/bin/env_parallel.ash", "env_parallel.bash": "/usr/local/bin/env_parallel.bash", "env_parallel.csh": "/usr/local/bin/env_parallel.csh", "env_parallel.dash": "/usr/local/bin/env_parallel.dash", "env_parallel.fish": "/usr/local/bin/env_parallel.fish", "env_parallel.ksh": "/usr/local/bin/env_parallel.ksh", "env_parallel.mksh": "/usr/local/bin/env_parallel.mksh", "env_parallel.pdksh": "/usr/local/bin/env_parallel.pdksh", "env_parallel.sh": "/usr/local/bin/env_parallel.sh", "env_parallel.tcsh": "/usr/local/bin/env_parallel.tcsh", "env_parallel.zsh": "/usr/local/bin/env_parallel.zsh", "niceload": "/usr/local/bin/niceload", "parcat": "/usr/local/bin/parcat", "parset": "/usr/local/bin/parset", "sem": "/usr/local/bin/sem", "sql": "/usr/local/bin/sql", "parallel": "/usr/local/bin/parallel", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/peregrine-2021.
singularity registry hpc automated addition for peregrine-2021
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/peregrine-2021
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/peregrine-2021:0.4.13--h503566f_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/peregrine-2021/0.4.13--h503566f_4
$ module help quay.io/biocontainers/peregrine-2021/0.4.13--h503566f_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### peregrine-2021-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### peregrine-2021-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### peregrine-2021-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### peregrine-2021-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### peregrine-2021-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### peregrine-2021-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pg_asm

```bash
$ singularity exec <container> /usr/local/bin/pg_asm
$ podman run --it --rm --entrypoint /usr/local/bin/pg_asm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_asm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_build_idx

```bash
$ singularity exec <container> /usr/local/bin/pg_build_idx
$ podman run --it --rm --entrypoint /usr/local/bin/pg_build_idx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_build_idx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_build_sdb

```bash
$ singularity exec <container> /usr/local/bin/pg_build_sdb
$ podman run --it --rm --entrypoint /usr/local/bin/pg_build_sdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_build_sdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_dedup

```bash
$ singularity exec <container> /usr/local/bin/pg_dedup
$ podman run --it --rm --entrypoint /usr/local/bin/pg_dedup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_dedup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_dp_graph

```bash
$ singularity exec <container> /usr/local/bin/pg_dp_graph
$ podman run --it --rm --entrypoint /usr/local/bin/pg_dp_graph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_dp_graph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_getreads

```bash
$ singularity exec <container> /usr/local/bin/pg_getreads
$ podman run --it --rm --entrypoint /usr/local/bin/pg_getreads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_getreads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_graph

```bash
$ singularity exec <container> /usr/local/bin/pg_graph
$ podman run --it --rm --entrypoint /usr/local/bin/pg_graph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_graph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_layout

```bash
$ singularity exec <container> /usr/local/bin/pg_layout
$ podman run --it --rm --entrypoint /usr/local/bin/pg_layout   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_layout   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_ovlp

```bash
$ singularity exec <container> /usr/local/bin/pg_ovlp
$ podman run --it --rm --entrypoint /usr/local/bin/pg_ovlp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_ovlp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_ovlp_ec

```bash
$ singularity exec <container> /usr/local/bin/pg_ovlp_ec
$ podman run --it --rm --entrypoint /usr/local/bin/pg_ovlp_ec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_ovlp_ec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_resolve

```bash
$ singularity exec <container> /usr/local/bin/pg_resolve
$ podman run --it --rm --entrypoint /usr/local/bin/pg_resolve   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_resolve   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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