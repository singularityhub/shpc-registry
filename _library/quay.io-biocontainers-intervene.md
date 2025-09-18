---
layout: container
name:  "quay.io/biocontainers/intervene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/intervene/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/intervene/container.yaml"
updated_at: "2025-09-18 03:20:58.118158"
latest: "0.6.5--pyh3252c3a_1"
container_url: "https://biocontainers.pro/tools/intervene"
aliases:
 - "intervene"
 - "intersection_matrix.py"
 - "intron_exon_reads.py"
 - "pbt_plotting_example.py"
 - "peak_pie.py"
 - "pybedtools"
 - "venn_gchart.py"
 - "venn_mpl.py"
 - "annotate.py"
 - "shiftBed"
 - "annotateBed"
versions:
 - "0.6.5--pyh3252c3a_1"
description: "shpc-registry automated BioContainers addition for intervene"
config: {"url": "https://biocontainers.pro/tools/intervene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for intervene", "latest": {"0.6.5--pyh3252c3a_1": "sha256:936817596f2e8cec901c264c7178adec98f96c17b9b1f8bde62d07bf2ba7e0df"}, "tags": {"0.6.5--pyh3252c3a_1": "sha256:936817596f2e8cec901c264c7178adec98f96c17b9b1f8bde62d07bf2ba7e0df"}, "docker": "quay.io/biocontainers/intervene", "aliases": {"intervene": "/usr/local/bin/intervene", "intersection_matrix.py": "/usr/local/bin/intersection_matrix.py", "intron_exon_reads.py": "/usr/local/bin/intron_exon_reads.py", "pbt_plotting_example.py": "/usr/local/bin/pbt_plotting_example.py", "peak_pie.py": "/usr/local/bin/peak_pie.py", "pybedtools": "/usr/local/bin/pybedtools", "venn_gchart.py": "/usr/local/bin/venn_gchart.py", "venn_mpl.py": "/usr/local/bin/venn_mpl.py", "annotate.py": "/usr/local/bin/annotate.py", "shiftBed": "/usr/local/bin/shiftBed", "annotateBed": "/usr/local/bin/annotateBed"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/intervene.
shpc-registry automated BioContainers addition for intervene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/intervene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/intervene:0.6.5--pyh3252c3a_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/intervene/0.6.5--pyh3252c3a_1
$ module help quay.io/biocontainers/intervene/0.6.5--pyh3252c3a_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### intervene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### intervene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### intervene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### intervene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### intervene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### intervene-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### intervene

```bash
$ singularity exec <container> /usr/local/bin/intervene
$ podman run --it --rm --entrypoint /usr/local/bin/intervene   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intervene   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intersection_matrix.py

```bash
$ singularity exec <container> /usr/local/bin/intersection_matrix.py
$ podman run --it --rm --entrypoint /usr/local/bin/intersection_matrix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intersection_matrix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intron_exon_reads.py

```bash
$ singularity exec <container> /usr/local/bin/intron_exon_reads.py
$ podman run --it --rm --entrypoint /usr/local/bin/intron_exon_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intron_exon_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbt_plotting_example.py

```bash
$ singularity exec <container> /usr/local/bin/pbt_plotting_example.py
$ podman run --it --rm --entrypoint /usr/local/bin/pbt_plotting_example.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbt_plotting_example.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### peak_pie.py

```bash
$ singularity exec <container> /usr/local/bin/peak_pie.py
$ podman run --it --rm --entrypoint /usr/local/bin/peak_pie.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/peak_pie.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybedtools

```bash
$ singularity exec <container> /usr/local/bin/pybedtools
$ podman run --it --rm --entrypoint /usr/local/bin/pybedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### venn_gchart.py

```bash
$ singularity exec <container> /usr/local/bin/venn_gchart.py
$ podman run --it --rm --entrypoint /usr/local/bin/venn_gchart.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/venn_gchart.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### venn_mpl.py

```bash
$ singularity exec <container> /usr/local/bin/venn_mpl.py
$ podman run --it --rm --entrypoint /usr/local/bin/venn_mpl.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/venn_mpl.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotate.py

```bash
$ singularity exec <container> /usr/local/bin/annotate.py
$ podman run --it --rm --entrypoint /usr/local/bin/annotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiftBed

```bash
$ singularity exec <container> /usr/local/bin/shiftBed
$ podman run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotateBed

```bash
$ singularity exec <container> /usr/local/bin/annotateBed
$ podman run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
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