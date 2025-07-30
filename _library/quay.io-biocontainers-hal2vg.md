---
layout: container
name:  "quay.io/biocontainers/hal2vg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hal2vg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hal2vg/container.yaml"
updated_at: "2025-07-30 04:33:21.718306"
latest: "1.1.8--hee927d3_0"
container_url: "https://biocontainers.pro/tools/hal2vg"
aliases:
 - "clip-vg"
 - "count-vg-hap-cov"
 - "filter-paf-deletions"
 - "hal2vg"
 - "halMergeChroms"
 - "halRemoveDupes"
 - "halUnclip"
 - "h5tools_test_utils"
 - "h5fuse.sh"
 - "h5delete"
 - "h5fc"
 - "h5clear"
 - "h5format_convert"
 - "h5watch"
 - "gif2h5"
 - "h52gif"
 - "h5c++"
 - "h5cc"
 - "h5copy"
 - "h5debug"
 - "h5diff"
 - "h5import"
 - "h5jam"
 - "h5ls"
 - "h5mkgrp"
 - "h5perf_serial"
 - "h5redeploy"
 - "h5repack"
 - "h5repart"
 - "h5stat"
 - "h5unjam"
 - "h5dump"
versions:
 - "1.1.8--hee927d3_0"
description: "singularity registry hpc automated addition for hal2vg"
config: {"url": "https://biocontainers.pro/tools/hal2vg", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for hal2vg", "latest": {"1.1.8--hee927d3_0": "sha256:18a6184d8e0234c9ea38ba7d2e73e306ebf824c2ba573a55102024af6957d9f5"}, "tags": {"1.1.8--hee927d3_0": "sha256:18a6184d8e0234c9ea38ba7d2e73e306ebf824c2ba573a55102024af6957d9f5"}, "docker": "quay.io/biocontainers/hal2vg", "aliases": {"clip-vg": "/usr/local/bin/clip-vg", "count-vg-hap-cov": "/usr/local/bin/count-vg-hap-cov", "filter-paf-deletions": "/usr/local/bin/filter-paf-deletions", "hal2vg": "/usr/local/bin/hal2vg", "halMergeChroms": "/usr/local/bin/halMergeChroms", "halRemoveDupes": "/usr/local/bin/halRemoveDupes", "halUnclip": "/usr/local/bin/halUnclip", "h5tools_test_utils": "/usr/local/bin/h5tools_test_utils", "h5fuse.sh": "/usr/local/bin/h5fuse.sh", "h5delete": "/usr/local/bin/h5delete", "h5fc": "/usr/local/bin/h5fc", "h5clear": "/usr/local/bin/h5clear", "h5format_convert": "/usr/local/bin/h5format_convert", "h5watch": "/usr/local/bin/h5watch", "gif2h5": "/usr/local/bin/gif2h5", "h52gif": "/usr/local/bin/h52gif", "h5c++": "/usr/local/bin/h5c++", "h5cc": "/usr/local/bin/h5cc", "h5copy": "/usr/local/bin/h5copy", "h5debug": "/usr/local/bin/h5debug", "h5diff": "/usr/local/bin/h5diff", "h5import": "/usr/local/bin/h5import", "h5jam": "/usr/local/bin/h5jam", "h5ls": "/usr/local/bin/h5ls", "h5mkgrp": "/usr/local/bin/h5mkgrp", "h5perf_serial": "/usr/local/bin/h5perf_serial", "h5redeploy": "/usr/local/bin/h5redeploy", "h5repack": "/usr/local/bin/h5repack", "h5repart": "/usr/local/bin/h5repart", "h5stat": "/usr/local/bin/h5stat", "h5unjam": "/usr/local/bin/h5unjam", "h5dump": "/usr/local/bin/h5dump"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hal2vg.
singularity registry hpc automated addition for hal2vg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hal2vg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hal2vg:1.1.8--hee927d3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hal2vg/1.1.8--hee927d3_0
$ module help quay.io/biocontainers/hal2vg/1.1.8--hee927d3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hal2vg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hal2vg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hal2vg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hal2vg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hal2vg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hal2vg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### clip-vg

```bash
$ singularity exec <container> /usr/local/bin/clip-vg
$ podman run --it --rm --entrypoint /usr/local/bin/clip-vg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clip-vg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### count-vg-hap-cov

```bash
$ singularity exec <container> /usr/local/bin/count-vg-hap-cov
$ podman run --it --rm --entrypoint /usr/local/bin/count-vg-hap-cov   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/count-vg-hap-cov   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-paf-deletions

```bash
$ singularity exec <container> /usr/local/bin/filter-paf-deletions
$ podman run --it --rm --entrypoint /usr/local/bin/filter-paf-deletions   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-paf-deletions   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hal2vg

```bash
$ singularity exec <container> /usr/local/bin/hal2vg
$ podman run --it --rm --entrypoint /usr/local/bin/hal2vg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hal2vg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### halMergeChroms

```bash
$ singularity exec <container> /usr/local/bin/halMergeChroms
$ podman run --it --rm --entrypoint /usr/local/bin/halMergeChroms   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/halMergeChroms   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### halRemoveDupes

```bash
$ singularity exec <container> /usr/local/bin/halRemoveDupes
$ podman run --it --rm --entrypoint /usr/local/bin/halRemoveDupes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/halRemoveDupes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### halUnclip

```bash
$ singularity exec <container> /usr/local/bin/halUnclip
$ podman run --it --rm --entrypoint /usr/local/bin/halUnclip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/halUnclip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5tools_test_utils

```bash
$ singularity exec <container> /usr/local/bin/h5tools_test_utils
$ podman run --it --rm --entrypoint /usr/local/bin/h5tools_test_utils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5tools_test_utils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5fuse.sh

```bash
$ singularity exec <container> /usr/local/bin/h5fuse.sh
$ podman run --it --rm --entrypoint /usr/local/bin/h5fuse.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5fuse.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5delete

```bash
$ singularity exec <container> /usr/local/bin/h5delete
$ podman run --it --rm --entrypoint /usr/local/bin/h5delete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5delete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5fc

```bash
$ singularity exec <container> /usr/local/bin/h5fc
$ podman run --it --rm --entrypoint /usr/local/bin/h5fc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5fc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5clear

```bash
$ singularity exec <container> /usr/local/bin/h5clear
$ podman run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5format_convert

```bash
$ singularity exec <container> /usr/local/bin/h5format_convert
$ podman run --it --rm --entrypoint /usr/local/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5watch

```bash
$ singularity exec <container> /usr/local/bin/h5watch
$ podman run --it --rm --entrypoint /usr/local/bin/h5watch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5watch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2h5

```bash
$ singularity exec <container> /usr/local/bin/gif2h5
$ podman run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h52gif

```bash
$ singularity exec <container> /usr/local/bin/h52gif
$ podman run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5c++

```bash
$ singularity exec <container> /usr/local/bin/h5c++
$ podman run --it --rm --entrypoint /usr/local/bin/h5c++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5c++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5cc

```bash
$ singularity exec <container> /usr/local/bin/h5cc
$ podman run --it --rm --entrypoint /usr/local/bin/h5cc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5cc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5copy

```bash
$ singularity exec <container> /usr/local/bin/h5copy
$ podman run --it --rm --entrypoint /usr/local/bin/h5copy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5copy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5debug

```bash
$ singularity exec <container> /usr/local/bin/h5debug
$ podman run --it --rm --entrypoint /usr/local/bin/h5debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5debug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5diff

```bash
$ singularity exec <container> /usr/local/bin/h5diff
$ podman run --it --rm --entrypoint /usr/local/bin/h5diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5import

```bash
$ singularity exec <container> /usr/local/bin/h5import
$ podman run --it --rm --entrypoint /usr/local/bin/h5import   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5import   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5jam

```bash
$ singularity exec <container> /usr/local/bin/h5jam
$ podman run --it --rm --entrypoint /usr/local/bin/h5jam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5jam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5ls

```bash
$ singularity exec <container> /usr/local/bin/h5ls
$ podman run --it --rm --entrypoint /usr/local/bin/h5ls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5ls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5mkgrp

```bash
$ singularity exec <container> /usr/local/bin/h5mkgrp
$ podman run --it --rm --entrypoint /usr/local/bin/h5mkgrp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5mkgrp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5perf_serial

```bash
$ singularity exec <container> /usr/local/bin/h5perf_serial
$ podman run --it --rm --entrypoint /usr/local/bin/h5perf_serial   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5perf_serial   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5redeploy

```bash
$ singularity exec <container> /usr/local/bin/h5redeploy
$ podman run --it --rm --entrypoint /usr/local/bin/h5redeploy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5redeploy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5repack

```bash
$ singularity exec <container> /usr/local/bin/h5repack
$ podman run --it --rm --entrypoint /usr/local/bin/h5repack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5repack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5repart

```bash
$ singularity exec <container> /usr/local/bin/h5repart
$ podman run --it --rm --entrypoint /usr/local/bin/h5repart   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5repart   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5stat

```bash
$ singularity exec <container> /usr/local/bin/h5stat
$ podman run --it --rm --entrypoint /usr/local/bin/h5stat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5stat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5unjam

```bash
$ singularity exec <container> /usr/local/bin/h5unjam
$ podman run --it --rm --entrypoint /usr/local/bin/h5unjam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5unjam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5dump

```bash
$ singularity exec <container> /usr/local/bin/h5dump
$ podman run --it --rm --entrypoint /usr/local/bin/h5dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5dump   -v ${PWD} -w ${PWD} <container> -c " $@"
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