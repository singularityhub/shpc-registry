---
layout: container
name:  "quay.io/biocontainers/bleties"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bleties/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bleties/container.yaml"
updated_at: "2023-06-22 04:08:59.700561"
latest: "0.1.11--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/bleties"
aliases:
 - "NCRF"
 - "bleties"
 - "milcor_plot.py"
 - "milraa_plot.py"
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
 - "spoa"
 - "muscle"
 - "f2py3.7"
 - "opj_compress"
 - "opj_decompress"
 - "opj_dump"
 - "2to3-3.7"
 - "idle3.7"
 - "pydoc3.7"
 - "python3.7"
 - "python3.7-config"
versions:
 - "0.1.9--pyhdfd78af_0"
 - "0.1.11--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for bleties"
config: {"url": "https://biocontainers.pro/tools/bleties", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bleties", "latest": {"0.1.11--pyhdfd78af_1": "sha256:4baecaeab13e9c7071868250cd8cd30873109bf264ac0fa7a26f5e5ff1ee3def"}, "tags": {"0.1.9--pyhdfd78af_0": "sha256:15d5ec60cc4117788297db9e6a3d07c1a508ff6e6a947a1c27a0d8bf240ef22d", "0.1.11--pyhdfd78af_1": "sha256:4baecaeab13e9c7071868250cd8cd30873109bf264ac0fa7a26f5e5ff1ee3def"}, "docker": "quay.io/biocontainers/bleties", "aliases": {"NCRF": "/usr/local/bin/NCRF", "bleties": "/usr/local/bin/bleties", "milcor_plot.py": "/usr/local/bin/milcor_plot.py", "milraa_plot.py": "/usr/local/bin/milraa_plot.py", "ncrf_cat": "/usr/local/bin/ncrf_cat", "ncrf_cat.py": "/usr/local/bin/ncrf_cat.py", "ncrf_consensus_filter": "/usr/local/bin/ncrf_consensus_filter", "ncrf_consensus_filter.py": "/usr/local/bin/ncrf_consensus_filter.py", "ncrf_parse.py": "/usr/local/bin/ncrf_parse.py", "ncrf_resolve_overlaps": "/usr/local/bin/ncrf_resolve_overlaps", "ncrf_resolve_overlaps.py": "/usr/local/bin/ncrf_resolve_overlaps.py", "ncrf_sort": "/usr/local/bin/ncrf_sort", "ncrf_sort.py": "/usr/local/bin/ncrf_sort.py", "ncrf_summary": "/usr/local/bin/ncrf_summary", "ncrf_summary.py": "/usr/local/bin/ncrf_summary.py", "ncrf_to_bed": "/usr/local/bin/ncrf_to_bed", "ncrf_to_bed.py": "/usr/local/bin/ncrf_to_bed.py", "spoa": "/usr/local/bin/spoa", "muscle": "/usr/local/bin/muscle", "f2py3.7": "/usr/local/bin/f2py3.7", "opj_compress": "/usr/local/bin/opj_compress", "opj_decompress": "/usr/local/bin/opj_decompress", "opj_dump": "/usr/local/bin/opj_dump", "2to3-3.7": "/usr/local/bin/2to3-3.7", "idle3.7": "/usr/local/bin/idle3.7", "pydoc3.7": "/usr/local/bin/pydoc3.7", "python3.7": "/usr/local/bin/python3.7", "python3.7-config": "/usr/local/bin/python3.7-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bleties.
shpc-registry automated BioContainers addition for bleties
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bleties
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bleties:0.1.11--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bleties/0.1.11--pyhdfd78af_1
$ module help quay.io/biocontainers/bleties/0.1.11--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bleties-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bleties-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bleties-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bleties-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bleties-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bleties-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### NCRF

```bash
$ singularity exec <container> /usr/local/bin/NCRF
$ podman run --it --rm --entrypoint /usr/local/bin/NCRF   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NCRF   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bleties

```bash
$ singularity exec <container> /usr/local/bin/bleties
$ podman run --it --rm --entrypoint /usr/local/bin/bleties   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bleties   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### milcor_plot.py

```bash
$ singularity exec <container> /usr/local/bin/milcor_plot.py
$ podman run --it --rm --entrypoint /usr/local/bin/milcor_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/milcor_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### milraa_plot.py

```bash
$ singularity exec <container> /usr/local/bin/milraa_plot.py
$ podman run --it --rm --entrypoint /usr/local/bin/milraa_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/milraa_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### spoa

```bash
$ singularity exec <container> /usr/local/bin/spoa
$ podman run --it --rm --entrypoint /usr/local/bin/spoa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spoa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### muscle

```bash
$ singularity exec <container> /usr/local/bin/muscle
$ podman run --it --rm --entrypoint /usr/local/bin/muscle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/muscle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.7

```bash
$ singularity exec <container> /usr/local/bin/f2py3.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_compress

```bash
$ singularity exec <container> /usr/local/bin/opj_compress
$ podman run --it --rm --entrypoint /usr/local/bin/opj_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_decompress

```bash
$ singularity exec <container> /usr/local/bin/opj_decompress
$ podman run --it --rm --entrypoint /usr/local/bin/opj_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_dump

```bash
$ singularity exec <container> /usr/local/bin/opj_dump
$ podman run --it --rm --entrypoint /usr/local/bin/opj_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.7

```bash
$ singularity exec <container> /usr/local/bin/idle3.7
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.7

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7

```bash
$ singularity exec <container> /usr/local/bin/python3.7
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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