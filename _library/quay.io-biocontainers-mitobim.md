---
layout: container
name:  "quay.io/biocontainers/mitobim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mitobim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mitobim/container.yaml"
updated_at: "2024-10-18 03:37:35.464840"
latest: "1.9.1--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/mitobim"
aliases:
 - "MITObim.pl"
 - "circules.py"
 - "downsample.py"
 - "fasta2frag.tcl"
 - "fixACE4consed.tcl"
 - "get_wiggle.pl"
 - "interleave-fastqgz-MITOBIM.py"
 - "mira"
 - "mirabait"
 - "miraconvert"
 - "miramem"
 - "parsort"
 - "perl5.32.0"
 - "env_parallel"
 - "env_parallel.ash"
 - "env_parallel.bash"
 - "env_parallel.csh"
 - "env_parallel.dash"
 - "env_parallel.fish"
 - "env_parallel.ksh"
 - "env_parallel.mksh"
versions:
 - "1.9.1--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for mitobim"
config: {"url": "https://biocontainers.pro/tools/mitobim", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mitobim", "latest": {"1.9.1--hdfd78af_1": "sha256:0e64e7e086bb0c369747abd9871cae67d1163424da4c655d237b814f65d75968"}, "tags": {"1.9.1--hdfd78af_1": "sha256:0e64e7e086bb0c369747abd9871cae67d1163424da4c655d237b814f65d75968"}, "docker": "quay.io/biocontainers/mitobim", "aliases": {"MITObim.pl": "/usr/local/bin/MITObim.pl", "circules.py": "/usr/local/bin/circules.py", "downsample.py": "/usr/local/bin/downsample.py", "fasta2frag.tcl": "/usr/local/bin/fasta2frag.tcl", "fixACE4consed.tcl": "/usr/local/bin/fixACE4consed.tcl", "get_wiggle.pl": "/usr/local/bin/get_wiggle.pl", "interleave-fastqgz-MITOBIM.py": "/usr/local/bin/interleave-fastqgz-MITOBIM.py", "mira": "/usr/local/bin/mira", "mirabait": "/usr/local/bin/mirabait", "miraconvert": "/usr/local/bin/miraconvert", "miramem": "/usr/local/bin/miramem", "parsort": "/usr/local/bin/parsort", "perl5.32.0": "/usr/local/bin/perl5.32.0", "env_parallel": "/usr/local/bin/env_parallel", "env_parallel.ash": "/usr/local/bin/env_parallel.ash", "env_parallel.bash": "/usr/local/bin/env_parallel.bash", "env_parallel.csh": "/usr/local/bin/env_parallel.csh", "env_parallel.dash": "/usr/local/bin/env_parallel.dash", "env_parallel.fish": "/usr/local/bin/env_parallel.fish", "env_parallel.ksh": "/usr/local/bin/env_parallel.ksh", "env_parallel.mksh": "/usr/local/bin/env_parallel.mksh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mitobim.
shpc-registry automated BioContainers addition for mitobim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mitobim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mitobim:1.9.1--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mitobim/1.9.1--hdfd78af_1
$ module help quay.io/biocontainers/mitobim/1.9.1--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mitobim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mitobim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mitobim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mitobim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mitobim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mitobim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MITObim.pl

```bash
$ singularity exec <container> /usr/local/bin/MITObim.pl
$ podman run --it --rm --entrypoint /usr/local/bin/MITObim.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MITObim.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### circules.py

```bash
$ singularity exec <container> /usr/local/bin/circules.py
$ podman run --it --rm --entrypoint /usr/local/bin/circules.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/circules.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### downsample.py

```bash
$ singularity exec <container> /usr/local/bin/downsample.py
$ podman run --it --rm --entrypoint /usr/local/bin/downsample.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/downsample.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta2frag.tcl

```bash
$ singularity exec <container> /usr/local/bin/fasta2frag.tcl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta2frag.tcl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta2frag.tcl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fixACE4consed.tcl

```bash
$ singularity exec <container> /usr/local/bin/fixACE4consed.tcl
$ podman run --it --rm --entrypoint /usr/local/bin/fixACE4consed.tcl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fixACE4consed.tcl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_wiggle.pl

```bash
$ singularity exec <container> /usr/local/bin/get_wiggle.pl
$ podman run --it --rm --entrypoint /usr/local/bin/get_wiggle.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_wiggle.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interleave-fastqgz-MITOBIM.py

```bash
$ singularity exec <container> /usr/local/bin/interleave-fastqgz-MITOBIM.py
$ podman run --it --rm --entrypoint /usr/local/bin/interleave-fastqgz-MITOBIM.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interleave-fastqgz-MITOBIM.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mira

```bash
$ singularity exec <container> /usr/local/bin/mira
$ podman run --it --rm --entrypoint /usr/local/bin/mira   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mira   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mirabait

```bash
$ singularity exec <container> /usr/local/bin/mirabait
$ podman run --it --rm --entrypoint /usr/local/bin/mirabait   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mirabait   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### miraconvert

```bash
$ singularity exec <container> /usr/local/bin/miraconvert
$ podman run --it --rm --entrypoint /usr/local/bin/miraconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miraconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### miramem

```bash
$ singularity exec <container> /usr/local/bin/miramem
$ podman run --it --rm --entrypoint /usr/local/bin/miramem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miramem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parsort

```bash
$ singularity exec <container> /usr/local/bin/parsort
$ podman run --it --rm --entrypoint /usr/local/bin/parsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
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