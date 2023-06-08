---
layout: container
name:  "quay.io/biocontainers/ncrf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ncrf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ncrf/container.yaml"
updated_at: "2023-06-08 03:15:11.272946"
latest: "1.01.02--h031d066_5"
container_url: "https://biocontainers.pro/tools/ncrf"
aliases:
 - "NCRF"
 - "ncrf_cat"
 - "ncrf_cat.py"
 - "ncrf_consensus_filter"
 - "ncrf_consensus_filter.py"
 - "ncrf_parse.py"
 - "ncrf_resolve_overlaps"
 - "ncrf_resolve_overlaps.py"
 - "ncrf_sort"
 - "ncrf_sort.py"
 - "ncrf_summary"
 - "ncrf_summary.py"
 - "ncrf_to_bed"
 - "ncrf_to_bed.py"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
versions:
 - "1.01.02--hec16e2b_3"
 - "1.01.02--h031d066_5"
description: "shpc-registry automated BioContainers addition for ncrf"
config: {"url": "https://biocontainers.pro/tools/ncrf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ncrf", "latest": {"1.01.02--h031d066_5": "sha256:9da8870a85aa26fae19df40ff734baf98e1f410f339b3d8c0a2541c9c6d15a2f"}, "tags": {"1.01.02--hec16e2b_3": "sha256:a81f0c9601c9ba6a2fec8acf5092572ef1068eead081b18d155d3263187432b6", "1.01.02--h031d066_5": "sha256:9da8870a85aa26fae19df40ff734baf98e1f410f339b3d8c0a2541c9c6d15a2f"}, "docker": "quay.io/biocontainers/ncrf", "aliases": {"NCRF": "/usr/local/bin/NCRF", "ncrf_cat": "/usr/local/bin/ncrf_cat", "ncrf_cat.py": "/usr/local/bin/ncrf_cat.py", "ncrf_consensus_filter": "/usr/local/bin/ncrf_consensus_filter", "ncrf_consensus_filter.py": "/usr/local/bin/ncrf_consensus_filter.py", "ncrf_parse.py": "/usr/local/bin/ncrf_parse.py", "ncrf_resolve_overlaps": "/usr/local/bin/ncrf_resolve_overlaps", "ncrf_resolve_overlaps.py": "/usr/local/bin/ncrf_resolve_overlaps.py", "ncrf_sort": "/usr/local/bin/ncrf_sort", "ncrf_sort.py": "/usr/local/bin/ncrf_sort.py", "ncrf_summary": "/usr/local/bin/ncrf_summary", "ncrf_summary.py": "/usr/local/bin/ncrf_summary.py", "ncrf_to_bed": "/usr/local/bin/ncrf_to_bed", "ncrf_to_bed.py": "/usr/local/bin/ncrf_to_bed.py", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ncrf.
shpc-registry automated BioContainers addition for ncrf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ncrf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ncrf:1.01.02--h031d066_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ncrf/1.01.02--h031d066_5
$ module help quay.io/biocontainers/ncrf/1.01.02--h031d066_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ncrf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ncrf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ncrf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ncrf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ncrf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ncrf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### NCRF

```bash
$ singularity exec <container> /usr/local/bin/NCRF
$ podman run --it --rm --entrypoint /usr/local/bin/NCRF   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NCRF   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncrf_cat

```bash
$ singularity exec <container> /usr/local/bin/ncrf_cat
$ podman run --it --rm --entrypoint /usr/local/bin/ncrf_cat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncrf_cat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncrf_cat.py

```bash
$ singularity exec <container> /usr/local/bin/ncrf_cat.py
$ podman run --it --rm --entrypoint /usr/local/bin/ncrf_cat.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncrf_cat.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncrf_consensus_filter

```bash
$ singularity exec <container> /usr/local/bin/ncrf_consensus_filter
$ podman run --it --rm --entrypoint /usr/local/bin/ncrf_consensus_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncrf_consensus_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncrf_consensus_filter.py

```bash
$ singularity exec <container> /usr/local/bin/ncrf_consensus_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/ncrf_consensus_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncrf_consensus_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncrf_parse.py

```bash
$ singularity exec <container> /usr/local/bin/ncrf_parse.py
$ podman run --it --rm --entrypoint /usr/local/bin/ncrf_parse.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncrf_parse.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncrf_resolve_overlaps

```bash
$ singularity exec <container> /usr/local/bin/ncrf_resolve_overlaps
$ podman run --it --rm --entrypoint /usr/local/bin/ncrf_resolve_overlaps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncrf_resolve_overlaps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncrf_resolve_overlaps.py

```bash
$ singularity exec <container> /usr/local/bin/ncrf_resolve_overlaps.py
$ podman run --it --rm --entrypoint /usr/local/bin/ncrf_resolve_overlaps.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncrf_resolve_overlaps.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncrf_sort

```bash
$ singularity exec <container> /usr/local/bin/ncrf_sort
$ podman run --it --rm --entrypoint /usr/local/bin/ncrf_sort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncrf_sort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncrf_sort.py

```bash
$ singularity exec <container> /usr/local/bin/ncrf_sort.py
$ podman run --it --rm --entrypoint /usr/local/bin/ncrf_sort.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncrf_sort.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncrf_summary

```bash
$ singularity exec <container> /usr/local/bin/ncrf_summary
$ podman run --it --rm --entrypoint /usr/local/bin/ncrf_summary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncrf_summary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncrf_summary.py

```bash
$ singularity exec <container> /usr/local/bin/ncrf_summary.py
$ podman run --it --rm --entrypoint /usr/local/bin/ncrf_summary.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncrf_summary.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncrf_to_bed

```bash
$ singularity exec <container> /usr/local/bin/ncrf_to_bed
$ podman run --it --rm --entrypoint /usr/local/bin/ncrf_to_bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncrf_to_bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncrf_to_bed.py

```bash
$ singularity exec <container> /usr/local/bin/ncrf_to_bed.py
$ podman run --it --rm --entrypoint /usr/local/bin/ncrf_to_bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncrf_to_bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2-config

```bash
$ singularity exec <container> /usr/local/bin/python2-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7-config

```bash
$ singularity exec <container> /usr/local/bin/python2.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2

```bash
$ singularity exec <container> /usr/local/bin/python2
$ podman run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7

```bash
$ singularity exec <container> /usr/local/bin/python2.7
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle

```bash
$ singularity exec <container> /usr/local/bin/idle
$ podman run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-config

```bash
$ singularity exec <container> /usr/local/bin/python-config
$ podman run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smtpd.py

```bash
$ singularity exec <container> /usr/local/bin/smtpd.py
$ podman run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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