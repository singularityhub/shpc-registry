---
layout: container
name:  "quay.io/biocontainers/tepid"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tepid/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tepid/container.yaml"
updated_at: "2023-06-26 03:41:07.304747"
latest: "0.10--py_0"
container_url: "https://biocontainers.pro/tools/tepid"
aliases:
 - "samblaster"
 - "tepid-discover"
 - "tepid-map"
 - "tepid-map-se"
 - "tepid-refine"
 - "yaha"
 - "intersection_matrix.py"
 - "intron_exon_reads.py"
 - "nosetests"
 - "pbt_plotting_example.py"
 - "peak_pie.py"
 - "pybedtools"
 - "venn_gchart.py"
 - "venn_mpl.py"
 - "annotate.py"
 - "bowtie2"
versions:
 - "0.8--py_3"
 - "0.10--py_0"
description: "shpc-registry automated BioContainers addition for tepid"
config: {"url": "https://biocontainers.pro/tools/tepid", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tepid", "latest": {"0.10--py_0": "sha256:586e342ced54a5ced60d9cf92afa0fdb29b95a3fe506f3dcff5905ffb2d6872a"}, "tags": {"0.8--py_3": "sha256:d6d03c578db8761b8fc517c2fa2cf2de0e2feeaac8e9414174a8afd635d051d0", "0.10--py_0": "sha256:586e342ced54a5ced60d9cf92afa0fdb29b95a3fe506f3dcff5905ffb2d6872a"}, "docker": "quay.io/biocontainers/tepid", "aliases": {"samblaster": "/usr/local/bin/samblaster", "tepid-discover": "/usr/local/bin/tepid-discover", "tepid-map": "/usr/local/bin/tepid-map", "tepid-map-se": "/usr/local/bin/tepid-map-se", "tepid-refine": "/usr/local/bin/tepid-refine", "yaha": "/usr/local/bin/yaha", "intersection_matrix.py": "/usr/local/bin/intersection_matrix.py", "intron_exon_reads.py": "/usr/local/bin/intron_exon_reads.py", "nosetests": "/usr/local/bin/nosetests", "pbt_plotting_example.py": "/usr/local/bin/pbt_plotting_example.py", "peak_pie.py": "/usr/local/bin/peak_pie.py", "pybedtools": "/usr/local/bin/pybedtools", "venn_gchart.py": "/usr/local/bin/venn_gchart.py", "venn_mpl.py": "/usr/local/bin/venn_mpl.py", "annotate.py": "/usr/local/bin/annotate.py", "bowtie2": "/usr/local/bin/bowtie2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tepid.
shpc-registry automated BioContainers addition for tepid
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tepid
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tepid:0.10--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tepid/0.10--py_0
$ module help quay.io/biocontainers/tepid/0.10--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tepid-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tepid-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tepid-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tepid-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tepid-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tepid-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### samblaster

```bash
$ singularity exec <container> /usr/local/bin/samblaster
$ podman run --it --rm --entrypoint /usr/local/bin/samblaster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samblaster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tepid-discover

```bash
$ singularity exec <container> /usr/local/bin/tepid-discover
$ podman run --it --rm --entrypoint /usr/local/bin/tepid-discover   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tepid-discover   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tepid-map

```bash
$ singularity exec <container> /usr/local/bin/tepid-map
$ podman run --it --rm --entrypoint /usr/local/bin/tepid-map   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tepid-map   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tepid-map-se

```bash
$ singularity exec <container> /usr/local/bin/tepid-map-se
$ podman run --it --rm --entrypoint /usr/local/bin/tepid-map-se   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tepid-map-se   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tepid-refine

```bash
$ singularity exec <container> /usr/local/bin/tepid-refine
$ podman run --it --rm --entrypoint /usr/local/bin/tepid-refine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tepid-refine   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yaha

```bash
$ singularity exec <container> /usr/local/bin/yaha
$ podman run --it --rm --entrypoint /usr/local/bin/yaha   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yaha   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### nosetests

```bash
$ singularity exec <container> /usr/local/bin/nosetests
$ podman run --it --rm --entrypoint /usr/local/bin/nosetests   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nosetests   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### bowtie2

```bash
$ singularity exec <container> /usr/local/bin/bowtie2
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
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