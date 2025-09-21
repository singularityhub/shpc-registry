---
layout: container
name:  "quay.io/biocontainers/sfold"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sfold/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sfold/container.yaml"
updated_at: "2025-09-21 03:30:48.581050"
latest: "2.2--pl5321r44h7b50bb2_4"
container_url: "https://biocontainers.pro/tools/sfold"
aliases:
 - "bp_count.pl"
 - "bprob.X86_64.LINUX"
 - "find.dist.X86_64.LINUX"
 - "findfe"
 - "findfe.X86_64.LINUX"
 - "gawk-5.3.1"
 - "gcg2bp.pl"
 - "getu0.X86_64.LINUX"
 - "getu0.X86_64.SUNOS"
 - "hybrid_en.pl"
 - "sclass.X86_64.LINUX"
 - "sfold"
 - "sfold.X86_64.LINUX"
 - "sfold.pl"
 - "sfold.pl~"
 - "showsysinfo.sh"
 - "egrep"
 - "fgrep"
 - "grep"
 - "gawkbug"
 - "awk"
 - "gawk"
 - "hb-info"
 - "tjbench"
versions:
 - "2.2--pl5321r43h031d066_0"
 - "2.2--pl5321r43h031d066_3"
 - "2.2--pl5321r44h7b50bb2_4"
description: "singularity registry hpc automated addition for sfold"
config: {"url": "https://biocontainers.pro/tools/sfold", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sfold", "latest": {"2.2--pl5321r44h7b50bb2_4": "sha256:0c3a4398b31526ae2af723190bbf8fd9b5fe577b08a301a7f41f948f846eca2d"}, "tags": {"2.2--pl5321r43h031d066_0": "sha256:f6e4823ce12a6035cdb3aaf7553d0086ca94eb9ba67762c298f2773705bfad66", "2.2--pl5321r43h031d066_3": "sha256:f82cb6556b436ebf54d5965494a1ac3213c2425f239efed2a96b2025ae6e4432", "2.2--pl5321r44h7b50bb2_4": "sha256:0c3a4398b31526ae2af723190bbf8fd9b5fe577b08a301a7f41f948f846eca2d"}, "docker": "quay.io/biocontainers/sfold", "aliases": {"bp_count.pl": "/usr/local/bin/bp_count.pl", "bprob.X86_64.LINUX": "/usr/local/bin/bprob.X86_64.LINUX", "find.dist.X86_64.LINUX": "/usr/local/bin/find.dist.X86_64.LINUX", "findfe": "/usr/local/bin/findfe", "findfe.X86_64.LINUX": "/usr/local/bin/findfe.X86_64.LINUX", "gawk-5.3.1": "/usr/local/bin/gawk-5.3.1", "gcg2bp.pl": "/usr/local/bin/gcg2bp.pl", "getu0.X86_64.LINUX": "/usr/local/bin/getu0.X86_64.LINUX", "getu0.X86_64.SUNOS": "/usr/local/bin/getu0.X86_64.SUNOS", "hybrid_en.pl": "/usr/local/bin/hybrid_en.pl", "sclass.X86_64.LINUX": "/usr/local/bin/sclass.X86_64.LINUX", "sfold": "/usr/local/bin/sfold", "sfold.X86_64.LINUX": "/usr/local/bin/sfold.X86_64.LINUX", "sfold.pl": "/usr/local/bin/sfold.pl", "sfold.pl~": "/usr/local/bin/sfold.pl~", "showsysinfo.sh": "/usr/local/bin/showsysinfo.sh", "egrep": "/usr/local/bin/egrep", "fgrep": "/usr/local/bin/fgrep", "grep": "/usr/local/bin/grep", "gawkbug": "/usr/local/bin/gawkbug", "awk": "/usr/local/bin/awk", "gawk": "/usr/local/bin/gawk", "hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sfold.
singularity registry hpc automated addition for sfold
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sfold
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sfold:2.2--pl5321r44h7b50bb2_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sfold/2.2--pl5321r44h7b50bb2_4
$ module help quay.io/biocontainers/sfold/2.2--pl5321r44h7b50bb2_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sfold-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sfold-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sfold-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sfold-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sfold-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sfold-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bp_count.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_count.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_count.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_count.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bprob.X86_64.LINUX

```bash
$ singularity exec <container> /usr/local/bin/bprob.X86_64.LINUX
$ podman run --it --rm --entrypoint /usr/local/bin/bprob.X86_64.LINUX   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bprob.X86_64.LINUX   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find.dist.X86_64.LINUX

```bash
$ singularity exec <container> /usr/local/bin/find.dist.X86_64.LINUX
$ podman run --it --rm --entrypoint /usr/local/bin/find.dist.X86_64.LINUX   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find.dist.X86_64.LINUX   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### findfe

```bash
$ singularity exec <container> /usr/local/bin/findfe
$ podman run --it --rm --entrypoint /usr/local/bin/findfe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/findfe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### findfe.X86_64.LINUX

```bash
$ singularity exec <container> /usr/local/bin/findfe.X86_64.LINUX
$ podman run --it --rm --entrypoint /usr/local/bin/findfe.X86_64.LINUX   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/findfe.X86_64.LINUX   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.3.1

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.3.1
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcg2bp.pl

```bash
$ singularity exec <container> /usr/local/bin/gcg2bp.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gcg2bp.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcg2bp.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getu0.X86_64.LINUX

```bash
$ singularity exec <container> /usr/local/bin/getu0.X86_64.LINUX
$ podman run --it --rm --entrypoint /usr/local/bin/getu0.X86_64.LINUX   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getu0.X86_64.LINUX   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getu0.X86_64.SUNOS

```bash
$ singularity exec <container> /usr/local/bin/getu0.X86_64.SUNOS
$ podman run --it --rm --entrypoint /usr/local/bin/getu0.X86_64.SUNOS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getu0.X86_64.SUNOS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hybrid_en.pl

```bash
$ singularity exec <container> /usr/local/bin/hybrid_en.pl
$ podman run --it --rm --entrypoint /usr/local/bin/hybrid_en.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hybrid_en.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sclass.X86_64.LINUX

```bash
$ singularity exec <container> /usr/local/bin/sclass.X86_64.LINUX
$ podman run --it --rm --entrypoint /usr/local/bin/sclass.X86_64.LINUX   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sclass.X86_64.LINUX   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sfold

```bash
$ singularity exec <container> /usr/local/bin/sfold
$ podman run --it --rm --entrypoint /usr/local/bin/sfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sfold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sfold.X86_64.LINUX

```bash
$ singularity exec <container> /usr/local/bin/sfold.X86_64.LINUX
$ podman run --it --rm --entrypoint /usr/local/bin/sfold.X86_64.LINUX   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sfold.X86_64.LINUX   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sfold.pl

```bash
$ singularity exec <container> /usr/local/bin/sfold.pl
$ podman run --it --rm --entrypoint /usr/local/bin/sfold.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sfold.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sfold.pl~

```bash
$ singularity exec <container> /usr/local/bin/sfold.pl~
$ podman run --it --rm --entrypoint /usr/local/bin/sfold.pl~   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sfold.pl~   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### showsysinfo.sh

```bash
$ singularity exec <container> /usr/local/bin/showsysinfo.sh
$ podman run --it --rm --entrypoint /usr/local/bin/showsysinfo.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/showsysinfo.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### egrep

```bash
$ singularity exec <container> /usr/local/bin/egrep
$ podman run --it --rm --entrypoint /usr/local/bin/egrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/egrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fgrep

```bash
$ singularity exec <container> /usr/local/bin/fgrep
$ podman run --it --rm --entrypoint /usr/local/bin/fgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grep

```bash
$ singularity exec <container> /usr/local/bin/grep
$ podman run --it --rm --entrypoint /usr/local/bin/grep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawkbug

```bash
$ singularity exec <container> /usr/local/bin/gawkbug
$ podman run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### awk

```bash
$ singularity exec <container> /usr/local/bin/awk
$ podman run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk

```bash
$ singularity exec <container> /usr/local/bin/gawk
$ podman run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
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