---
layout: container
name:  "quay.io/biocontainers/merfin"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/merfin/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/merfin/container.yaml"
updated_at: "2024-03-29 02:40:31.145872"
latest: "1.0--h4ac6f70_2"
container_url: "https://biocontainers.pro/tools/merfin"
aliases:
 - "gunzip"
 - "gzexe"
 - "gzip"
 - "merfin"
 - "meryl-analyze"
 - "meryl-import"
 - "meryl-lookup"
 - "meryl-simple"
 - "uncompress"
 - "zcat"
 - "zcmp"
 - "zdiff"
 - "zegrep"
 - "zfgrep"
 - "zforce"
 - "zgrep"
 - "zless"
 - "zmore"
 - "znew"
 - "meryl"
 - "pigz"
 - "unpigz"
versions:
 - "1.0--h9f5acd7_1"
 - "1.0--h4ac6f70_2"
description: "singularity registry hpc automated addition for merfin"
config: {"url": "https://biocontainers.pro/tools/merfin", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for merfin", "latest": {"1.0--h4ac6f70_2": "sha256:0187816d6849f9254fac4063babe024657829d09adf421100df825616bf2e1f6"}, "tags": {"1.0--h9f5acd7_1": "sha256:2c2641a46d1ffcd92fe650c750e9ab3528be742180bcb68c85f7dd9bbbf964c5", "1.0--h4ac6f70_2": "sha256:0187816d6849f9254fac4063babe024657829d09adf421100df825616bf2e1f6"}, "docker": "quay.io/biocontainers/merfin", "aliases": {"gunzip": "/usr/local/bin/gunzip", "gzexe": "/usr/local/bin/gzexe", "gzip": "/usr/local/bin/gzip", "merfin": "/usr/local/bin/merfin", "meryl-analyze": "/usr/local/bin/meryl-analyze", "meryl-import": "/usr/local/bin/meryl-import", "meryl-lookup": "/usr/local/bin/meryl-lookup", "meryl-simple": "/usr/local/bin/meryl-simple", "uncompress": "/usr/local/bin/uncompress", "zcat": "/usr/local/bin/zcat", "zcmp": "/usr/local/bin/zcmp", "zdiff": "/usr/local/bin/zdiff", "zegrep": "/usr/local/bin/zegrep", "zfgrep": "/usr/local/bin/zfgrep", "zforce": "/usr/local/bin/zforce", "zgrep": "/usr/local/bin/zgrep", "zless": "/usr/local/bin/zless", "zmore": "/usr/local/bin/zmore", "znew": "/usr/local/bin/znew", "meryl": "/usr/local/bin/meryl", "pigz": "/usr/local/bin/pigz", "unpigz": "/usr/local/bin/unpigz"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/merfin.
singularity registry hpc automated addition for merfin
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/merfin
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/merfin:1.0--h4ac6f70_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/merfin/1.0--h4ac6f70_2
$ module help quay.io/biocontainers/merfin/1.0--h4ac6f70_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### merfin-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### merfin-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### merfin-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### merfin-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### merfin-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### merfin-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gunzip

```bash
$ singularity exec <container> /usr/local/bin/gunzip
$ podman run --it --rm --entrypoint /usr/local/bin/gunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gzexe

```bash
$ singularity exec <container> /usr/local/bin/gzexe
$ podman run --it --rm --entrypoint /usr/local/bin/gzexe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gzexe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gzip

```bash
$ singularity exec <container> /usr/local/bin/gzip
$ podman run --it --rm --entrypoint /usr/local/bin/gzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merfin

```bash
$ singularity exec <container> /usr/local/bin/merfin
$ podman run --it --rm --entrypoint /usr/local/bin/merfin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merfin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meryl-analyze

```bash
$ singularity exec <container> /usr/local/bin/meryl-analyze
$ podman run --it --rm --entrypoint /usr/local/bin/meryl-analyze   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meryl-analyze   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meryl-import

```bash
$ singularity exec <container> /usr/local/bin/meryl-import
$ podman run --it --rm --entrypoint /usr/local/bin/meryl-import   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meryl-import   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meryl-lookup

```bash
$ singularity exec <container> /usr/local/bin/meryl-lookup
$ podman run --it --rm --entrypoint /usr/local/bin/meryl-lookup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meryl-lookup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meryl-simple

```bash
$ singularity exec <container> /usr/local/bin/meryl-simple
$ podman run --it --rm --entrypoint /usr/local/bin/meryl-simple   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meryl-simple   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uncompress

```bash
$ singularity exec <container> /usr/local/bin/uncompress
$ podman run --it --rm --entrypoint /usr/local/bin/uncompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uncompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zcat

```bash
$ singularity exec <container> /usr/local/bin/zcat
$ podman run --it --rm --entrypoint /usr/local/bin/zcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zcmp

```bash
$ singularity exec <container> /usr/local/bin/zcmp
$ podman run --it --rm --entrypoint /usr/local/bin/zcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zdiff

```bash
$ singularity exec <container> /usr/local/bin/zdiff
$ podman run --it --rm --entrypoint /usr/local/bin/zdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zegrep

```bash
$ singularity exec <container> /usr/local/bin/zegrep
$ podman run --it --rm --entrypoint /usr/local/bin/zegrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zegrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zfgrep

```bash
$ singularity exec <container> /usr/local/bin/zfgrep
$ podman run --it --rm --entrypoint /usr/local/bin/zfgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zfgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zforce

```bash
$ singularity exec <container> /usr/local/bin/zforce
$ podman run --it --rm --entrypoint /usr/local/bin/zforce   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zforce   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zgrep

```bash
$ singularity exec <container> /usr/local/bin/zgrep
$ podman run --it --rm --entrypoint /usr/local/bin/zgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zless

```bash
$ singularity exec <container> /usr/local/bin/zless
$ podman run --it --rm --entrypoint /usr/local/bin/zless   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zless   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zmore

```bash
$ singularity exec <container> /usr/local/bin/zmore
$ podman run --it --rm --entrypoint /usr/local/bin/zmore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zmore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### znew

```bash
$ singularity exec <container> /usr/local/bin/znew
$ podman run --it --rm --entrypoint /usr/local/bin/znew   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/znew   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meryl

```bash
$ singularity exec <container> /usr/local/bin/meryl
$ podman run --it --rm --entrypoint /usr/local/bin/meryl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meryl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pigz

```bash
$ singularity exec <container> /usr/local/bin/pigz
$ podman run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unpigz

```bash
$ singularity exec <container> /usr/local/bin/unpigz
$ podman run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
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