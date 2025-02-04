---
layout: container
name:  "quay.io/biocontainers/perl-hpc-runner-slurm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-hpc-runner-slurm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-hpc-runner-slurm/container.yaml"
updated_at: "2025-02-04 03:10:41.760860"
latest: "2.58--2"
container_url: "https://biocontainers.pro/tools/perl-hpc-runner-slurm"
aliases:
 - "cpus.in"
 - "cpus.pl"
 - "mcerunner.pl"
 - "slurmrunner.pl"
 - "slurmrunnerbasic.pl"
 - "slurmrunnerrsyslog.pl"
 - "testnodes.pl"
 - "findrule"
 - "l4p-tmpl"
 - "config_data"
 - "perl5.22.0"
 - "c2ph"
 - "pstruct"
 - "imgsize"
 - "tpage"
 - "ttree"
 - "dbilogstrip"
versions:
 - "2.58--2"
description: "shpc-registry automated BioContainers addition for perl-hpc-runner-slurm"
config: {"url": "https://biocontainers.pro/tools/perl-hpc-runner-slurm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-hpc-runner-slurm", "latest": {"2.58--2": "sha256:f06b6fb49dd0c3b321614272b586e29af558cd354837e6b03b07096e872ffd9e"}, "tags": {"2.58--2": "sha256:f06b6fb49dd0c3b321614272b586e29af558cd354837e6b03b07096e872ffd9e"}, "docker": "quay.io/biocontainers/perl-hpc-runner-slurm", "aliases": {"cpus.in": "/usr/local/bin/cpus.in", "cpus.pl": "/usr/local/bin/cpus.pl", "mcerunner.pl": "/usr/local/bin/mcerunner.pl", "slurmrunner.pl": "/usr/local/bin/slurmrunner.pl", "slurmrunnerbasic.pl": "/usr/local/bin/slurmrunnerbasic.pl", "slurmrunnerrsyslog.pl": "/usr/local/bin/slurmrunnerrsyslog.pl", "testnodes.pl": "/usr/local/bin/testnodes.pl", "findrule": "/usr/local/bin/findrule", "l4p-tmpl": "/usr/local/bin/l4p-tmpl", "config_data": "/usr/local/bin/config_data", "perl5.22.0": "/usr/local/bin/perl5.22.0", "c2ph": "/usr/local/bin/c2ph", "pstruct": "/usr/local/bin/pstruct", "imgsize": "/usr/local/bin/imgsize", "tpage": "/usr/local/bin/tpage", "ttree": "/usr/local/bin/ttree", "dbilogstrip": "/usr/local/bin/dbilogstrip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-hpc-runner-slurm.
shpc-registry automated BioContainers addition for perl-hpc-runner-slurm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-hpc-runner-slurm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-hpc-runner-slurm:2.58--2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-hpc-runner-slurm/2.58--2
$ module help quay.io/biocontainers/perl-hpc-runner-slurm/2.58--2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-hpc-runner-slurm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-hpc-runner-slurm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-hpc-runner-slurm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-hpc-runner-slurm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-hpc-runner-slurm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-hpc-runner-slurm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cpus.in

```bash
$ singularity exec <container> /usr/local/bin/cpus.in
$ podman run --it --rm --entrypoint /usr/local/bin/cpus.in   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpus.in   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpus.pl

```bash
$ singularity exec <container> /usr/local/bin/cpus.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cpus.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpus.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcerunner.pl

```bash
$ singularity exec <container> /usr/local/bin/mcerunner.pl
$ podman run --it --rm --entrypoint /usr/local/bin/mcerunner.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcerunner.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slurmrunner.pl

```bash
$ singularity exec <container> /usr/local/bin/slurmrunner.pl
$ podman run --it --rm --entrypoint /usr/local/bin/slurmrunner.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slurmrunner.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slurmrunnerbasic.pl

```bash
$ singularity exec <container> /usr/local/bin/slurmrunnerbasic.pl
$ podman run --it --rm --entrypoint /usr/local/bin/slurmrunnerbasic.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slurmrunnerbasic.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slurmrunnerrsyslog.pl

```bash
$ singularity exec <container> /usr/local/bin/slurmrunnerrsyslog.pl
$ podman run --it --rm --entrypoint /usr/local/bin/slurmrunnerrsyslog.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slurmrunnerrsyslog.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### testnodes.pl

```bash
$ singularity exec <container> /usr/local/bin/testnodes.pl
$ podman run --it --rm --entrypoint /usr/local/bin/testnodes.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/testnodes.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### findrule

```bash
$ singularity exec <container> /usr/local/bin/findrule
$ podman run --it --rm --entrypoint /usr/local/bin/findrule   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/findrule   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### l4p-tmpl

```bash
$ singularity exec <container> /usr/local/bin/l4p-tmpl
$ podman run --it --rm --entrypoint /usr/local/bin/l4p-tmpl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/l4p-tmpl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### config_data

```bash
$ singularity exec <container> /usr/local/bin/config_data
$ podman run --it --rm --entrypoint /usr/local/bin/config_data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/config_data   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.22.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.22.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.22.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.22.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c2ph

```bash
$ singularity exec <container> /usr/local/bin/c2ph
$ podman run --it --rm --entrypoint /usr/local/bin/c2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pstruct

```bash
$ singularity exec <container> /usr/local/bin/pstruct
$ podman run --it --rm --entrypoint /usr/local/bin/pstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imgsize

```bash
$ singularity exec <container> /usr/local/bin/imgsize
$ podman run --it --rm --entrypoint /usr/local/bin/imgsize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imgsize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tpage

```bash
$ singularity exec <container> /usr/local/bin/tpage
$ podman run --it --rm --entrypoint /usr/local/bin/tpage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tpage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ttree

```bash
$ singularity exec <container> /usr/local/bin/ttree
$ podman run --it --rm --entrypoint /usr/local/bin/ttree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ttree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbilogstrip

```bash
$ singularity exec <container> /usr/local/bin/dbilogstrip
$ podman run --it --rm --entrypoint /usr/local/bin/dbilogstrip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbilogstrip   -v ${PWD} -w ${PWD} <container> -c " $@"
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