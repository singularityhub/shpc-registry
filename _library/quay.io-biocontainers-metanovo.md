---
layout: container
name:  "quay.io/biocontainers/metanovo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metanovo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metanovo/container.yaml"
updated_at: "2025-03-02 03:05:07.201523"
latest: "1.9.4"
container_url: "https://biocontainers.pro/tools/metanovo"
aliases:
 - "bp_export_proteins.py"
 - "bp_export_tags.py"
 - "bp_fasta_prepare.py"
 - "bp_mapped_tags.py"
 - "bp_parse_tags.py"
 - "compomics.sh"
 - "flex"
 - "flex++"
 - "m4"
 - "metanovo.sh"
 - "bc"
 - "dc"
 - "clhsdb"
 - "hsdb"
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
 - "extcheck"
 - "java-rmi.cgi"
versions:
 - "1.9.4--py39h9ee0642_5"
 - "1.9.4"
 - "1.9.4--py39h9ee0642_8"
 - "1.9.4--py39h9ee0642_9"
description: "singularity registry hpc automated addition for metanovo"
config: {"url": "https://biocontainers.pro/tools/metanovo", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for metanovo", "latest": {"1.9.4": "sha256:83ef7e4898dd776f3930ca7671ed1c6ec6a5befb03e798dedcda5b946f88e7ed"}, "tags": {"1.9.4--py39h9ee0642_5": "sha256:fe8c5c651660faf9b3bdeb4265c0c76d7429607d0df9919086351d0c5eadbad6", "1.9.4": "sha256:83ef7e4898dd776f3930ca7671ed1c6ec6a5befb03e798dedcda5b946f88e7ed", "1.9.4--py39h9ee0642_8": "sha256:74a13887172a475ac4f9fe92f39c7f41fa0fb59e2fe87d031ac292ea93387874", "1.9.4--py39h9ee0642_9": "sha256:39ba8ee745964b067027ec43c60df32b73e0e819ab7e09f097b3123c7ad3054d"}, "docker": "quay.io/biocontainers/metanovo", "aliases": {"bp_export_proteins.py": "/usr/local/bin/bp_export_proteins.py", "bp_export_tags.py": "/usr/local/bin/bp_export_tags.py", "bp_fasta_prepare.py": "/usr/local/bin/bp_fasta_prepare.py", "bp_mapped_tags.py": "/usr/local/bin/bp_mapped_tags.py", "bp_parse_tags.py": "/usr/local/bin/bp_parse_tags.py", "compomics.sh": "/usr/local/bin/compomics.sh", "flex": "/usr/local/bin/flex", "flex++": "/usr/local/bin/flex++", "m4": "/usr/local/bin/m4", "metanovo.sh": "/usr/local/bin/metanovo.sh", "bc": "/usr/local/bin/bc", "dc": "/usr/local/bin/dc", "clhsdb": "/usr/local/bin/clhsdb", "hsdb": "/usr/local/bin/hsdb", "parsort": "/usr/local/bin/parsort", "env_parallel": "/usr/local/bin/env_parallel", "env_parallel.ash": "/usr/local/bin/env_parallel.ash", "env_parallel.bash": "/usr/local/bin/env_parallel.bash", "env_parallel.csh": "/usr/local/bin/env_parallel.csh", "env_parallel.dash": "/usr/local/bin/env_parallel.dash", "env_parallel.fish": "/usr/local/bin/env_parallel.fish", "env_parallel.ksh": "/usr/local/bin/env_parallel.ksh", "env_parallel.mksh": "/usr/local/bin/env_parallel.mksh", "env_parallel.pdksh": "/usr/local/bin/env_parallel.pdksh", "env_parallel.sh": "/usr/local/bin/env_parallel.sh", "env_parallel.tcsh": "/usr/local/bin/env_parallel.tcsh", "env_parallel.zsh": "/usr/local/bin/env_parallel.zsh", "niceload": "/usr/local/bin/niceload", "parcat": "/usr/local/bin/parcat", "parset": "/usr/local/bin/parset", "sem": "/usr/local/bin/sem", "sql": "/usr/local/bin/sql", "parallel": "/usr/local/bin/parallel", "extcheck": "/usr/local/bin/extcheck", "java-rmi.cgi": "/usr/local/bin/java-rmi.cgi"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metanovo.
singularity registry hpc automated addition for metanovo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metanovo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metanovo:1.9.4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metanovo/1.9.4
$ module help quay.io/biocontainers/metanovo/1.9.4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metanovo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metanovo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metanovo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metanovo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metanovo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metanovo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bp_export_proteins.py

```bash
$ singularity exec <container> /usr/local/bin/bp_export_proteins.py
$ podman run --it --rm --entrypoint /usr/local/bin/bp_export_proteins.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_export_proteins.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_export_tags.py

```bash
$ singularity exec <container> /usr/local/bin/bp_export_tags.py
$ podman run --it --rm --entrypoint /usr/local/bin/bp_export_tags.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_export_tags.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_fasta_prepare.py

```bash
$ singularity exec <container> /usr/local/bin/bp_fasta_prepare.py
$ podman run --it --rm --entrypoint /usr/local/bin/bp_fasta_prepare.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_fasta_prepare.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_mapped_tags.py

```bash
$ singularity exec <container> /usr/local/bin/bp_mapped_tags.py
$ podman run --it --rm --entrypoint /usr/local/bin/bp_mapped_tags.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_mapped_tags.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_parse_tags.py

```bash
$ singularity exec <container> /usr/local/bin/bp_parse_tags.py
$ podman run --it --rm --entrypoint /usr/local/bin/bp_parse_tags.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_parse_tags.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compomics.sh

```bash
$ singularity exec <container> /usr/local/bin/compomics.sh
$ podman run --it --rm --entrypoint /usr/local/bin/compomics.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compomics.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flex

```bash
$ singularity exec <container> /usr/local/bin/flex
$ podman run --it --rm --entrypoint /usr/local/bin/flex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flex++

```bash
$ singularity exec <container> /usr/local/bin/flex++
$ podman run --it --rm --entrypoint /usr/local/bin/flex++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flex++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### m4

```bash
$ singularity exec <container> /usr/local/bin/m4
$ podman run --it --rm --entrypoint /usr/local/bin/m4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/m4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metanovo.sh

```bash
$ singularity exec <container> /usr/local/bin/metanovo.sh
$ podman run --it --rm --entrypoint /usr/local/bin/metanovo.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metanovo.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bc

```bash
$ singularity exec <container> /usr/local/bin/bc
$ podman run --it --rm --entrypoint /usr/local/bin/bc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dc

```bash
$ singularity exec <container> /usr/local/bin/dc
$ podman run --it --rm --entrypoint /usr/local/bin/dc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clhsdb

```bash
$ singularity exec <container> /usr/local/bin/clhsdb
$ podman run --it --rm --entrypoint /usr/local/bin/clhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hsdb

```bash
$ singularity exec <container> /usr/local/bin/hsdb
$ podman run --it --rm --entrypoint /usr/local/bin/hsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### extcheck

```bash
$ singularity exec <container> /usr/local/bin/extcheck
$ podman run --it --rm --entrypoint /usr/local/bin/extcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### java-rmi.cgi

```bash
$ singularity exec <container> /usr/local/bin/java-rmi.cgi
$ podman run --it --rm --entrypoint /usr/local/bin/java-rmi.cgi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/java-rmi.cgi   -v ${PWD} -w ${PWD} <container> -c " $@"
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