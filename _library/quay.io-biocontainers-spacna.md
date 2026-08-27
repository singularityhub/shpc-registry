---
layout: container
name:  "quay.io/biocontainers/spacna"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/spacna/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/spacna/container.yaml"
updated_at: "2026-08-27 23:28:11.121780"
latest: "0.1.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/spacna"
aliases:
 - "axis-dna"
 - "bigWigAverageOverBed"
 - "mosdepth"
 - "seq_cache_populate.py"
 - "spacna"
 - "umi_tools"
 - "trim_galore"
 - "fastp"
 - "fc-genconf"
 - "seqkit"
 - "parsort"
 - "my_print_defaults"
 - "mysql_config"
 - "perror"
 - "igzip"
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
versions:
 - "0.1.0--hdfd78af_0"
description: "singularity registry hpc automated addition for spacna"
config: {"url": "https://biocontainers.pro/tools/spacna", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for spacna", "latest": {"0.1.0--hdfd78af_0": "sha256:e869bb70e3765e1e992be6c4d9c7eeefb670eb13d71706ad9aa9457884cc0abf"}, "tags": {"0.1.0--hdfd78af_0": "sha256:e869bb70e3765e1e992be6c4d9c7eeefb670eb13d71706ad9aa9457884cc0abf"}, "docker": "quay.io/biocontainers/spacna", "aliases": {"axis-dna": "/usr/local/bin/axis-dna", "bigWigAverageOverBed": "/usr/local/bin/bigWigAverageOverBed", "mosdepth": "/usr/local/bin/mosdepth", "seq_cache_populate.py": "/usr/local/bin/seq_cache_populate.py", "spacna": "/usr/local/bin/spacna", "umi_tools": "/usr/local/bin/umi_tools", "trim_galore": "/usr/local/bin/trim_galore", "fastp": "/usr/local/bin/fastp", "fc-genconf": "/usr/local/bin/fc-genconf", "seqkit": "/usr/local/bin/seqkit", "parsort": "/usr/local/bin/parsort", "my_print_defaults": "/usr/local/bin/my_print_defaults", "mysql_config": "/usr/local/bin/mysql_config", "perror": "/usr/local/bin/perror", "igzip": "/usr/local/bin/igzip", "env_parallel": "/usr/local/bin/env_parallel", "env_parallel.ash": "/usr/local/bin/env_parallel.ash", "env_parallel.bash": "/usr/local/bin/env_parallel.bash", "env_parallel.csh": "/usr/local/bin/env_parallel.csh", "env_parallel.dash": "/usr/local/bin/env_parallel.dash", "env_parallel.fish": "/usr/local/bin/env_parallel.fish", "env_parallel.ksh": "/usr/local/bin/env_parallel.ksh", "env_parallel.mksh": "/usr/local/bin/env_parallel.mksh", "env_parallel.pdksh": "/usr/local/bin/env_parallel.pdksh", "env_parallel.sh": "/usr/local/bin/env_parallel.sh", "env_parallel.tcsh": "/usr/local/bin/env_parallel.tcsh", "env_parallel.zsh": "/usr/local/bin/env_parallel.zsh", "niceload": "/usr/local/bin/niceload", "parcat": "/usr/local/bin/parcat", "parset": "/usr/local/bin/parset", "sem": "/usr/local/bin/sem"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/spacna.
singularity registry hpc automated addition for spacna
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/spacna
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/spacna:0.1.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/spacna/0.1.0--hdfd78af_0
$ module help quay.io/biocontainers/spacna/0.1.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### spacna-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### spacna-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### spacna-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### spacna-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### spacna-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### spacna-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### axis-dna

```bash
$ singularity exec <container> /usr/local/bin/axis-dna
$ podman run --it --rm --entrypoint /usr/local/bin/axis-dna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/axis-dna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigWigAverageOverBed

```bash
$ singularity exec <container> /usr/local/bin/bigWigAverageOverBed
$ podman run --it --rm --entrypoint /usr/local/bin/bigWigAverageOverBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigWigAverageOverBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mosdepth

```bash
$ singularity exec <container> /usr/local/bin/mosdepth
$ podman run --it --rm --entrypoint /usr/local/bin/mosdepth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mosdepth   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seq_cache_populate.py

```bash
$ singularity exec <container> /usr/local/bin/seq_cache_populate.py
$ podman run --it --rm --entrypoint /usr/local/bin/seq_cache_populate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seq_cache_populate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spacna

```bash
$ singularity exec <container> /usr/local/bin/spacna
$ podman run --it --rm --entrypoint /usr/local/bin/spacna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spacna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### umi_tools

```bash
$ singularity exec <container> /usr/local/bin/umi_tools
$ podman run --it --rm --entrypoint /usr/local/bin/umi_tools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/umi_tools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trim_galore

```bash
$ singularity exec <container> /usr/local/bin/trim_galore
$ podman run --it --rm --entrypoint /usr/local/bin/trim_galore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trim_galore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastp

```bash
$ singularity exec <container> /usr/local/bin/fastp
$ podman run --it --rm --entrypoint /usr/local/bin/fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-genconf

```bash
$ singularity exec <container> /usr/local/bin/fc-genconf
$ podman run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqkit

```bash
$ singularity exec <container> /usr/local/bin/seqkit
$ podman run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parsort

```bash
$ singularity exec <container> /usr/local/bin/parsort
$ podman run --it --rm --entrypoint /usr/local/bin/parsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### my_print_defaults

```bash
$ singularity exec <container> /usr/local/bin/my_print_defaults
$ podman run --it --rm --entrypoint /usr/local/bin/my_print_defaults   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/my_print_defaults   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_config

```bash
$ singularity exec <container> /usr/local/bin/mysql_config
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perror

```bash
$ singularity exec <container> /usr/local/bin/perror
$ podman run --it --rm --entrypoint /usr/local/bin/perror   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perror   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igzip

```bash
$ singularity exec <container> /usr/local/bin/igzip
$ podman run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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